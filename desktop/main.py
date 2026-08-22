import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from api.client import NexoraClient
from ui.main_window import Ui_MainWindow

from datetime import datetime

from PySide6.QtCore import QThread, QTimer

from workers.agents import AgentsWorker


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.client = NexoraClient(
            "http://127.0.0.1:8000/api/v1/",
            "TOKEN",
        )

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh_agents_table)
        self.timer.start(5000)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setup_navigation()

        self.setup_dashboard_buttons()

    def setup_navigation(self):
        self.ui.dashboard_button.clicked.connect(
            lambda: self.ui.content_stack.setCurrentWidget(self.ui.dashboard_page)
        )

        self.ui.agents_button.clicked.connect(
            lambda: self.ui.content_stack.setCurrentWidget(self.ui.agents_page)
        )

    def setup_dashboard_buttons(self):
        self.ui.refresh_table_button.clicked.connect(
            lambda: self.refresh_agents_table()
        )

    def populate_agents_table(self, agents: list[dict]):
        self.ui.agents_count.setText(str(len(agents)))

        table = self.ui.agents_table
        table.setRowCount(len(agents))

        online_count = sum(agent["status"] == "ON" for agent in agents)
        offline_count = len(agents) - online_count

        for row, agent in enumerate(agents):
            table.setItem(row, 0, QTableWidgetItem(agent["status"]))
            table.setItem(row, 1, QTableWidgetItem(agent["name"]))
            table.setItem(row, 2, QTableWidgetItem(agent["hostname"]))
            table.setItem(row, 3, QTableWidgetItem(str(agent["cpu_load"])))
            table.setItem(row, 4, QTableWidgetItem(str(agent["ram_load"])))
            dt = datetime.fromisoformat(agent["last_seen"])
            table.setItem(row, 5, QTableWidgetItem(dt.strftime("%d %b %Y, %H:%M:%S")))

        self.ui.online_count.setText(str(online_count))
        self.ui.offline_count.setText(str(offline_count))

    def refresh_agents_table(self):
        self.thread = QThread()
        self.worker = AgentsWorker(self.client)

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)

        self.worker.success.connect(self.populate_agents_table)
        self.worker.error.connect(self.show_api_error)

        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()

    def show_api_error(self, message: str):
        print(f"API error: {message}")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())
