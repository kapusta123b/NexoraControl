from datetime import datetime

import numpy as np

import pyqtgraph as pg

from PySide6.QtCore import Qt

from services.agent_poller import AgentPoller
from services.agent_store import MetricStore

from ui.main_window import Ui_MainWindow


class AgentDetailController:
    def __init__(self, ui: Ui_MainWindow, store: MetricStore, poller: AgentPoller):
        self.ui = ui
        self.store = store
        self.poller = poller

        self.agent_id = None
        self.from_hours = None

        self.x_data = []
        self.cpu_data = []
        self.ram_data = []

        self.store.metrics_changed.connect(self.update_metrics)
        
        self.ui.back_to_agents_button.clicked.connect(
            lambda: self.ui.content_stack.setCurrentWidget(self.ui.agents_page)
        )

        self._apply_graph_styles()
        self._create_curves()
        self._create_crosshair()

    def show_agent(self, agent: dict, hours_count: int):
        self.agent_id = agent["id"]
        self.from_hours = hours_count

        self.ui.detail_top_agent_name_label.setText(agent["name"])
        self.ui.detail_top_agent_status_label.setText("Loading metrics...")
        self.ui.cpu_load_label.setText("--")
        self.ui.ram_load_label.setText("--")
        self.ui.disk_load_label.setText("--")
        self.ui.up_time_label.setText("--")

        self._update_graph_data([], [], [])
        self.poller.set_agent(self.agent_id, hours_count)
        self.poller.refresh(force=True)

    def update_metrics(self, metrics):
        if not metrics:
            self.ui.detail_top_agent_status_label.setText("No metrics yet")
            self._update_graph_data([], [], [])
            return

        timestamps = metrics.get("timestamps", [])
        cpu_values = metrics.get("cpu_values", [])
        ram_values = metrics.get("ram_values", [])

        timestamps = [int(value) for value in timestamps]
        cpu_values = [value for value in cpu_values]
        ram_values = [value for value in ram_values]

        if not timestamps:
            self.ui.detail_top_agent_status_label.setText("No metrics yet")

        self._update_graph_data(
            timestamps,
            cpu_values,
            ram_values,
        )

    def _update_graph_data(self, timestamps, cpu_values, ram_values):
        self.x_data = timestamps
        self.cpu_data = cpu_values
        self.ram_data = ram_values

        self.cpu_curve.setData(timestamps, cpu_values)
        self.ram_curve.setData(timestamps, ram_values)

        self.tooltip_text.setHtml("")

        if not timestamps:
            self.ui.metric_graph.setXRange(0, 60, padding=0)
            self.ui.metric_graph.getViewBox().setLimits(xMin=None, xMax=None)
            return

        self.ui.detail_top_agent_status_label.setText("Metrics loaded")
        self.ui.cpu_load_label.setText(f"{cpu_values[-1]:.1f}%")
        self.ui.ram_load_label.setText(f"{ram_values[-1]:.1f}%")

        if len(timestamps) == 1:
            x_min = timestamps[0] - 30
            x_max = timestamps[0] + 30
        else:
            x_min = min(timestamps)
            x_max = max(timestamps)

        self.ui.metric_graph.setXRange(x_min, x_max, padding=0)
        self.ui.metric_graph.getViewBox().setLimits(xMin=x_min, xMax=x_max)

    def _format_timestamp_ticks(self, values: list[int], scale, spacing):
        formatted = []

        for v in values:
            try:
                formatted.append(datetime.fromtimestamp(v).strftime("%H:%M:%S"))
            except (ValueError, OverflowError):
                formatted.append("")
        return formatted

    def _apply_graph_styles(self):
        graph = self.ui.metric_graph
        graph.setBackground(None)

        graph.showGrid(x=True, y=True, alpha=0.1)

        axis_font = {
            "color": "#c4c8cc",
            "size": "9pt",
        }
        graph.setLabel("left", "Usage (%)", **axis_font)
        graph.setLabel("bottom", "Time", **axis_font)

        graph.getAxis("left").setPen("#21262d", width=1)
        graph.getAxis("bottom").setPen("#21262d", width=1)

        graph.setYRange(0, 100, padding=0)
        graph.getViewBox().setLimits(yMin=0, yMax=100)

        legend = graph.addLegend(offset=(50, 10), frame=False)
        legend.setLabelTextColor("#c9d1d9")
        legend.setLabelTextSize("9pt")

        graph.getAxis("bottom").tickStrings = self._format_timestamp_ticks

    def _create_curves(self):
        self.cpu_curve = self.ui.metric_graph.plot(
            name="CPU Usage",
            pen=pg.mkPen(color="#426a97", width=1.5),
        )

        self.ram_curve = self.ui.metric_graph.plot(
            name="RAM Usage",
            pen=pg.mkPen(color="#2F923B", width=1.5),
        )

    def _create_crosshair(self):
        graph = self.ui.metric_graph

        self.v_line = pg.InfiniteLine(
            angle=90,
            movable=False,
            pen=pg.mkPen("#30363d", width=1, style=Qt.PenStyle.DashLine),
        )

        self.h_line = pg.InfiniteLine(
            angle=0,
            movable=False,
            pen=pg.mkPen("#30363d", width=1, style=Qt.PenStyle.DashLine),
        )

        graph.addItem(self.v_line, ignoreBounds=True)
        graph.addItem(self.h_line, ignoreBounds=True)

        self.tooltip_text = pg.TextItem(anchor=(0, 0), color="#c9d1d9")

        graph.addItem(self.tooltip_text, ignoreBounds=True)

        graph.scene().sigMouseMoved.connect(self._mouse_moved)

    def _mouse_moved(self, evt):
        graph = self.ui.metric_graph
        view_box = graph.getViewBox()

        if not self.x_data:
            return

        if graph.sceneBoundingRect().contains(evt):
            mouse_point = view_box.mapSceneToView(evt)
            x_val = mouse_point.x()

            idx = int(np.searchsorted(self.x_data, x_val))
            idx = min(max(idx, 0), len(self.x_data) - 1)

            if idx > 0:
                if abs(self.x_data[idx] - x_val) > abs(self.x_data[idx - 1] - x_val):
                    idx -= 1

            actual_x = self.x_data[idx]
            cpu_val = self.cpu_data[idx]
            ram_val = self.ram_data[idx]

            self.v_line.setPos(actual_x)
            self.h_line.setPos(cpu_val)

            time_str = datetime.fromtimestamp(actual_x).strftime("%H:%M:%S")

            html_code = (
                f"<div style='font-size: 10pt; "
                f"background-color: rgba(22, 27, 34, 0.85); padding: 6px 10px; "
                f"border-radius: 4px; border: 1px solid #30363d;'>"
                f"<span style='color: #8b949e;'>Time:</span> {time_str}<br>"
                f"<span style='color: #426a97;'>CPU:</span> {cpu_val:.1f}%<br>"
                f"<span style='color: #2F923B;'>RAM:</span> {ram_val:.1f}%"
                f"</div>"
            )
            self.tooltip_text.setHtml(html_code)

            x_range, y_range = view_box.viewRange()
            x_min, x_max = x_range
            y_min, y_max = y_range

            view_width = x_max - x_min

            tooltip_x = x_max - (view_width * 0.20)

            self.tooltip_text.setPos(tooltip_x, y_max)
