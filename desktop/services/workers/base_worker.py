import asyncio

from PySide6.QtCore import QObject, Signal


class BaseWorker(QObject):
    finished = Signal()
    success = Signal(object)
    error = Signal(str)

    def _run_async(self, async_func, *args, **kwargs) -> None:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        try:
            raw_results = loop.run_until_complete(async_func(*args, **kwargs))

            if isinstance(raw_results, dict) and "results" in raw_results:
                self.success.emit(raw_results["results"])
            else:
                self.success.emit(raw_results)

        except Exception as exc:
            self.error.emit(str(exc))

        finally:
            loop.close()
            self.finished.emit()
