from PySide6.QtCore import QTimer

from api.client import NexoraClient
from services.pollers.base_poller import BasePoller
from services.stores.agent_store import AgentsListStore

from services.workers.agents_list_worker import AgentsListWorker


class AgentsListPoller(BasePoller):
    def __init__(self, client: NexoraClient, store: AgentsListStore) -> None:
        super().__init__(client)

        self.agents_store = store

        self._setup_timer()
        self.refresh()

    def _setup_timer(self) -> None:
        if self.client.base_url:
            self.timer = QTimer(self)

            self.timer.setInterval(10000)
            self.timer.timeout.connect(self.refresh)
            self.timer.start()

    def refresh(self) -> None:
        if self.is_polling or not self.client.base_url:
            return

        worker = AgentsListWorker(self.client)

        self._start_worker(worker, worker.run, self.agents_store.set_agents)

    def start_auto_updates(self):
        if hasattr(self, "timer") and not self.timer.isActive():
            self.timer.start()
