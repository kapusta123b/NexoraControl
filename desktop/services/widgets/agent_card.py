from PySide6.QtCore import Qt, Signal

from PySide6.QtWidgets import QWidget

from ui.agent_card import Ui_card_form


class AgentCardWidget(QWidget):
    open_requested = Signal()

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.ui = Ui_card_form()
        self.ui.setupUi(self)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.ui.agent_information_widget.setAttribute(
            Qt.WA_TransparentForMouseEvents,
            True,
        )
        self.setCursor(Qt.CursorShape.PointingHandCursor)

    def set_agent(self, agent: dict) -> None:
        self._update_agent_information(agent)
        self._update_status(agent)

    def _update_agent_information(self, agent: dict) -> None:
        self.ui.vps_name_label.setText(agent["name"])
        self.ui.ip_os_label.setText(f"{agent['ip']} · {agent['os']}")
        self.ui.cpu_ram_label.setText(
            f"CPU {agent['cpu_load']}%   RAM {agent['ram_load']}%"
        )

    def _update_status(self, agent: dict) -> None:
        is_online = agent["status"] == ("ON")
        status_val = "online" if is_online else "offline"
        status_str = status_val.upper()

        self.ui.online_dot.setText("●" if is_online else "○")
        self.ui.status_label.setText(status_str)

        self._apply_style_property(self.ui.status_label, "agent_status", status_val)

    def _apply_style_property(self, widget, prop_name: str, prop_value: str) -> None:
        widget.setProperty(prop_name, prop_value)
        widget.style().unpolish(widget)
        widget.style().polish(widget)

    def mousePressEvent(self, event) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.open_requested.emit()

        super().mousePressEvent(event)
