from PySide6.QtCore import Slot

from api.client import NexoraClient

from services.workers.base_worker import BaseWorker


class CommandsWorker(BaseWorker):
    def __init__(self, client: NexoraClient, agent_id: int):
        super().__init__()
        self.client = client
        self.agent_id = agent_id

    @Slot()
    def get_agent_commands(self, count: int = 5):
        self._run_async(self.client.commands.get_commands, self.agent_id, count)

    @Slot()
    def create_agent_command(self, command_type: str, payload: dict = {}):
        self._run_async(
            self.client.commands.create_command, self.agent_id, command_type, payload
        )
