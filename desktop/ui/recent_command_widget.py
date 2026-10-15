# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recent_commands.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_recent_command_widget(object):
    def setupUi(self, recent_command_widget):
        if not recent_command_widget.objectName():
            recent_command_widget.setObjectName(u"recent_command_widget")
        recent_command_widget.resize(520, 34)
        recent_command_widget.setMinimumSize(QSize(200, 30))
        recent_command_widget.setMaximumSize(QSize(16777215, 36))
        recent_command_widget.setStyleSheet(u"QWidget#recent_command_widget {background:#151D27;border-bottom:1px solid #2D3A47;\n"
"    font-family:\"Noto Sans\",\"Segoe UI\",sans-serif;font-size:11px;}\n"
"QLabel {background:transparent;border:none;color:#BECBD5;font-size:11px;}\n"
"QLabel#command_mark {font-size:12px;color:#90BCAD;}\n"
"QLabel#command_mark[status=\"success\"] {color:#90BCAD;}\n"
"QLabel#command_mark[status=\"failed\"] {color:#D19B9E;}\n"
"QLabel#command_mark[status=\"pending\"] {color:#D2B98F;}\n"
"QLabel#command_name {color:#DAE4EA;font-family:\"JetBrains Mono\",\"Consolas\",monospace;font-size:11px;}\n"
"QLabel#command_status {color:#90BCAD;font-family:\"JetBrains Mono\",\"Consolas\",monospace;font-size:10px;font-weight:600;}\n"
"QLabel#command_status[status=\"success\"] {color:#90BCAD;}\n"
"QLabel#command_status[status=\"failed\"] {color:#D19B9E;}\n"
"QLabel#command_status[status=\"pending\"] {color:#D2B98F;}\n"
"QLabel#command_executed_time {color:#738897;font-size:10px;}")
        self.recent_command_layout = QHBoxLayout(recent_command_widget)
        self.recent_command_layout.setSpacing(11)
        self.recent_command_layout.setObjectName(u"recent_command_layout")
        self.recent_command_layout.setContentsMargins(9, 3, 9, 3)
        self.command_mark = QLabel(recent_command_widget)
        self.command_mark.setObjectName(u"command_mark")
        self.command_mark.setMinimumSize(QSize(29, 29))
        self.command_mark.setMaximumSize(QSize(16, 16777215))
        self.command_mark.setAlignment(Qt.AlignCenter)

        self.recent_command_layout.addWidget(self.command_mark)

        self.command_name = QLabel(recent_command_widget)
        self.command_name.setObjectName(u"command_name")

        self.recent_command_layout.addWidget(self.command_name)

        self.command_status = QLabel(recent_command_widget)
        self.command_status.setObjectName(u"command_status")
        self.command_status.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.command_status.setMinimumSize(QSize(68, 0))

        self.recent_command_layout.addWidget(self.command_status)

        self.command_executed_time = QLabel(recent_command_widget)
        self.command_executed_time.setObjectName(u"command_executed_time")
        self.command_executed_time.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.command_executed_time.setMinimumSize(QSize(56, 0))

        self.recent_command_layout.addWidget(self.command_executed_time)


        self.retranslateUi(recent_command_widget)

        QMetaObject.connectSlotsByName(recent_command_widget)
    # setupUi

    def retranslateUi(self, recent_command_widget):
        recent_command_widget.setWindowTitle(QCoreApplication.translate("recent_command_widget", u"Recent Command", None))
        self.command_mark.setText(QCoreApplication.translate("recent_command_widget", u"\u2713", None))
        self.command_name.setText(QCoreApplication.translate("recent_command_widget", u"docker ps", None))
        self.command_status.setText(QCoreApplication.translate("recent_command_widget", u"SUCCESS", None))
        self.command_executed_time.setText(QCoreApplication.translate("recent_command_widget", u"2m ago", None))
    # retranslateUi

