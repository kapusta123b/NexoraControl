from services.graph_helper import MetricGraphHelper
from services.stores.metric_store import MetricStore
from services.widgets.gauge import SimpleNetdataGauge

from ui.main_window import Ui_MainWindow


class PerformanceStoragePage:

    def __init__(self, ui: Ui_MainWindow, store: MetricStore):
        self.performance_store = store
        self.ui = ui

        self.disk_usage_gauge = SimpleNetdataGauge(
            "DISK USAGE",
            color="#34d399",
        )

        self.disk_read_gauge = SimpleNetdataGauge(
            "READ",
            "MB/s",
            "#60a5fa",
        )

        self.disk_write_gauge = SimpleNetdataGauge(
            "WRITE",
            "MB/s",
            "#f59e0b",
        )

        self.ui.storage_gauge_layout.addWidget(self.disk_usage_gauge)
        self.ui.storage_gauge_layout.addWidget(self.disk_read_gauge)
        self.ui.storage_gauge_layout.addWidget(self.disk_write_gauge)

        self.disk_io_graph = MetricGraphHelper(
            self.ui.disk_write_read_graph, y_label="Speed (MB/S)", y_range=(0, 10000)
        )

        self._setup_static_series()

    def _setup_static_series(self):
        self.disk_io_graph.add_series("READ", "#60a5fa")
        self.disk_io_graph.add_series("WRITE", "#f59e0b")
