from PySide6.QtCore import QObject, Signal


class AgentsListStore(QObject):
    agents_changed = Signal(list)

    def __init__(self) -> None:
        super().__init__()
        self._agents: list[dict] = []

    def set_agents(self, agents: list[dict]) -> None:
        self._agents = agents
        self.agents_changed.emit(agents)

    @property
    def agents(self) -> list[dict | None]:
        return self._agents


class AgentSystemInfoStore(QObject):
    system_info_changed = Signal(dict)

    def __init__(self):
        super().__init__()

        self._agent_system_info = {}

    def set_system_info(self, system_info: dict | None) -> None:
        self._agent_system_info = system_info
        self.system_info_changed.emit(system_info)

    @property
    def system_info(self) -> dict:
        return self._agent_system_info


class DetailAgentStore(QObject):
    agent_changed = Signal(dict)

    def __init__(self) -> None:
        super().__init__()
        self._agent = {}

    def set_agent(self, agent: dict | None) -> None:
        self._agent = agent
        self.agent_changed.emit(agent)

    @property
    def agent(self) -> dict | None:
        return self._agent
