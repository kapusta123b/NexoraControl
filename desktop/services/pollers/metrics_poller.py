from PySide6.QtCore import QObject
from api.client import NexoraClient
from services.stores.metric_store import MetricStore
from services.pollers.base_poller import BasePoller
from services.workers.metric_worker import AgentMetricWorker


class AgentMetricPoller(BasePoller):
    def __init__(self, client: NexoraClient, metric_store: MetricStore):
        super().__init__(client)
        self.metric_store = metric_store

        self.agent_id: int | None = None
        self.from_hours = 1
        self.metric_type: str = "resources"
        self.query_params = {}

    def on_clicked(
        self, agent_id: int = None, metric_type: str = None, query_params: dict = {}
    ) -> None:
        if agent_id:
            self.agent_id = agent_id

        self.metric_type = metric_type or "resources"

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

        worker = AgentMetricWorker(
            self.client,
            self.agent_id,
            self.from_hours,
            self.metric_type,
            self.query_params,
        )

        self._start_worker(
            worker=worker,
            worker_slot=worker.run,
            success_callback=self.metric_store.set_history,
        )
