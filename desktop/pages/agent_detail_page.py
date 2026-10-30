from PySide6.QtCore import QObject

from PySide6.QtWidgets import QButtonGroup

from api.client import NexoraClient

from services.stores.agent_command_store import CommandsStore

from pages.detail_pages.command_page import DetailCommandController
from pages.detail_pages.hardware_page import DetailHardwareController
from pages.detail_pages.performance_page import DetailPerformanceController
from pages.detail_pages.overview_page import DetailOverviewController

from ui.main_window import Ui_MainWindow


class AgentDetailController(QObject):
    def __init__(self, ui: Ui_MainWindow, client: NexoraClient) -> None:
        super().__init__()
        self.ui = ui
        self.client = client
        self.agent = {}

        self.commands_store = CommandsStore()

        self.overview_controller = DetailOverviewController(
            ui=self.ui, client=self.client, store=self.commands_store
        )
        self.performance_controller = DetailPerformanceController(
            ui=self.ui, client=self.client
        )
        self.hardware_controller = DetailHardwareController(
            ui=self.ui,
            client=self.client,
        )
        self.commands_controller = DetailCommandController(
            ui=self.ui, client=self.client, store=self.commands_store
        )

        self._connect_signals()

    def _connect_signals(self) -> None:
        self.ui.back_to_agents_button.clicked.connect(self.on_back_to_agents)

        self.ui.overview_nav_button.setChecked(True)

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
            self.ui.hardware_nav_button: (
                self.ui.hardware_detail_page,
                self.hardware_controller.activate,
            ),
            self.ui.commands_nav_button: (
                self.ui.agent_commands_page,
                self.commands_controller.activate,
            ),
        }

        for button, (page_widget, activate_method) in self.nav_mapping.items():
            self.detail_nav_group.addButton(button)

            button.clicked.connect(self.on_nav_button_clicked)

    def set_agent(self, agent: dict) -> None:
        self.agent = agent

        self.overview_controller.agent = agent
        self.performance_controller.agent = agent
        self.hardware_controller.agent = agent
        self.commands_controller.agent = agent

        if (
            self.ui.agent_detail_stacked_content.currentWidget()
            == self.ui.overview_detail_page
        ):
            self.overview_controller.activate()

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
