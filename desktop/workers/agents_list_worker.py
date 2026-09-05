from PySide6.QtCore import QObject, Signal, Slot

from api.client import NexoraClient


class AgentsListWorker(QObject):
    finished = Signal()
    success = Signal(list)
    error = Signal(str)

    def __init__(self, client: NexoraClient):
        super().__init__()
        self.client = client

    @Slot()
    def run(self):
        try:
            agents = self.client.get_agents()
            self.success.emit(agents)
        except Exception as exc:
            self.error.emit(str(exc))
        finally:
            self.finished.emit()