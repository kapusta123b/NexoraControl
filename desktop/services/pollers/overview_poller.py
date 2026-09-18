from PySide6.QtCore import QObject, QThread, QTimer

from api.client import NexoraClient

from services.stores.agent_command_store import CommandsStore
from services.widgets.box_messages import MessageBox
from services.stores.agent_store import DetailAgentStore

from workers.overview_worker import OverviewWorker, RecentCommandsWorker


class DetailOverviewPoller(QObject):

    def __init__(
        self,
        client: NexoraClient,
        detail_agent_store: DetailAgentStore,
        commands_store: CommandsStore,
    ):
        super().__init__()

        self.client = client
        self.detail_agent_store = detail_agent_store
        self.commands_store = commands_store

        self.agent_id: int | None = None
        self.is_polling = False
        self.api_error_shown = False

        self._active_workers = []

        self.timer = QTimer(self)
        self.timer.setInterval(5000)
        self.timer.timeout.connect(self.refresh_all)

    def on_clicked(self, agent_id: int) -> None:
        self.agent_id = agent_id

        if self.client.base_url and not self.timer.isActive():
            self.timer.start()

        self.refresh_all()

    def stop_polling(self) -> None:
        if self.timer.isActive():
            self.timer.stop()

    def refresh_all(self) -> None:
        if self.is_polling or not self.client.base_url or self.agent_id is None:
            return

        self.is_polling = True
        
        self._start_overview_worker()
        self._start_commands_worker()

    def _start_overview_worker(self) -> None:
        thread = QThread(self)
        worker = OverviewWorker(self.client, self.agent_id)
        worker.moveToThread(thread)

        worker_context = {"thread": thread, "worker": worker}

        self._active_workers.append(worker_context)

        thread.started.connect(worker.run)
        worker.success.connect(self.detail_agent_store.set_agent)
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

    def _start_commands_worker(self) -> None:
        thread = QThread(self)
        worker = RecentCommandsWorker(self.client, self.agent_id)
        worker.moveToThread(thread)

        worker_context = {"thread": thread, "worker": worker}

        self._active_workers.append(worker_context)

        thread.started.connect(worker.run)
        worker.success.connect(self.commands_store.set_commands)
        worker.error.connect(self.show_api_error)

        worker.finished.connect(thread.quit)
        worker.finished.connect(worker.deleteLater)

        def cleanup():
            thread.deleteLater()
            if worker_context in self._active_workers:
                self._active_workers.remove(worker_context)

        thread.finished.connect(cleanup)
        thread.start()

    def show_api_error(self, message: str = None) -> None:
        if not self.api_error_shown:
            self.api_error_shown = True
            self.stop_polling()

            MessageBox().show_message(
                "critical",
                "API error",
                message or "API connection failed! Please change the API URL",
            )
