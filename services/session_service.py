from typing import Dict, Any

class InMemorySessionService:
    def __init__(self):
        self._store: Dict[str, Dict[str, Any]] = {}

    def get_session(self, user_id: str) -> Dict[str, Any]:
        return self._store.setdefault(user_id, {})

    def save_session(self, user_id: str, session: Dict[str, Any]):
        self._store[user_id] = session

    def clear_session(self, user_id: str):
        if user_id in self._store:
            del self._store[user_id]
