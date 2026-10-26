from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QAbstractSpinBox,
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QSizePolicy,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class CommandFieldBuilder:

    def __init__(self, layout) -> None:
        self.WIDGET_MAP = {
            "string": QLineEdit,
            "integer": QSpinBox,
            "float": QDoubleSpinBox,
            "boolean": QCheckBox,
            "choice": QComboBox,
        }

        self.layout = layout

        self.widgets = {}

    def build(self, fields: dict[str, dict]) -> None:
        self.clear()

        if not fields:
            return

        for name, config in fields.items():
            row = QFrame()
            row.setObjectName("command_field_row")

            row, widget = self._create_field_row(name, config)

            self.layout.addWidget(row)
            self.widgets[name] = widget

            self.layout.addWidget(row)

    def _create_field_row(self, name, config):
        row = QFrame()
        row.setProperty("fieldRole", "row")

        row_layout = QVBoxLayout(row)
        row_layout.setContentsMargins(0, 0, 0, 0)
        row_layout.setSpacing(7)

        field_type = config["type"]
        widget_class = self.WIDGET_MAP[field_type]
        widget = widget_class()

        self._setup_widget(widget, config)

        title = config.get("label", name.replace("_", " "))

        if isinstance(widget, QCheckBox):
            widget.setText(title)
            row_layout.addWidget(widget)
        else:
            required = "  *" if config.get("required") else ""

            label = QLabel(f"{title.upper()}{required}")
            label.setProperty("fieldRole", "label")

            row_layout.addWidget(label)
            row_layout.addWidget(widget)

        status = "Required" if config.get("required") else "Optional"

        hint = QLabel(
            f"{status} · {field_type.capitalize()} · "
            f"{config.get('description', '')}"
        )
        hint.setProperty("fieldRole", "hint")
        hint.setWordWrap(True)

        row_layout.addWidget(hint)

        return row, widget

    def _setup_widget(self, widget: QWidget, config: dict[str, str | int]):
        if isinstance(widget, QLineEdit):
            widget.setPlaceholderText(config["placeholder"])

        if isinstance(widget, QSpinBox):
            widget.setRange(
                config.get("min", 0),
                config.get("max", 1_000_000),
            )
            widget.setValue(config.get("default", 0))

            widget.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

    def clear(self):
        self.widgets = {}
        while self.layout.count():
            item = self.layout.takeAt(0)

            if item is not None:
                widget = item.widget()

                if widget is not None:
                    widget.deleteLater()
