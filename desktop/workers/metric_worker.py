from PySide6.QtCore import QObject, Signal, Slot

from api.client import NexoraClient


class AgentMetricWorker(QObject):
    finished = Signal()
    success = Signal(dict)
    error = Signal(str)

    def __init__(
        self,
        client: NexoraClient,
        agent_id: int,
        hours: int,
        metric_type: str,
    ):
        super().__init__()

        self.client = client
        self.agent_id = agent_id
        self.hours = hours
        self.metric_type = metric_type

    @Slot()
    def run(self):
        try:
            metrics = self.client.get_agent_metrics(
                self.agent_id,
                self.hours,
                self.metric_type
            )
            self.success.emit(metrics)

        except Exception as exc:
            self.error.emit(str(exc))

        finally:
            self.finished.emit()
