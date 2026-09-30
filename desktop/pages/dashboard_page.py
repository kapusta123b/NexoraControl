from PySide6.QtWidgets import QHeaderView

from services.utils import update_or_create_row_item
from services.pollers.agents_list_poller import AgentsListPoller
from services.stores.agent_store import AgentsStore

from datetime import datetime

from ui.main_window import Ui_MainWindow


class DashboardController:
    def __init__(
        self, ui: Ui_MainWindow, store: AgentsStore, poller: AgentsListPoller
    ) -> None:
        self.ui = ui
        self.store = store
        self.dashboard_poller = poller

        self.ui.agents_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self._setup_connections()

    def _setup_connections(self) -> None:
        self.ui.refresh_table_button.clicked.connect(self.dashboard_poller.refresh)

        self.store.agents_changed.connect(self.populate_agents_table)

    def populate_agents_table(self, agents: list[dict]) -> None:
        table = self.ui.agents_table

        online_count = sum(agent["status"] == "ON" for agent in agents)
        offline_count = len(agents) - online_count

        for agent in agents:
            name = agent["name"]
            row = -1

            for r in range(table.rowCount()):
                item = table.item(r, 1)
                if item and item.text() == name:
                    row = r

                    break

            if row == -1:
                row = table.rowCount()
                table.insertRow(row)

            last_seen = agent.get("last_seen")

            if last_seen:
                dt = datetime.fromisoformat(last_seen)
                last_seen_text = dt.strftime("%d %b %Y, %H:%M:%S")
            else:
                last_seen_text = "Never"

            update_or_create_row_item(table, row, 0, agent["status"])
            update_or_create_row_item(table, row, 1, name)
            update_or_create_row_item(table, row, 2, agent["hostname"])
            update_or_create_row_item(table, row, 3, str(agent["cpu_load"]))
            update_or_create_row_item(table, row, 4, str(agent["ram_load"]))
            update_or_create_row_item(table, row, 5, last_seen_text)

        self.ui.online_count.setText(str(online_count))
        self.ui.offline_count.setText(str(offline_count))
        self.ui.agents_count.setText(str(len(agents)))
