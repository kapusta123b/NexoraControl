import sys

from PySide6.QtWidgets import QApplication, QButtonGroup, QMainWindow

from api.client import NexoraClient

from pages.agent_detail import AgentDetailController
from pages.agents import AgentsController
from pages.dashboard import DashboardController

from services.agent_poller import AgentMetricPoller, AgentPoller
from services.agent_store import AgentStore, MetricStore

from ui.main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.client = NexoraClient(
            "http://127.0.0.1:8000/api/v1/",
            "TOKEN",
        )

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.agent_store = AgentStore()
        self.metric_store = MetricStore()

        self.agent_poller = AgentPoller(client=self.client, store=self.agent_store)
        self.agent_metric_poller = AgentMetricPoller(
            client=self.client,
            store=self.metric_store,
        )

        self.setup_pages()
        self.setup_navigation()

        self.ui.content_stack.setCurrentWidget(self.ui.dashboard_page)
        self.ui.dashboard_button.setChecked(True)

    def setup_navigation(self):
        self.nav_group = QButtonGroup(self)
        self.nav_group.setExclusive(True)

        buttons = {
            self.ui.dashboard_button: self.ui.dashboard_page,
            self.ui.agents_button: self.ui.agents_page,
        }

        for button, page in buttons.items():
            self.nav_group.addButton(button)
            button.clicked.connect(
                lambda checked=False, page=page: self.ui.content_stack.setCurrentWidget(
                    page
                )
            )

    def setup_pages(self):
        self.dashboard_controller = DashboardController(
            ui=self.ui, store=self.agent_store, poller=self.agent_poller
        )

        self.agent_detail_controller = AgentDetailController(
            ui=self.ui,
            store=self.metric_store,
            poller=self.agent_metric_poller,
        )

        self.agents_controller = AgentsController(
            ui=self.ui,
            store=self.agent_store,
            poller=self.agent_poller,
            detail_controller=self.agent_detail_controller,
        )


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())
