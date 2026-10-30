from services.utils.string_utils import (
    UNIT_MAP,
    byte_converter,
    calculate_bytes_per_second,
    calculate_metric_rate,
)
from services.utils.widgets_utils import (
    apply_style_for_tables,
    set_gauge,
    update_or_create_row_item,
)

from styles.metric_colors import MetricColors as C

from services.pollers.metrics_poller import AgentMetricPoller

from services.stores.agent_metric_store import MetricStore

from services.graph_helper import MetricGraphHelper

from services.widgets.gauge import SimpleNetdataGauge
from services.widgets.box_messages import MessageBox

from PySide6.QtWidgets import QHeaderView, QButtonGroup

from PySide6.QtCore import QObject

from ui.main_window import Ui_MainWindow


class PerformanceNetworkPage(QObject):

    def __init__(
        self, ui: Ui_MainWindow, store: MetricStore, poller: AgentMetricPoller
    ):
        super().__init__()
        self.performance_store = store
        self.performance_poller = poller

        self.ui = ui

        self.traffic_rx_gauge = SimpleNetdataGauge(
            title="TRAFFIC RX", unit="MB/s", color=C.NETWORK_RX
        )

        self.traffic_tx_gauge = SimpleNetdataGauge(
            title="TRAFFIC TX", unit="MB/s", color=C.NETWORK_TX
        )

        self.packets_rx_gauge = SimpleNetdataGauge(
            title="PACKETS RX", unit="pkt/s", color=C.PACKETS_RX
        )

        self.packets_tx_gauge = SimpleNetdataGauge(
            title="PACKETS TX", unit="pkt/s", color=C.PACKETS_TX
        )

        self.packets_tx_gauge = SimpleNetdataGauge(
            "PACKETS TX",
            unit="MB/s",
            color="#228ebc",
        )

        self.ui.network_gauge_layout.addWidget(self.traffic_rx_gauge)
        self.ui.network_gauge_layout.addWidget(self.traffic_tx_gauge)

        self.ui.network_gauge_layout.addWidget(self.packets_rx_gauge)
        self.ui.network_gauge_layout.addWidget(self.packets_tx_gauge)

        self.network_traffic_graph = MetricGraphHelper(
            self.ui.network_graph,
            antialias=True,
            y_label="Speed",
            y_range=(0, 10000000),
        )

        self.is_init_networks_groups_selector = False

        self.current_network_group = None

        self.current_unit = None

        self.delta_time = None

        self.default_graph_data_type = "traffic"
        self.current_graph_data_type = None

        self.traffic_rx_speed = 0
        self.traffic_tx_speed = 0

        self.packets_rx_speed = 0
        self.packets_tx_speed = 0

        self.last_network_metric = {}

        self.network_counters = {}

        self._setup_style()
        self._setup_static_series()
        self._connect_signals()
        self._init_data_unit_selector()

        self.performance_store.metrics_loaded.connect(self.on_history_received)
        self.performance_store.metrics_appended.connect(self.on_latest_received)

    def _connect_signals(self):
        self.network_graph_nav_group = QButtonGroup(self)
        self.network_graph_nav_group.setExclusive(True)

        buttons = {
            self.ui.network_traffic_toggle_button: "traffic",
            self.ui.network_packets_toggle_button: "packets",
        }

        for button, mode in buttons.items():
            self.network_graph_nav_group.addButton(button)
            button.clicked.connect(
                lambda checked=False, mode=mode: self.on_toggle_button_clicked(mode)
            )

    def _setup_style(self):
        apply_style_for_tables(self.ui.network_interfaces_table)

    def on_history_received(self, metrics: dict):
        current_page_widget = self.ui.performance_stacked_content.currentWidget()

        if not current_page_widget == self.ui.performance_network_page:
            return

        incoming_timestamps = metrics.get("timestamps", [])

        if not incoming_timestamps:
            if not self.is_init_networks_groups_selector:
                self._init_network_group_selector(metrics.get("network_names", {}))

            return

        network_data = metrics.get("network_metrics", {})
        if network_data:
            for network_name, network_info in network_data.items():
                self.network_counters[network_name] = {
                    "timestamps": incoming_timestamps,
                    **network_info,
                }

            self._change_network_data_on_graph(self.current_network_group)

    def on_latest_received(self, metric: dict) -> None:
        timestamp = metric.get("timestamp")
        current_network = metric.get("network_metrics", {})

        self.current_network = current_network

        if not timestamp:
            return

        if not self.last_network_metric:
            self.last_network_metric = current_network
            self.last_timestamp = timestamp

            return

        self.delta_time = timestamp - self.last_timestamp
        if self.delta_time > 0:
            for network_name in self.network_counters.keys():
                if network_name not in current_network:
                    return

                traffic_recv = current_network[network_name].get("traffic_recv", 0)
                traffic_sent = current_network[network_name].get("traffic_sent", 0)

                packets_recv = current_network[network_name].get("packets_recv", 0)
                packets_sent = current_network[network_name].get("packets_sent", 0)

                self.network_counters[network_name]["timestamps"].append(timestamp)

                if self.current_network_group:
                    if network_name == self.current_network_group:
                        self._prepare_dynamic_data()
                        if (
                            self.current_unit
                            and network_name == self.current_network_group
                        ):
                            if self.current_graph_data_type == "traffic":
                                self.network_traffic_graph.append_point(
                                    timestamp,
                                    {
                                        "TX": self.traffic_tx_speed,
                                        "RX": self.traffic_rx_speed,
                                    },
                                )

                            if self.current_graph_data_type == "packets":
                                self.network_traffic_graph.append_point(
                                    timestamp,
                                    {
                                        "TX": self.packets_tx_speed,
                                        "RX": self.packets_rx_speed,
                                    },
                                )

                if self.network_counters[network_name].get("traffic", None):
                    self.network_counters[network_name]["traffic"][
                        "traffic_recv"
                    ].append(traffic_recv)
                    self.network_counters[network_name]["traffic"][
                        "traffic_sent"
                    ].append(traffic_sent)

                if self.network_counters[network_name].get("packets", None):
                    self.network_counters[network_name]["packets"][
                        "packets_recv"
                    ].append(packets_recv)
                    self.network_counters[network_name]["packets"][
                        "packets_sent"
                    ].append(packets_sent)

        self.last_network_metric = current_network
        self.last_timestamp = timestamp

        self._update_network_interfaces_table(current_network)

    def on_toggle_button_clicked(self, graph_mode: str):
        self.current_graph_data_type = graph_mode

        if self.current_network_group:
            self._change_network_data_on_graph(self.current_network_group)

    def _update_network_interfaces_table(
        self, network_data: dict[str, dict[str, int]] | None
    ) -> None:
        if not network_data:
            return

        table = self.ui.network_interfaces_table

        for interface_name, interface_data in network_data.items():
            row = -1

            for r in range(table.rowCount()):
                item_group = table.item(r, 0)
                item_label = table.item(r, 1)

                if item_group and item_label:
                    if item_group.text() == interface_name:
                        row = r
                        break

            if row == -1:
                row = table.rowCount()
                table.insertRow(row)

            update_or_create_row_item(table, row, 0, interface_name)
            update_or_create_row_item(
                table,
                row,
                1,
                byte_converter(interface_data["traffic_recv"], "mb", rate=True),
            )
            update_or_create_row_item(
                table,
                row,
                2,
                byte_converter(interface_data["traffic_sent"], "mb", rate=True),
            )
            update_or_create_row_item(
                table,
                row,
                3,
                byte_converter(interface_data["packets_recv"], "mb", rate=True),
            )
            update_or_create_row_item(
                table,
                row,
                4,
                byte_converter(interface_data["packets_sent"], "mb", rate=True),
            )

            update_or_create_row_item(
                table,
                row,
                5,
                f'{interface_data["errin"]} / {interface_data["errout"]}',
            )

            update_or_create_row_item(
                table,
                row,
                6,
                f'{interface_data["dropin"]} / {interface_data["dropout"]}',
            )

    def _change_network_data_on_graph(
        self, current_network_group: str | None = None
    ) -> None:
        if not current_network_group:
            return

        self.current_network_group = current_network_group

        self.current_unit = self.ui.network_traffic_unit_combo_box.currentText()
        self.formatted_current_unit = self.current_unit.split("/")[0].lower()

        if not self.current_graph_data_type:
            self.current_graph_data_type = self.default_graph_data_type

        if (
            current_network_group not in self.network_counters
            or not self.current_graph_data_type
            in self.network_counters[current_network_group]
        ):
            fields_map = {
                "traffic": "traffic_recv,traffic_sent",
                "packets": "packets_sent,packets_recv",
            }

            self.performance_poller.on_clicked(
                metric_type="network",
                query_params={
                    "interface": current_network_group,
                    "fields": fields_map[self.current_graph_data_type],
                },
            )

            return

        if self.current_network_group:
            self._prepare_dynamic_data()

        network_cache = self.network_counters[current_network_group]
        timestamps = network_cache["timestamps"]

        self.network_traffic_graph.series_suffixes["RX"] = self.current_unit
        self.network_traffic_graph.series_suffixes["TX"] = self.current_unit

        rx_speed = calculate_bytes_per_second(
            network_cache[self.current_graph_data_type][
                f"{self.current_graph_data_type}_recv"
            ],
            timestamps,
            self.formatted_current_unit,
        )
        tx_speed = calculate_bytes_per_second(
            network_cache[self.current_graph_data_type][
                f"{self.current_graph_data_type}_sent"
            ],
            timestamps,
            self.formatted_current_unit,
        )

        self.network_traffic_graph.update_data(
            timestamps[1:],
            {
                "RX": rx_speed,
                "TX": tx_speed,
            },
        )

    def _init_network_group_selector(self, networks: dict[str, list[str]]):
        if networks:
            self.ui.network_traffic_graph_combo_box.addItems(networks)

            self.ui.network_traffic_graph_combo_box.currentTextChanged.connect(
                self._change_network_data_on_graph
            )
            self.is_init_networks_groups_selector = True

            self.ui.network_traffic_unit_combo_box.setEnabled(True)

        else:
            MessageBox().show_message(
                message_type="warning",
                title="Networks interfaces not found",
                text=(
                    "Error to get a hardwares list.\n\n"
                    "Possible causes:\n"
                    "1. The backend API is not running, or an incorrect API URL s specified in the settings.\n"
                    "2. The NexoraControl agent does not have permission to save system thermal metrics.\n\n"
                    "3. The NexoraControl agent not running.\n"
                    "Check the thermal driver on the agent side."
                ),
            )

    def _init_data_unit_selector(self) -> None:
        unit_keys = [unit.upper() + "/s" for unit in UNIT_MAP.keys()]
        self.ui.network_traffic_unit_combo_box.addItems(unit_keys)

        default_index = self.ui.network_traffic_unit_combo_box.findText("MB/s")

        self.ui.network_traffic_unit_combo_box.setCurrentIndex(default_index)

        self.ui.network_traffic_unit_combo_box.currentTextChanged.connect(
            lambda: (
                self._change_network_data_on_graph(self.current_network_group)
                if self.current_network_group
                else None
            )
        )

    def _prepare_dynamic_data(self) -> None:
        if not self.delta_time or not self.current_network_group:
            return

        delta_time = self.delta_time

        current_network_interface = self.current_network[self.current_network_group]
        last_network_interface = self.last_network_metric[self.current_network_group]

        traffic_rx_bps = calculate_metric_rate(
            current_network_interface,
            last_network_interface,
            f"traffic_recv",
            delta_time,
        )
        traffic_tx_bps = calculate_metric_rate(
            current_network_interface,
            last_network_interface,
            f"traffic_sent",
            delta_time,
        )

        packets_rx_bps = calculate_metric_rate(
            current_network_interface,
            last_network_interface,
            f"packets_recv",
            delta_time,
        )
        packets_tx_bps = calculate_metric_rate(
            current_network_interface,
            last_network_interface,
            f"packets_sent",
            delta_time,
        )

        self.traffic_rx_speed = byte_converter(
            traffic_rx_bps, unit=self.formatted_current_unit, precision=3, as_float=True
        )
        self.traffic_tx_speed = byte_converter(
            traffic_tx_bps, unit=self.formatted_current_unit, precision=3, as_float=True
        )

        self.packets_rx_speed = byte_converter(
            packets_rx_bps, unit=self.formatted_current_unit, precision=3, as_float=True
        )
        self.packets_tx_speed = byte_converter(
            packets_tx_bps, unit=self.formatted_current_unit, precision=3, as_float=True
        )

        set_gauge(self.traffic_rx_gauge, self.traffic_rx_speed, self.current_unit)
        set_gauge(self.traffic_tx_gauge, self.traffic_tx_speed, self.current_unit)

        set_gauge(self.packets_tx_gauge, self.packets_tx_speed, self.current_unit)
        set_gauge(self.packets_tx_gauge, self.packets_rx_speed, self.current_unit)

        heath_data = {
            "traffic_recv": self.current_network[self.current_network_group][
                "traffic_recv"
            ],
            "traffic_sent": self.current_network[self.current_network_group][
                "traffic_sent"
            ],
            "packets_recv": self.current_network[self.current_network_group][
                "packets_recv"
            ],
            "packets_sent": self.current_network[self.current_network_group][
                "packets_sent"
            ],
            "errin": self.current_network[self.current_network_group]["errin"],
            "errout": self.current_network[self.current_network_group]["errout"],
            "dropin": self.current_network[self.current_network_group]["dropin"],
            "dropout": self.current_network[self.current_network_group]["dropout"],
        }

        self._set_network_io(heath_data)

    def _set_network_io(self, data: dict) -> None:
        traffic_recv = byte_converter(
            data["traffic_recv"], self.formatted_current_unit, rate=True
        )
        traffic_sent = byte_converter(
            data["traffic_sent"], self.formatted_current_unit, rate=True
        )

        packets_recv = byte_converter(
            data["packets_recv"], self.formatted_current_unit, rate=True
        )
        packets_sent = byte_converter(
            data["packets_sent"], self.formatted_current_unit, rate=True
        )

        self.ui.network_health_total_content_bottom_rx_data_value_label.setText(
            traffic_recv
        )
        self.ui.network_health_total_content_bottom_tx_data_value_label.setText(
            traffic_sent
        )

        self.ui.network_health_total_content_top_rx_packets_value_label.setText(
            packets_recv
        )
        self.ui.network_health_total_content_top_tx_packets_value_label.setText(
            packets_sent
        )

        self.ui.network_health_drops_content_top_rx_drops_value_label.setText(
            str(data["dropin"])
        )
        self.ui.network_health_drops_content_bottom_tx_drops_value_label.setText(
            str(data["dropout"])
        )
        self.ui.network_health_errors_content_top_rx_errors_value_label.setText(
            str(data["errin"])
        )
        self.ui.network_health_errors_content_bottom_tx_errors_value_label.setText(
            str(data["errout"])
        )

    def _setup_static_series(self) -> None:
        self.network_traffic_graph.add_series("RX", C.NETWORK_RX, width=1.8)
        self.network_traffic_graph.add_series("TX", C.NETWORK_TX, width=1.8)
