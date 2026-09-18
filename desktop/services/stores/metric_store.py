from PySide6.QtCore import QObject, Signal


class MetricStore(QObject):
    metrics_loaded = Signal(dict)
    metrics_appended = Signal(dict)

    def __init__(self) -> None:
        super().__init__()
        self._metrics: dict[str, list[float] | float] = {}

    @property
    def metrics(self) -> dict[str, list[float] | float]:
        return self._metrics

    def set_history(self, metrics: dict[str, list[float]]) -> None:
        self._metrics = metrics
        self.metrics_loaded.emit(self._metrics)

    def append_point(self, new_metrics: dict[str, float]) -> None:
        for key, value in new_metrics.items():
            current = self._metrics.get(key)
            if isinstance(current, list):
                current.append(value)
            else:
                self._metrics[key] = value

        self.metrics_appended.emit(new_metrics)
