from PySide6.QtCore import QObject, Signal, Slot

from api.client import NexoraClient


class AgentMetricWorker(QObject):
    finished = Signal()
    success = Signal(object)
    error = Signal(str)

    def __init__(
        self,
        client: NexoraClient,
        agent_id: int,
        hours: int,
        metric_type: str,
        partial: bool,
    ) -> None:
        super().__init__()
        self.client = client
        self.agent_id = agent_id
        self.hours = hours
        self.metric_type = metric_type
        self.partial = partial

    @Slot()
    def run(self) -> None:
        try:
            metrics = self.client.get_agent_metrics(
                agent_id=self.agent_id,
                hours=self.hours,
                metric_type=self.metric_type,
                partial=self.partial,
            )

            self.success.emit(metrics)
        except Exception as exc:
            self.error.emit(f"Error metric: {exc}")
        finally:
            self.finished.emit()
