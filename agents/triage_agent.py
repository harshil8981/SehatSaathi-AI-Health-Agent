from typing import Dict, Any

class TriageAgent:
    def __init__(self, model_client=None):
        self.model = model_client

    async def run(self, intake: Dict[str, Any], session: Dict[str, Any]):
        prompt = (
            'You are a triage assistant. Given the user\'s symptoms, respond JSON with fields: '
            'urgency (LOW/MEDIUM/HIGH), reason, next_steps (list). Keep reasons short.\n\n'
            f"Symptoms: {intake.get('symptoms')}"
        )
        resp = self.model.generate(prompt) if self.model else '{"urgency": "LOW", "reason": "Mock", "next_steps": ["Rest"]}'
        session['triage_raw'] = resp
        return resp
