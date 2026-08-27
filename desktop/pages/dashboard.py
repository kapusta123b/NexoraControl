from PySide6.QtWidgets import QHeaderView, QTableWidgetItem

from services.agent_poller import AgentPoller
from services.agent_store import AgentStore

from datetime import datetime

from ui.main_window import Ui_MainWindow


class DashboardController:
    def __init__(self, ui: Ui_MainWindow, store: AgentStore, poller: AgentPoller):
        self.ui = ui
        self.store = store
        self.poller = poller

        self.ui.agents_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.setup_connections()

    def setup_connections(self):
        self.ui.refresh_table_button.clicked.connect(self.poller.refresh)

        self.store.agents_changed.connect(self.populate_agents_table)

    def populate_agents_table(self, agents: list[dict]):
        if not isinstance(agents, list):
            QMessageBox.critical(
                None,
                "Error!",
                "Invalid agent data received.",
            )
            return

        self.ui.agents_count.setText(str(len(agents)))

        table = self.ui.agents_table
        table.setRowCount(len(agents))

        online_count = sum(agent["status"] == "ON" for agent in agents)
        offline_count = len(agents) - online_count

        for row, agent in enumerate(agents):
            table.setItem(
                row,
                0,
                QTableWidgetItem(agent["status"]),
            )
            table.setItem(
                row,
                1,
                QTableWidgetItem(agent["name"]),
            )
            table.setItem(
                row,
                2,
                QTableWidgetItem(agent["hostname"]),
            )
            table.setItem(
                row,
                3,
                QTableWidgetItem(str(agent["cpu_load"])),
            )
            table.setItem(
                row,
                4,
                QTableWidgetItem(str(agent["ram_load"])),
            )

            last_seen = agent.get("last_seen")

            if last_seen:
                dt = datetime.fromisoformat(last_seen)
                last_seen_text = dt.strftime("%d %b %Y, %H:%M:%S")
            else:
                last_seen_text = "Never"

            table.setItem(
                row,
                5,
                QTableWidgetItem(last_seen_text),
            )

        self.ui.online_count.setText(str(online_count))
        self.ui.offline_count.setText(str(offline_count))
