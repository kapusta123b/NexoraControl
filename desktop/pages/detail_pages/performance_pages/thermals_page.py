from services.pollers.metrics_poller import AgentMetricPoller
from services.stores.metric_store import MetricStore

from services.graph_helper import MetricGraphHelper

from services.widgets.gauge import SimpleNetdataGauge

from PySide6.QtWidgets import QHeaderView


from ui.main_window import Ui_MainWindow


class PerformanceThermalPage:

    def __init__(
        self, ui: Ui_MainWindow, store: MetricStore, poller: AgentMetricPoller
    ):
        self.performance_store = store
        self.performance_poller = poller

        self.ui = ui

        self.cpu_package_gauge = SimpleNetdataGauge(
            title="CPU PACKAGE",
            unit="°C",
            color="#fb923c",
        )

        self.hottest_sensor_gauge = SimpleNetdataGauge(
            title="HOTTEST SENSOR",
            unit="°C",
            color="#f43f5e",
        )

        self.nvme_gauge = SimpleNetdataGauge(
            title="NVMe",
            unit="°C",
            color="#facc15",
        )

        self.ui.thermals_gauge_layout.addWidget(self.cpu_package_gauge)
        self.ui.thermals_gauge_layout.addWidget(self.hottest_sensor_gauge)
        self.ui.thermals_gauge_layout.addWidget(self.nvme_gauge)

        self.thermals_graph = MetricGraphHelper(
            self.ui.thermals_graph,
            antialias=True,
            y_label="Speed",
            y_range=(0, 100),
        )

        self._setup_style_page()

    def _setup_style_page(self):
        self.ui.sensors_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.ui.sensors_table.verticalHeader().setVisible(False)
        self.ui.sensors_table.horizontalHeader().setHighlightSections(False)

        self.ui.thermal_sensor_name_combo_box.setEnabled(False)
