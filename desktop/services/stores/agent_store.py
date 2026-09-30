from PySide6.QtCore import QObject, Signal


class AgentsStore(QObject):
    agents_changed = Signal(list)

    def __init__(self) -> None:
        super().__init__()
        self._agents: list[dict] = []

    def set_agents(self, agents: list[dict]) -> None:
        self._agents = agents
        self.agents_changed.emit(agents)

    def get_agents(self) -> list[dict]:
        return self._agents


class DetailAgentStore(QObject):
    agent_changed = Signal(dict)

    def __init__(self) -> None:
        super().__init__()
        self._agent = {}

    def set_agent(self, agent: dict | None) -> None:
        self._agent = agent
        self.agent_changed.emit(agent)

    def get_agent(self) -> dict | None:
        return self._agent
