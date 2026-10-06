from services.utils.widgets_utils import (
    set_gauge,
    setup_table_progress_bar,
    update_or_create_row_item,
)
from services.pollers.metrics_poller import AgentMetricPoller

from services.stores.agent_metric_store import MetricStore

from services.graph_helper import MetricGraphHelper

from services.widgets.gauge import SimpleNetdataGauge
from services.widgets.box_messages import MessageBox

from PySide6.QtWidgets import QHeaderView

from ui.main_window import Ui_MainWindow


class PerformanceThermalPage:

    def __init__(
        self, ui: Ui_MainWindow, store: MetricStore, poller: AgentMetricPoller
    ):
        self.performance_store = store
        self.performance_poller = poller

        self.ui = ui

        self.current_sensor_gauge = SimpleNetdataGauge(
            title="CURRENT SENSOR",
            unit="°C",
            color="#fb923c",
        )

        self.hottest_sensor_gauge = SimpleNetdataGauge(
            title="HOTTEST SENSOR",
            unit="°C",
            color="#f43f5e",
        )

        self.ui.thermals_gauge_layout.addWidget(self.current_sensor_gauge)
        self.ui.thermals_gauge_layout.addWidget(self.hottest_sensor_gauge)

        self.thermals_graph = MetricGraphHelper(
            self.ui.thermals_graph,
            antialias=False,
            y_label="Temperature",
            y_range=(0, 100),
        )

        self.is_init_hardware_group_selector = False

        self.current_hardware = None
        self.current_sensor = None

        self.thermal_sensors_counters = {}

        self._setup_style_page()
        self._setup_static_series()

        self.performance_store.metrics_loaded.connect(self.on_history_received)
        self.performance_store.metrics_appended.connect(self.on_latest_received)

    def _setup_style_page(self):
        self.ui.sensors_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.ui.sensors_table.verticalHeader().setVisible(False)
        self.ui.sensors_table.horizontalHeader().setHighlightSections(False)

        self.ui.thermal_sensor_name_combo_box.setEnabled(False)

    def on_history_received(self, metrics: dict):
        current_page_widget = self.ui.performance_stacked_content.currentWidget()

        if not current_page_widget == self.ui.performance_thermal_page:
            return

        incoming_timestamps = metrics.get("timestamps", [])
        if not incoming_timestamps:
            if not self.is_init_hardware_group_selector:
                self._init_hardware_group_selector(metrics.get("hardwares_names", {}))

            return

        thermal_data = metrics.get("thermal_metrics", {})
        if thermal_data:
            for hardware, sensors in thermal_data.items():
                self.thermal_sensors_counters[hardware] = {
                    "timestamps": incoming_timestamps,
                    **sensors,
                }

            self._change_thermal_data_on_graph(self.current_sensor)

    def on_latest_received(self, metric: dict) -> None:
        timestamp = metric.get("timestamp")
        current_thermals = metric.get("thermal_metrics", {})

        if not timestamp:
            return

        for hardware_name in self.thermal_sensors_counters.keys():
            if hardware_name not in current_thermals:
                return

            current_hardware_sensors = self.thermal_sensors_counters[
                hardware_name
            ].keys()

            self.thermal_sensors_counters[hardware_name]["timestamps"].append(timestamp)

            for metric_hardware, sensors in current_thermals.items():
                if metric_hardware == self.current_hardware and self.current_sensor:
                    current_metric_hardware_sensors = current_thermals[metric_hardware]
                    for sensor in current_metric_hardware_sensors:
                        if self.current_sensor == sensor["label"]:
                            current_temperature = sensor["current"]

                            set_gauge(self.current_sensor_gauge, current_temperature)

                            self.thermals_graph.append_point(
                                timestamp, {"TEMPERATURE": current_temperature}
                            )

                for sensor in sensors:
                    current_temp = sensor["current"]
                    sensor_name = sensor["label"]
                    if sensor_name in current_hardware_sensors:
                        self.thermal_sensors_counters[hardware_name][
                            sensor_name
                        ].append(current_temp)

        self._find_hottest_sensor(current_thermals)
        self._update_sensors_table(current_thermals)

    def _find_hottest_sensor(self, thermals: dict):
        if not thermals:
            return

        hottest_sensor = ("", 0)

        for hardware, sensors in thermals.items():
            for sensor in sensors:
                sensor_name, temperature = hottest_sensor

                metric_temperature = sensor["current"]
                metric_sensor_name = sensor["label"]
                if sensor["current"] > temperature:
                    hottest_sensor = (
                        f"{hardware} {metric_sensor_name}",
                        metric_temperature,
                    )

        hottest_sensor_name, hottest_temperature = hottest_sensor

        self.hottest_sensor_gauge.legend = hottest_sensor_name
        set_gauge(self.hottest_sensor_gauge, hottest_temperature)

    def _update_sensors_table(self, thermals: dict[str, list[dict]] | None) -> None:
        if not thermals:
            return

        table = self.ui.sensors_table

        for hardware, sensors in thermals.items():
            for sensor in sensors:
                row = -1

                for r in range(table.rowCount()):
                    item_group = table.item(r, 0)
                    item_label = table.item(r, 1)

                    if item_group and item_label:
                        if (
                            item_group.text() == hardware
                            and item_label.text() == sensor["label"]
                        ):
                            row = r
                            break

                if row == -1:
                    row = table.rowCount()
                    table.insertRow(row)

                update_or_create_row_item(table, row, 0, hardware)
                update_or_create_row_item(table, row, 1, sensor["label"])
                update_or_create_row_item(table, row, 2, str(sensor["high"]))
                update_or_create_row_item(table, row, 3, str(sensor["critical"]))

                setup_table_progress_bar(table, row, 4, sensor["current"])

    def _change_thermal_data_on_graph(self, current_sensor=None) -> None:
        if not self.current_hardware and current_sensor:
            return

        self.current_sensor = current_sensor

        if self.current_hardware or current_sensor:
            if (
                self.current_hardware not in self.thermal_sensors_counters
                or self.current_sensor
                not in self.thermal_sensors_counters[self.current_hardware]
            ):
                self.performance_poller.on_clicked(
                    metric_type="thermal",
                    query_params={
                        "hardware": self.current_hardware,
                        "sensors": current_sensor,
                    },
                )

                return

        hardware_cache = self.thermal_sensors_counters[self.current_hardware]
        disk_timestamps = hardware_cache["timestamps"]

        sensor_temperatures = hardware_cache[self.current_sensor]

        if sensor_temperatures:
            set_gauge(self.current_sensor_gauge, sensor_temperatures[-1])

        self.thermals_graph.update_data(
            disk_timestamps,
            {
                "TEMPERATURE": sensor_temperatures,
            },
        )

    def _change_sensors_group_by_hardware(self):
        self.current_hardware = self.ui.hardware_group_combo_box.currentText()

        current_sensors = self.hardwares_with_sensors_list[self.current_hardware]

        self.ui.thermal_sensor_name_combo_box.clear()
        self.ui.thermal_sensor_name_combo_box.addItems(current_sensors)

    def _init_hardware_group_selector(self, hardwares: dict[str, list[str]]):
        if hardwares:
            self.hardwares_with_sensors_list = hardwares

            hardwares_keys = hardwares.keys()

            self.ui.hardware_group_combo_box.addItems(hardwares_keys)

            self.ui.hardware_group_combo_box.currentTextChanged.connect(
                self._change_sensors_group_by_hardware
            )

            self.ui.thermal_sensor_name_combo_box.currentTextChanged.connect(
                self._change_thermal_data_on_graph
            )
            self.is_init_hardware_group_selector = True

            self.ui.thermal_sensor_name_combo_box.setEnabled(True)
        else:
            MessageBox().show_message(
                message_type="warning",
                title="Hardwares not found",
                text=(
                    "Error to get a hardwares list.\n\n"
                    "Possible causes:\n"
                    "1. The backend API is not running, or an incorrect API URL s specified in the settings.\n"
                    "2. The NexoraControl agent does not have permission to save system thermal metrics.\n\n"
                    "3. The NexoraControl agent not running.\n"
                    "Check the thermal driver on the agent side."
                ),
            )

    def _setup_static_series(self) -> None:
        self.thermals_graph.add_series("TEMPERATURE", "#f97316", suffix="°C")
