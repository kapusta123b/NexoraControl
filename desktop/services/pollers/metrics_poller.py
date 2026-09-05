from PySide6.QtCore import QObject, QThread, QTimer

from api.client import NexoraClient

from services.stores.metric_stores import MetricStore

from workers.metric_worker import AgentResourceMetricWorker

from ..box_messages import MessageBox


class AgentMetricPoller(QObject):
    def __init__(self, client: NexoraClient, store: MetricStore):
        super().__init__()

        self.client = client
        self.store = store

        self.thread: QThread | None = None
        self.worker: AgentResourceMetricWorker | None = None
        self.is_polling = False
        self.pending_refresh = False
        self.api_error_shown = False

        self.agent_id: int | None = None
        self.from_timestamp: int | None = None

        self.setup_timer()

    def setup_timer(self) -> None:
        if self.client.base_url:
            self.timer = QTimer(self)
            self.timer.setInterval(5000)
            self.timer.timeout.connect(self.refresh)
            self.timer.start()

    def set_agent(self, agent_id: int, from_timestamp: int) -> None:
        self.agent_id = agent_id
        self.from_timestamp = from_timestamp

    def refresh(self, force=False) -> None:
        if self.is_polling:
            if force:
                self.pending_refresh = True
            return

        if (
            not self.client.base_url
            or self.agent_id is None
            or self.from_timestamp is None
        ):
            return

        self.is_polling = True

        self.thread = QThread()

        self.worker = AgentResourceMetricWorker(
            client=self.client,
            agent_id=self.agent_id,
            timestamp=self.from_timestamp,
        )

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)

        self.worker.success.connect(self.on_success)

        self.worker.error.connect(self.show_api_error)

        self.worker.finished.connect(self.thread.quit)

        self.worker.finished.connect(self.worker.deleteLater)

        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.finished.connect(self.on_finished)

        self.thread.start()

    def on_success(self, agent_id: int, from_timestamp: int, metrics: dict) -> None:
        if agent_id != self.agent_id or from_timestamp != self.from_timestamp:
            return

        self.api_error_shown = False
        self.store.set_metrics(metrics)

    def on_finished(self) -> None:
        self.is_polling = False
        self.thread = None
        self.worker = None

        if self.pending_refresh:
            self.pending_refresh = False
            self.refresh()

    def show_api_error(self, message=None) -> None:
        if not self.api_error_shown:
            self.api_error_shown = True

            MessageBox().show_message(
                "critical",
                "API error",
                "API connection failed! Please change the API URL",
            )
