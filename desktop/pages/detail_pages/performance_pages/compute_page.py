import colorsys

from services.utils import byte_converter

from ui.main_window import Ui_MainWindow

from services.widgets.gauge import SimpleNetdataGauge
from services.graph_helper import MetricGraphHelper
from services.stores.metric_store import MetricStore


class PerformanceComputePage:
    def __init__(self, ui: Ui_MainWindow, store: MetricStore):
        self.performance_store = store
        self.ui = ui

        self.cpu_gauge = SimpleNetdataGauge(title="CPU", unit="%", color="#38bdf8")
        self.ram_gauge = SimpleNetdataGauge(title="RAM", unit="%", color="#c084fc")
        self.disk_gauge = SimpleNetdataGauge(
            title="AVG DISK", unit="%", color="#34d399"
        )

        self.ui.compute_gauge_layout.addWidget(self.cpu_gauge)
        self.ui.compute_gauge_layout.addWidget(self.ram_gauge)
        self.ui.compute_gauge_layout.addWidget(self.disk_gauge)

        self.cpu_ram_graph = MetricGraphHelper(
            self.ui.cpu_ram_metric_graph,
            y_label="Usage (%)",
            antialias=True,
            y_range=(0, 100),
        )
        self.load_average_graph = MetricGraphHelper(
            self.ui.load_average_metric_graph,
            y_label="Load Avg",
            antialias=True,
            y_range=(0, 100),
        )
        self.cpu_cores_metric_graph = MetricGraphHelper(
            self.ui.cpu_cores_metric_graph,
            y_label="Usage (%)",
            antialias=True,
            y_range=(0, 100),
        )

        self.cores_initialized = False

        self.compute_metrics = {}

        self._setup_static_series()

        self.performance_store.metrics_loaded.connect(self.on_history_received)
        self.performance_store.metrics_appended.connect(self.on_latest_received)

    def on_history_received(self, metrics: dict):
        timestamps = metrics.get("timestamps", [])
        if not timestamps:
            return

        cpu_values = metrics.get("cpu_values", [])
        ram_values = metrics.get("ram_values", [])
        load_average_values = metrics.get("load_average", [])
        cpu_load_per_core_timestamps = metrics.get("cpu_load_per_core_timestamps", [])
        cpu_load_per_core_values = metrics.get("cpu_load_per_core", [])

        if cpu_values and ram_values:
            self._set_gauges(cpu_values[-1], ram_values[-1])

        self.cpu_ram_graph.update_data(
            timestamps, {"CPU": cpu_values, "RAM": ram_values}
        )

        if load_average_values:
            m1, m5, m15 = zip(*load_average_values)
            self.load_average_graph.update_data(
                timestamps, {"1m": list(m1), "5m": list(m5), "15m": list(m15)}
            )

        if cpu_load_per_core_values:
            cores_transposed = list(zip(*cpu_load_per_core_values))
            if not self.cores_initialized:
                self._init_core_series(len(cores_transposed))

            core_dict = {
                f"Core {i}": list(vals) for i, vals in enumerate(cores_transposed)
            }
            self.cpu_cores_metric_graph.update_data(
                cpu_load_per_core_timestamps, core_dict
            )

    def on_latest_received(self, metric: dict):
        timestamp = metric.get("timestamp")
        if not timestamp:
            return

        cpu_value = metric["cpu_metrics"].get("cpu_load", 0.0)
        ram_value = metric["memory_metrics"].get("ram_load", 0.0)
        disk_value = metric["storage_metrics"].get("disk_value", 0.0)
        cpu_per_core_values = metric["cpu_metrics"].get("cpu_per_core", [])
        load_avg = metric["cpu_metrics"].get("load_average", [0.0, 0.0, 0.0])

        ram_used = metric["memory_metrics"].get("ram_used_bytes", 0)
        ram_available = metric["memory_metrics"].get("ram_available_bytes", 0)

        self.cpu_ram_graph.append_point(
            timestamp,
            {"CPU": cpu_value, "RAM": ram_value},
        )
        self.load_average_graph.append_point(
            timestamp,
            {
                "1m": load_avg[0] if len(load_avg) > 0 else 0.0,
                "5m": load_avg[1] if len(load_avg) > 1 else 0.0,
                "15m": load_avg[2] if len(load_avg) > 2 else 0.0,
            },
        )

        if cpu_per_core_values:
            core_dict = {f"Core {i}": val for i, val in enumerate(cpu_per_core_values)}
            self.cpu_cores_metric_graph.append_point(timestamp, core_dict)

        self._set_gauges(cpu_value, ram_value, disk_value)

        used_gb = byte_converter(ram_used, "gb")
        avail_gb = byte_converter(ram_available, "gb")

        self.ui.used_memory_value_label.setText(used_gb)
        self.ui.available_memory_value_label.setText(avail_gb)
        self.ui.memory_progress_bar.setValue(int(ram_value))

    def _init_core_series(self, num_cores: int):
        for i in range(num_cores):
            color = self._get_core_color(i, num_cores)
            self.cpu_cores_metric_graph.add_series(f"Core {i}", color, width=1.0)

        self.cores_initialized = True

    def _setup_static_series(self):
        self.cpu_ram_graph.add_series("CPU", "#38bdf8")
        self.cpu_ram_graph.add_series("RAM", "#c084fc")

        self.load_average_graph.add_series("1m", "#fb923c", width=1.5, suffix="")
        self.load_average_graph.add_series("5m", "#818cf8", width=1.5, suffix="")
        self.load_average_graph.add_series("15m", "#64748b", width=1.5, suffix="")

    def _get_core_color(self, index: int, total_cores: int) -> str:
        step = 0.30 / max(total_cores - 1, 1)
        hue = 0.50 + (index * step)
        val = 0.95 if index % 2 == 0 else 0.70

        r, g, b = colorsys.hsv_to_rgb(hue, 0.60, val)
        return f"#{int(r * 255):02x}{int(g * 255):02x}{int(b * 255):02x}A0"

    def _set_gauges(
        self,
        cpu_value: float = 0.0,
        ram_value: float = 0.0,
        disk_value: float = 0.0,
    ):
        self.cpu_gauge.set_value(cpu_value)
        self.ram_gauge.set_value(ram_value)
        self.disk_gauge.set_value(disk_value)
