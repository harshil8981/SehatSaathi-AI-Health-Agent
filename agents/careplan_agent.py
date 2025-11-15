from typing import Dict, Any

class CarePlanAgent:
    def __init__(self, model_client=None):
        self.model = model_client

    async def run(self, triage: Dict[str, Any], intake: Dict[str, Any], session: Dict[str, Any]):
        prompt = (
            'You are a patient education assistant. Produce a short care plan (3-5 steps) and red flags.\n'
            f"Symptoms: {intake.get('symptoms')}\nTriage: {triage if isinstance(triage, str) else repr(triage)}"
        )
        resp = self.model.generate(prompt) if self.model else {'care_plan': ['Rest', 'Hydrate'], 'red_flags': ['Difficulty breathing']}
        session.setdefault('care_plans', []).append(resp)
        return resp
