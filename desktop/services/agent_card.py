from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget

from ui.agent_card import Ui_card_form


class AgentCardWidget(QWidget):
    open_requested = Signal(int, str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_card_form()
        self.ui.setupUi(self)

        self.agent_id = None
        self.agent_name = ""

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.ui.agent_information_widget.setAttribute(
            Qt.WA_TransparentForMouseEvents,
            True,
        )
        self.setCursor(Qt.CursorShape.PointingHandCursor)

    def set_agent(self, agent: dict):
        self.agent_id = agent["id"]
        self.agent_name = agent["name"]

        self.ui.vps_name_label.setText(self.agent_name)
        self.ui.ip_os_label.setText(f"{agent['ip']} · {agent['os']}")
        self.ui.cpu_ram_label.setText(
            f"CPU {agent['cpu_load']}%   RAM {agent['ram_load']}%"
        )
        is_online = agent.get("status") in ("ON")

        self.ui.online_dot.setText("●" if is_online else "○")
        self.ui.status_label.setText("ONLINE" if is_online else "OFFLINE")

        status_value = "online" if is_online else "offline"
        self.ui.status_label.setProperty("agent_status", status_value)

        self.ui.status_label.style().unpolish(self.ui.status_label)
        self.ui.status_label.style().polish(self.ui.status_label)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton and self.agent_id is not None:
            self.open_requested.emit(self.agent_id, self.agent_name)

        super().mousePressEvent(event)
