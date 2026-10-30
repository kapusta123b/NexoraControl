import sys

import PySide6.QtOpenGL

from PySide6.QtWidgets import QApplication, QButtonGroup, QMainWindow

from api.client import NexoraClient

from pages.settings_page import SettingsController
from pages.logs_page import LogsController

from services.stores.settings_store import DesktopSettingsStore
from services.stores.agent_store import AgentsListStore

from services.pollers.agents_list_poller import AgentsListPoller

from pages.agent_detail_page import AgentDetailController
from pages.agents_list_page import AgentsController
from pages.dashboard_page import DashboardController
from pages.fleet_command_page import FleetCommandController

from ui.main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.settings_store = DesktopSettingsStore()
        self.startup_preferences = self.settings_store.load()
        startup_preferences = self.startup_preferences

        self.client = NexoraClient(
            startup_preferences.api_base_url,
            "TOKEN",
            timeout_seconds=startup_preferences.request_timeout_seconds,
        )
        self.client.confirm_dangerous_commands = (
            startup_preferences.confirm_dangerous_commands
        )
        self.client.notify_failures = startup_preferences.notify_failures

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setup_pages()
        self.setup_navigation()

        self.ui.content_stack.setCurrentWidget(self.ui.dashboard_page)
        self.ui.dashboard_button.setChecked(True)

    def setup_navigation(self) -> None:
        self.nav_group = QButtonGroup(self)
        self.nav_group.setExclusive(True)

        buttons = {
            self.ui.dashboard_button: self.ui.dashboard_page,
            self.ui.agents_button: self.ui.agents_page,
            self.ui.commands_button: self.ui.fleet_commands_page,
            self.ui.logs_button: self.ui.fleet_logs_page,
            self.ui.settings_button: self.ui.preferences_page,
            self.ui.about_button: self.ui.application_about_page,
        }

        for button, page in buttons.items():
            self.nav_group.addButton(button)
            button.clicked.connect(
                lambda checked=False, page=page: self.ui.content_stack.setCurrentWidget(
                    page
                )
            )

    def setup_pages(self) -> None:
        self.agent_store = AgentsListStore()
        self.agent_poller = AgentsListPoller(client=self.client, store=self.agent_store)

        timer = getattr(self.agent_poller, "timer", None)
        if timer is not None:
            timer.setInterval(self.startup_preferences.refresh_interval_seconds * 1000)
            if self.startup_preferences.auto_refresh_enabled:
                timer.start()
            else:
                timer.stop()

        self.dashboard_controller = DashboardController(
            ui=self.ui, dashboard_store=self.agent_store, poller=self.agent_poller
        )

        self.agent_detail_controller = AgentDetailController(
            ui=self.ui, client=self.client
        )

        self.agents_controller = AgentsController(
            ui=self.ui,
            agents_store=self.agent_store,
            poller=self.agent_poller,
            detail_controller=self.agent_detail_controller,
        )

        self.fleet_commands_controller = FleetCommandController(
            ui=self.ui,
            client=self.client,
            agent_store=self.agent_store,
        )

        self.logs_controller = LogsController(
            ui=self.ui, client=self.client, agent_store=self.agent_store
        )

        self.settings_controller = SettingsController(
            ui=self.ui,
            client=self.client,
            agents_poller=self.agent_poller,
            settings_store=self.settings_store,
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    try:
        with open("styles/theme.qss", "r") as f:
            qss_rules = f.read()
            app.setStyleSheet(qss_rules)

    except FileNotFoundError:
        print("Warning: theme.qss file not found. Running without custom styles.")

    window.show()

    sys.exit(app.exec())
