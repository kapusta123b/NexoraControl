from PySide6.QtCore import QObject, QThread

from api.client import NexoraClient

from services.stores.metric_store import MetricStore

from workers.metric_worker import AgentMetricWorker

from ..widgets.box_messages import MessageBox


class AgentMetricPoller(QObject):
    def __init__(
        self,
        client: NexoraClient,
        metric_store: MetricStore,
    ):
        super().__init__()

        self.client = client
        self.metric_store = metric_store

        self.agent_id: int | None = None

        self.from_hours = 1
        self.metric_type: str = None
        self.query_params = {}

        self.is_polling = False
        self.api_error_shown = False

        self._active_workers = []

    def on_clicked(
        self, agent_id: int = None, metric_type: str = None, query_params: dict = {}
    ) -> None:
        if agent_id:
            self.agent_id = agent_id

        if not metric_type:
            self.metric_type = "resources"

        else:
            self.metric_type = metric_type

        if isinstance(query_params, dict):

            self.query_params = query_params

        self.refresh()

    def change_hours(self, hours: int):
        self.from_hours = hours

        self.refresh(force=True)

    def refresh(self, force: bool = False) -> None:
        if not force:
            if self.is_polling or not self.client.base_url or self.agent_id is None:
                return

        self.is_polling = True

        self._start_metric_worker()

    def _start_metric_worker(self) -> None:
        thread = QThread(self)
        worker = AgentMetricWorker(
            self.client,
            self.agent_id,
            self.from_hours,
            self.metric_type,
            self.query_params,
        )
        worker.moveToThread(thread)

        worker_context = {"thread": thread, "worker": worker}
        self._active_workers.append(worker_context)

        thread.started.connect(worker.run)

        worker.success.connect(self.metric_store.set_history)
        worker.error.connect(self.show_api_error)

        worker.finished.connect(thread.quit)
        worker.finished.connect(worker.deleteLater)

        def cleanup() -> None:
            thread.deleteLater()
            if worker_context in self._active_workers:
                self._active_workers.remove(worker_context)

            self.is_polling = False

        thread.finished.connect(cleanup)
        thread.start()

    def show_api_error(self, message: str | None = None) -> None:
        if not self.api_error_shown:
            self.api_error_shown = True

            MessageBox().show_message(
                "critical",
                "API error",
                message or "API connection failed! Please change the API URL",
            )
