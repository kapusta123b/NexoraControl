import json
from PySide6.QtCore import QObject, Signal, Slot, QUrl

from api.client import NexoraClient

from PySide6.QtWebSockets import QWebSocket


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
        query_params: dict,
    ) -> None:
        super().__init__()
        self.client = client
        self.agent_id = agent_id
        self.hours = hours
        self.metric_type = metric_type
        self.query_params = query_params

    @Slot()
    def run(self) -> None:
        try:
            metrics = self.client.get_agent_metrics(
                agent_id=self.agent_id,
                hours=self.hours,
                metric_type=self.metric_type,
                query_params=self.query_params
            )

            self.success.emit(metrics)
        except Exception as exc:
            self.error.emit(f"Error metric: {exc}")
        finally:
            self.finished.emit()


class LiveMetricsWorker(QObject):
    finished = Signal()
    metrics_received = Signal(dict)
    error = Signal(str)

    def __init__(self, url: str):
        super().__init__()
        self.url = QUrl(url)
        self.socket = None

    @Slot()
    def run(self):
        self.socket = QWebSocket()

        self.socket.textMessageReceived.connect(self.on_message_received)
        self.socket.error.connect(self.on_error)

        self.socket.open(self.url)

    def on_message_received(self, message: str):
        try:
            data = json.loads(message)

            self.metrics_received.emit(data)

        except Exception as e:
            self.error.emit(f"Parser error: {e}")

    def on_error(self, error_code):
        self.error.emit(f"WebSocket Error: {self.socket.errorString()}")

    @Slot()
    def stop(self):
        if self.socket:
            self.socket.close()
        self.finished.emit()
