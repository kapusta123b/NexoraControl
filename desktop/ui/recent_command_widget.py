# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recent_command_widget.ui'
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
        recent_command_widget.resize(400, 37)
        recent_command_widget.setMinimumSize(QSize(200, 0))
        self.recent_command_layout = QHBoxLayout(recent_command_widget)
        self.recent_command_layout.setSpacing(6)
        self.recent_command_layout.setObjectName(u"recent_command_layout")
        self.recent_command_layout.setContentsMargins(0, 0, 0, 0)
        self.command_mark = QLabel(recent_command_widget)
        self.command_mark.setObjectName(u"command_mark")
        self.command_mark.setMaximumSize(QSize(20, 16777215))
        self.command_mark.setStyleSheet(u"QLabel {\n"
"	font: 12pt\n"
"}\n"
"\n"
"QLabel[status=\"success\"] {\n"
"    color: #4caf50;\n"
"}\n"
"\n"
"QLabel[status=\"failed\"] {\n"
"    color: #f44336; \n"
"}\n"
"\n"
"QLabel[status=\"pending\"] {\n"
"    color: #ff9800;\n"
"}")
        self.command_mark.setAlignment(Qt.AlignCenter)

        self.recent_command_layout.addWidget(self.command_mark)

        self.command_name = QLabel(recent_command_widget)
        self.command_name.setObjectName(u"command_name")

        self.recent_command_layout.addWidget(self.command_name)

        self.command_status = QLabel(recent_command_widget)
        self.command_status.setObjectName(u"command_status")
        self.command_status.setStyleSheet(u"QLabel[status=\"success\"] {\n"
"    color: #4caf50;\n"
"}\n"
"\n"
"QLabel[status=\"failed\"] {\n"
"    color: #f44336;\n"
"}\n"
"\n"
"QLabel[status=\"pending\"] {\n"
"    color: #ff9800;\n"
"}")
        self.command_status.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.recent_command_layout.addWidget(self.command_status)

        self.command_executed_time = QLabel(recent_command_widget)
        self.command_executed_time.setObjectName(u"command_executed_time")
        self.command_executed_time.setAlignment(Qt.AlignCenter)

        self.recent_command_layout.addWidget(self.command_executed_time)


        self.retranslateUi(recent_command_widget)

        QMetaObject.connectSlotsByName(recent_command_widget)
    # setupUi

    def retranslateUi(self, recent_command_widget):
        recent_command_widget.setWindowTitle(QCoreApplication.translate("recent_command_widget", u"Form", None))
        self.command_mark.setText(QCoreApplication.translate("recent_command_widget", u"\u2713", None))
        self.command_name.setText(QCoreApplication.translate("recent_command_widget", u"docker ps", None))
        self.command_status.setText(QCoreApplication.translate("recent_command_widget", u"SUCCESS", None))
        self.command_executed_time.setText(QCoreApplication.translate("recent_command_widget", u" 2m ago", None))
    # retranslateUi

