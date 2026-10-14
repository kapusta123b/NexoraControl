from services.utils.widgets_utils import (
    set_gauge,
    setup_table_progress_bar,
    update_or_create_row_item,
)
from services.utils.string_utils import (
    UNIT_MAP,
    byte_converter,
    calculate_bytes_per_second,
    calculate_metric_rate,
)

from services.pollers.metrics_poller import AgentMetricPoller
from services.stores.agent_metric_store import MetricStore

from services.graph_helper import MetricGraphHelper

from services.widgets.gauge import SimpleNetdataGauge
from services.widgets.box_messages import MessageBox

from PySide6.QtWidgets import QHeaderView

from ui.main_window import Ui_MainWindow


class PerformanceStoragePage:

    def __init__(
        self, ui: Ui_MainWindow, store: MetricStore, poller: AgentMetricPoller
    ) -> None:
        self.performance_store = store
        self.performance_poller = poller

        self.ui = ui

        self.disk_read_gauge = SimpleNetdataGauge(
            title="READ",
            unit="MB/s",
            color="#60a5fa",
        )

        self.disk_write_gauge = SimpleNetdataGauge(
            title="WRITE",
            unit="MB/s",
            color="#f59e0b",
        )

        self.ui.storage_gauge_layout.addWidget(self.disk_read_gauge)
        self.ui.storage_gauge_layout.addWidget(self.disk_write_gauge)

        self.disk_io_graph = MetricGraphHelper(
            self.ui.disk_write_read_graph,
            antialias=True,
            y_label="Speed",
            y_range=(0, 10000000),
        )
        self.current_disk = None

        self.read_speed = 0
        self.write_speed = 0

        self.is_init_disk_selector = False

        self.storage_io_counters = {}

        self.delta_time = None

        self.last_storage_metric = {}
        self.current_metric = {}

        self._setup_style_page()
        self._setup_static_series()
        self._init_data_unit_selector()

        self.performance_store.metrics_loaded.connect(self.on_history_received)
        self.performance_store.metrics_appended.connect(self.on_latest_received)

    def _setup_style_page(self) -> None:
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

    def on_history_received(self, metrics: dict) -> None:
        current_page_widget = self.ui.performance_stacked_content.currentWidget()

        if not current_page_widget == self.ui.performance_storage_page:
            return

        incoming_timestamps = metrics.get("timestamps", [])
        if not incoming_timestamps:
            if not self.is_init_disk_selector:
                self._init_disk_selector(metrics.get("disks_names", []))

            return

        storage_data = metrics.get("storage_metrics", {})
        if storage_data:
            for disk_name, disk_info in storage_data.items():
                self.storage_io_counters[disk_name] = {
                    "timestamps": incoming_timestamps,
                    **disk_info,
                }

            self._change_disk_on_graph(self.current_disk)

    def on_latest_received(self, metric: dict) -> None:
        timestamp = metric.get("timestamp")
        current_storage = metric.get("storage_metrics", {})

        current_devices = current_storage.get("devices", {})
        current_filesystems = current_storage.get("filesystems", {})

        if not timestamp:
            return

        if not self.last_storage_metric:
            self.last_storage_metric = current_storage
            self.last_timestamp = timestamp

            return

        last_devices = self.last_storage_metric.get("devices", {})

        self.delta_time = timestamp - self.last_timestamp

        self.current_devices = current_devices
        self.last_devices = last_devices

        self.current_filesystems = current_filesystems

        if self.delta_time > 0:
            for disk_name in self.storage_io_counters.keys():
                if disk_name not in current_devices and disk_name not in last_devices:
                    return

                read_bytes = current_devices[disk_name].get("read_bytes", 0)
                write_bytes = current_devices[disk_name].get("write_bytes", 0)

                self.storage_io_counters[disk_name]["timestamps"].append(timestamp)

                if disk_name == self.current_disk:
                    self._prepare_dynamic_data()
                    self.disk_io_graph.append_point(
                        timestamp, {"READ": self.read_speed, "WRITE": self.write_speed}
                    )

                self.storage_io_counters[disk_name]["read"].append(read_bytes)
                self.storage_io_counters[disk_name]["write"].append(write_bytes)
        self.last_storage_metric = current_storage
        self.last_timestamp = timestamp

        self._update_storage_tables(current_devices, current_filesystems)

    def _change_disk_on_graph(self, disk_name: str | None) -> None:
        if not disk_name:
            return

        self.current_disk = disk_name
        self.current_unit = self.ui.disk_data_unit_combo_box.currentText()
        self.formatted_current_unit = self.current_unit.split("/")[0].lower()

        if not disk_name in self.storage_io_counters:
            self.performance_poller.on_clicked(
                metric_type="storage", query_params={"disk": disk_name}
            )

            return

        if self.current_disk:
            self._prepare_dynamic_data()

        disk_cache = self.storage_io_counters[disk_name]
        disk_timestamps = disk_cache["timestamps"]

        self.disk_io_graph.series_suffixes["READ"] = self.current_unit
        self.disk_io_graph.series_suffixes["WRITE"] = self.current_unit

        read_speed = calculate_bytes_per_second(
            disk_cache["read"], disk_timestamps, self.formatted_current_unit
        )
        write_speed = calculate_bytes_per_second(
            disk_cache["write"], disk_timestamps, self.formatted_current_unit
        )

        self.disk_io_graph.update_data(
            disk_timestamps[1:],
            {
                "READ": read_speed,
                "WRITE": write_speed,
            },
        )

    def _init_data_unit_selector(self) -> None:
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

    def _init_disk_selector(self, disks: list[str]) -> None:
        if disks:
            disks = [disk for disk in disks if not "p" in disk]
            self.ui.disks_combo_box.addItems(disks)

            self.ui.disks_combo_box.currentTextChanged.connect(
                self._change_disk_on_graph
            )
            self.is_init_disk_selector = True

            self.ui.disk_data_unit_combo_box.setEnabled(True)
        else:
            MessageBox().show_message(
                message_type="warning",
                title="Disks not found",
                text=(
                    "Error to get a disks list.\n\n"
                    "Possible causes:\n"
                    "1. The backend API is not running, or an incorrect API URL s specified in the settings.\n"
                    "2. There are no mounted disks on the target server/agent.\n"
                    "3. The NexoraControl agent does not have permission to read system metrics.\n\n"
                    "4. The NexoraControl agent not running.\n"
                    "Check the mount settings on the agent side."
                ),
            )

    def _update_storage_tables(self, devices: dict, filesystems: dict) -> None:
        self._update_devices_table(devices)
        self._update_filesystems_table(filesystems)

    def _update_devices_table(self, devices: dict) -> None:
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

    def _update_filesystems_table(self, filesystems: dict) -> None:
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

            percent = info["percent"]

            update_or_create_row_item(table, row, 0, info["mount"])
            update_or_create_row_item(table, row, 1, fs_name)
            update_or_create_row_item(table, row, 2, info["fstype"])
            update_or_create_row_item(table, row, 3, byte_converter(info["used"], "gb"))
            update_or_create_row_item(table, row, 4, byte_converter(info["free"], "gb"))

            setup_table_progress_bar(table, row, 5, percent)

    def _setup_static_series(self) -> None:
        self.disk_io_graph.add_series("READ", "#60a5fa", suffix=" MB/s")
        self.disk_io_graph.add_series("WRITE", "#f59e0b", suffix=" MB/s")

    def _prepare_dynamic_data(self) -> None:
        if not self.delta_time:
            return

        delta_time = self.delta_time

        current_device_disk = self.current_devices[self.current_disk]
        last_device_disk = self.last_devices[self.current_disk]

        raw_r_bps = calculate_metric_rate(
            current_device_disk, last_device_disk, "read_bytes", delta_time
        )
        raw_w_bps = calculate_metric_rate(
            current_device_disk, last_device_disk, "write_bytes", delta_time
        )

        self.read_speed = byte_converter(
            raw_r_bps, unit=self.formatted_current_unit, precision=2, as_float=True
        )

        self.write_speed = byte_converter(
            raw_w_bps, unit=self.formatted_current_unit, precision=2, as_float=True
        )

        r_iops = calculate_metric_rate(
            current_device_disk, last_device_disk, "read_count", delta_time
        )
        w_iops = calculate_metric_rate(
            current_device_disk, last_device_disk, "write_count", delta_time
        )

        set_gauge(self.disk_write_gauge, self.write_speed, self.current_unit)
        set_gauge(self.disk_read_gauge, self.read_speed, self.current_unit)

        io_data = {
            "read_speed": self.read_speed,
            "write_speed": self.write_speed,
            "read_iops": int(r_iops),
            "write_iops": int(w_iops),
            # "avg_latency": current_device_disk["avg_latency"],
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

        # self.ui.disk_avg_latency_value.setText(f"{str(data["avg_latency"])} ms")
