from typing import Dict, Any

class IntakeAgent:
    """Collects symptoms and basic metadata from user input and stores them in session."""

    def __init__(self):
        pass

    def run(self, message: str, session: Dict[str, Any]):
        symptoms = message.strip()
        intake = {
            'symptoms': symptoms,
            'raw_message': message,
        }
        session['intake'] = intake
        return intake
