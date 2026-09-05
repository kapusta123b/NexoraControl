from PySide6.QtCore import QObject, Signal, Slot

from api.client import NexoraClient


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