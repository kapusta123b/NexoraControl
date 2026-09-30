from pages.agent_detail_page import AgentDetailController

from services.pollers.agents_list_poller import AgentsListPoller
from services.widgets.agent_card import AgentCardWidget
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

        self.agent_cards = []

        self.ui.search_input_line.textChanged.connect(self.filter_agents)

        self.setup_connections()

    def setup_connections(self) -> None:
        self.ui.refresh_agents_button.clicked.connect(self.poller.refresh)
        self.ui.agents_button.clicked.connect(
            lambda checked=False: self.ui.content_stack.setCurrentWidget(
                self.ui.agents_page
            )
        )

        self.store.agents_changed.connect(self.populate_agents)

    def populate_agents(self, agents: list[dict]) -> None:
        self.clear_cards()

        layout = self.ui.agent_scroll.layout()
        if layout is None:
            return

        for agent in agents:
            card = AgentCardWidget(self.ui.agent_scroll)
            card.set_agent(agent)

            card.ui.agent_open_button.clicked.connect(
                lambda a=agent: self.open_agent(a)
            )
            card.open_requested.connect(lambda a=agent: self.open_agent(a))

            search_string = f"{agent['name']} {agent['ip']}".lower()

            self.agent_cards.append((card, search_string))
            layout.addWidget(card)

        layout.addStretch(1)

        self.filter_agents(self.ui.search_input_line.text())

    def open_agent(self, agent: dict) -> None:
        self.detail_controller.set_agent(agent=agent)

        self.ui.content_stack.setCurrentWidget(self.ui.agent_detail_page)
        self.ui.agent_detail_stacked_content.setCurrentWidget(
            self.ui.overview_detail_page
        )

    def filter_agents(self, text):
        search_query = text.strip().lower()

        for card_widget, search_string in self.agent_cards:
            if not search_query or search_query in search_string:
                card_widget.show()
            else:
                card_widget.hide()

    def clear_cards(self) -> None:
        self.agent_cards = []

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
                if item.spacerItem() is not None:
                    del item
