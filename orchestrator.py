from typing import Dict, Any
from services.session_service import InMemorySessionService
from agents.intake_agent import IntakeAgent
from agents.triage_agent import TriageAgent
from agents.careplan_agent import CarePlanAgent
from agents.resource_agent import ResourceAgent
from model_client import GeminiClient

session_service = InMemorySessionService()
model_client = GeminiClient()

intake_agent = IntakeAgent()
triage_agent = TriageAgent(model_client=model_client)
careplan_agent = CarePlanAgent(model_client=model_client)
resource_agent = ResourceAgent()

async def handle_message(user_id: str, message: str, location: Dict[str, float] = None):
    session = session_service.get_session(user_id)
    intake = intake_agent.run(message, session)
    triage = await triage_agent.run(intake, session)
    careplan = await careplan_agent.run(triage, intake, session)
    resources = resource_agent.run(intake, user_location=location)
    result = {
        'intake': intake,
        'triage': triage,
        'careplan': careplan,
        'resources': resources,
    }
    session_service.save_session(user_id, session)
    return result
