from PySide6.QtCore import QObject, Signal, Slot

from api.client import NexoraClient

import traceback

class OverviewWorker(QObject):
    finished = Signal()
    success = Signal(dict)
    error = Signal(str)

    def __init__(self, client: NexoraClient, agent_id: int):
        super().__init__()
        self.client = client
        self.agent_id = agent_id

    @Slot()
    def run(self):
        try:
            agent = self.client.get_detail_agent(self.agent_id)

            self.success.emit(agent)

        except Exception as exc:
            self.error.emit(str(exc))
        finally:
            self.finished.emit()



class RecentCommandsWorker(QObject):
    finished = Signal()
    success = Signal(list)
    error = Signal(str)

    def __init__(self, client: NexoraClient, agent_id: int):
        super().__init__()
        self.client = client
        self.agent_id = agent_id

    @Slot()
    def run(self):
        try:
            commands = self.client.get_agent_commands(self.agent_id, 5)

            self.success.emit(commands)
        except Exception as exc:
            self.error.emit(str(exc))
        finally:
            self.finished.emit()