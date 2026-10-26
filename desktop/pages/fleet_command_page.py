from PySide6.QtWidgets import QAbstractItemView

from api.client import NexoraClient

from services.stores.agent_store import AgentsListStore

from services.command_controller import CommandController, CommandWidgets

from services.commands_map import COMMANDS_REGISTRY

from services.utils.widgets_utils import apply_style_for_tables, setup_table

from services.stores.agent_command_store import CommandsStore

from ui.main_window import Ui_MainWindow


class FleetCommandController(CommandController):
    def __init__(
        self, ui: Ui_MainWindow, client: NexoraClient, agent_store: AgentsListStore
    ) -> None:
        self.ui = ui

        widgets = CommandWidgets(
            layout=self.ui.fleet_command_fields_layout,
            payload_editor=self.ui.fleet_command_payload_editor,
            request_preview=self.ui.fleet_command_request_preview,
            output_view=self.ui.fleet_command_output_view,
            stderr_view=self.ui.fleet_command_stderr_view,
        )

        self.command_store = CommandsStore()
        self.agent_store = agent_store

        super().__init__(client, self.command_store, widgets)

        self.agents_by_name = {}

        self.commands_catalog = []

        self.setup_connections()
        self.setup_style()

    def setup_connections(self) -> None:
        self.command_store.commands_changed.connect(self.setup_command_history_table)

        self.agent_store.agents_changed.connect(self.on_agents_changed)

        self.ui.fleet_command_category_combo.currentTextChanged.connect(
            lambda text: self._change_command_list_by_category(
                self.ui.fleet_command_type_combo, text
            )
        )

        self.ui.fleet_command_history_refresh_button.clicked.connect(
            self.command_poller.refresh
        )

        self.ui.fleet_command_type_combo.currentTextChanged.connect(
            self._setup_command_fields_by_command
        )

        self.ui.fleet_command_raw_mode_checkbox.stateChanged.connect(
            lambda value: self.ui.fleet_command_payload_editor.setReadOnly(
                (False if value else True)
            )
        )

        self.ui.fleet_command_payload_editor.textChanged.connect(
            lambda: self.ui.fleet_command_request_preview.setPlainText(
                self.ui.fleet_command_payload_editor.toPlainText()
            )
        )

        self.ui.fleet_command_history_table.itemSelectionChanged.connect(
            lambda: self.show_selected_command(
                self.ui.fleet_command_history_table, self.ui.fleet_command_result_status
            )
        )

        self.ui.fleet_command_execute_button.clicked.connect(self.send_command)

        self.ui.fleet_command_target_combo.currentTextChanged.connect(
            self.on_select_target_agent
        )

        self.ui.fleet_command_copy_output_button.clicked.connect(
            lambda: self.copy_history_output_to_clipboard(
                self.ui.fleet_command_result_tabs
            )
        )

        self.ui.fleet_command_category.currentTextChanged.connect(
            self._setup_command_catalog_table
        )

        self.ui.fleet_command_catalog_table.itemSelectionChanged.connect(
            self.show_category_selected_command
        )

    def setup_style(self) -> None:
        self.ui.fleet_command_category_combo.addItems(COMMANDS_REGISTRY.keys())

        self.ui.fleet_command_type_combo.setEnabled(False)

        tables = (
            self.ui.fleet_command_history_table,
            self.ui.fleet_command_catalog_table,
        )

        self._setup_command_catalog_table()
        apply_style_for_tables(tables, edit_triggers=False)

    def _setup_command_catalog_table(self, category_name: str = None) -> None:
        if not hasattr(self, "_full_commands_catalog"):
            self.ui.fleet_command_category.addItems(COMMANDS_REGISTRY.keys())

            self._full_commands_catalog = [
                {
                    "category": category,
                    "command_name": command_name,
                    "risk": data["risk"].upper(),
                }
                for category, commands in COMMANDS_REGISTRY.items()
                for command_name, data in commands.items()
            ]

        if category_name and not category_name == "All categories":
            self.commands_catalog = [
                cmd
                for cmd in self._full_commands_catalog
                if cmd["category"] == category_name
            ]
        else:
            self.commands_catalog = list(self._full_commands_catalog)

        setup_table(
            self.ui.fleet_command_catalog_table,
            self.commands_catalog,
            (
                "command_name",
                "category",
                "risk",
            ),
        )

    def on_select_target_agent(self, agent_name: str) -> None:
        if not agent_name:
            return

        self.agent = self.agents_by_name[agent_name]

        self.activate()

    def on_agents_changed(self, agents: list[dict]) -> None:
        if not agents:
            return

        self.agents_by_name = {agent["name"]: agent for agent in agents}

        index = self.ui.fleet_command_target_combo.currentIndex()

        self.ui.fleet_command_target_combo.clear()

        self.ui.fleet_command_target_combo.addItems(self.agents_by_name.keys())

        self.ui.fleet_command_target_combo.setCurrentIndex(index)

    def setup_command_history_table(self, commands: list[dict]) -> None:
        self.commands_by_id = {command["id"]: command for command in commands}

        setup_table(
            self.ui.fleet_command_history_table,
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

    def _setup_command_fields_by_command(self, command: str) -> None:
        self.ui.fleet_command_type_combo.setEnabled(True)

        self._setup_command_fields_container(
            command,
            self.ui.fleet_command_display_title,
            self.ui.fleet_command_command_key,
            self.ui.fleet_command_description,
            self.ui.fleet_command_risk_badge,
            self.ui.fleet_command_fields_count,
        )

    def show_category_selected_command(self) -> None:
        table = self.ui.fleet_command_catalog_table

        row = table.currentRow()

        if row < 0:
            return

        command_type = table.item(row, 0).text()
        category = table.item(row, 1).text()

        if command_type is None or category is None:
            return

        self.current_command_category = category

        self._setup_command_fields_container(
            command_type,
            self.ui.fleet_command_display_title,
            self.ui.fleet_command_command_key,
            self.ui.fleet_command_description,
            self.ui.fleet_command_risk_badge,
            self.ui.fleet_command_fields_count,
        )
