from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QPainter, QPen, QColor, QFont
from PySide6.QtWidgets import QWidget


class SimpleNetdataGauge(QWidget):
    def __init__(self, title="", unit="%", color="#a5b4fc", max_value: float = 100.0, parent=None):
        super().__init__(parent)
        self.title = title
        self.unit = unit
        self.color = QColor(color)
        self.bg_color = QColor("#2A2C32")
        self.text_muted = QColor("#8A8F9D")
        self.text_white = QColor("#a5b4fc")

        self.value = 0.0
        self.max_value = max_value

        self.setMinimumSize(150, 150)

        self.font_title = QFont("JetBrainsMonoNL Nerd Font Propo", 9)
        self.font_val = QFont("JetBrainsMonoNL Nerd Font Propo", 11, QFont.Weight.Bold)
        self.font_unit = QFont("JetBrainsMonoNL Nerd Font Propo", 8)


    def set_value(self, val: float = 0.0):
        new_val = max(0.0, min(float(val), self.max_value))
        if self.value == new_val:
            return
        
        self.value = new_val
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        w, h = self.width(), self.height()
        center_y = h / 2
        stroke_width = 10
        margin = stroke_width + 25

        size = min(w, h) - margin
        rect = QRectF((w - size) / 2, (h - size) / 2 + 5, size, size)

        painter.setPen(self.text_muted)
        painter.setFont(self.font_title)
        painter.drawText(0, -1, w, 30, Qt.AlignmentFlag.AlignHCenter, self.title)

        bg_pen = QPen(
            self.bg_color,
            stroke_width,
            Qt.PenStyle.SolidLine,
            Qt.PenCapStyle.RoundCap,
        )
        painter.setPen(bg_pen)
        painter.drawArc(rect, 225 * 16, -270 * 16)

        progress = self.value / self.max_value if self.max_value > 0 else 0.0
        span_angle = int(progress * -270 * 16)

        val_pen = QPen(
            self.color,
            stroke_width,
            Qt.PenStyle.SolidLine,
            Qt.PenCapStyle.RoundCap,
        )
        painter.setPen(val_pen)
        painter.drawArc(rect, 225 * 16, span_angle)

        painter.setPen(self.text_white)
        painter.setFont(self.font_val)
        val_str = f"{self.value:.2f}".replace(".", ",")
        painter.drawText(
            QRectF(0, center_y - 15, w, 25), Qt.AlignmentFlag.AlignCenter, val_str
        )

        painter.setPen(self.text_muted)
        painter.setFont(self.font_unit)
        painter.drawText(
            QRectF(0, center_y + 12, w, 20), Qt.AlignmentFlag.AlignCenter, self.unit
        )

