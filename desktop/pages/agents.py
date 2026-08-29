from datetime import datetime, timedelta

from pages.agent_detail import AgentDetailController

from services.agent_card import AgentCardWidget
from services.agent_poller import AgentPoller
from services.agent_store import AgentStore
from ui.main_window import Ui_MainWindow


class AgentsController:
    def __init__(
        self,
        ui: Ui_MainWindow,
        store: AgentStore,
        poller: AgentPoller,
        detail_controller: AgentDetailController,
    ):
        self.ui = ui
        self.store = store
        self.poller = poller
        self.detail_controller = detail_controller

        self.setup_connections()

    def populate_agents(self, agents):
        self.clear_cards()

        layout = self.ui.agent_scroll.layout()

        for agent in agents:
            card = AgentCardWidget(self.ui.agent_scroll)

            card.set_agent(agent)

            card.ui.agent_open_button.clicked.connect(
                lambda checked=False, agent_id=agent["id"], agent_name=agent['name']: self.open_agent(agent_id, agent_name)
            )
            card.open_requested.connect(self.open_agent)

            layout.addWidget(card)

        layout.addStretch(1)

    def open_agent(self, agent_id, agent_name):
        from_timestamp = int((datetime.now() - timedelta(hours=1)).timestamp())
        self.detail_controller.show_agent(agent_id, agent_name, from_timestamp)

        self.ui.content_stack.setCurrentWidget(self.ui.agent_detail)

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
        self.ui.agents_button.clicked.connect(
            lambda checked=False: self.ui.content_stack.setCurrentWidget(
                self.ui.agents_page
            )
        )

        self.store.agents_changed.connect(self.populate_agents)
