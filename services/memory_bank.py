import json
import sqlite3
from typing import Dict, Any

class MemoryBank:
    def __init__(self, db_path: str = 'memory.db'):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.execute('CREATE TABLE IF NOT EXISTS memory (user TEXT PRIMARY KEY, data TEXT)')
        self.conn.commit()

    def get(self, user: str) -> Dict[str, Any]:
        r = self.conn.execute('SELECT data FROM memory WHERE user=?', (user,)).fetchone()
        return json.loads(r[0]) if r else {}

    def set(self, user: str, data: Dict[str, Any]):
        self.conn.execute('REPLACE INTO memory(user, data) VALUES(?,?)', (user, json.dumps(data)))
        self.conn.commit()
