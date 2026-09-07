from PySide6.QtCore import QObject, QThread, QTimer

from api.client import NexoraClient

from services.stores.metric_store import MetricStore

from workers.metric_worker import AgentMetricWorker

from ..box_messages import MessageBox


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

        self.is_polling = False
        self.api_error_shown = False

        self._active_workers = []

        self.timer = QTimer(self)
        self.timer.setInterval(5000)
        self.timer.timeout.connect(self.refresh)

    def on_clicked(self, agent_id: int, metric_type: str = None) -> None:
        self.agent_id = agent_id

        if not self.metric_type:
            self.metric_type = "resources"

        else:
            self.metric_type = metric_type

        if self.client.base_url and not self.timer.isActive():
            self.timer.start()

        self.refresh()

    def change_hours(self, hours: int):
        self.from_hours = hours

        self.refresh(force=True)

    def stop_polling(self) -> None:
        if self.timer.isActive():
            self.timer.stop()

    def refresh(self, force: bool = False) -> None:
        if not force:
            if self.is_polling or not self.client.base_url or self.agent_id is None:
                return

        self.is_polling = True

        self._start_metric_worker()

    def _start_metric_worker(self) -> None:
        thread = QThread(self)
        worker = AgentMetricWorker(
            self.client, self.agent_id, self.from_hours, self.metric_type
        )
        worker.moveToThread(thread)

        worker_context = {"thread": thread, "worker": worker}

        self._active_workers.append(worker_context)

        thread.started.connect(worker.run)
        worker.success.connect(self.metric_store.set_metrics)
        worker.error.connect(self.show_api_error)

        worker.finished.connect(thread.quit)
        worker.finished.connect(worker.deleteLater)

        def cleanup():
            thread.deleteLater()
            if worker_context in self._active_workers:
                self._active_workers.remove(worker_context)

            self.is_polling = False

        thread.finished.connect(cleanup)

        thread.start()

    def on_finished(self):
        self.is_polling = False

    def show_api_error(self, message: str = None) -> None:
        if not self.api_error_shown:
            self.api_error_shown = True
            self.stop_polling()

            MessageBox().show_message(
                "critical",
                "API error",
                message or "API connection failed! Please change the API URL",
            )
