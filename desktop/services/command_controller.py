from dataclasses import dataclass
from multiprocessing import Value

from PySide6.QtCore import QObject, Qt, Signal
from PySide6.QtWidgets import (
    QAbstractItemView,
    QApplication,
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QPlainTextEdit,
    QMessageBox,
    QSpinBox,
    QTabWidget,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
)

import json

from typing import Any

from api.client import NexoraClient

from services.command_field_helper import CommandFieldBuilder

from services.widgets.box_messages import MessageBox

from services.commands_map import COMMANDS_REGISTRY

from services.utils.widgets_utils import apply_style_for_tables, setup_table

from services.pollers.command_poller import CommandPoller

from services.stores.agent_command_store import CommandsStore

from ui.main_window import Ui_MainWindow


@dataclass
class CommandWidgets:
    layout: QVBoxLayout
    payload_editor: QPlainTextEdit
    request_preview: QPlainTextEdit
    output_view: QPlainTextEdit
    stderr_view: QPlainTextEdit


class CommandController(QObject):
    def __init__(
        self,
        client: NexoraClient,
        store: CommandsStore,
        widgets: CommandWidgets,
    ) -> None:
        super().__init__()

        self.client = client

        self.agent = {}

        self.widgets = widgets

        self.current_command_category = None
        self.current_command_type = None

        self.payload_editor_data = {}
        self.commands_by_id = {}

        self.command_store = store
        self.command_poller = CommandPoller(self.client, self.command_store)
        self.command_builder = CommandFieldBuilder(self.widgets.layout)

        self.widgets.payload_editor.textChanged.connect(
            lambda: self.widgets.request_preview.setPlainText(
                self.widgets.payload_editor.toPlainText()
            )
        )

    def _change_command_list_by_category(
        self, command_list_combo: QComboBox, category: str
    ):

        self.current_command_category = category

        command_list_combo.clear()
        command_list_combo.addItems(COMMANDS_REGISTRY[category].keys())
        command_list_combo.setEnabled(True)

        self.clear_payload_and_preview_editor()

    def _setup_command_fields_container(
        self,
        command: str,
        title: QLabel,
        command_key: QLabel,
        description: QLabel,
        risk_badge: QLabel,
        fields_label: QLabel,
    ):
        self.clear_payload_and_preview_editor()

        if not command:
            self.current_command_type = None
            self.command_builder.clear()

            return

        self.current_command_type = command

        command_fields = COMMANDS_REGISTRY[self.current_command_category][
            self.current_command_type
        ]["fields"]

        fields_count = len(command_fields)

        self.command_builder.build(command_fields)

        self.setup_command_identify_card(
            title,
            command_key,
            description,
            risk_badge,
            fields_label,
            fields_count,
        )

    def setup_command_identify_card(
        self,
        title: QLabel,
        command_key: QLabel,
        description: QLabel,
        risk_badge: QLabel,
        fields_label: QLabel,
        fields_count: int,
    ):
        current_command = COMMANDS_REGISTRY[self.current_command_category][
            self.current_command_type
        ]

        title.setText(self.current_command_type)
        command_key.setText(
            f"{current_command["json_title"]} / {self.current_command_category}"
        )
        description.setText(current_command["description"])
        risk_badge.setText(current_command["risk"].upper())

        fields_label.setText(f"{fields_count} FIELDS")

        if self.command_builder.widgets:
            for name, widget in self.command_builder.widgets.items():
                if isinstance(widget, (QLineEdit, QComboBox)):
                    signal = (
                        widget.textChanged
                        if isinstance(widget, QLineEdit)
                        else widget.currentTextChanged
                    )

                    signal.connect(
                        lambda text, n=name: self._fill_payload_editors(n, text)
                    )

                if isinstance(widget, QCheckBox):
                    widget.stateChanged.connect(
                        lambda value, n=name: self._fill_payload_editors(
                            n, (True if value else False)
                        )
                    )

                if isinstance(widget, (QSpinBox, QDoubleSpinBox)):
                    widget.valueChanged.connect(
                        lambda value, n=name: self._fill_payload_editors(n, value)
                    )

    def _fill_payload_editors(self, name: str, value: Any):
        self.payload_editor_data.update({name: value})

        payload_format_text = json.dumps(
            self.payload_editor_data, indent=4, ensure_ascii=False
        )

        self.widgets.payload_editor.setPlainText(payload_format_text)

    def send_command(self):
        if not self.current_command_type:
            MessageBox().show_message(
                "warning",
                "Just make a choice!",
                "A command type must be selected before sending the request.",
            )

            return

        if not self.agent:
            MessageBox().show_message(
                "warning",
                "No chosen agent!",
                "An agent must be selected before sending the request.",
            )

            return

        command_definition = COMMANDS_REGISTRY[self.current_command_category][
            self.current_command_type
        ]
        risk = str(command_definition.get("risk", "safe")).lower()

        if risk == "dangerous" and getattr(
            self.client, "confirm_dangerous_commands", True
        ):
            target_name = (
                self.agent.get("name") or f"agent #{self.agent.get('id', '?')}"
            )
            answer = QMessageBox.question(
                QApplication.activeWindow(),
                "Confirm dangerous command",
                (
                    f"'{command_definition.get('title', self.current_command_type)}' "
                    f"is marked as dangerous.\n\nTarget: {target_name}\n\n"
                    "This operation may disrupt the target system. Continue?"
                ),
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel,
                QMessageBox.StandardButton.Cancel,
            )
            if answer != QMessageBox.StandardButton.Yes:
                return

        current_command_type_json = command_definition["json_title"]
        self.command_poller._start_commands_worker(
            current_command_type_json, payload=self.payload_editor_data
        )

    def show_selected_command(self, table: QTableWidget, result_status: QLabel):
        command_id = self._get_selected_command_id(table)

        if command_id is None:
            self.clear_command_output()
            return

        command = self.commands_by_id.get(command_id)

        if command is None:
            self.clear_command_output()
            return

        output = command["output"]

        errors = command["errors"]

        errors_text = (
            json.dumps(
                errors,
                indent=4,
                ensure_ascii=False,
            )
            if errors
            else ""
        )

        result_status.setText(f'STATUS / {command["status"]}')

        self.widgets.output_view.setPlainText(output)
        self.widgets.stderr_view.setPlainText(errors_text)

    def _get_selected_command_id(self, table: QTableWidget):

        row = table.currentRow()

        if row < 0:
            return None

        item = table.item(row, 0)

        if item is None:
            return None

        try:
            return int(item.text())
        except ValueError:
            return None

    def clear_command_output(self):
        self.widgets.output_view.clear()
        self.widgets.stderr_view.clear()

    def clear_payload_and_preview_editor(self):
        self.payload_editor_data.clear()

        self.widgets.request_preview.clear()
        self.widgets.payload_editor.clear()

    def copy_history_output_to_clipboard(self, tab_view: QTabWidget):
        if "stdout" in tab_view.currentWidget().objectName():
            QApplication.clipboard().setText(self.widgets.output_view.toPlainText())
        else:
            QApplication.clipboard().setText(self.widgets.stderr_view.toPlainText())

    def activate_raw_mode_for_payload_editor(
        self,
        state: int,
    ):
        is_read_only = False if state else True

        self.widgets.payload_editor.setReadOnly(is_read_only)

    def activate(self) -> None:
        if self.agent:
            self.command_poller.on_clicked(self.agent["id"])
