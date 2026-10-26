from PySide6.QtCore import Slot

from api.client import NexoraClient

from services.workers.base_worker import BaseWorker


class OverviewWorker(BaseWorker):
    def __init__(self, client: NexoraClient, agent_id: int):
        super().__init__()
        self.client = client
        self.agent_id = agent_id

    @Slot()
    def run(self):
        self._run_async(self.client.agents.get_detail, self.agent_id)
