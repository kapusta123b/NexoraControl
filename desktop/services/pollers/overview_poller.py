from PySide6.QtCore import QObject, QThread, QTimer

from api.client import NexoraClient

from services.box_messages import MessageBox
from services.stores.agent_store import DetailAgentStore

from workers.overview_worker import OverviewWorker


class DetailOverviewPoller(QObject):

    def __init__(self, client: NexoraClient, store: DetailAgentStore):
        super().__init__()

        self.client = client
        self.store = store

        self.thread: QThread | None = None
        self.worker: OverviewWorker | None = None
        self.is_polling = False
        self.api_error_shown = False

        self.timer = QTimer(self)
        self.timer.setInterval(5000)
        self.timer.timeout.connect(self.refresh)

    def on_clicked(self, agent_id: int) -> None:
        self.agent_id = agent_id

        if self.client.base_url and not self.timer.isActive():
            self.timer.start()

        self.refresh()

    def stop_polling(self) -> None:
        if self.timer.isActive():
            print('stop polling')
            self.timer.stop()

    def refresh(self) -> None:
        if self.is_polling or not self.client.base_url:
            return

        self.is_polling = True

        self.thread = QThread()
        self.worker = OverviewWorker(self.client, self.agent_id)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)

        self.worker.success.connect(self.store.set_agent)
        self.worker.error.connect(self.show_api_error)

        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.finished.connect(self.on_finished)

        self.thread.start()

    def on_finished(self) -> None:
        self.is_polling = False
        self.thread = None
        self.worker = None

    def show_api_error(self, message=None) -> None:
        if not self.api_error_shown:
            self.api_error_shown = True
            self.timer.stop()

            MessageBox().show_message(
                "critical",
                "API error",
                "API connection failed! Please change the API URL",
            )
