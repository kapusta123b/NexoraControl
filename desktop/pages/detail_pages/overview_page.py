from datetime import datetime

from PySide6.QtWidgets import QButtonGroup, QLayout
from PySide6.QtCore import QObject

from api.client import NexoraClient

from services.utils.widgets_utils import apply_style_property

from services.widgets.recent_command_card import CommandCardWidget

from services.pollers.overview_poller import DetailOverviewPoller

from services.stores.agent_command_store import CommandsStore
from services.stores.agent_store import DetailAgentStore

from ui.main_window import Ui_MainWindow


class DetailOverviewController(QObject):
    def __init__(self, ui: Ui_MainWindow, client: NexoraClient, store: CommandsStore):
        super().__init__()
        self.ui = ui
        self.agent = {}

        self.detail_agent_store = DetailAgentStore()

        self.commands_store = store

        self.overview_poller = DetailOverviewPoller(
            client, self.detail_agent_store, self.commands_store
        )

        self._connect_signals()

        self.detail_agent_store.agent_changed.connect(self.set_overview_information)
        self.commands_store.commands_changed.connect(self.populate_recent_commands)

    def activate(self) -> None:
        if self.agent:
            self.overview_poller.on_clicked(self.agent["id"])

    def set_overview_information(self, agent: dict | None = None) -> None:
        current_agent = agent or self.agent
        if not current_agent:
            return

        self._update_system_info(current_agent)
        self._update_metrics(current_agent)
        self._update_status(current_agent)

    def populate_recent_commands(self, commands: list[dict]) -> None:
        layout = self.ui.recent_command_box_widget.layout()
        if layout is None:
            return

        self._clear_layout(layout)

        for command in commands:
            card = CommandCardWidget()
            card.set_command(command)

            layout.addWidget(card)

        layout.addStretch(1)

    def _connect_signals(self) -> None:
        self.quick_commands_nav_group = QButtonGroup(self)
        self.quick_commands_nav_group.setExclusive(True)

        self.command_mapping = {
            self.ui.docker_ps_quick_button: ("docker_ps", {}),
            self.ui.reboot_quick_button: (
                "system_reboot",
                {"confirmation": "REBOOT"},
            ),
            self.ui.stop_all_docker_cont_quick_button: (
                "docker_stop_all_containers",
                {"confirmation": "STOP_ALL"},
            ),
            self.ui.restart_all_docker_cont_quick_button: (
                "docker_restart_all_containers",
                {"confirmation": "RESTART_ALL"},
            ),
        }

        for button in self.command_mapping:
            self.quick_commands_nav_group.addButton(button)
            button.clicked.connect(self.on_nav_button_clicked)

    def on_nav_button_clicked(self) -> None:
        clicked_button = self.sender()

        if clicked_button not in self.command_mapping:
            return

        if not self.agent:
            return

        command_type, payload = self.command_mapping[clicked_button]

        self.overview_poller.on_clicked(
            agent_id=self.agent["id"],
            command_type=command_type,
            payload=payload,
        )

    def _clear_layout(self, layout: QLayout) -> None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()

            if widget is not None:
                widget.setParent(None)
                widget.deleteLater()

            elif item.layout() is not None:
                self._clear_layout(item.layout())

    def _update_system_info(self, agent: dict) -> None:
        self.ui.detail_top_agent_name_label.setText(agent.get("name", "Loading..."))
        self.ui.hostname_value_label.setText(agent.get("hostname", "Unknown"))
        self.ui.ip_value_label.setText(agent.get("ip", "Unknown"))
        self.ui.os_name_value_label.setText(agent.get("os", "Unknown"))

        last_seen = agent.get("last_seen")

        try:
            last_seen_text = (
                datetime.fromisoformat(last_seen).strftime("%d %b %Y, %H:%M:%S")
                if last_seen
                else "Never"
            )
        except ValueError:
            last_seen_text = "Invalid Date"

        self.ui.last_seen_value_label.setText(last_seen_text)

    def _update_metrics(self, agent: dict) -> None:
        cpu = str(agent.get("cpu_load", "---"))
        ram = str(agent.get("ram_load", "---"))

        self.ui.cpu_load_label.setText(f"{cpu}%")
        self.ui.ram_load_label.setText(f"{ram}%")
        self.ui.disk_load_label.setText("---")
        self.ui.up_time_label.setText("---")

        self._set_widget_load_level(self.ui.cpu_load_label, cpu)
        self._set_widget_load_level(self.ui.ram_load_label, ram)

    def _update_status(self, agent: dict) -> None:
        is_online = agent.get("status") == "ON"
        status_val = "online" if is_online else "offline"
        status_str = status_val.upper()

        self.ui.agent_status_value_label.setText(status_str)
        self.ui.detail_top_agent_status_label.setText(
            f"{'●' if is_online else '○'} {status_str}"
        )

        apply_style_property(
            self.ui.agent_status_value_label, "agent_status", status_val
        )
        apply_style_property(
            self.ui.detail_top_agent_status_label, "agent_status", status_val
        )

    def _set_widget_load_level(self, widget, value: str) -> None:
        try:
            val = int(value)
            level = "low" if val < 30 else "medium" if val < 75 else "high"

        except (ValueError, TypeError):
            level = "low"

        apply_style_property(widget, "load_level", level)
