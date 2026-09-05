from PySide6.QtCore import QObject, QThread, QTimer

from api.client import NexoraClient

from services.stores.agent_store import AgentsStore

from workers.agents_list_worker import AgentsListWorker

from ..box_messages import MessageBox


class AgentsListPoller(QObject):
    def __init__(self, client: NexoraClient, store: AgentsStore):
        super().__init__()

        self.client = client
        self.store = store

        self.thread: QThread | None = None
        self.worker: AgentsListWorker | None = None
        self.is_polling = False

        self.api_error_shown = False

        self.setup_timer()

        self.refresh()

    def setup_timer(self) -> None:
        if self.client.base_url:
            self.timer = QTimer(self)
            self.timer.setInterval(5000)
            self.timer.timeout.connect(self.refresh)
            self.timer.start()

    def refresh(self) -> None:
        if self.is_polling or not self.client.base_url:
            return

        self.is_polling = True

        self.thread = QThread()
        self.worker = AgentsListWorker(self.client)

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)

        self.worker.success.connect(self.store.set_agents)

        self.worker.error.connect(self.show_api_error)

        self.worker.finished.connect(self.thread.quit)

        self.worker.finished.connect(self.worker.deleteLater)

        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.finished.connect(self.on_finished)

        self.thread.start()

    def on_finished(self):
        self.is_polling = False
        self.thread = None
        self.worker = None

    def show_api_error(self, message=None) -> None:
        if not self.api_error_shown:
            self.api_error_shown = True

            MessageBox().show_message(
                "critical",
                "API error",
                "API connection failed! Please change the API URL",
            )
