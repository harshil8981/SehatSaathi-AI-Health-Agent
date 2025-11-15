from typing import Dict, Any
import uuid

class LongRunningManager:
    def __init__(self):
        self.tasks: Dict[str, Dict[str, Any]] = {}

    def create_task(self, payload: Dict[str, Any]) -> str:
        task_id = str(uuid.uuid4())
        self.tasks[task_id] = {'state': 'PENDING', 'payload': payload}
        return task_id

    def update_task(self, task_id: str, state: str, result: Dict[str, Any] = None):
        if task_id in self.tasks:
            self.tasks[task_id]['state'] = state
            if result is not None:
                self.tasks[task_id]['result'] = result

    def get_task(self, task_id: str) -> Dict[str, Any]:
        return self.tasks.get(task_id, {})
