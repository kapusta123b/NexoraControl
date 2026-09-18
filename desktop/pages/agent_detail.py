from PySide6.QtCore import QObject

from PySide6.QtWidgets import QButtonGroup

from api.client import NexoraClient

from pages.detail_pages.agent_performance import DetailPerformanceController

from ui.main_window import Ui_MainWindow

from pages.detail_pages.agent_overview import DetailOverviewController


class AgentDetailController(QObject):
    def __init__(self, ui: Ui_MainWindow, client: NexoraClient):
        super().__init__()
        self.ui = ui
        self.client = client
        self.agent = {}

        self.overview_controller = DetailOverviewController(
            ui=self.ui, client=self.client
        )
        self.performance_controller = DetailPerformanceController(
            ui=self.ui, client=self.client
        )

        self.setup_connections()

    def set_agent(self, agent: dict) -> None:
        self.agent = agent

        self.overview_controller.agent = agent
        self.performance_controller.agent = agent
        self.overview_controller.activate()

        if self.ui.content_stack.currentWidget() == self.ui.overview_detail_page:
            self.overview_controller.activate()

    def setup_connections(self) -> None:
        self.ui.back_to_agents_button.clicked.connect(self.on_back_to_agents)

        self.detail_nav_group = QButtonGroup(self)
        self.detail_nav_group.setExclusive(True)

        self.nav_mapping = {
            self.ui.overview_nav_button: (
                self.ui.overview_detail_page,
                self.overview_controller.activate,
            ),
            self.ui.performance_nav_button: (
                self.ui.performance_detail_page,
                self.performance_controller.activate,
            ),
        }

        for button, (page_widget, activate_method) in self.nav_mapping.items():
            self.detail_nav_group.addButton(button)

            button.clicked.connect(self.on_nav_button_clicked)

    def on_nav_button_clicked(self) -> None:
        clicked_button = self.sender()

        if clicked_button not in self.nav_mapping:
            return

        page_widget, activate_method = self.nav_mapping[clicked_button]

        self.overview_controller.overview_poller.stop_polling()

        self.ui.agent_detail_stacked_content.setCurrentWidget(page_widget)

        if self.agent:
            activate_method()

    def on_back_to_agents(self) -> None:
        self.overview_controller.overview_poller.stop_polling()
        self.ui.content_stack.setCurrentWidget(self.ui.agents_page)
