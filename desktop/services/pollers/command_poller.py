from api.client import NexoraClient

from services.workers.command_worker import CommandsWorker

from services.stores.agent_command_store import CommandsStore

from services.pollers.base_poller import BasePoller


class CommandPoller(BasePoller):

    def __init__(self, client: NexoraClient, commands_store: CommandsStore):
        super().__init__(client)

        self.commands_store = commands_store

        self.agent_id = {}

    def on_clicked(
        self, agent_id: int | None = None, command_type: str | None = None
    ) -> None:
        if agent_id:
            if self.agent_id != agent_id:
                self._cancel_all_requests()

            self.agent_id = agent_id

        if command_type:
            self._start_commands_worker(command_type)

            return

        self.refresh()

    def refresh(self, force: bool = False) -> None:
        if not force:
            if not self.client.base_url or self.agent_id is None:
                return

        self._start_commands_worker()

    def _start_commands_worker(
        self, command_type: str | None = None, payload: dict = {}, params: dict = {}
    ) -> None:
        worker = CommandsWorker(self.client, self.agent_id)

        if command_type:
            self._start_worker(
                worker=worker,
                worker_slot=lambda: worker.create_agent_command(command_type, payload),
                success_callback=self._on_command_created,
            )
        else:
            self._start_worker(
                worker=worker,
                worker_slot=lambda: worker.get_agent_commands(params),
                success_callback=self.commands_store.set_commands,
            )

    def _on_command_created(self) -> None:
        self._start_commands_worker()
