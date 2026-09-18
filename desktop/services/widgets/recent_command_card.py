from datetime import datetime
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget

from ui.recent_command_widget import Ui_recent_command_widget


class CommandCardWidget(QWidget):
    open_requested = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_recent_command_widget()
        self.ui.setupUi(self)

        self.setAttribute(Qt.WA_StyledBackground, True)

    def set_command(self, command: dict) -> None:
        self._update_command_information(command)
        self._update_status(command)

    def _update_command_information(self, command: dict) -> None:
        self.ui.command_name.setText(
            str(command.get("command_type", "Unknown Command"))
        )

        created_at = command.get("created_at", "---")
        created_at = datetime.fromisoformat(created_at).strftime("%d %b, %H:%M")
        self.ui.command_executed_time.setText(str(created_at))

    def _update_status(self, command: dict) -> None:
        status = str(command.get("status", "PENDING"))

        self.ui.command_status.setText(status)

        if status == "SUCCESS":
            mark = "✓"
            status_prop = "success"

        elif status == "FAILED":
            mark = "✕"
            status_prop = "failed"

        else:
            mark = "⟳"
            status_prop = "pending"

        self.ui.command_mark.setText(mark)

        self._apply_style_property(self.ui.command_mark, "status", status_prop)
        self._apply_style_property(self.ui.command_status, "status", status_prop)

    def _apply_style_property(self, widget, prop_name: str, prop_value: str) -> None:
        widget.setProperty(prop_name, prop_value)
        widget.style().unpolish(widget)
        widget.style().polish(widget)