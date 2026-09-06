from PySide6.QtCore import QObject, Signal



class CommandsStore(QObject):
    commands_changed = Signal(list)

    def __init__(self):
        super().__init__()
        self._commands: list[dict] = []

    def set_commands(self, commands: list[dict]) -> None:
        self._commands = commands
        self.commands_changed.emit(commands)

    def get_commands(self) -> list[dict]:
        return self._commands