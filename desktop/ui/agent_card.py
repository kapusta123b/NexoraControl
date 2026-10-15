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
        card_form.resize(900, 88)
        card_form.setMinimumSize(QSize(0, 80))
        card_form.setMaximumSize(QSize(16777215, 94))
        card_form.setStyleSheet(u"")
        self.card_form_layout = QHBoxLayout(card_form)
        self.card_form_layout.setSpacing(11)
        self.card_form_layout.setObjectName(u"card_form_layout")
        self.card_form_layout.setContentsMargins(13, 8, 13, 8)
        self.agent_information_layout = QHBoxLayout()
        self.agent_information_layout.setSpacing(6)
        self.agent_information_layout.setObjectName(u"agent_information_layout")
        self.agent_information_layout.setContentsMargins(0, 0, 0, 0)
        self.online_dot = QLabel(card_form)
        self.online_dot.setObjectName(u"online_dot")
        self.online_dot.setMinimumSize(QSize(16, 0))
        self.online_dot.setMaximumSize(QSize(16, 16777215))
        self.online_dot.setAlignment(Qt.AlignCenter)

        self.agent_information_layout.addWidget(self.online_dot)

        self.system_information_layout = QVBoxLayout()
        self.system_information_layout.setSpacing(2)
        self.system_information_layout.setObjectName(u"system_information_layout")
        self.system_information_layout.setContentsMargins(0, 0, 0, 0)
        self.vps_name_label = QLabel(card_form)
        self.vps_name_label.setObjectName(u"vps_name_label")
        self.vps_name_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.vps_name_label.setWordWrap(True)

        self.system_information_layout.addWidget(self.vps_name_label)

        self.ip_os_label = QLabel(card_form)
        self.ip_os_label.setObjectName(u"ip_os_label")
        self.ip_os_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ip_os_label.setWordWrap(True)

        self.system_information_layout.addWidget(self.ip_os_label)

        self.cpu_ram_label = QLabel(card_form)
        self.cpu_ram_label.setObjectName(u"cpu_ram_label")
        self.cpu_ram_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.cpu_ram_label.setWordWrap(True)

        self.system_information_layout.addWidget(self.cpu_ram_label)


        self.agent_information_layout.addLayout(self.system_information_layout)


        self.card_form_layout.addLayout(self.agent_information_layout)

        self.card_content_spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.card_form_layout.addItem(self.card_content_spacer)

        self.right_widget_layout = QVBoxLayout()
        self.right_widget_layout.setSpacing(5)
        self.right_widget_layout.setObjectName(u"right_widget_layout")
        self.right_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.status_label = QLabel(card_form)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setMaximumSize(QSize(110, 40))
        self.status_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.right_widget_layout.addWidget(self.status_label)

        self.agent_open_button = QPushButton(card_form)
        self.agent_open_button.setObjectName(u"agent_open_button")
        self.agent_open_button.setMinimumSize(QSize(0, 0))
        self.agent_open_button.setMaximumSize(QSize(138, 16777215))
        self.agent_open_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.right_widget_layout.addWidget(self.agent_open_button)


        self.card_form_layout.addLayout(self.right_widget_layout)


        self.retranslateUi(card_form)

        QMetaObject.connectSlotsByName(card_form)
    # setupUi

    def retranslateUi(self, card_form):
        card_form.setWindowTitle(QCoreApplication.translate("card_form", u"Agent", None))
        self.online_dot.setText(QCoreApplication.translate("card_form", u"\u25cf", None))
        self.vps_name_label.setText(QCoreApplication.translate("card_form", u"production-eu-01", None))
        self.ip_os_label.setText(QCoreApplication.translate("card_form", u"10.12.0.24   /   Ubuntu 24.04", None))
        self.cpu_ram_label.setText(QCoreApplication.translate("card_form", u"CPU 23%   \u00b7   MEMORY 41%", None))
        self.status_label.setText(QCoreApplication.translate("card_form", u"ONLINE", None))
        self.agent_open_button.setText(QCoreApplication.translate("card_form", u"Open agent  \u2192", None))
    # retranslateUi

