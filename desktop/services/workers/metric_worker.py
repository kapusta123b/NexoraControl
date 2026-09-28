import json
from PySide6.QtCore import Signal, Slot, QUrl
from PySide6.QtWebSockets import QWebSocket

from api.client import NexoraClient
from services.workers.base_worker import BaseWorker


class AgentMetricWorker(BaseWorker):
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
    def run(self):
        self._run_async(
            self.client.get_agent_metrics,
            agent_id=self.agent_id,
            hours=self.hours,
            metric_type=self.metric_type,
            query_params=self.query_params,
        )


class LiveMetricsWorker(BaseWorker):
    metrics_received = Signal(dict)

    def __init__(self, url: str):
        super().__init__(None)
        self.url = QUrl(url)
        self.socket = None

    @Slot()
    def run(self):
        self.socket = QWebSocket()
        self.socket.textMessageReceived.connect(self.on_message_received)
        self.socket.error.connect(self.on_error)
        self.socket.disconnected.connect(self._on_disconnected)
        self.socket.open(self.url)

    def on_message_received(self, message: str):
        try:
            data = json.loads(message)
            self.metrics_received.emit(data)
        except Exception as e:
            self.error.emit(f"Parser error: {e}")

    def on_error(self, error_code):
        if self.socket:
            self.error.emit(f"WebSocket Error: {self.socket.errorString()}")
        self._clean_up()

    def _on_disconnected(self):
        self._clean_up()

    @Slot()
    def stop(self):
        if self.socket and self.socket.isValid():
            self.socket.close()
        else:
            self._clean_up()

    def _clean_up(self):
        if self.socket:
            try:
                self.socket.textMessageReceived.disconnect()
                self.socket.error.disconnect()
                self.socket.disconnected.disconnect()
            except RuntimeError:
                pass
            self.socket.deleteLater()
            self.socket = None

        self.finished.emit()
