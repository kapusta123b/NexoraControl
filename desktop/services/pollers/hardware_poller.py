from api.client import NexoraClient

from services.stores.agent_store import AgentHardwareInfoStore

from services.workers.hardware_worker import HardwareWorker

from services.pollers.base_poller import BasePoller


class HardwarePoller(BasePoller):
    def __init__(
        self, client: NexoraClient, hardware_store: AgentHardwareInfoStore
    ) -> None:
        super().__init__(client)
        self.hardware_store = hardware_store

        self.agent_id: int | None = None

    def on_clicked(
        self,
        agent_id: int | None = None,
    ) -> None:
        if agent_id:
            self.agent_id = agent_id

        self.refresh()

    def refresh(self, force: bool = False) -> None:
        if not force:
            if self.is_polling or not self.client.base_url or self.agent_id is None:
                return

        worker = HardwareWorker(
            self.client,
            self.agent_id,
        )

        self._start_worker(
            worker=worker,
            worker_slot=worker.run,
            success_callback=self.hardware_store.set_system_info,
        )
