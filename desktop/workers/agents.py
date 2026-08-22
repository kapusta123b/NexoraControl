from PySide6.QtCore import QObject, Signal, Slot


class AgentsWorker(QObject):
    finished = Signal()
    success = Signal(list)
    error = Signal(str)

    def __init__(self, client):
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
