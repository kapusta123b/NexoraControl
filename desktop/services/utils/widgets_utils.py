from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QProgressBar, QHeaderView

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


def apply_style_for_tables(
    tables: tuple[QTableWidget] | QTableWidget, edit_triggers: bool = True
):
    """
    Apply a consistent UI style to a single QTableWidget or a tuple of QTableWidgets.

    Args:
        tables (tuple[QTableWidget, ...] | QTableWidget): A single table or a tuple of tables.

    Raises:
        TypeError: If the 'tables' argument is neither a tuple nor a QTableWidget instance.
        TypeError: If any item inside the tuple is not a QTableWidget instance.
    """

    if not isinstance(tables, tuple):
        if isinstance(tables, QTableWidget):
            # convert a single QTableWidget into a tuple
            tables = (tables,)
        else:
            raise TypeError(
                f"argument 'tables' must be tuple of QTableWidgets or be singular QTableWidget, got {tables}"
            )

    for table in tables:
        if not isinstance(table, QTableWidget):
            raise TypeError(f"table class must be a QTableWidget, got {table}")

        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        table.verticalHeader().setVisible(False)
        table.horizontalHeader().setHighlightSections(False)

        if edit_triggers:
            table.setEditTriggers(table.EditTrigger.AllEditTriggers)


def setup_table(table: QTableWidget, table_data: dict | list, info_keys: tuple):
    if not table_data or not isinstance(table, QTableWidget):
        return

    table.blockSignals(True)
    table.setRowCount(0)

    if isinstance(table_data, dict):
        table_data = [table_data]

    for data in table_data:
        row = table.rowCount()
        table.insertRow(row)

        for col, info_key in enumerate(info_keys):
            val = data.get(info_key, "")

            update_or_create_row_item(table, row, col, str(val))

    table.blockSignals(False)
