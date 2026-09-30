import asyncio
import sys

from PySide6.QtWidgets import QApplication, QButtonGroup, QMainWindow

from api.client import NexoraClient

from services.pollers.agents_list_poller import AgentsListPoller

from services.stores.agent_store import AgentsStore

from pages.agent_detail_page import AgentDetailController
from pages.agents_list_page import AgentsController
from pages.dashboard_page import DashboardController

from ui.main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.client = NexoraClient(
            "http://127.0.0.1:8000/api/v1/",
            "TOKEN",
        )

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setup_pages()
        self.setup_navigation()

        if sys.platform == "win32":
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        else:
            asyncio.get_event_loop_policy().get_event_loop = asyncio.new_event_loop

        self.ui.content_stack.setCurrentWidget(self.ui.dashboard_page)
        self.ui.dashboard_button.setChecked(True)

    def setup_navigation(self) -> None:
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

    def setup_pages(self) -> None:
        self.agent_store = AgentsStore()
        self.agent_poller = AgentsListPoller(client=self.client, store=self.agent_store)

        self.dashboard_controller = DashboardController(
            ui=self.ui, store=self.agent_store, poller=self.agent_poller
        )

        self.agent_detail_controller = AgentDetailController(
            ui=self.ui, client=self.client
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
