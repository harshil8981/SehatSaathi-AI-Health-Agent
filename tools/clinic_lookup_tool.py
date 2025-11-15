import json
from pathlib import Path
from typing import Tuple, List, Dict

CLINICS_PATH = Path('clinics.json')

class ClinicLookupTool:
    def __init__(self):
        if CLINICS_PATH.exists():
            with open(CLINICS_PATH, 'r', encoding='utf-8') as f:
                self.clinics = json.load(f)
        else:
            self.clinics = [
                {"name":"Community Clinic A","lat":28.6139,"lon":77.2090,"distance_km":1.2,"phone":"+91-90000-00001"},
                {"name":"Telemedicine Portal","lat":None,"lon":None,"distance_km":None,"url":"https://telemed.example"}
            ]

    def find_nearby(self, coords: Tuple[float, float]) -> List[Dict[str, str]]:
        return self.clinics

    def find_all(self) -> List[Dict[str, str]]:
        return self.clinics
