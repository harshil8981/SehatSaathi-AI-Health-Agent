# main.py
import uvicorn, os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional, Dict, Any

from orchestrator import handle_message, session_service

app = FastAPI(title="SehatSaathi - Local API")

# CORS — dev convenience; tighten for production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static directory at /static
static_dir = os.path.join(os.path.dirname(__file__), "static")
if not os.path.exists(static_dir):
    os.makedirs(static_dir, exist_ok=True)
app.mount("/static", StaticFiles(directory=static_dir), name="static")

class MessageRequest(BaseModel):
    user_id: str
    message: str
    lat: Optional[float] = None
    lon: Optional[float] = None

@app.post("/message")
async def message(req: MessageRequest):
    try:
        location = None
        if req.lat is not None and req.lon is not None:
            location = {"lat": req.lat, "lon": req.lon}
        result = await handle_message(req.user_id, req.message, location)
        return {"status": "ok", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/session/{user_id}")
def get_session(user_id: str):
    s = session_service.get_session(user_id)
    return {"user_id": user_id, "session": s}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
