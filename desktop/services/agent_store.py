from PySide6.QtCore import QObject, Signal


class AgentStore(QObject):
    agents_changed = Signal(list)

    def __init__(self):
        super().__init__()
        self._agents: list[dict] = []

    def set_agents(self, agents: list[dict]) -> None:
        self._agents = agents
        self.agents_changed.emit(agents)

    def get_agents(self) -> list[dict]:
        return self._agents


class MetricStore(QObject):
    metrics_changed = Signal(dict)

    def __init__(self):
        super().__init__()
        self._metrics: dict | None = None

    def set_metrics(self, metrics: dict) -> None:
        self._metrics = metrics
        self.metrics_changed.emit(metrics)

    def get_metrics(self) -> dict | None:
        return self._metrics
