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