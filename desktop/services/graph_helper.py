from datetime import datetime
from re import S
from typing import Any
import numpy as np
import pyqtgraph as pg
from PySide6.QtCore import Qt


class TimeAxisItem(pg.AxisItem):

    def tickStrings(self, values, scale, spacing):
        formatted = []
        for v in values:
            try:
                formatted.append(datetime.fromtimestamp(v).strftime("%H:%M:%S"))
            except (ValueError, OverflowError, OSError):
                formatted.append("")
        return formatted


class MetricGraphHelper:
    def __init__(
        self,
        graph: pg.PlotWidget,
        y_label: str = "Usage (%)",
        antialias: bool = False,
        y_range: tuple[float, float] | None = (0, 100),
    ):
        self.TOOLTIP_COLS_COUNT = 3

        self.graph = graph

        self.antialias = antialias

        self.curves: dict[str, pg.PlotDataItem] = {}

        self.series_colors: dict[str, str] = {}
        self.series_suffixes: dict[str, str] = {}
        self.series_data: dict[str, list[float]] = {}

        self.timestamps: list[int] = []

        self.y_range = y_range

        self._setup_style(y_label)
        self._setup_crosshair()

        self.graph.disableAutoRange()

        self.graph.plotItem.getAxis("left").enableAutoSIPrefix(False)
        self.graph.enableAutoRange(axis='y', enable=True)


    def update_data(
        self,
        timestamps: list[int] = None,
        data_dict: dict[str, list[float | int]] = None,
    ) -> dict:
        self.timestamps = timestamps or []
        self.series_data = data_dict or {}

        if not self.timestamps:
            self.graph.setXRange(0, 60, padding=0)
            self.graph.getViewBox().setLimits(xMin=None, xMax=None)
            self.tooltip.setHtml("")
            return

        for name, values in self.series_data.items():
            if not values:
                continue

            if name in self.curves:
                self.curves[name].setData(self.timestamps, values)

        x_min = (
            self.timestamps[0] - 30
            if len(self.timestamps) == 1
            else min(self.timestamps)
        )
        x_max = (
            self.timestamps[0] + 30
            if len(self.timestamps) == 1
            else max(self.timestamps)
        )

        if len(timestamps) < 300:
            pg.setConfigOptions(antialias=self.antialias)

        else:
            pg.setConfigOptions(antialias=False)

        self.graph.setXRange(x_min, x_max, padding=0)
        self.graph.getViewBox().setLimits(xMin=x_min, xMax=x_max)

    def append_point(self, timestamp: int, values_dict: dict[str, float | int]) -> None:
        self.timestamps.append(timestamp)

        for name in self.series_data:
            val = values_dict.get(name, 0.0)
            self.series_data[name].append(val)

        target_len = len(self.timestamps)

        for name, data in self.series_data.items():
            diff = target_len - len(data)
            if diff > 0:
                data.extend([0.0] * diff)
            elif diff < 0:
                self.series_data[name] = data[:target_len]

        for name, curve in self.curves.items():
            if name in self.series_data:
                curve.setData(self.timestamps, self.series_data[name])

    def add_series(
        self, name: str, color: str, width: float = 2.0, suffix: str = "%"
    ) -> str:
        pen = pg.mkPen(color=color, width=width)

        pen.setJoinStyle(Qt.PenJoinStyle.RoundJoin)
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)

        curve = self.graph.plot(name=name, pen=pen)

        self.curves[name] = curve
        self.series_colors[name] = color
        self.series_suffixes[name] = suffix
        self.series_data[name] = []

        return name

    def _setup_style(self, y_label: str):
        self.graph.setBackground(None)

        axis_pen = pg.mkPen(color="#475569", width=1)
        text_pen = pg.mkPen(color="#adb3bb", width=1)

        plot_item = self.graph.plotItem

        time_axis = TimeAxisItem(orientation="bottom")
        time_axis.enableAutoSIPrefix(False)

        plot_item.setAxisItems({"bottom": time_axis})
        plot_item.layout.setContentsMargins(5, 0, 0, 5)

        for axis_name in ["left", "bottom"]:
            axis = plot_item.getAxis(axis_name)
            axis.setPen(axis_pen)
            axis.setTextPen(text_pen)

        self.graph.showGrid(x=True, y=True, alpha=0.3)
        self.graph.setLabel("bottom", "Time")
        self.graph.setLabel("left", y_label)

        plot_item.showAxis("top", False)
        plot_item.showAxis("right", False)

        if self.y_range:
            self.graph.getViewBox().setLimits(
                yMin=self.y_range[0], yMax=self.y_range[1]
            )

    def _setup_crosshair(self):
        self.v_line = pg.InfiniteLine(
            angle=90,
            movable=False,
            pen=pg.mkPen("#4b5157", width=1, style=Qt.PenStyle.DashLine),
        )
        self.h_line = pg.InfiniteLine(
            angle=0,
            movable=False,
            pen=pg.mkPen("#4b5157", width=1, style=Qt.PenStyle.DashLine),
        )
        self.tooltip = pg.TextItem(anchor=(0, 0), color="#c9d1d9")

        self.graph.addItem(self.v_line, ignoreBounds=True)
        self.graph.addItem(self.h_line, ignoreBounds=True)
        self.graph.addItem(self.tooltip, ignoreBounds=True)

        self.graph.scene().sigMouseMoved.connect(self._on_mouse_moved)

    def _on_mouse_moved(self, pos):
        if not self.timestamps:
            return

        view_box = self.graph.getViewBox()
        if not self.graph.sceneBoundingRect().contains(pos):
            return

        mouse_point = view_box.mapSceneToView(pos)
        x_val = mouse_point.x()

        idx = int(np.searchsorted(self.timestamps, x_val))
        idx = min(max(idx, 0), len(self.timestamps) - 1)

        if idx > 0 and abs(self.timestamps[idx] - x_val) > abs(
            self.timestamps[idx - 1] - x_val
        ):
            idx -= 1

        actual_x = self.timestamps[idx]
        self.v_line.setPos(actual_x)

        time_str = datetime.fromtimestamp(actual_x).strftime("%H:%M:%S")

        lines = [
            f"<td colspan='{self.TOOLTIP_COLS_COUNT}' style='padding: 2px 8px; font-weight: bold;'>"
            f"<span style='color: #8b949e;'>Time:</span> {time_str}"
            f"</td>"
        ]

        first_val = None
        for name, values in self.series_data.items():
            if values and idx < len(values):
                val = values[idx]
                color = self.series_colors.get(name, "#ffffff")
                suffix = self.series_suffixes.get(name, "")

                cell_html = (
                    f"<td style='padding: 2px 8px; min-width: 90px;'>"
                    f"<span style='color: {color}; font-weight: bold;'>{name}:</span> "
                    f"<span style='color: #ffffff;'>{val}{suffix}</span>"
                    f"</td>"
                )
                lines.append(cell_html)

                if first_val is None:
                    first_val = val

        if first_val is not None:
            self.h_line.setPos(first_val)

        table_rows = []
        table_rows.append(f"<tr>{lines[0]}</tr>")

        for i in range(1, len(lines), self.TOOLTIP_COLS_COUNT):
            row_cells = lines[i : i + self.TOOLTIP_COLS_COUNT]
            table_rows.append(f"<tr>{''.join(row_cells)}</tr>")

        html_code = (
            f"<div style='"
            f"font-family: sans-serif; "
            f"font-size: 9pt; "
            f"background-color: #161b22; "
            f"color: #c9d1d9; "
            f"padding: 6px 10px; "
            f"border-radius: 6px; "
            f"border: 1px solid #30363d;"
            f"'>"
            f"<table border='0' cellpadding='0' cellspacing='0'>"
            f"{''.join(table_rows)}"
            f"</table>"
            f"</div>"
        )

        self.tooltip.setHtml(html_code)

        x_range, y_range = view_box.viewRange()
        self.tooltip.setPos(x_range[0], y_range[1])
