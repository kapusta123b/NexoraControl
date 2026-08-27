from services.agent_card import AgentCardWidget
from services.agent_poller import AgentPoller
from services.agent_store import AgentStore


from ui.main_window import Ui_MainWindow


class AgentsController:
    def __init__(self, ui: Ui_MainWindow, store: AgentStore, poller: AgentPoller):
        self.ui = ui
        self.store = store
        self.poller = poller

        self.setup_connections()

    def populate_agents(self, agents):
        self.clear_cards()

        layout = self.ui.agent_scroll.layout()

        for agent in agents:
            card = AgentCardWidget(self.ui.agent_scroll)

            card.ui.agent_open_button.clicked.connect(
                lambda: self.ui.content_stack.setCurrentWidget(self.ui.agent_detail)
            )
            
            card.set_agent(agent)
            layout.addWidget(card)

        layout.addStretch(1)

    def clear_cards(self):
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

    def setup_connections(self):
        self.ui.refresh_agents_button.clicked.connect(self.poller.refresh)

        self.store.agents_changed.connect(self.populate_agents)
