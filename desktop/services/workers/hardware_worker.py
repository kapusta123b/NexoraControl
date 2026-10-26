from PySide6.QtCore import Slot

from api.client import NexoraClient

from services.workers.base_worker import BaseWorker


class HardwareWorker(BaseWorker):
    def __init__(self, client: NexoraClient, agent_id: int | None) -> None:
        super().__init__()
        self.client = client
        self.agent_id = agent_id

    @Slot()
    def run(self) -> None:
        self._run_async(self.client.hardware.get_system_information, self.agent_id)
