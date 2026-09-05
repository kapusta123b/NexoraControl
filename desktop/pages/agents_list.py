from pages.agent_detail import AgentDetailController

from services.pollers.agents_list_poller import AgentsListPoller
from services.agent_card import AgentCardWidget
from services.stores.agent_store import AgentsStore

from ui.main_window import Ui_MainWindow


class AgentsController:
    def __init__(
        self,
        ui: Ui_MainWindow,
        store: AgentsStore,
        poller: AgentsListPoller,
        detail_controller: AgentDetailController,
    ):
        self.ui = ui
        self.store = store
        self.poller = poller
        self.detail_controller = detail_controller

        self.setup_connections()

    def populate_agents(self, agents: list[dict]) -> None:
        self.clear_cards()

        layout = self.ui.agent_scroll.layout()

        for agent in agents:
            card = AgentCardWidget(self.ui.agent_scroll)

            card.set_agent(agent)

            card.ui.agent_open_button.clicked.connect(
                lambda checked=False: self.open_agent(agent)
            )
            card.open_requested.connect(lambda: self.open_agent(agent))

            layout.addWidget(card)

        layout.addStretch(1)

    def open_agent(self, agent: dict) -> None:

        self.detail_controller.set_agent(agent=agent)

        self.ui.content_stack.setCurrentWidget(self.ui.agent_detail_page)
        
        self.ui.agent_detail_stacked_content.setCurrentWidget(
            self.ui.overview_detail_page
        )

    def clear_cards(self) -> None:
        layout = self.ui.agent_scroll.layout()
        if layout is None:
            return

        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()

            if widget is not None:
                widget.setParent(None)
                widget.deleteLater()

            else:
                del item

    def setup_connections(self) -> None:
        self.ui.refresh_agents_button.clicked.connect(self.poller.refresh)
        self.ui.agents_button.clicked.connect(
            lambda checked=False: self.ui.content_stack.setCurrentWidget(
                self.ui.agents_page
            )
        )

        self.store.agents_changed.connect(self.populate_agents)
