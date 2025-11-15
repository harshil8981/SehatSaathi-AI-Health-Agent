from typing import Dict, Any
from tools.clinic_lookup_tool import ClinicLookupTool

class ResourceAgent:
    def __init__(self, clinic_lookup: ClinicLookupTool = None):
        self.clinic_lookup = clinic_lookup or ClinicLookupTool()

    def run(self, intake: Dict[str, Any], user_location: Dict[str, float] = None):
        if not user_location:
            return {'resources': self.clinic_lookup.find_all()}
        coords = (user_location.get('lat'), user_location.get('lon'))
        clinics = self.clinic_lookup.find_nearby(coords)
        return {'resources': clinics}
