from PySide6.QtWidgets import QAbstractItemView, QCheckBox, QLineEdit, QTableWidgetItem

import json

from typing import Any

from api.client import NexoraClient

from services.command_controller import CommandController, CommandWidgets

from services.commands_map import COMMANDS_REGISTRY

from services.utils.widgets_utils import apply_style_for_tables, setup_table

from services.stores.agent_command_store import CommandsStore

from ui.main_window import Ui_MainWindow


class DetailCommandController(CommandController):
    def __init__(
        self, ui: Ui_MainWindow, client: NexoraClient, store: CommandsStore
    ) -> None:
        self.ui = ui

        widgets = CommandWidgets(
            layout=self.ui.agent_command_fields_layout,
            payload_editor=self.ui.agent_command_payload_editor,
            request_preview=self.ui.agent_command_request_preview,
            output_view=self.ui.agent_command_output_view,
            stderr_view=self.ui.agent_command_stderr_view,
        )

        super().__init__(client, store, widgets)

        self.agent = {}

        self.setup_connections()
        self.setup_style()

    def setup_connections(self):
        self.ui.agent_command_category_combo.currentTextChanged.connect(
            lambda text: self._change_command_list_by_category(
                self.ui.agent_command_type_combo, text
            )
        )

        self.ui.agent_command_type_combo.currentTextChanged.connect(
            lambda command: self._setup_command_fields_container(
                command,
                self.ui.agent_command_display_title,
                self.ui.agent_command_command_key,
                self.ui.agent_command_description,
                self.ui.agent_command_risk_badge,
                self.ui.agent_command_fields_count,
            )
        )

        self.ui.agent_command_raw_mode_checkbox.stateChanged.connect(
            lambda value: self.ui.agent_command_payload_editor.setReadOnly(
                (False if value else True)
            )
        )

        self.ui.agent_command_payload_editor.textChanged.connect(
            lambda: self.ui.agent_command_request_preview.setPlainText(
                self.ui.agent_command_payload_editor.toPlainText()
            )
        )

        self.ui.agent_command_history_table.itemSelectionChanged.connect(
            lambda: self.show_selected_command(
                self.ui.agent_command_history_table, self.ui.agent_command_result_status
            )
        )

        self.ui.agent_command_copy_output_button.clicked.connect(
            lambda: self.copy_history_output_to_clipboard(
                self.ui.agent_command_result_tabs
            )
        )

        self.ui.agent_command_history_refresh_button.clicked.connect(
            self.command_poller.refresh
        )

        self.command_store.commands_changed.connect(self.setup_command_history_table)

        self.ui.agent_command_execute_button.clicked.connect(self.send_command)

    def setup_style(self):
        self.ui.agent_command_category_combo.addItems(COMMANDS_REGISTRY.keys())

        self.ui.agent_command_type_combo.setEnabled(False)

        table = self.ui.agent_command_history_table

        table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        apply_style_for_tables(table, edit_triggers=False)

    def setup_command_history_table(self, commands: list[dict]):
        self.commands_by_id = {command["id"]: command for command in commands}

        setup_table(
            self.ui.agent_command_history_table,
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
