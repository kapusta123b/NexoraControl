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
        self._run_async(self.client.get_detail_agent, self.agent_id)


class RecentCommandsWorker(BaseWorker):
    def __init__(self, client: NexoraClient, agent_id: int):
        super().__init__()
        self.client = client
        self.agent_id = agent_id

    @Slot()
    def get_agent_commands(self):
        self._run_async(self.client.get_agent_commands, self.agent_id, count=5)

    @Slot()
    def create_agent_command(self, command_type: str):
        self._run_async(self.client.create_agent_command, self.agent_id, command_type)
