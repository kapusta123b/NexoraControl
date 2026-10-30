from PySide6.QtWidgets import QHeaderView

from services.utils.widgets_utils import (
    apply_style_for_tables,
    setup_table,
    update_or_create_row_item,
)
from services.pollers.agents_list_poller import AgentsListPoller
from services.stores.agent_store import AgentsListStore

from datetime import datetime

from ui.main_window import Ui_MainWindow


class DashboardController:
    def __init__(
        self,
        ui: Ui_MainWindow,
        dashboard_store: AgentsListStore,
        poller: AgentsListPoller,
    ) -> None:
        self.ui = ui
        self.dashboard_store = dashboard_store
        self.dashboard_poller = poller

        self.setup_style()
        self.__connect_signals()

    def setup_style(self):
        apply_style_for_tables(self.ui.agents_table)

    def __connect_signals(self) -> None:
        self.ui.refresh_table_button.clicked.connect(self.dashboard_poller.refresh)

        self.dashboard_store.agents_changed.connect(self.populate_agents_table)

    def populate_agents_table(self, agents: list[dict]) -> None:
        table = self.ui.agents_table

        online_count = sum(agent["status"] == "ON" for agent in agents)
        offline_count = len(agents) - online_count

        setup_table(
            table,
            agents,
            ("status", "name", "hostname", "cpu_load", "ram_load", "last_seen"),
        )

        self.ui.online_count.setText(str(online_count))
        self.ui.offline_count.setText(str(offline_count))
        self.ui.agents_count.setText(str(len(agents)))
