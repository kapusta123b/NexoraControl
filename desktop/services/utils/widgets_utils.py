from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QProgressBar

from services.widgets.gauge import SimpleNetdataGauge


def update_or_create_row_item(
    table: QTableWidget, row: int, column: int, text: str
) -> None:
    if not isinstance(table, QTableWidget):
        raise TypeError(f"table class must be QTableWidget, got {table}")

    item = table.item(row, column)

    if item:
        if item.text() != text:
            item.setText(text)
    else:
        table.setItem(row, column, QTableWidgetItem(text))


def setup_table_progress_bar(
    table: QTableWidget, row: int = 0, column: int = 0, percent: int | float = 0
) -> None:
    if not isinstance(table, QTableWidget):
        raise TypeError(f"table class must be QTableWidget, got {table}")

    if percent < 60:
        load_level = "low"
    elif percent < 85:
        load_level = "medium"
    else:
        load_level = "high"

    progress_bar = table.cellWidget(row, column)

    progress_bar

    if not isinstance(progress_bar, QProgressBar):
        progress_bar = QProgressBar()
        progress_bar.setRange(0, 100)

        table.setRowHeight(row, 34)

        table.setCellWidget(row, column, progress_bar)

    if progress_bar.value() != percent:
        progress_bar.setValue(percent)
        progress_bar.setFormat(f"{percent}%")

        progress_bar.setProperty("load_level", load_level)

        progress_bar.style().unpolish(progress_bar)
        progress_bar.style().polish(progress_bar)


def set_gauge(
    gauge: SimpleNetdataGauge, value: int | float, unit: str | None = None
) -> None:

    if not isinstance(gauge, SimpleNetdataGauge):
        raise TypeError(f"gauge class must be SimpleNetdataGauge, got {gauge}")

    if not isinstance(value, (int, float)):
        raise TypeError(f"value must be int or float, got {type(value).__name__}")

    if unit:
        if not isinstance(unit, str):
            raise TypeError(f"unit must be str, got {type(unit).__name__}")

        gauge.unit = unit

    if value > gauge.max_value:
        gauge.max_value = round(value)

    gauge.set_value(value)


def apply_style_property(widget, prop_name: str, prop_value: str) -> None:
    widget.setProperty(prop_name, prop_value)
    widget.style().unpolish(widget)
    widget.style().polish(widget)
