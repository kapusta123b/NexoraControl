from PySide6.QtCore import QObject, Signal, Slot

from api.client import NexoraClient


class AgentResourceMetricWorker(QObject):
    finished = Signal()
    success = Signal(int, int, dict)
    error = Signal(str)

    def __init__(
        self,
        client: NexoraClient,
        agent_id: int,
        timestamp: int,
    ):
        super().__init__()

        self.client = client
        self.agent_id = agent_id
        self.timestamp = timestamp

    @Slot()
    def run(self):
        try:
            metrics = self.client.get_agent_resource_metrics(
                self.agent_id,
                self.timestamp,
            )

            self.success.emit(self.agent_id, self.timestamp, metrics)

        except Exception as exc:
            self.error.emit(str(exc))

        finally:
            self.finished.emit()
