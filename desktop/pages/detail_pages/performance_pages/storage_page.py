from services.utils import UNIT_MAP, byte_converter, update_or_create_row_item

from services.pollers.metrics_poller import AgentMetricPoller
from services.stores.metric_store import MetricStore

from services.graph_helper import MetricGraphHelper

from services.widgets.gauge import SimpleNetdataGauge

from PySide6.QtWidgets import QHeaderView, QProgressBar

from PySide6.QtCore import Qt
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
            self.ui.disk_write_read_graph,
            antialias=True,
            y_label="Speed",
            y_range=(0, 1000000),
        )
        self.current_disk = None

        self.is_init_disk_selector = False

        self.storage_io_counters = {}

        self.last_storage_metric = {}
        self.current_metric = {}

        self.current_disk_info = {}
        self.last_disk_info = {}

        self._setup_style_page()
        self._setup_static_series()
        self._init_data_unit_selector()

        self.performance_store.metrics_loaded.connect(self.on_history_received)
        self.performance_store.metrics_appended.connect(self.on_latest_received)

    def _setup_style_page(self):
        # Растягиваем колонки [1]
        self.ui.file_systems_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.ui.storage_devices_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.ui.file_systems_table.verticalHeader().setVisible(False)
        self.ui.storage_devices_table.verticalHeader().setVisible(False)

        self.ui.file_systems_table.horizontalHeader().setHighlightSections(False)
        self.ui.storage_devices_table.horizontalHeader().setHighlightSections(False)

        self.ui.disk_data_unit_combo_box.setEnabled(False)

    def on_history_received(self, metrics: dict):
        incoming_timestamps = metrics.get("timestamps", [])
        if not incoming_timestamps:
            if not self.is_init_disk_selector:
                self._init_disk_selector(metrics.get("disks_names", []))

            return

        storage_data = metrics.get("storage_metrics", {})

        for disk_name, disk_info in storage_data.items():
            self.storage_io_counters[disk_name] = {
                "timestamps": list(incoming_timestamps),
                "read": disk_info.get("read", []),
                "write": disk_info.get("write", []),
            }

        self._change_disk_on_graph(self.current_disk)

    def on_latest_received(self, metric: dict):
        timestamp = metric.get("timestamp")
        current_storage = metric.get("storage_metrics", {})

        current_devices = current_storage.get("devices", {})
        current_filesystems = current_storage.get("filesystems", {})

        if not timestamp or not current_devices or not self.current_disk:
            return

        if not self.last_storage_metric:
            self.last_storage_metric = current_storage
            self.last_timestamp = timestamp

            return

        self._update_storage_tables(current_devices, current_filesystems)

        last_devices = self.last_storage_metric.get("devices", {})
        self.delta_time = timestamp - self.last_timestamp

        if self.delta_time > 0:
            for disk_name in list(self.storage_io_counters.keys()):
                if disk_name in current_devices and disk_name in last_devices:
                    self.current_disk_info = current_devices[disk_name]
                    self.last_disk_info = last_devices[disk_name]

                    if disk_name == self.current_disk:
                        self._prepare_dynamic_data(
                            self.current_disk_info, self.last_disk_info, self.delta_time
                        )

                    self.storage_io_counters[disk_name]["timestamps"].append(timestamp)
                    self.storage_io_counters[disk_name]["read"].append(
                        self.current_disk_info.get("read_bytes", 0)
                    )
                    self.storage_io_counters[disk_name]["write"].append(
                        self.current_disk_info.get("write_bytes", 0)
                    )

        self._change_disk_on_graph(self.current_disk)

        self.last_storage_metric = current_storage
        self.last_timestamp = timestamp

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
            disks = [disk for disk in disks if not "p" in disk]
            self.ui.disks_combo_box.addItems(disks)

            self.ui.disks_combo_box.currentTextChanged.connect(
                self._change_disk_on_graph
            )
            self.is_init_disk_selector = True

            self.ui.disk_data_unit_combo_box.setEnabled(True)

    def _change_disk_on_graph(self, disk_name):
        self.current_disk = disk_name

        self.current_unit = self.ui.disk_data_unit_combo_box.currentText()

        if not disk_name in self.storage_io_counters:
            self.performance_poller.on_clicked(
                metric_type="storage", query_params={"disk": disk_name}
            )

            return

        if self.current_disk_info and self.last_disk_info:
            self._prepare_dynamic_data(
                self.current_disk_info, self.last_disk_info, self.delta_time
            )

        disk_cache = self.storage_io_counters[disk_name]
        disk_timestamps = disk_cache["timestamps"]

        read_speed = self._calculate_bytes_per_second(
            disk_cache["read"], disk_timestamps
        )
        write_speed = self._calculate_bytes_per_second(
            disk_cache["write"], disk_timestamps
        )

        self.disk_io_graph.update_data(
            disk_timestamps[1:],
            {
                "READ": read_speed,
                "WRITE": write_speed,
            },
        )

    def _calculate_bytes_per_second(
        self, raw_bytes: list[int], disk_timestamps: list[int]
    ) -> list[float]:
        speed_in_bytes = []

        self.disk_io_graph.series_suffixes["READ"] = self.current_unit
        self.disk_io_graph.series_suffixes["WRITE"] = self.current_unit

        if raw_bytes and len(raw_bytes) == len(disk_timestamps):
            for i in range(1, len(raw_bytes)):
                delta_raw_bytes = raw_bytes[i] - raw_bytes[i - 1]
                delta_time = disk_timestamps[i] - disk_timestamps[i - 1]

                if delta_time > 0 and delta_raw_bytes >= 0:
                    bytes_per_second = delta_raw_bytes / delta_time
                else:
                    bytes_per_second = 0

                converted_speed = byte_converter(
                    bytes_per_second,
                    unit=self.current_unit.split("/")[0].lower(),
                    precision=4,
                    as_float=True,
                )
                speed_in_bytes.append(converted_speed)

        return speed_in_bytes

    def _set_gauges(self, r_speed: dict, w_speed: dict) -> None:
        self.disk_write_gauge.set_value(r_speed)
        self.disk_read_gauge.set_value(w_speed)

        if self.current_unit:
            self.disk_read_gauge.unit = self.current_unit
            self.disk_write_gauge.unit = self.current_unit

        if w_speed > self.disk_write_gauge.max_value:
            self.disk_write_gauge.max_value = round(w_speed)

        if r_speed > self.disk_read_gauge.max_value:
            self.disk_read_gauge.max_value = round(r_speed)

    def _calculate_metric_rate(
        self, current_data: dict, last_data: dict, key: str, delta_time: float
    ) -> float:

        if delta_time <= 0:
            return 0.0

        delta_value = current_data.get(key, 0) - last_data.get(key, 0)

        return max(0.0, delta_value / delta_time)

    def _prepare_dynamic_data(
        self, current_disk: dict, last_disk: dict, delta_time: float
    ) -> None:

        r_bps = self._calculate_metric_rate(
            current_disk, last_disk, "read_bytes", delta_time
        )
        w_bps = self._calculate_metric_rate(
            current_disk, last_disk, "write_bytes", delta_time
        )

        r_iops = self._calculate_metric_rate(
            current_disk, last_disk, "read_count", delta_time
        )
        w_iops = self._calculate_metric_rate(
            current_disk, last_disk, "write_count", delta_time
        )

        current_unit = self.current_unit.split("/")[0].lower()

        read_speed = byte_converter(
            r_bps, unit=current_unit, precision=1, as_float=True
        )
        write_speed = byte_converter(
            w_bps, unit=current_unit, precision=1, as_float=True
        )

        self._set_gauges(read_speed, write_speed)

        io_data = {
            "read_speed": read_speed,
            "write_speed": write_speed,
            "read_iops": int(r_iops),
            "write_iops": int(w_iops),
            "avg_latency": current_disk.get("avg_latency", 0),
        }

        self._set_io_summary(io_data)

    def _set_io_summary(self, data: dict) -> None:
        self.ui.disk_read_information_value.setText(
            f"{data['read_speed']} {self.current_unit}"
        )
        self.ui.disk_write_information_value.setText(
            f"{data['write_speed']} {self.current_unit}"
        )

        self.ui.disk_read_per_sec_information_value.setText(str(data["read_iops"]))
        self.ui.disk_write_per_sec_information_value.setText(str(data["write_iops"]))

        self.ui.disk_avg_latency_value.setText(str(data["avg_latency"]))

    def _update_storage_tables(self, devices: dict, filesystems: dict):
        self._update_devices_table(devices)
        self._update_filesystems_table(filesystems)

    def _update_devices_table(self, devices: dict):
        table = self.ui.storage_devices_table

        for disk_name, info in devices.items():
            row = -1
            for r in range(table.rowCount()):
                item = table.item(r, 0)
                if item and item.text() == disk_name:
                    row = r
                    break

            if row == -1:
                row = table.rowCount()
                table.insertRow(row)

            update_or_create_row_item(table, row, 0, disk_name)
            update_or_create_row_item(table, row, 1, info.get("model", "Unknown"))
            update_or_create_row_item(table, row, 2, info.get("type", "N/A"))
            update_or_create_row_item(table, row, 3, info.get("capacity", "N/A"))
            update_or_create_row_item(table, row, 4, info.get("status", "UNKNOWN"))

    def _update_filesystems_table(self, filesystems: dict):
        table = self.ui.file_systems_table

        for fs_name, info in filesystems.items():
            row = -1
            for r in range(table.rowCount()):
                item = table.item(r, 1)
                if item and item.text() == fs_name:
                    row = r
                    break

            if row == -1:
                row = table.rowCount()
                table.insertRow(row)

            percent = info.get("percent", 0)
            used_pct = f"{percent}%"

            update_or_create_row_item(table, row, 0, info.get("mount", "N/A"))
            update_or_create_row_item(table, row, 1, fs_name)
            update_or_create_row_item(table, row, 2, info.get("fstype", "N/A"))
            update_or_create_row_item(
                table, row, 3, byte_converter(info.get("used", "N/A"), "gb")
            )
            update_or_create_row_item(
                table, row, 4, byte_converter(info.get("free", "N/A"), "gb")
            )
            update_or_create_row_item(
                table, row, 4, byte_converter(info.get("free", "N/A"), "gb")
            )

            if percent < 60:
                load_level = "low"
            elif percent < 85:
                load_level = "medium"
            else:
                load_level = "high"

            progress_bar = table.cellWidget(row, 5)

            if not isinstance(progress_bar, QProgressBar):
                progress_bar = QProgressBar()
                progress_bar.setRange(0, 100)

                table.setRowHeight(row, 34)

                table.setCellWidget(row, 5, progress_bar)

            if progress_bar.value() != percent:
                progress_bar.setValue(percent)
                progress_bar.setFormat(f"{percent}%")

                progress_bar.setProperty("load_level", load_level)

                progress_bar.style().unpolish(progress_bar)
                progress_bar.style().polish(progress_bar)

    def _setup_static_series(self):
        self.disk_io_graph.add_series("READ", "#60a5fa", suffix=" MB/s")
        self.disk_io_graph.add_series("WRITE", "#f59e0b", suffix=" MB/s")
