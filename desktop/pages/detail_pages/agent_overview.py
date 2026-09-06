from datetime import datetime
from PySide6.QtWidgets import QLayout

from api.client import NexoraClient
from services.recent_command_card import CommandCardWidget
from services.stores.agent_command_store import CommandsStore
from services.pollers.overview_poller import DetailOverviewPoller
from services.stores.agent_store import DetailAgentStore
from ui.main_window import Ui_MainWindow


class DetailOverviewController:
    def __init__(self, ui: Ui_MainWindow, client: NexoraClient, agent: dict):
        self.ui = ui
        self.agent = agent

        self.detail_agent_store = DetailAgentStore()
        self.commands_store = CommandsStore()

        self.overview_poller = DetailOverviewPoller(
            client, self.detail_agent_store, self.commands_store
        )

        self.detail_agent_store.agent_changed.connect(self.set_overview_information)
        self.commands_store.commands_changed.connect(self.populate_recent_commands)

    def activate(self) -> None:
        if self.agent:
            self.overview_poller.on_clicked(self.agent.get("id"))

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

        self.ui.cpu_load_label.setText(f"{cpu}%" if cpu != "---" else "---")
        self.ui.ram_load_label.setText(f"{ram}%" if ram != "---" else "---")
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

        self._apply_style_property(
            self.ui.agent_status_value_label, "agent_status", status_val
        )
        self._apply_style_property(
            self.ui.detail_top_agent_status_label, "agent_status", status_val
        )

    def _set_widget_load_level(self, widget, value: str) -> None:
        try:
            val = int(value)
            level = "low" if val < 30 else "medium" if val < 75 else "high"
        except (ValueError, TypeError):
            level = "low"

        self._apply_style_property(widget, "load_level", level)

    def _apply_style_property(self, widget, prop_name: str, prop_value: str) -> None:
        widget.setProperty(prop_name, prop_value)
        widget.style().unpolish(widget)
        widget.style().polish(widget)
