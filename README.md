# 🩺 SehatSaathi – AI Health Assistant
### Multi-Agent Healthcare System powered by Google AI Studio (Gemini)

SehatSaathi is a modern, production-ready healthcare assistant that uses a **multi-agent AI architecture** to provide early-stage medical guidance. It supports symptom intake, LLM-powered triage, personalized care-plan generation, clinic suggestions, and session/memory management.  
Built for the **Agents for Good** track of Google’s AI Agents Intensive Capstone Project (2025).

---

## ⭐ Features

### 🤖 Multi-Agent System
- **Intake Agent** – Extracts symptoms & user context  
- **Triage Agent** – Determines urgency using Gemini / MockLLM  
- **CarePlan Agent** – Produces a personalized care plan  
- **Resource Agent** – Suggests nearby clinics or telemedicine  
- **Session & Memory Service** – Maintains continuous user context  

### 🧠 Gemini Integration  
- Uses **Google AI Studio (Gemini API)**  
- Automatically falls back to **MockLLM** when key not provided  
- Safe prompt engineering & structured output  

### 🛠 Technology Stack  
| Component | Technology |
|----------|------------|
| AI Model | Google Gemini |
| Backend | FastAPI |
| Language | Python 3.10+ |
| DB | SQLite |
| Tools | Clinic Lookup, Geocode Stub |
| Design | Multi-Agent Architecture |

---

## 📁 Project Structure

```
sehatsaathi/
├── agents/
│   ├── intake_agent.py
│   ├── triage_agent.py
│   ├── careplan_agent.py
│   └── resource_agent.py
├── tools/
│   ├── clinic_lookup_tool.py
│   ├── geocode_tool.py
├── services/
│   ├── long_running.py
│   ├── memory_bank.py
│   ├── observability.py
│   └── session_service.py
├── model_client.py
├── orchestrator.py
├── main.py
├── init_db.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Create virtual environment
```
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Initialize local DB & clinic data
```
python init_db.py
```

### 4. Start the FastAPI server
```
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 5. Open interactive API UI  
👉 http://127.0.0.1:8000/docs

---

## 🔑 Gemini API Setup (Optional but Recommended)

Set your key:

**Linux/macOS**
```
export GOOGLE_API_KEY="your-key"
```

**Windows PowerShell**
```
setx GOOGLE_API_KEY "your-key"
```

If unset → system uses **MockLLM**.

---

## 🧪 API Usage Example

### POST `/message`
```
curl -X POST "http://127.0.0.1:8000/message" -H "Content-Type: application/json" -d '{
  "user_id": "test_user",
  "message": "I have fever and cough",
  "lat": 28.6139,
  "lon": 77.2090
}'
```

Response includes:
- Intake summary  
- AI triage  
- Care plan  
- Nearby clinics  

---

## 🧠 System Flow (Architecture)

```
User → FastAPI → Orchestrator
   → IntakeAgent
   → TriageAgent → Gemini / MockLLM
   → CarePlanAgent → Gemini / MockLLM
   → ResourceAgent → clinics.json
        ↓
   Memory + Session
        ↓
Structured Response
```

---

## 🔐 Security
- API keys are **never stored** in the repo  
- Environment variables only  
- This is **not a medical diagnosis tool**  
- Safety disclaimers included in prompts  

---

## 🤝 Contributing
Feel free to submit issues or PRs:
- New agents  
- Better prompts  
- Improved clinic data  
- Frontend UI  

---

## 📄 License
MIT License

---

## 🎉 Final Notes
SehatSaathi demonstrates a complete, scalable multi-agent system with real-world healthcare value, ideal for GitHub portfolios, Kaggle submissions, and AI engineering showcases.

