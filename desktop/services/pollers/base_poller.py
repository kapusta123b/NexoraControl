from typing import Any, Callable

from PySide6.QtCore import QObject, QThread

from api.client import NexoraClient

from services.widgets.box_messages import MessageBox


class BasePoller(QObject):
    def __init__(self, client: NexoraClient):
        super().__init__()
        self.client = client

        self._active_workers: list[dict] = []

        self.is_polling = False
        self.api_error_shown = False

    def _cancel_all_requests(self) -> None:
        for ctx in self._active_workers:
            thread = ctx["thread"]
            worker = ctx["worker"]

            if thread.isRunning():
                try:
                    worker.success.disconnect()
                    worker.error.disconnect()
                except (RuntimeError, AttributeError):
                    pass

                thread.quit()

                worker.deleteLater()
                thread.deleteLater()

        self._active_workers.clear()
        self.is_polling = False

    def _start_worker(
        self,
        worker: QObject,
        worker_slot: Callable[[], None],
        success_callback: Callable[[Any], None],
        error_callback: Callable[[Any], None] = None,
    ) -> None:
        self.is_polling = True

        thread = QThread(self)
        worker.moveToThread(thread)

        worker_context = {"thread": thread, "worker": worker}
        self._active_workers.append(worker_context)

        thread.started.connect(worker_slot)
        worker.success.connect(success_callback)
        worker.error.connect(error_callback or self._show_api_error)

        worker.finished.connect(thread.quit)
        worker.finished.connect(worker.deleteLater)
        thread.finished.connect(thread.deleteLater)

        def cleanup() -> None:
            if worker_context in self._active_workers:
                self._active_workers.remove(worker_context)

            if not self._active_workers:
                self.is_polling = False

        thread.finished.connect(cleanup)
        thread.start()

    def _show_api_error(self, message: str | None = None) -> None:
        if not self.api_error_shown:
            self.api_error_shown = True
            MessageBox().show_message(
                "critical",
                "API error",
                "API connection failed! Please check your settings.",
            )
