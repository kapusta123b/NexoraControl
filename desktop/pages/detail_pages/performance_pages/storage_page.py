from services.utils import UNIT_MAP, byte_converter

from services.pollers.metrics_poller import AgentMetricPoller
from services.stores.metric_store import MetricStore

from services.graph_helper import MetricGraphHelper

from services.widgets.gauge import SimpleNetdataGauge

from PySide6.QtWidgets import QHeaderView

from ui.main_window import Ui_MainWindow


class PerformanceStoragePage:

    def __init__(
        self, ui: Ui_MainWindow, store: MetricStore, poller: AgentMetricPoller
    ):
        self.performance_store = store
        self.performance_poller = poller

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
            self.ui.disk_write_read_graph, y_label="Speed", y_range=(0, 100000)
        )
        self.current_disk = None

        self.is_init_disk_selector = False

        self.storage_io_counters = {}

        self._setup_style_page()
        self._setup_static_series()
        self._init_data_unit_selector()

        self.performance_store.metrics_loaded.connect(self.on_history_received)
        self.performance_store.metrics_appended.connect(self.on_latest_received)

    def _setup_style_page(self):
        self.ui.file_systems_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.ui.storage_devices_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.ui.device_activity_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.ui.disk_data_unit_combo_box.setEnabled(False)

    def on_history_received(self, metrics: dict):
        self.timestamps = metrics.get("timestamps", [])
        if not self.timestamps:
            if not self.is_init_disk_selector:
                self._init_disk_selector(metrics.get("disks_names", []))

        self.storage_io_counters.update(metrics.get("storage_metrics", {}))

        self._change_disk_on_graph(self.current_disk)

    def on_latest_received(self, metric: dict):
        timestamp = metric.get("timestamp")
        if not timestamp:
            return

        if self.current_disk:
            self.disk_usage_gauge.set_value(
                metric["storage_metrics"][self.current_disk].get("percent", 0.0)
            )

    def _init_data_unit_selector(self):
        unit_keys = [unit.upper() + "/s" for unit in UNIT_MAP.keys()]
        self.ui.disk_data_unit_combo_box.addItems(unit_keys)

        default_index = self.ui.disk_data_unit_combo_box.findText("MB/s")

        if default_index >= 0:
            self.ui.disk_data_unit_combo_box.setCurrentIndex(default_index)

        self.ui.disk_data_unit_combo_box.currentTextChanged.connect(
            lambda: (
                self._change_disk_on_graph(self.current_disk)
                if self.current_disk
                else None
            )
        )

    def _init_disk_selector(self, disks: list[str]):
        if disks and isinstance(disks, list):
            self.ui.disks_combo_box.addItems(disks)

            self.ui.disks_combo_box.currentTextChanged.connect(
                self._change_disk_on_graph
            )
            self.is_init_disk_selector = True

            self.ui.disk_data_unit_combo_box.setEnabled(True)

    def _change_disk_on_graph(self, disk_name):

        self.current_disk = disk_name

        if not disk_name in list(self.storage_io_counters.keys()):
            self.performance_poller.on_clicked(
                metric_type="storage", query_params={"disk": disk_name}
            )

            return

        if self.storage_io_counters:
            write_bytes = self.storage_io_counters[disk_name]["write"]
            read_bytes = self.storage_io_counters[disk_name]["read"]

            read_speed = self._calculate_bytes_per_second(read_bytes)
            write_speed = self._calculate_bytes_per_second(write_bytes)

            if read_speed and write_speed:
                self._set_gauges(read_speed=read_speed[-1], write_speed=write_speed[-1])

            self.disk_io_graph.update_data(
                self.timestamps[1:],
                {
                    "READ": read_speed,
                    "WRITE": write_speed,
                },
            )

    def _calculate_bytes_per_second(self, raw_bytes: list[int]) -> list[float]:
        speed_in_bytes = []

        self.current_unit = self.ui.disk_data_unit_combo_box.currentText()

        self.disk_io_graph.series_suffixes["READ"] = self.current_unit
        self.disk_io_graph.series_suffixes["WRITE"] = self.current_unit

        if raw_bytes:
            for i in range(1, len(raw_bytes)):
                delta_raw_bytes = raw_bytes[i] - raw_bytes[i - 1]
                delta_time = self.timestamps[i] - self.timestamps[i - 1]

                if delta_time > 0:
                    bytes_per_second = delta_raw_bytes / delta_time
                else:
                    bytes_per_second = 0

                converted_speed = byte_converter(
                    bytes_per_second,
                    unit=self.current_unit.split("/")[0].lower(),
                    as_float=True,
                )
                speed_in_bytes.append(converted_speed)

        return speed_in_bytes

    def _set_gauges(self, write_speed: int, read_speed: int):
        self.disk_write_gauge.set_value(write_speed)
        self.disk_read_gauge.set_value(read_speed)

        if write_speed > self.disk_write_gauge.max_value:
            self.disk_write_gauge.max_value = round(write_speed)

        if read_speed > self.disk_read_gauge.max_value:
            self.disk_read_gauge.max_value = round(read_speed)

    def _setup_static_series(self):
        self.disk_io_graph.add_series("READ", "#60a5fa", suffix=" MB/s")
        self.disk_io_graph.add_series("WRITE", "#f59e0b", suffix=" MB/s")
