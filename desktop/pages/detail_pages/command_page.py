from PySide6.QtCore import QObject

from api.client import NexoraClient

from services.stores.agent_command_store import CommandsStore

from ui.main_window import Ui_MainWindow


class DetailCommandController(QObject):
    def __init__(self, ui: Ui_MainWindow, client: NexoraClient, store: CommandsStore):
        super().__init__()

        self.ui = ui
        self.client = client

        self.command_store = store

        self.agent = {}

    def activate(self) -> None:
        pass
