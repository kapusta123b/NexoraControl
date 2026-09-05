# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'agent_card.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_card_form(object):
    def setupUi(self, card_form):
        if not card_form.objectName():
            card_form.setObjectName(u"card_form")
        card_form.resize(800, 137)
        card_form.setMinimumSize(QSize(800, 120))
        card_form.setMaximumSize(QSize(16777215, 137))
        card_form.setStyleSheet(u"#card_form {\n"
"    background-color: #161920;\n"
"    border-radius: 4px;\n"
"	margin-right: 10px\n"
"}\n"
"\n"
"QWidget {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #a5b4fc;\n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: #a5b4fc; \n"
"    background-color: transparent;\n"
"    border: 1px solid #242936;\n"
"    border-radius: 4px;\n"
"    padding: 6px 12px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1e2230;\n"
"    border-color: #38bdf8;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0f111a;\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(card_form)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 9, 0)
        self.agent_information_widget = QWidget(card_form)
        self.agent_information_widget.setObjectName(u"agent_information_widget")
        self.agent_information_widget.setMinimumSize(QSize(300, 0))
        self.agent_information_widget.setMaximumSize(QSize(400, 150))
        self.agent_information_widget.setStyleSheet(u"")
        self.horizontalLayout_10 = QHBoxLayout(self.agent_information_widget)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 9, 0, 0)
        self.online_dot = QLabel(self.agent_information_widget)
        self.online_dot.setObjectName(u"online_dot")
        self.online_dot.setMaximumSize(QSize(20, 100))
        self.online_dot.setStyleSheet(u"")
        self.online_dot.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_10.addWidget(self.online_dot)

        self.system_information_widget = QWidget(self.agent_information_widget)
        self.system_information_widget.setObjectName(u"system_information_widget")
        self.system_information_widget.setMinimumSize(QSize(200, 100))
        self.system_information_widget.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_9 = QVBoxLayout(self.system_information_widget)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.vps_name_label = QLabel(self.system_information_widget)
        self.vps_name_label.setObjectName(u"vps_name_label")
        self.vps_name_label.setStyleSheet(u"font: 12pt;")
        self.vps_name_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.vps_name_label.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.vps_name_label)

        self.ip_os_label = QLabel(self.system_information_widget)
        self.ip_os_label.setObjectName(u"ip_os_label")
        self.ip_os_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.ip_os_label.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.ip_os_label)

        self.cpu_ram_label = QLabel(self.system_information_widget)
        self.cpu_ram_label.setObjectName(u"cpu_ram_label")
        self.cpu_ram_label.setMaximumSize(QSize(16777215, 16777215))
        self.cpu_ram_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.cpu_ram_label.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.cpu_ram_label)


        self.horizontalLayout_10.addWidget(self.system_information_widget)

        self.status_label = QLabel(self.agent_information_widget)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setStyleSheet(u"QLabel {\n"
"	font: 12pt;\n"
"}\n"
"QLabel[agent_status=\"online\"] {\n"
"    color: #4caf50;\n"
"}\n"
"QLabel[agent_status=\"offline\"] {\n"
"    color: #f44336;\n"
"}")
        self.status_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_10.addWidget(self.status_label)


        self.horizontalLayout.addWidget(self.agent_information_widget)

        self.spacer1 = QSpacerItem(200, 29, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.spacer1)

        self.right_widget = QWidget(card_form)
        self.right_widget.setObjectName(u"right_widget")
        self.right_widget.setMaximumSize(QSize(150, 120))
        self.right_widget.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.right_widget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 80, -1, -1)
        self.agent_open_button = QPushButton(self.right_widget)
        self.agent_open_button.setObjectName(u"agent_open_button")
        self.agent_open_button.setMaximumSize(QSize(104, 16777215))
        self.agent_open_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_10.addWidget(self.agent_open_button)


        self.horizontalLayout.addWidget(self.right_widget)

        self.spacer2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.spacer2)


        self.retranslateUi(card_form)

        QMetaObject.connectSlotsByName(card_form)
    # setupUi

    def retranslateUi(self, card_form):
        card_form.setWindowTitle(QCoreApplication.translate("card_form", u"Form", None))
        self.online_dot.setText(QCoreApplication.translate("card_form", u"\u25cf", None))
        self.vps_name_label.setText(QCoreApplication.translate("card_form", u"VPS Production", None))
        self.ip_os_label.setText(QCoreApplication.translate("card_form", u"1.2.3.4 \u00b7 Ubuntu 24.04", None))
        self.cpu_ram_label.setText(QCoreApplication.translate("card_form", u"CPU 23%   RAM 41%", None))
        self.status_label.setText(QCoreApplication.translate("card_form", u"ON", None))
        self.agent_open_button.setText(QCoreApplication.translate("card_form", u"[ Open \u2192 ]", None))
    # retranslateUi

