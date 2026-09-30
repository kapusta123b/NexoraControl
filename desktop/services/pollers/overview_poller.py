from PySide6.QtCore import QThread, QTimer

from api.client import NexoraClient

from services.pollers.base_poller import BasePoller

from services.stores.agent_command_store import CommandsStore
from services.stores.agent_store import DetailAgentStore

from services.widgets.box_messages import MessageBox

from services.workers.overview_worker import OverviewWorker, RecentCommandsWorker


class DetailOverviewPoller(BasePoller):

    def __init__(
        self,
        client: NexoraClient,
        detail_agent_store: DetailAgentStore,
        commands_store: CommandsStore,
    ) -> None:
        super().__init__(client)

        self.client = client
        self.detail_agent_store = detail_agent_store
        self.commands_store = commands_store

        self.agent_id: int | None = None

        self.timer = QTimer(self)
        self.timer.setInterval(5000)
        self.timer.timeout.connect(self.refresh_all)

    def on_clicked(self, agent_id: int = None, command_type: str = None) -> None:
        if agent_id:
            if self.agent_id != agent_id:
                self._cancel_all_requests()

            self.agent_id = agent_id

        if command_type:
            self._start_commands_worker(command_type)
            return

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
        worker = OverviewWorker(self.client, self.agent_id)

        self._start_worker(
            worker=worker,
            worker_slot=worker.run,
            success_callback=self.detail_agent_store.set_agent,
        )

    def _start_commands_worker(self, command_type: str = None) -> None:
        worker = RecentCommandsWorker(self.client, self.agent_id)

        if command_type:
            self._start_worker(
                worker=worker,
                worker_slot=lambda: worker.create_agent_command(command_type),
                success_callback=self._on_command_created,
            )
        else:
            self._start_worker(
                worker=worker,
                worker_slot=worker.get_agent_commands,
                success_callback=self.commands_store.set_commands,
            )

    def _on_command_created(self) -> None:
        self._start_overview_worker()
