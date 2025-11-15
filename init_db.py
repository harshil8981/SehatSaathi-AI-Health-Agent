import sqlite3, json
from pathlib import Path

DB_PATH = Path('memory.db')
CLINICS_PATH = Path('clinics.json')

def init_memory_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute('CREATE TABLE IF NOT EXISTS memory (user TEXT PRIMARY KEY, data TEXT)')
    sample = {
        'name': 'Test User',
        'age': 28,
        'allergies': ['penicillin'],
        'chronic': []
    }
    conn.execute('REPLACE INTO memory(user, data) VALUES(?,?)', ('test_user', json.dumps(sample)))
    conn.commit()
    conn.close()
    print('✅ memory.db created with sample user test_user')

def init_clinics():
    clinics = [
        {"name":"Community Clinic A","lat":28.6139,"lon":77.2090,"distance_km":1.2,"phone":"+91-90000-00001"},
        {"name":"Telemedicine Portal","lat":null,"lon":null,"distance_km":null,"url":"https://telemed.example"}
    ]
    with open(CLINICS_PATH, 'w', encoding='utf-8') as f:
        json.dump(clinics, f, indent=2)
    print('✅ clinics.json created')

if __name__ == '__main__':
    init_memory_db()
    init_clinics()
    print('Initialization complete.')
