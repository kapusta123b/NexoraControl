from PySide6.QtCore import QObject

from api.client import NexoraClient

from services.stores.agent_store import AgentSystemInfoStore

from ui.main_window import Ui_MainWindow


class DetailHardwareController(QObject):
    def __init__(self, ui: Ui_MainWindow, client: NexoraClient):
        super().__init__()

        self.ui = ui
        self.client = client

        self.hardware_store = AgentSystemInfoStore

        self.agent = {}

    def activate(self) -> None:
        if self.agent:
            self.hardware_poller.on_clicked(self.agent["id"])
