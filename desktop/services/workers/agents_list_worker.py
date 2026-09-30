import asyncio

from PySide6.QtCore import QObject, Signal, Slot

from api.client import NexoraClient


class AgentsListWorker(QObject):
    finished = Signal()
    success = Signal(list)
    error = Signal(str)

    def __init__(self, client: NexoraClient) -> None:
        super().__init__()
        self.client = client

    @Slot()
    def run(self) -> None:
        asyncio.run(self._execute_request())

    async def _execute_request(self) -> None:
        try:
            agents = await self.client.get_agents_list()
            self.success.emit(agents)

        except Exception as exc:
            self.error.emit(str(exc))

        finally:
            self.finished.emit()
