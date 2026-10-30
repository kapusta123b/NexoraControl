from PySide6.QtWidgets import QTableWidget

from api.client import NexoraClient

from services.command_controller import CommandController, CommandWidgets

from services.pollers.command_poller import CommandPoller

from services.stores.agent_command_store import CommandsStore
from services.stores.agent_store import AgentsListStore

from services.utils.widgets_utils import (
    apply_style_for_tables,
    setup_table,
)

from ui.main_window import Ui_MainWindow

LOG_COMMANDS = {
    "Docker logs": ("Docker", "Docker logs"),
    "Compose logs": ("Docker Compose", "Compose logs"),
    "Service logs": ("Services", "Service logs"),
    "Journal errors": ("Diagnostics", "Journal errors"),
    "Kernel messages": ("Diagnostics", "Kernel messages"),
    "Boot journal errors": ("Diagnostics", "Boot journal errors"),
}


class LogsController(CommandController):
    def __init__(
        self,
        ui: Ui_MainWindow,
        client: NexoraClient,
        agent_store: AgentsListStore,
    ) -> None:
        self.ui = ui

        self.client = client

        widgets = CommandWidgets(
            layout=self.ui.fleet_logs_command_fields_layout,
            payload_editor=self.ui.fleet_logs_payload_editor,
            request_preview=self.ui.fleet_logs_request_preview,
<<<<<<< HEAD
            output_view=self.ui.fleet_logs_stdout_view,
=======
            output_view=self.ui.fleet_logs_raw_view,
>>>>>>> refs/remotes/origin/main
            stderr_view=self.ui.fleet_logs_stderr_view,
        )

        self.agent_store = agent_store
        self.command_store = CommandsStore()

        self.command_poller = CommandPoller(self.client, self.command_store)

        super().__init__(self.client, self.command_store, widgets)

        self.agents_by_name = {}

        self.setup_style()
        self.__connect_signals()

    def setup_style(self):
        self.ui.fleet_logs_source_combo.addItems(LOG_COMMANDS.keys())

        apply_style_for_tables(
            self.ui.fleet_logs_request_history_table, edit_triggers=False
        )

    def __connect_signals(self) -> None:
        self.agent_store.agents_changed.connect(self.on_agents_changed)

        self.command_store.commands_changed.connect(self.populate_request_history_table)

        self.ui.fleet_logs_source_combo.currentTextChanged.connect(
            self._setup_command_fields_by_command
        )

        self.ui.fleet_logs_raw_mode_checkbox.stateChanged.connect(
            self.activate_raw_mode_for_payload_editor
        )

        self.ui.fleet_logs_agent_combo.currentTextChanged.connect(
            self.on_select_target_agent
        )

        self.ui.fleet_logs_request_history_table.currentItemChanged.connect(
            self.on_request_selected
        )

        self.ui.fleet_logs_refresh_button.clicked.connect(self.send_command)

<<<<<<< HEAD
        self.ui.fleet_logs_copy_output_button.clicked.connect(
            lambda: self.copy_history_output_to_clipboard(self.ui.fleet_logs_view_tabs)
        )

=======
>>>>>>> refs/remotes/origin/main
    def on_select_target_agent(self, agent_name: str) -> None:
        if not agent_name:
            return

        self.agent = self.agents_by_name[agent_name]

        params = {
            "command_type__in": (
                "docker_logs,"
                "docker_compose_logs,"
                "service_logs,"
                "diag_journal_errors,"
                "diag_kernel_logs,"
                "diag_boot_errors"
            ),
            "ordering": "-created_at",
        }

        self.command_poller.agent_id = self.agent["id"]

        self.command_poller._start_commands_worker(params=params)

    def on_agents_changed(self, agents: list[dict]) -> None:
        if not agents:
            return

        self.agents_by_name = {agent["name"]: agent for agent in agents}

        index = self.ui.fleet_logs_agent_combo.currentIndex()

        self.ui.fleet_logs_agent_combo.clear()

        self.ui.fleet_logs_agent_combo.addItems(self.agents_by_name.keys())

        self.ui.fleet_logs_agent_combo.setCurrentIndex(index)

    def _setup_command_fields_by_command(self, command: str) -> None:
        command_category, command = LOG_COMMANDS[command]

        self.current_command_category = command_category

        self._setup_command_fields_container(
            command,
            self.ui.fleet_logs_command_display_title,
            self.ui.fleet_logs_command_command_key,
            self.ui.fleet_logs_command_description,
            self.ui.fleet_logs_command_risk_badge,
            self.ui.fleet_logs_command_fields_count,
        )

    def on_request_selected(self):
        command_id = self._get_selected_command_id(
            self.ui.fleet_logs_request_history_table
        )
        command = self.commands_by_id[command_id]

        output = command["output"]
        errors = command["errors"]

<<<<<<< HEAD
        self.ui.fleet_logs_stdout_view.setPlainText(str(output))
        self.ui.fleet_logs_stderr_view.setPlainText(str(errors))

    def populate_request_history_table(self, commands: list[dict]):
=======
        self.ui.fleet_logs_raw_view.setPlainText(str(output))
        self.ui.fleet_logs_stderr_view.setPlainText(str(errors))

    def populate_request_history_table(self, commands: list[dict]):

>>>>>>> refs/remotes/origin/main
        self.commands_by_id = {command["id"]: command for command in commands}

        setup_table(
            self.ui.fleet_logs_request_history_table,
            commands,
            (
                "id",
                "command_type",
                "status",
                "created_at",
                "started_at",
                "finished_at",
            ),
        )
