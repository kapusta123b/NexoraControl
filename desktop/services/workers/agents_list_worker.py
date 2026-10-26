from PySide6.QtCore import QObject, Signal, Slot

from api.client import NexoraClient

from services.workers.base_worker import BaseWorker


class AgentsListWorker(BaseWorker):
    def __init__(self, client: NexoraClient) -> None:
        super().__init__()
        self.client = client

    @Slot()
    def run(self) -> None:
        self._run_async(self.client.agents.get_list)
