from PySide6.QtWidgets import QWidget

from ui.agent_card import Ui_card_form

from PySide6.QtCore import Qt


class AgentCardWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_card_form()
        self.ui.setupUi(self)

        

        self.setAttribute(Qt.WA_StyledBackground, True)

    def set_agent(self, agent: dict):
        self.ui.vps_name_label.setText(agent["name"])
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
