# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NexoraControl.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1174, 558)
        icon = QIcon()
        iconThemeName = u"camera-photo"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"../.designer/.designer/backup", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QStackedWidget {\n"
"	background-color: rgb(237, 21, 59);\n"
"}")
        self.central_content = QWidget(MainWindow)
        self.central_content.setObjectName(u"central_content")
        self.central_content.setMinimumSize(QSize(993, 300))
        self.central_content.setMaximumSize(QSize(16777215, 16777215))
        self.central_content.setStyleSheet(u"QMainWindow, QWidget {\n"
"    background-color: #0d1117; \n"
"    color: #c9d1d9;            \n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"}\n"
"\n"
"\n"
"#left_panel {\n"
"    background-color: #161b22; \n"
"    border-right: 1px solid #21262d;\n"
"}\n"
"\n"
"#card_agents, #card_online, #card_offline {\n"
"    background-color: #161b22;\n"
"    border: 1px solid #30363d;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"\n"
"QTableWidget {\n"
"    background-color: #161b22;\n"
"    color: #e6edf3;\n"
"    border: 1px solid #30363d;\n"
"	border-top-right: none;\n"
"    gridline-color: #21262d;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #11151c;\n"
"    color: #58a6ff;\n"
"    padding: 8px;\n"
"    border: none;\n"
"    border-bottom: 2px solid #30363d;\n"
"    font-weight: bold;\n"
"    font-size: 11px;\n"
"    text-transform: uppercase;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #1f6feb;\n"
"    color: #ff"
                        "ffff;\n"
"}\n"
"\n"
"QPushButton {\n"
"    text-align: left;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    margin-left: 2px;\n"
"    padding: 8px 12px;\n"
"    color: #8b949e;\n"
"    font-size: 13px;\n"
"    border-radius: 6px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: rgba(54, 120, 196, 186); \n"
"    color: #ffffff;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"\n"
"Line {\n"
"    background-color: #1E2633;\n"
"    border: none;\n"
"    max-height: 1px;\n"
"}\n"
"")
        self.left_panel = QWidget(self.central_content)
        self.left_panel.setObjectName(u"left_panel")
        self.left_panel.setGeometry(QRect(0, 0, 171, 555))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_panel.sizePolicy().hasHeightForWidth())
        self.left_panel.setSizePolicy(sizePolicy)
        self.left_panel.setMinimumSize(QSize(160, 200))
        self.left_panel.setMaximumSize(QSize(200, 16000))
        self.left_panel.setStyleSheet(u"QWidget {\n"
"	background-color: #161b22; \n"
"    border-right: 1px solid #21262d;\n"
"	font: 200 10pt \"JetBrainsMonoNL Nerd Font Propo\";\n"
"}\n"
"\n"
"\n"
"\n"
"QLabel {\n"
"	border: none;\n"
"}\n"
"\n"
"#label_logo { \n"
"    color: #58a6ff; \n"
"    font-weight: 800;\n"
"    letter-spacing: 2px;\n"
"}\n"
"\n"
"Line {\n"
"	background-color: rgba(244, 244, 244, 164);\n"
"\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.left_panel)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.nexora_logo = QLabel(self.left_panel)
        self.nexora_logo.setObjectName(u"nexora_logo")
        self.nexora_logo.setStyleSheet(u"QLabel {\n"
"    color: #58a6ff;\n"
"    font: 800 25pt;\n"
"    letter-spacing: 2px;\n"
" 	margin-left: 2px;\n"
"}")
        self.nexora_logo.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.nexora_logo)

        self.dashboard_button = QPushButton(self.left_panel)
        self.dashboard_button.setObjectName(u"dashboard_button")
        self.dashboard_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dashboard_button.setCheckable(True)

        self.verticalLayout_2.addWidget(self.dashboard_button)

        self.agents_button = QPushButton(self.left_panel)
        self.agents_button.setObjectName(u"agents_button")
        self.agents_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.agents_button.setCheckable(True)

        self.verticalLayout_2.addWidget(self.agents_button)

        self.commands_button = QPushButton(self.left_panel)
        self.commands_button.setObjectName(u"commands_button")
        self.commands_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.commands_button.setCheckable(True)

        self.verticalLayout_2.addWidget(self.commands_button)

        self.metrics_button = QPushButton(self.left_panel)
        self.metrics_button.setObjectName(u"metrics_button")
        self.metrics_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.metrics_button.setCheckable(True)

        self.verticalLayout_2.addWidget(self.metrics_button)

        self.logs_button = QPushButton(self.left_panel)
        self.logs_button.setObjectName(u"logs_button")
        self.logs_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.logs_button.setCheckable(True)

        self.verticalLayout_2.addWidget(self.logs_button)

        self.line = QFrame(self.left_panel)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.settings_button = QPushButton(self.left_panel)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.settings_button.setCheckable(True)

        self.verticalLayout_2.addWidget(self.settings_button)

        self.about_button = QPushButton(self.left_panel)
        self.about_button.setObjectName(u"about_button")
        self.about_button.setCursor(QCursor(Qt.CursorShape.WhatsThisCursor))
        self.about_button.setCheckable(True)
        self.about_button.setChecked(False)
        self.about_button.setAutoRepeat(False)

        self.verticalLayout_2.addWidget(self.about_button)

        self.bottom_spacer = QSpacerItem(20, 200, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.bottom_spacer)

        self.content_stack = QStackedWidget(self.central_content)
        self.content_stack.setObjectName(u"content_stack")
        self.content_stack.setGeometry(QRect(171, 0, 769, 553))
        self.content_stack.setMinimumSize(QSize(500, 411))
        self.content_stack.setMaximumSize(QSize(16777215, 16777215))
        self.content_stack.setStyleSheet(u"QWidget {\n"
"    color: #c9d1d9;\n"
"	font: 200 10pt \"JetBrainsMonoNL Nerd Font Propo\";\n"
"}\n"
"")
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.dashboard_page.setStyleSheet(u"QPushButton {\n"
"    color: #a5b4fc; \n"
"    background-color: transparent;\n"
"    border: 1px solid #242936;\n"
"    border-radius: 4px;\n"
"    padding: 6px 12px;	\n"
"	text-align: center;\n"
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
"}")
        self.verticalLayout_7 = QVBoxLayout(self.dashboard_page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.dashboard_layout = QVBoxLayout()
        self.dashboard_layout.setSpacing(6)
        self.dashboard_layout.setObjectName(u"dashboard_layout")
        self.dashboard_label = QLabel(self.dashboard_page)
        self.dashboard_label.setObjectName(u"dashboard_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dashboard_label.sizePolicy().hasHeightForWidth())
        self.dashboard_label.setSizePolicy(sizePolicy1)
        self.dashboard_label.setMaximumSize(QSize(16777215, 30))
        self.dashboard_label.setStyleSheet(u"QLabel {\n"
"	font: 500 15pt;\n"
"}")

        self.dashboard_layout.addWidget(self.dashboard_label)

        self.dashboard_line = QFrame(self.dashboard_page)
        self.dashboard_line.setObjectName(u"dashboard_line")
        self.dashboard_line.setFrameShape(QFrame.Shape.HLine)
        self.dashboard_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.dashboard_layout.addWidget(self.dashboard_line)

        self.top_spacer = QSpacerItem(20, 22, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.dashboard_layout.addItem(self.top_spacer)

        self.cards = QWidget(self.dashboard_page)
        self.cards.setObjectName(u"cards")
        self.cards.setStyleSheet(u"#card_agents, #card_online, #card_offline {\n"
"    background-color: #161b22;\n"
"\n"
"}\n"
"\n"
"QLabel {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.cards)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.card_agents = QWidget(self.cards)
        self.card_agents.setObjectName(u"card_agents")
        self.card_agents.setMaximumSize(QSize(16777215, 65))
        self.card_agents.setStyleSheet(u"")
        self.verticalLayout_12 = QVBoxLayout(self.card_agents)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.agent_label = QLabel(self.card_agents)
        self.agent_label.setObjectName(u"agent_label")
        self.agent_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.agent_label)

        self.agents_count = QLabel(self.card_agents)
        self.agents_count.setObjectName(u"agents_count")
        self.agents_count.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.agents_count)


        self.horizontalLayout_3.addWidget(self.card_agents)

        self.card_online = QWidget(self.cards)
        self.card_online.setObjectName(u"card_online")
        self.card_online.setMaximumSize(QSize(16777215, 65))
        self.card_online.setStyleSheet(u"")
        self.verticalLayout_13 = QVBoxLayout(self.card_online)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.online_label = QLabel(self.card_online)
        self.online_label.setObjectName(u"online_label")
        self.online_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.online_label)

        self.online_count = QLabel(self.card_online)
        self.online_count.setObjectName(u"online_count")
        self.online_count.setStyleSheet(u"QLabel { \n"
"	color: #4ef2d2;\n"
"    font-weight: bold;\n"
"}")
        self.online_count.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.online_count)


        self.horizontalLayout_3.addWidget(self.card_online)

        self.card_offline = QWidget(self.cards)
        self.card_offline.setObjectName(u"card_offline")
        self.card_offline.setMaximumSize(QSize(16777215, 65))
        self.card_offline.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.card_offline)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.offline_label = QLabel(self.card_offline)
        self.offline_label.setObjectName(u"offline_label")
        self.offline_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.offline_label)

        self.offline_count = QLabel(self.card_offline)
        self.offline_count.setObjectName(u"offline_count")
        self.offline_count.setStyleSheet(u"QLabel {\n"
"    color: #f85149;\n"
"    font-weight: bold;\n"
"}")
        self.offline_count.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.offline_count)


        self.horizontalLayout_3.addWidget(self.card_offline)


        self.dashboard_layout.addWidget(self.cards)

        self.agents_label = QLabel(self.dashboard_page)
        self.agents_label.setObjectName(u"agents_label")
        self.agents_label.setEnabled(True)
        self.agents_label.setMaximumSize(QSize(16777215, 30))
        self.agents_label.setStyleSheet(u"QLabel {\n"
"	font: 500 15pt;\n"
"}")

        self.dashboard_layout.addWidget(self.agents_label)

        self.line_4 = QFrame(self.dashboard_page)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.dashboard_layout.addWidget(self.line_4)

        self.agents_table = QTableWidget(self.dashboard_page)
        if (self.agents_table.columnCount() < 6):
            self.agents_table.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.agents_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.agents_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.agents_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.agents_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.agents_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.agents_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.agents_table.setObjectName(u"agents_table")
        self.agents_table.setEnabled(True)
        self.agents_table.setMaximumSize(QSize(16777215, 16777215))
        self.agents_table.setStyleSheet(u"")
        self.agents_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.agents_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.agents_table.setAlternatingRowColors(False)
        self.agents_table.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.agents_table.setSortingEnabled(True)
        self.agents_table.horizontalHeader().setVisible(True)
        self.agents_table.horizontalHeader().setCascadingSectionResizes(True)
        self.agents_table.horizontalHeader().setMinimumSectionSize(20)
        self.agents_table.horizontalHeader().setDefaultSectionSize(120)
        self.agents_table.horizontalHeader().setHighlightSections(False)
        self.agents_table.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.agents_table.horizontalHeader().setStretchLastSection(False)
        self.agents_table.verticalHeader().setVisible(False)
        self.agents_table.verticalHeader().setCascadingSectionResizes(False)
        self.agents_table.verticalHeader().setMinimumSectionSize(25)
        self.agents_table.verticalHeader().setDefaultSectionSize(48)
        self.agents_table.verticalHeader().setHighlightSections(True)
        self.agents_table.verticalHeader().setProperty(u"showSortIndicator", False)
        self.agents_table.verticalHeader().setStretchLastSection(False)

        self.dashboard_layout.addWidget(self.agents_table)

        self.middle_spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.dashboard_layout.addItem(self.middle_spacer)

        self.layout_buttons = QHBoxLayout()
        self.layout_buttons.setObjectName(u"layout_buttons")
        self.refresh_table_button = QPushButton(self.dashboard_page)
        self.refresh_table_button.setObjectName(u"refresh_table_button")
        self.refresh_table_button.setMaximumSize(QSize(350, 16777215))
        self.refresh_table_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.refresh_table_button.setLayoutDirection(Qt.LeftToRight)

        self.layout_buttons.addWidget(self.refresh_table_button)


        self.dashboard_layout.addLayout(self.layout_buttons)

        self.bottom_spacer_2 = QSpacerItem(20, 64, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.dashboard_layout.addItem(self.bottom_spacer_2)


        self.verticalLayout_7.addLayout(self.dashboard_layout)

        self.content_stack.addWidget(self.dashboard_page)
        self.agents_page = QWidget()
        self.agents_page.setObjectName(u"agents_page")
        self.agents_page.setStyleSheet(u"QPushButton {\n"
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
"\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #161920; \n"
"    border: 1px solid #242936; \n"
"    border-radius: 4px; \n"
"    color: #ffffff; \n"
"    font-size: 13px;\n"
"    padding: 6px 10px 6px 10px;  \n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #4b5563; \n"
"    font-style: italic;\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #38bdf8; \n"
"    background-color: #1c202b; \n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.agents_page)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.agents_main_layout = QVBoxLayout()
        self.agents_main_layout.setSpacing(0)
        self.agents_main_layout.setObjectName(u"agents_main_layout")
        self.agents_headline_label = QLabel(self.agents_page)
        self.agents_headline_label.setObjectName(u"agents_headline_label")
        self.agents_headline_label.setMinimumSize(QSize(0, 0))
        self.agents_headline_label.setMaximumSize(QSize(16777215, 25))
        self.agents_headline_label.setStyleSheet(u"QLabel {\n"
"	font: 500 15pt;\n"
"}")

        self.agents_main_layout.addWidget(self.agents_headline_label)

        self.page_description_label = QLabel(self.agents_page)
        self.page_description_label.setObjectName(u"page_description_label")
        self.page_description_label.setMaximumSize(QSize(16777215, 40))

        self.agents_main_layout.addWidget(self.page_description_label)

        self.page_description_line = QFrame(self.agents_page)
        self.page_description_line.setObjectName(u"page_description_line")
        self.page_description_line.setFrameShape(QFrame.Shape.HLine)
        self.page_description_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.agents_main_layout.addWidget(self.page_description_line)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.agents_main_layout.addItem(self.verticalSpacer_5)

        self.help_bar_layout = QHBoxLayout()
        self.help_bar_layout.setSpacing(0)
        self.help_bar_layout.setObjectName(u"help_bar_layout")
        self.horizontalSpacer_2 = QSpacerItem(10, 14, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.help_bar_layout.addItem(self.horizontalSpacer_2)

        self.search_input_line = QLineEdit(self.agents_page)
        self.search_input_line.setObjectName(u"search_input_line")
        self.search_input_line.setClearButtonEnabled(False)

        self.help_bar_layout.addWidget(self.search_input_line)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.help_bar_layout.addItem(self.horizontalSpacer)

        self.refresh_agents_button = QPushButton(self.agents_page)
        self.refresh_agents_button.setObjectName(u"refresh_agents_button")
        self.refresh_agents_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.help_bar_layout.addWidget(self.refresh_agents_button)

        self.horizontalSpacer_3 = QSpacerItem(17, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.help_bar_layout.addItem(self.horizontalSpacer_3)


        self.agents_main_layout.addLayout(self.help_bar_layout)

        self.agent_list = QScrollArea(self.agents_page)
        self.agent_list.setObjectName(u"agent_list")
        self.agent_list.setMaximumSize(QSize(16777215, 300))
        self.agent_list.setLayoutDirection(Qt.LeftToRight)
        self.agent_list.setAutoFillBackground(False)
        self.agent_list.setStyleSheet(u"QScrollArea {\n"
"    border: none;\n"
"\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QWidget#scrollAreaWidgetContents {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #11141a;\n"
"    width: 12px;\n"
"    margin: 0px 0px 0px 5px;\n"
"	\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #242936;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #38bdf8;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"    height: 0px;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"")
        self.agent_list.setFrameShape(QFrame.Box)
        self.agent_list.setFrameShadow(QFrame.Plain)
        self.agent_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.agent_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.agent_list.setWidgetResizable(True)
        self.agent_list.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.agent_scroll = QWidget()
        self.agent_scroll.setObjectName(u"agent_scroll")
        self.agent_scroll.setGeometry(QRect(0, 0, 971, 300))
        self.agent_scroll.setMaximumSize(QSize(16777215, 1000000))
        self.agent_scroll.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.agent_scroll)
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 16, 16, 16)
        self.agent_list.setWidget(self.agent_scroll)

        self.agents_main_layout.addWidget(self.agent_list)


        self.verticalLayout_8.addLayout(self.agents_main_layout)

        self.content_stack.addWidget(self.agents_page)
        self.agent_detail_page = QWidget()
        self.agent_detail_page.setObjectName(u"agent_detail_page")
        self.agent_detail_page.setStyleSheet(u"QPushButton {\n"
"    color: #a5b4fc; \n"
"    background-color: transparent;\n"
"    border: 1px solid #242936;\n"
"    border-radius: 4px;\n"
"    padding: 6px 12px;	\n"
"	text-align: center;\n"
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
"}")
        self.verticalLayout_3 = QVBoxLayout(self.agent_detail_page)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.agent_detail_content = QWidget(self.agent_detail_page)
        self.agent_detail_content.setObjectName(u"agent_detail_content")
        self.verticalLayout = QVBoxLayout(self.agent_detail_content)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.detail_top_widget = QWidget(self.agent_detail_content)
        self.detail_top_widget.setObjectName(u"detail_top_widget")
        self.detail_top_widget.setMinimumSize(QSize(0, 0))
        self.detail_top_widget.setMaximumSize(QSize(16777215, 300))
        self.detail_top_widget.setStyleSheet(u"")
        self.verticalLayout_17 = QVBoxLayout(self.detail_top_widget)
        self.verticalLayout_17.setSpacing(10)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.detail_top_layout = QHBoxLayout()
        self.detail_top_layout.setObjectName(u"detail_top_layout")
        self.back_to_agents_button = QPushButton(self.detail_top_widget)
        self.back_to_agents_button.setObjectName(u"back_to_agents_button")
        self.back_to_agents_button.setMinimumSize(QSize(180, 0))
        self.back_to_agents_button.setMaximumSize(QSize(185, 16777215))
        self.back_to_agents_button.setLayoutDirection(Qt.RightToLeft)
        self.back_to_agents_button.setStyleSheet(u"QPushButton {\n"
"	text-align: left;\n"
"}")
        self.back_to_agents_button.setCheckable(False)
        self.back_to_agents_button.setAutoRepeat(False)

        self.detail_top_layout.addWidget(self.back_to_agents_button)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.detail_top_layout.addItem(self.horizontalSpacer_4)

        self.detail_top_agent_name_label = QLabel(self.detail_top_widget)
        self.detail_top_agent_name_label.setObjectName(u"detail_top_agent_name_label")
        self.detail_top_agent_name_label.setStyleSheet(u"font: 12pt")
        self.detail_top_agent_name_label.setWordWrap(True)

        self.detail_top_layout.addWidget(self.detail_top_agent_name_label)

        self.detail_top_info_spacer = QSpacerItem(28, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.detail_top_layout.addItem(self.detail_top_info_spacer)

        self.detail_top_agent_status_label = QLabel(self.detail_top_widget)
        self.detail_top_agent_status_label.setObjectName(u"detail_top_agent_status_label")

        self.detail_top_layout.addWidget(self.detail_top_agent_status_label)


        self.verticalLayout_17.addLayout(self.detail_top_layout)

        self.detail_top_navigation_layout = QHBoxLayout()
        self.detail_top_navigation_layout.setSpacing(2)
        self.detail_top_navigation_layout.setObjectName(u"detail_top_navigation_layout")
        self.detail_top_navigation_layout.setContentsMargins(0, 10, 0, 10)
        self.overview_nav_button = QPushButton(self.detail_top_widget)
        self.overview_nav_button.setObjectName(u"overview_nav_button")

        self.detail_top_navigation_layout.addWidget(self.overview_nav_button)

        self.perfomance_nav_button = QPushButton(self.detail_top_widget)
        self.perfomance_nav_button.setObjectName(u"perfomance_nav_button")

        self.detail_top_navigation_layout.addWidget(self.perfomance_nav_button)

        self.hardware_nav_button = QPushButton(self.detail_top_widget)
        self.hardware_nav_button.setObjectName(u"hardware_nav_button")

        self.detail_top_navigation_layout.addWidget(self.hardware_nav_button)

        self.storage_nav_button = QPushButton(self.detail_top_widget)
        self.storage_nav_button.setObjectName(u"storage_nav_button")

        self.detail_top_navigation_layout.addWidget(self.storage_nav_button)

        self.network_nav_button = QPushButton(self.detail_top_widget)
        self.network_nav_button.setObjectName(u"network_nav_button")

        self.detail_top_navigation_layout.addWidget(self.network_nav_button)

        self.commands_nav_button = QPushButton(self.detail_top_widget)
        self.commands_nav_button.setObjectName(u"commands_nav_button")

        self.detail_top_navigation_layout.addWidget(self.commands_nav_button)


        self.verticalLayout_17.addLayout(self.detail_top_navigation_layout)


        self.verticalLayout.addWidget(self.detail_top_widget)

        self.detail_top_line = QFrame(self.agent_detail_content)
        self.detail_top_line.setObjectName(u"detail_top_line")
        self.detail_top_line.setFrameShape(QFrame.Shape.HLine)
        self.detail_top_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.detail_top_line)

        self.agent_detail_stacked_content = QStackedWidget(self.agent_detail_content)
        self.agent_detail_stacked_content.setObjectName(u"agent_detail_stacked_content")
        self.overview_detail_page = QWidget()
        self.overview_detail_page.setObjectName(u"overview_detail_page")
        self.verticalLayout_25 = QVBoxLayout(self.overview_detail_page)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.overview_detail_scroll = QScrollArea(self.overview_detail_page)
        self.overview_detail_scroll.setObjectName(u"overview_detail_scroll")
        self.overview_detail_scroll.setStyleSheet(u"QScrollArea {\n"
"    border: none;\n"
"\n"
"\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QWidget#scrollAreaWidgetContents {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #11141a;\n"
"    width: 12px;\n"
"    margin: 0px 0px 0px 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #242936;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #38bdf8;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"    height: 0px;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"")
        self.overview_detail_scroll.setWidgetResizable(True)
        self.agent_detail_information = QWidget()
        self.agent_detail_information.setObjectName(u"agent_detail_information")
        self.agent_detail_information.setGeometry(QRect(0, 0, 833, 700))
        self.agent_detail_information.setMinimumSize(QSize(0, 700))
        self.verticalLayout_18 = QVBoxLayout(self.agent_detail_information)
        self.verticalLayout_18.setSpacing(5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.overview_widget = QWidget(self.agent_detail_information)
        self.overview_widget.setObjectName(u"overview_widget")
        self.overview_widget.setMaximumSize(QSize(16777215, 120))
        self.overview_widget.setStyleSheet(u"#uptime_widget, #ram_widget, #disk_widget, #cpu_widget {\n"
"	background-color: #161b22;\n"
"	border: 1px solid #30363d;\n"
"\n"
"    padding: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QLabel {\n"
"	background-color: transparent;\n"
"}")
        self.verticalLayout_19 = QVBoxLayout(self.overview_widget)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.overview_label = QLabel(self.overview_widget)
        self.overview_label.setObjectName(u"overview_label")
        self.overview_label.setMaximumSize(QSize(16777215, 30))
        self.overview_label.setStyleSheet(u"QLabel {\n"
"	font: 600 17pt;\n"
"}")
        self.overview_label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_19.addWidget(self.overview_label)

        self.resource_boxes_widget = QWidget(self.overview_widget)
        self.resource_boxes_widget.setObjectName(u"resource_boxes_widget")
        self.resource_boxes_widget.setMaximumSize(QSize(16777215, 70))
        self.resource_boxes_layout = QHBoxLayout(self.resource_boxes_widget)
        self.resource_boxes_layout.setSpacing(100)
        self.resource_boxes_layout.setObjectName(u"resource_boxes_layout")
        self.resource_boxes_layout.setContentsMargins(0, 0, 0, 0)
        self.cpu_widget = QWidget(self.resource_boxes_widget)
        self.cpu_widget.setObjectName(u"cpu_widget")
        self.cpu_widget.setMinimumSize(QSize(0, 60))
        self.cpu_widget.setMaximumSize(QSize(140, 90))
        self.verticalLayout_20 = QVBoxLayout(self.cpu_widget)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.cpu_label = QLabel(self.cpu_widget)
        self.cpu_label.setObjectName(u"cpu_label")
        self.cpu_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.cpu_label)

        self.cpu_load_label = QLabel(self.cpu_widget)
        self.cpu_load_label.setObjectName(u"cpu_load_label")
        self.cpu_load_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.cpu_load_label)


        self.resource_boxes_layout.addWidget(self.cpu_widget)

        self.ram_widget = QWidget(self.resource_boxes_widget)
        self.ram_widget.setObjectName(u"ram_widget")
        self.ram_widget.setMinimumSize(QSize(0, 60))
        self.ram_widget.setMaximumSize(QSize(140, 90))
        self.verticalLayout_21 = QVBoxLayout(self.ram_widget)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.ram_label = QLabel(self.ram_widget)
        self.ram_label.setObjectName(u"ram_label")
        self.ram_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.ram_label)

        self.ram_load_label = QLabel(self.ram_widget)
        self.ram_load_label.setObjectName(u"ram_load_label")
        self.ram_load_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.ram_load_label)


        self.resource_boxes_layout.addWidget(self.ram_widget)

        self.disk_widget = QWidget(self.resource_boxes_widget)
        self.disk_widget.setObjectName(u"disk_widget")
        self.disk_widget.setMinimumSize(QSize(0, 60))
        self.disk_widget.setMaximumSize(QSize(140, 90))
        self.verticalLayout_22 = QVBoxLayout(self.disk_widget)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.disk_label = QLabel(self.disk_widget)
        self.disk_label.setObjectName(u"disk_label")
        self.disk_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.disk_label)

        self.disk_load_label = QLabel(self.disk_widget)
        self.disk_load_label.setObjectName(u"disk_load_label")
        self.disk_load_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.disk_load_label)


        self.resource_boxes_layout.addWidget(self.disk_widget)

        self.uptime_widget = QWidget(self.resource_boxes_widget)
        self.uptime_widget.setObjectName(u"uptime_widget")
        self.uptime_widget.setMinimumSize(QSize(0, 60))
        self.uptime_widget.setMaximumSize(QSize(140, 90))
        self.verticalLayout_23 = QVBoxLayout(self.uptime_widget)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.uptime_label = QLabel(self.uptime_widget)
        self.uptime_label.setObjectName(u"uptime_label")
        self.uptime_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.uptime_label)

        self.up_time_label = QLabel(self.uptime_widget)
        self.up_time_label.setObjectName(u"up_time_label")
        self.up_time_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.up_time_label)


        self.resource_boxes_layout.addWidget(self.uptime_widget)


        self.verticalLayout_19.addWidget(self.resource_boxes_widget)


        self.verticalLayout_18.addWidget(self.overview_widget)

        self.system_status_widget = QWidget(self.agent_detail_information)
        self.system_status_widget.setObjectName(u"system_status_widget")
        self.system_status_widget.setMinimumSize(QSize(0, 250))
        self.system_status_widget.setMaximumSize(QSize(16777215, 350))
        self.system_status_layout = QVBoxLayout(self.system_status_widget)
        self.system_status_layout.setObjectName(u"system_status_layout")
        self.system_status_layout.setContentsMargins(5, 0, 0, 0)
        self.system_status_label = QLabel(self.system_status_widget)
        self.system_status_label.setObjectName(u"system_status_label")
        self.system_status_label.setMaximumSize(QSize(16777215, 40))
        self.system_status_label.setStyleSheet(u"QLabel {\n"
"	font: 350 12pt;\n"
"}")

        self.system_status_layout.addWidget(self.system_status_label)

        self.system_status_box_widget = QWidget(self.system_status_widget)
        self.system_status_box_widget.setObjectName(u"system_status_box_widget")
        self.system_status_box_widget.setMaximumSize(QSize(500, 300))
        self.system_status_box_widget.setStyleSheet(u"#system_status_box_widget {\n"
"    background-color: #161b22;\n"
"	border: 1px solid #30363d;\n"
"	margin-left: 5px;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"#system_status_box_widget QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.system_status_box_widget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.system_status_box_layout = QHBoxLayout()
        self.system_status_box_layout.setObjectName(u"system_status_box_layout")
        self.system_status_rows_widget = QWidget(self.system_status_box_widget)
        self.system_status_rows_widget.setObjectName(u"system_status_rows_widget")
        self.system_status_rows_widget.setStyleSheet(u"QLabel {\n"
"	font: 200 12pt;\n"
"	margin-left: 20px;\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.system_status_rows_widget)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(10, 0, 0, 0)
        self.agent_row_label = QLabel(self.system_status_rows_widget)
        self.agent_row_label.setObjectName(u"agent_row_label")
        self.agent_row_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.agent_row_label.setMargin(0)

        self.verticalLayout_9.addWidget(self.agent_row_label)

        self.last_seen_row_label = QLabel(self.system_status_rows_widget)
        self.last_seen_row_label.setObjectName(u"last_seen_row_label")
        self.last_seen_row_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.last_seen_row_label.setMargin(0)

        self.verticalLayout_9.addWidget(self.last_seen_row_label)

        self.version_row_label = QLabel(self.system_status_rows_widget)
        self.version_row_label.setObjectName(u"version_row_label")
        self.version_row_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.version_row_label.setMargin(0)

        self.verticalLayout_9.addWidget(self.version_row_label)

        self.hostname_row_label = QLabel(self.system_status_rows_widget)
        self.hostname_row_label.setObjectName(u"hostname_row_label")
        self.hostname_row_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.hostname_row_label.setMargin(0)

        self.verticalLayout_9.addWidget(self.hostname_row_label)

        self.os_name_row_label = QLabel(self.system_status_rows_widget)
        self.os_name_row_label.setObjectName(u"os_name_row_label")
        self.os_name_row_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.os_name_row_label.setMargin(0)

        self.verticalLayout_9.addWidget(self.os_name_row_label)


        self.system_status_box_layout.addWidget(self.system_status_rows_widget)

        self.system_status_values_widget = QWidget(self.system_status_box_widget)
        self.system_status_values_widget.setObjectName(u"system_status_values_widget")
        self.system_status_values_widget.setStyleSheet(u"QLabel {\n"
"	font: 450 12pt;\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.system_status_values_widget)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.agent_status_value_label = QLabel(self.system_status_values_widget)
        self.agent_status_value_label.setObjectName(u"agent_status_value_label")

        self.verticalLayout_11.addWidget(self.agent_status_value_label)

        self.last_seen_value_label = QLabel(self.system_status_values_widget)
        self.last_seen_value_label.setObjectName(u"last_seen_value_label")

        self.verticalLayout_11.addWidget(self.last_seen_value_label)

        self.version_value_label = QLabel(self.system_status_values_widget)
        self.version_value_label.setObjectName(u"version_value_label")

        self.verticalLayout_11.addWidget(self.version_value_label)

        self.hostname_value_label = QLabel(self.system_status_values_widget)
        self.hostname_value_label.setObjectName(u"hostname_value_label")

        self.verticalLayout_11.addWidget(self.hostname_value_label)

        self.os_name_value_label = QLabel(self.system_status_values_widget)
        self.os_name_value_label.setObjectName(u"os_name_value_label")

        self.verticalLayout_11.addWidget(self.os_name_value_label)


        self.system_status_box_layout.addWidget(self.system_status_values_widget)


        self.horizontalLayout_4.addLayout(self.system_status_box_layout)


        self.system_status_layout.addWidget(self.system_status_box_widget)


        self.verticalLayout_18.addWidget(self.system_status_widget)

        self.quick_actions_widget = QWidget(self.agent_detail_information)
        self.quick_actions_widget.setObjectName(u"quick_actions_widget")
        self.quick_actions_widget.setMinimumSize(QSize(0, 80))
        self.quick_actions_widget.setMaximumSize(QSize(16777215, 80))
        self.verticalLayout_14 = QVBoxLayout(self.quick_actions_widget)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, -1, 0, 0)
        self.quick_actions_label = QLabel(self.quick_actions_widget)
        self.quick_actions_label.setObjectName(u"quick_actions_label")
        self.quick_actions_label.setStyleSheet(u"QLabel {\n"
"	font: 350 12pt;\n"
"}")

        self.verticalLayout_14.addWidget(self.quick_actions_label)

        self.quick_actions_layout = QHBoxLayout()
        self.quick_actions_layout.setSpacing(10)
        self.quick_actions_layout.setObjectName(u"quick_actions_layout")
        self.quick_actions_layout.setContentsMargins(10, -1, -1, -1)
        self.restart_all_docker_cont_quick_button = QPushButton(self.quick_actions_widget)
        self.restart_all_docker_cont_quick_button.setObjectName(u"restart_all_docker_cont_quick_button")

        self.quick_actions_layout.addWidget(self.restart_all_docker_cont_quick_button)

        self.stop_all_docker_cont_quick_button = QPushButton(self.quick_actions_widget)
        self.stop_all_docker_cont_quick_button.setObjectName(u"stop_all_docker_cont_quick_button")

        self.quick_actions_layout.addWidget(self.stop_all_docker_cont_quick_button)

        self.docker_ps_quick_button = QPushButton(self.quick_actions_widget)
        self.docker_ps_quick_button.setObjectName(u"docker_ps_quick_button")

        self.quick_actions_layout.addWidget(self.docker_ps_quick_button)

        self.reboot_quick_button = QPushButton(self.quick_actions_widget)
        self.reboot_quick_button.setObjectName(u"reboot_quick_button")

        self.quick_actions_layout.addWidget(self.reboot_quick_button)


        self.verticalLayout_14.addLayout(self.quick_actions_layout)


        self.verticalLayout_18.addWidget(self.quick_actions_widget)

        self.recent_commands_widget = QWidget(self.agent_detail_information)
        self.recent_commands_widget.setObjectName(u"recent_commands_widget")
        self.recent_commands_widget.setStyleSheet(u"#recent_command_box_widget {\n"
"    background-color: #161b22;\n"
"	border: 1px solid #30363d;\n"
"	margin-left: 5px;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"#recent_command_box_widget QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.recent_commands_widget)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 15, 0, 0)
        self.recent_commands_label = QLabel(self.recent_commands_widget)
        self.recent_commands_label.setObjectName(u"recent_commands_label")
        self.recent_commands_label.setMaximumSize(QSize(16777215, 30))
        self.recent_commands_label.setStyleSheet(u"QLabel {\n"
"	font: 350 12pt;\n"
"}")

        self.verticalLayout_15.addWidget(self.recent_commands_label)

        self.recent_command_box_widget = QWidget(self.recent_commands_widget)
        self.recent_command_box_widget.setObjectName(u"recent_command_box_widget")
        self.recent_command_box_widget.setMaximumSize(QSize(550, 150))
        self.recent_command_box_widget.setStyleSheet(u"QLabel {\n"
"	font: 300 10.5pt\n"
"}")
        self.horizontalLayout_6 = QHBoxLayout(self.recent_command_box_widget)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 0, 0, 0)

        self.verticalLayout_15.addWidget(self.recent_command_box_widget)


        self.verticalLayout_18.addWidget(self.recent_commands_widget)

        self.overview_detail_scroll.setWidget(self.agent_detail_information)

        self.verticalLayout_25.addWidget(self.overview_detail_scroll)

        self.agent_detail_stacked_content.addWidget(self.overview_detail_page)
        self.perfomance_detail_page = QWidget()
        self.perfomance_detail_page.setObjectName(u"perfomance_detail_page")
        self.verticalLayout_5 = QVBoxLayout(self.perfomance_detail_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.perfomance_detail_scroll = QScrollArea(self.perfomance_detail_page)
        self.perfomance_detail_scroll.setObjectName(u"perfomance_detail_scroll")
        self.perfomance_detail_scroll.setStyleSheet(u"QScrollArea {\n"
"    border: none;\n"
"\n"
"\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QWidget#scrollAreaWidgetContents {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #11141a;\n"
"    width: 12px;\n"
"    margin: 0px 0px 0px 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #242936;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #38bdf8;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"    height: 0px;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"")
        self.perfomance_detail_scroll.setWidgetResizable(True)
        self.agent_perfomance_information = QWidget()
        self.agent_perfomance_information.setObjectName(u"agent_perfomance_information")
        self.agent_perfomance_information.setGeometry(QRect(0, 0, 721, 475))
        self.verticalLayout_26 = QVBoxLayout(self.agent_perfomance_information)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.performance_content_widget = QWidget(self.agent_perfomance_information)
        self.performance_content_widget.setObjectName(u"performance_content_widget")
        self.performance_content_widget.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	margin-top: 5px;\n"
"	margin-bottom: 5px;\n"
"}")
        self.verticalLayout_32 = QVBoxLayout(self.performance_content_widget)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.perfomance_label = QLabel(self.performance_content_widget)
        self.perfomance_label.setObjectName(u"perfomance_label")
        self.perfomance_label.setMinimumSize(QSize(0, 0))
        self.perfomance_label.setStyleSheet(u"QLabel {\n"
"	font: 600 17pt;\n"
"}")
        self.perfomance_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_32.addWidget(self.perfomance_label)

        self.metric_buttons_layout = QHBoxLayout()
        self.metric_buttons_layout.setObjectName(u"metric_buttons_layout")
        self.compute_button = QPushButton(self.performance_content_widget)
        self.compute_button.setObjectName(u"compute_button")

        self.metric_buttons_layout.addWidget(self.compute_button)

        self.storage_button = QPushButton(self.performance_content_widget)
        self.storage_button.setObjectName(u"storage_button")

        self.metric_buttons_layout.addWidget(self.storage_button)

        self.thermals_button = QPushButton(self.performance_content_widget)
        self.thermals_button.setObjectName(u"thermals_button")

        self.metric_buttons_layout.addWidget(self.thermals_button)

        self.network_button = QPushButton(self.performance_content_widget)
        self.network_button.setObjectName(u"network_button")

        self.metric_buttons_layout.addWidget(self.network_button)


        self.verticalLayout_32.addLayout(self.metric_buttons_layout)

        self.metric_graph = PlotWidget(self.performance_content_widget)
        self.metric_graph.setObjectName(u"metric_graph")
        self.metric_graph.setMinimumSize(QSize(0, 400))
        self.metric_graph.setStyleSheet(u"QWidget {\n"
"    background-color: transparent;\n"
"    border: 1px solid #30363d;\n"
"    border-radius: 8px;\n"
"	margin: 10px 0px 0px 0px;\n"
"}")

        self.verticalLayout_32.addWidget(self.metric_graph)


        self.verticalLayout_26.addWidget(self.performance_content_widget)

        self.perfomance_detail_scroll.setWidget(self.agent_perfomance_information)

        self.verticalLayout_5.addWidget(self.perfomance_detail_scroll)

        self.agent_detail_stacked_content.addWidget(self.perfomance_detail_page)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_6 = QVBoxLayout(self.page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.scrollArea = QScrollArea(self.page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -281, 717, 940))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.verticalLayout_27 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.hardware_label = QLabel(self.scrollAreaWidgetContents)
        self.hardware_label.setObjectName(u"hardware_label")
        self.hardware_label.setMinimumSize(QSize(0, 0))
        self.hardware_label.setMaximumSize(QSize(16777215, 30))
        self.hardware_label.setStyleSheet(u"QLabel {\n"
"	font: 600 17pt;\n"
"}")
        self.hardware_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_27.addWidget(self.hardware_label)

        self.cpu_info_widget = QWidget(self.scrollAreaWidgetContents)
        self.cpu_info_widget.setObjectName(u"cpu_info_widget")
        self.cpu_info_widget.setMinimumSize(QSize(0, 250))
        self.cpu_info_widget.setMaximumSize(QSize(16777215, 350))
        self.system_status_layout_2 = QVBoxLayout(self.cpu_info_widget)
        self.system_status_layout_2.setObjectName(u"system_status_layout_2")
        self.system_status_layout_2.setContentsMargins(5, 0, 0, 0)
        self.cpu_info_label = QLabel(self.cpu_info_widget)
        self.cpu_info_label.setObjectName(u"cpu_info_label")
        self.cpu_info_label.setMaximumSize(QSize(16777215, 40))
        self.cpu_info_label.setStyleSheet(u"QLabel {\n"
"	font: 350 12pt;\n"
"}")

        self.system_status_layout_2.addWidget(self.cpu_info_label)

        self.cpu_info_box_widget = QWidget(self.cpu_info_widget)
        self.cpu_info_box_widget.setObjectName(u"cpu_info_box_widget")
        self.cpu_info_box_widget.setMaximumSize(QSize(500, 300))
        self.cpu_info_box_widget.setStyleSheet(u"#cpu_info_box_widget {\n"
"    background-color: #161b22;\n"
"	border: 1px solid #30363d;\n"
"	margin-left: 5px;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"#cpu_info_box_widget QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(self.cpu_info_box_widget)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 0, 0, 0)
        self.cpu_info_box_layout = QHBoxLayout()
        self.cpu_info_box_layout.setObjectName(u"cpu_info_box_layout")
        self.cpu_info_rows_widget = QWidget(self.cpu_info_box_widget)
        self.cpu_info_rows_widget.setObjectName(u"cpu_info_rows_widget")
        self.cpu_info_rows_widget.setStyleSheet(u"QLabel {\n"
"	font: 200 12pt;\n"
"	margin-left: 20px;\n"
"}")
        self.verticalLayout_16 = QVBoxLayout(self.cpu_info_rows_widget)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(10, 0, 0, 0)
        self.model_row_label = QLabel(self.cpu_info_rows_widget)
        self.model_row_label.setObjectName(u"model_row_label")
        self.model_row_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.model_row_label.setMargin(0)

        self.verticalLayout_16.addWidget(self.model_row_label)

        self.cores_row_label = QLabel(self.cpu_info_rows_widget)
        self.cores_row_label.setObjectName(u"cores_row_label")
        self.cores_row_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.cores_row_label.setMargin(0)

        self.verticalLayout_16.addWidget(self.cores_row_label)

        self.threads_row_label = QLabel(self.cpu_info_rows_widget)
        self.threads_row_label.setObjectName(u"threads_row_label")
        self.threads_row_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.threads_row_label.setMargin(0)

        self.verticalLayout_16.addWidget(self.threads_row_label)

        self.frequency_row_label = QLabel(self.cpu_info_rows_widget)
        self.frequency_row_label.setObjectName(u"frequency_row_label")
        self.frequency_row_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.frequency_row_label.setMargin(0)

        self.verticalLayout_16.addWidget(self.frequency_row_label)

        self.architecture_row_label = QLabel(self.cpu_info_rows_widget)
        self.architecture_row_label.setObjectName(u"architecture_row_label")
        self.architecture_row_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.architecture_row_label.setMargin(0)

        self.verticalLayout_16.addWidget(self.architecture_row_label)


        self.cpu_info_box_layout.addWidget(self.cpu_info_rows_widget)

        self.cpu_info_values_widget = QWidget(self.cpu_info_box_widget)
        self.cpu_info_values_widget.setObjectName(u"cpu_info_values_widget")
        self.cpu_info_values_widget.setStyleSheet(u"QLabel {\n"
"	font: 450 12pt;\n"
"}")
        self.verticalLayout_24 = QVBoxLayout(self.cpu_info_values_widget)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.model_value_label = QLabel(self.cpu_info_values_widget)
        self.model_value_label.setObjectName(u"model_value_label")

        self.verticalLayout_24.addWidget(self.model_value_label)

        self.cores_value_label = QLabel(self.cpu_info_values_widget)
        self.cores_value_label.setObjectName(u"cores_value_label")

        self.verticalLayout_24.addWidget(self.cores_value_label)

        self.threads_value_label = QLabel(self.cpu_info_values_widget)
        self.threads_value_label.setObjectName(u"threads_value_label")

        self.verticalLayout_24.addWidget(self.threads_value_label)

        self.frequency_value_label = QLabel(self.cpu_info_values_widget)
        self.frequency_value_label.setObjectName(u"frequency_value_label")

        self.verticalLayout_24.addWidget(self.frequency_value_label)

        self.architecture_value_label = QLabel(self.cpu_info_values_widget)
        self.architecture_value_label.setObjectName(u"architecture_value_label")

        self.verticalLayout_24.addWidget(self.architecture_value_label)


        self.cpu_info_box_layout.addWidget(self.cpu_info_values_widget)


        self.horizontalLayout_5.addLayout(self.cpu_info_box_layout)


        self.system_status_layout_2.addWidget(self.cpu_info_box_widget)


        self.verticalLayout_27.addWidget(self.cpu_info_widget)

        self.memory_info_widget = QWidget(self.scrollAreaWidgetContents)
        self.memory_info_widget.setObjectName(u"memory_info_widget")
        self.memory_info_widget.setMinimumSize(QSize(0, 180))
        self.memory_info_widget.setMaximumSize(QSize(16777215, 350))
        self.system_status_layout_3 = QVBoxLayout(self.memory_info_widget)
        self.system_status_layout_3.setObjectName(u"system_status_layout_3")
        self.system_status_layout_3.setContentsMargins(5, 0, 0, 0)
        self.memory_info_label = QLabel(self.memory_info_widget)
        self.memory_info_label.setObjectName(u"memory_info_label")
        self.memory_info_label.setMaximumSize(QSize(16777215, 40))
        self.memory_info_label.setStyleSheet(u"QLabel {\n"
"	font: 350 12pt;\n"
"}")

        self.system_status_layout_3.addWidget(self.memory_info_label)

        self.memory_info_box_widget = QWidget(self.memory_info_widget)
        self.memory_info_box_widget.setObjectName(u"memory_info_box_widget")
        self.memory_info_box_widget.setMaximumSize(QSize(500, 100))
        self.memory_info_box_widget.setStyleSheet(u"#cpu_info_box_widget {\n"
"    background-color: #161b22;\n"
"	border: 1px solid #30363d;\n"
"	margin-left: 5px;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"#cpu_info_box_widget QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_7 = QHBoxLayout(self.memory_info_box_widget)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 0, 0, 0)
        self.memory_info_box_layout = QHBoxLayout()
        self.memory_info_box_layout.setObjectName(u"memory_info_box_layout")
        self.cpu_info_rows_widget_2 = QWidget(self.memory_info_box_widget)
        self.cpu_info_rows_widget_2.setObjectName(u"cpu_info_rows_widget_2")
        self.cpu_info_rows_widget_2.setStyleSheet(u"QLabel {\n"
"	font: 200 12pt;\n"
"	margin-left: 20px;\n"
"}")
        self.verticalLayout_28 = QVBoxLayout(self.cpu_info_rows_widget_2)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(10, 0, 0, 0)
        self.model_row_label_2 = QLabel(self.cpu_info_rows_widget_2)
        self.model_row_label_2.setObjectName(u"model_row_label_2")
        self.model_row_label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.model_row_label_2.setMargin(0)

        self.verticalLayout_28.addWidget(self.model_row_label_2)

        self.cores_row_label_2 = QLabel(self.cpu_info_rows_widget_2)
        self.cores_row_label_2.setObjectName(u"cores_row_label_2")
        self.cores_row_label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.cores_row_label_2.setMargin(0)

        self.verticalLayout_28.addWidget(self.cores_row_label_2)

        self.threads_row_label_2 = QLabel(self.cpu_info_rows_widget_2)
        self.threads_row_label_2.setObjectName(u"threads_row_label_2")
        self.threads_row_label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.threads_row_label_2.setMargin(0)

        self.verticalLayout_28.addWidget(self.threads_row_label_2)


        self.memory_info_box_layout.addWidget(self.cpu_info_rows_widget_2)

        self.cpu_info_values_widget_2 = QWidget(self.memory_info_box_widget)
        self.cpu_info_values_widget_2.setObjectName(u"cpu_info_values_widget_2")
        self.cpu_info_values_widget_2.setStyleSheet(u"QLabel {\n"
"	font: 450 12pt;\n"
"}")
        self.verticalLayout_29 = QVBoxLayout(self.cpu_info_values_widget_2)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.model_value_label_2 = QLabel(self.cpu_info_values_widget_2)
        self.model_value_label_2.setObjectName(u"model_value_label_2")

        self.verticalLayout_29.addWidget(self.model_value_label_2)

        self.cores_value_label_2 = QLabel(self.cpu_info_values_widget_2)
        self.cores_value_label_2.setObjectName(u"cores_value_label_2")

        self.verticalLayout_29.addWidget(self.cores_value_label_2)

        self.threads_value_label_2 = QLabel(self.cpu_info_values_widget_2)
        self.threads_value_label_2.setObjectName(u"threads_value_label_2")

        self.verticalLayout_29.addWidget(self.threads_value_label_2)


        self.memory_info_box_layout.addWidget(self.cpu_info_values_widget_2)


        self.horizontalLayout_7.addLayout(self.memory_info_box_layout)


        self.system_status_layout_3.addWidget(self.memory_info_box_widget)


        self.verticalLayout_27.addWidget(self.memory_info_widget)

        self.cpu_info_widget_3 = QWidget(self.scrollAreaWidgetContents)
        self.cpu_info_widget_3.setObjectName(u"cpu_info_widget_3")
        self.cpu_info_widget_3.setMinimumSize(QSize(0, 150))
        self.cpu_info_widget_3.setMaximumSize(QSize(16777215, 350))
        self.system_status_layout_4 = QVBoxLayout(self.cpu_info_widget_3)
        self.system_status_layout_4.setObjectName(u"system_status_layout_4")
        self.system_status_layout_4.setContentsMargins(5, 0, 0, 0)
        self.cpu_info_label_5 = QLabel(self.cpu_info_widget_3)
        self.cpu_info_label_5.setObjectName(u"cpu_info_label_5")
        self.cpu_info_label_5.setMaximumSize(QSize(16777215, 40))
        self.cpu_info_label_5.setStyleSheet(u"QLabel {\n"
"	font: 350 12pt;\n"
"}")

        self.system_status_layout_4.addWidget(self.cpu_info_label_5)

        self.cpu_info_box_widget_3 = QWidget(self.cpu_info_widget_3)
        self.cpu_info_box_widget_3.setObjectName(u"cpu_info_box_widget_3")
        self.cpu_info_box_widget_3.setMaximumSize(QSize(500, 100))
        self.cpu_info_box_widget_3.setStyleSheet(u"#cpu_info_box_widget {\n"
"    background-color: #161b22;\n"
"	border: 1px solid #30363d;\n"
"	margin-left: 5px;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"#cpu_info_box_widget QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_8 = QHBoxLayout(self.cpu_info_box_widget_3)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(5, 0, 0, 0)
        self.cpu_info_box_layout_3 = QHBoxLayout()
        self.cpu_info_box_layout_3.setObjectName(u"cpu_info_box_layout_3")
        self.cpu_info_rows_widget_3 = QWidget(self.cpu_info_box_widget_3)
        self.cpu_info_rows_widget_3.setObjectName(u"cpu_info_rows_widget_3")
        self.cpu_info_rows_widget_3.setStyleSheet(u"QLabel {\n"
"	font: 200 12pt;\n"
"	margin-left: 20px;\n"
"}")
        self.verticalLayout_30 = QVBoxLayout(self.cpu_info_rows_widget_3)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(10, 0, 0, 0)
        self.model_row_label_3 = QLabel(self.cpu_info_rows_widget_3)
        self.model_row_label_3.setObjectName(u"model_row_label_3")
        self.model_row_label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.model_row_label_3.setMargin(0)

        self.verticalLayout_30.addWidget(self.model_row_label_3)

        self.cores_row_label_5 = QLabel(self.cpu_info_rows_widget_3)
        self.cores_row_label_5.setObjectName(u"cores_row_label_5")
        self.cores_row_label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.cores_row_label_5.setMargin(0)

        self.verticalLayout_30.addWidget(self.cores_row_label_5)

        self.threads_row_label_3 = QLabel(self.cpu_info_rows_widget_3)
        self.threads_row_label_3.setObjectName(u"threads_row_label_3")
        self.threads_row_label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.threads_row_label_3.setMargin(0)

        self.verticalLayout_30.addWidget(self.threads_row_label_3)


        self.cpu_info_box_layout_3.addWidget(self.cpu_info_rows_widget_3)

        self.cpu_info_values_widget_3 = QWidget(self.cpu_info_box_widget_3)
        self.cpu_info_values_widget_3.setObjectName(u"cpu_info_values_widget_3")
        self.cpu_info_values_widget_3.setStyleSheet(u"QLabel {\n"
"	font: 450 12pt;\n"
"}")
        self.verticalLayout_31 = QVBoxLayout(self.cpu_info_values_widget_3)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.model_value_label_3 = QLabel(self.cpu_info_values_widget_3)
        self.model_value_label_3.setObjectName(u"model_value_label_3")

        self.verticalLayout_31.addWidget(self.model_value_label_3)

        self.cores_value_label_5 = QLabel(self.cpu_info_values_widget_3)
        self.cores_value_label_5.setObjectName(u"cores_value_label_5")

        self.verticalLayout_31.addWidget(self.cores_value_label_5)

        self.threads_value_label_3 = QLabel(self.cpu_info_values_widget_3)
        self.threads_value_label_3.setObjectName(u"threads_value_label_3")

        self.verticalLayout_31.addWidget(self.threads_value_label_3)


        self.cpu_info_box_layout_3.addWidget(self.cpu_info_values_widget_3)


        self.horizontalLayout_8.addLayout(self.cpu_info_box_layout_3)


        self.system_status_layout_4.addWidget(self.cpu_info_box_widget_3)


        self.verticalLayout_27.addWidget(self.cpu_info_widget_3)

        self.cpu_info_widget_4 = QWidget(self.scrollAreaWidgetContents)
        self.cpu_info_widget_4.setObjectName(u"cpu_info_widget_4")
        self.cpu_info_widget_4.setMinimumSize(QSize(0, 180))
        self.cpu_info_widget_4.setMaximumSize(QSize(16777215, 350))
        self.system_status_layout_9 = QVBoxLayout(self.cpu_info_widget_4)
        self.system_status_layout_9.setObjectName(u"system_status_layout_9")
        self.system_status_layout_9.setContentsMargins(5, 0, 0, 0)
        self.cpu_info_label_6 = QLabel(self.cpu_info_widget_4)
        self.cpu_info_label_6.setObjectName(u"cpu_info_label_6")
        self.cpu_info_label_6.setMaximumSize(QSize(16777215, 40))
        self.cpu_info_label_6.setStyleSheet(u"QLabel {\n"
"	font: 350 12pt;\n"
"}")

        self.system_status_layout_9.addWidget(self.cpu_info_label_6)

        self.cpu_info_box_widget_8 = QWidget(self.cpu_info_widget_4)
        self.cpu_info_box_widget_8.setObjectName(u"cpu_info_box_widget_8")
        self.cpu_info_box_widget_8.setMaximumSize(QSize(500, 150))
        self.cpu_info_box_widget_8.setStyleSheet(u"#cpu_info_box_widget {\n"
"    background-color: #161b22;\n"
"	border: 1px solid #30363d;\n"
"	margin-left: 5px;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"#cpu_info_box_widget QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_13 = QHBoxLayout(self.cpu_info_box_widget_8)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(5, 0, 0, 0)
        self.cpu_info_box_layout_8 = QHBoxLayout()
        self.cpu_info_box_layout_8.setObjectName(u"cpu_info_box_layout_8")
        self.cpu_info_rows_widget_8 = QWidget(self.cpu_info_box_widget_8)
        self.cpu_info_rows_widget_8.setObjectName(u"cpu_info_rows_widget_8")
        self.cpu_info_rows_widget_8.setStyleSheet(u"QLabel {\n"
"	font: 200 12pt;\n"
"	margin-left: 20px;\n"
"}")
        self.verticalLayout_41 = QVBoxLayout(self.cpu_info_rows_widget_8)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(10, 0, 0, 0)
        self.model_row_label_8 = QLabel(self.cpu_info_rows_widget_8)
        self.model_row_label_8.setObjectName(u"model_row_label_8")
        self.model_row_label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.model_row_label_8.setMargin(0)

        self.verticalLayout_41.addWidget(self.model_row_label_8)

        self.cores_row_label_6 = QLabel(self.cpu_info_rows_widget_8)
        self.cores_row_label_6.setObjectName(u"cores_row_label_6")
        self.cores_row_label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.cores_row_label_6.setMargin(0)

        self.verticalLayout_41.addWidget(self.cores_row_label_6)

        self.threads_row_label_8 = QLabel(self.cpu_info_rows_widget_8)
        self.threads_row_label_8.setObjectName(u"threads_row_label_8")
        self.threads_row_label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.threads_row_label_8.setMargin(0)

        self.verticalLayout_41.addWidget(self.threads_row_label_8)

        self.architecture_row_label_8 = QLabel(self.cpu_info_rows_widget_8)
        self.architecture_row_label_8.setObjectName(u"architecture_row_label_8")
        self.architecture_row_label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.architecture_row_label_8.setMargin(0)

        self.verticalLayout_41.addWidget(self.architecture_row_label_8)


        self.cpu_info_box_layout_8.addWidget(self.cpu_info_rows_widget_8)

        self.cpu_info_values_widget_8 = QWidget(self.cpu_info_box_widget_8)
        self.cpu_info_values_widget_8.setObjectName(u"cpu_info_values_widget_8")
        self.cpu_info_values_widget_8.setStyleSheet(u"QLabel {\n"
"	font: 450 12pt;\n"
"}")
        self.verticalLayout_42 = QVBoxLayout(self.cpu_info_values_widget_8)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.model_value_label_8 = QLabel(self.cpu_info_values_widget_8)
        self.model_value_label_8.setObjectName(u"model_value_label_8")

        self.verticalLayout_42.addWidget(self.model_value_label_8)

        self.cores_value_label_6 = QLabel(self.cpu_info_values_widget_8)
        self.cores_value_label_6.setObjectName(u"cores_value_label_6")

        self.verticalLayout_42.addWidget(self.cores_value_label_6)

        self.threads_value_label_8 = QLabel(self.cpu_info_values_widget_8)
        self.threads_value_label_8.setObjectName(u"threads_value_label_8")

        self.verticalLayout_42.addWidget(self.threads_value_label_8)

        self.architecture_value_label_8 = QLabel(self.cpu_info_values_widget_8)
        self.architecture_value_label_8.setObjectName(u"architecture_value_label_8")

        self.verticalLayout_42.addWidget(self.architecture_value_label_8)


        self.cpu_info_box_layout_8.addWidget(self.cpu_info_values_widget_8)


        self.horizontalLayout_13.addLayout(self.cpu_info_box_layout_8)


        self.system_status_layout_9.addWidget(self.cpu_info_box_widget_8)


        self.verticalLayout_27.addWidget(self.cpu_info_widget_4)

        self.cpu_info_widget_7 = QWidget(self.scrollAreaWidgetContents)
        self.cpu_info_widget_7.setObjectName(u"cpu_info_widget_7")
        self.cpu_info_widget_7.setMinimumSize(QSize(0, 150))
        self.cpu_info_widget_7.setMaximumSize(QSize(16777215, 350))
        self.system_status_layout_11 = QVBoxLayout(self.cpu_info_widget_7)
        self.system_status_layout_11.setObjectName(u"system_status_layout_11")
        self.system_status_layout_11.setContentsMargins(5, 0, 0, 0)
        self.cpu_info_label_8 = QLabel(self.cpu_info_widget_7)
        self.cpu_info_label_8.setObjectName(u"cpu_info_label_8")
        self.cpu_info_label_8.setMaximumSize(QSize(16777215, 40))
        self.cpu_info_label_8.setStyleSheet(u"QLabel {\n"
"	font: 350 12pt;\n"
"}")

        self.system_status_layout_11.addWidget(self.cpu_info_label_8)

        self.cpu_info_box_widget_10 = QWidget(self.cpu_info_widget_7)
        self.cpu_info_box_widget_10.setObjectName(u"cpu_info_box_widget_10")
        self.cpu_info_box_widget_10.setMaximumSize(QSize(500, 100))
        self.cpu_info_box_widget_10.setStyleSheet(u"#cpu_info_box_widget {\n"
"    background-color: #161b22;\n"
"	border: 1px solid #30363d;\n"
"	margin-left: 5px;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"#cpu_info_box_widget QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_15 = QHBoxLayout(self.cpu_info_box_widget_10)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(5, 0, 0, 0)
        self.cpu_info_box_layout_10 = QHBoxLayout()
        self.cpu_info_box_layout_10.setObjectName(u"cpu_info_box_layout_10")
        self.cpu_info_rows_widget_10 = QWidget(self.cpu_info_box_widget_10)
        self.cpu_info_rows_widget_10.setObjectName(u"cpu_info_rows_widget_10")
        self.cpu_info_rows_widget_10.setStyleSheet(u"QLabel {\n"
"	font: 200 12pt;\n"
"	margin-left: 20px;\n"
"}")
        self.verticalLayout_45 = QVBoxLayout(self.cpu_info_rows_widget_10)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(10, 0, 0, 0)
        self.model_row_label_10 = QLabel(self.cpu_info_rows_widget_10)
        self.model_row_label_10.setObjectName(u"model_row_label_10")
        self.model_row_label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.model_row_label_10.setMargin(0)

        self.verticalLayout_45.addWidget(self.model_row_label_10)

        self.cores_row_label_8 = QLabel(self.cpu_info_rows_widget_10)
        self.cores_row_label_8.setObjectName(u"cores_row_label_8")
        self.cores_row_label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.cores_row_label_8.setMargin(0)

        self.verticalLayout_45.addWidget(self.cores_row_label_8)

        self.threads_row_label_10 = QLabel(self.cpu_info_rows_widget_10)
        self.threads_row_label_10.setObjectName(u"threads_row_label_10")
        self.threads_row_label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.threads_row_label_10.setMargin(0)

        self.verticalLayout_45.addWidget(self.threads_row_label_10)


        self.cpu_info_box_layout_10.addWidget(self.cpu_info_rows_widget_10)

        self.cpu_info_values_widget_10 = QWidget(self.cpu_info_box_widget_10)
        self.cpu_info_values_widget_10.setObjectName(u"cpu_info_values_widget_10")
        self.cpu_info_values_widget_10.setStyleSheet(u"QLabel {\n"
"	font: 450 12pt;\n"
"}")
        self.verticalLayout_46 = QVBoxLayout(self.cpu_info_values_widget_10)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.model_value_label_10 = QLabel(self.cpu_info_values_widget_10)
        self.model_value_label_10.setObjectName(u"model_value_label_10")

        self.verticalLayout_46.addWidget(self.model_value_label_10)

        self.cores_value_label_8 = QLabel(self.cpu_info_values_widget_10)
        self.cores_value_label_8.setObjectName(u"cores_value_label_8")

        self.verticalLayout_46.addWidget(self.cores_value_label_8)

        self.threads_value_label_10 = QLabel(self.cpu_info_values_widget_10)
        self.threads_value_label_10.setObjectName(u"threads_value_label_10")

        self.verticalLayout_46.addWidget(self.threads_value_label_10)


        self.cpu_info_box_layout_10.addWidget(self.cpu_info_values_widget_10)


        self.horizontalLayout_15.addLayout(self.cpu_info_box_layout_10)


        self.system_status_layout_11.addWidget(self.cpu_info_box_widget_10)


        self.verticalLayout_27.addWidget(self.cpu_info_widget_7)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_6.addWidget(self.scrollArea)

        self.agent_detail_stacked_content.addWidget(self.page)

        self.verticalLayout.addWidget(self.agent_detail_stacked_content)


        self.verticalLayout_3.addWidget(self.agent_detail_content)

        self.content_stack.addWidget(self.agent_detail_page)
        MainWindow.setCentralWidget(self.central_content)

        self.retranslateUi(MainWindow)

        self.content_stack.setCurrentIndex(2)
        self.agent_detail_stacked_content.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"NexoraControl", None))
        self.nexora_logo.setText(QCoreApplication.translate("MainWindow", u"NEXORA", None))
        self.dashboard_button.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.agents_button.setText(QCoreApplication.translate("MainWindow", u"Agents", None))
        self.commands_button.setText(QCoreApplication.translate("MainWindow", u"Commands", None))
        self.metrics_button.setText(QCoreApplication.translate("MainWindow", u"Metrics", None))
        self.logs_button.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.about_button.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.dashboard_label.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.agent_label.setText(QCoreApplication.translate("MainWindow", u"Agents", None))
        self.agents_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.online_label.setText(QCoreApplication.translate("MainWindow", u"Online", None))
        self.online_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.offline_label.setText(QCoreApplication.translate("MainWindow", u"Offline", None))
        self.offline_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.agents_label.setText(QCoreApplication.translate("MainWindow", u"Agents", None))
        ___qtablewidgetitem = self.agents_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        ___qtablewidgetitem1 = self.agents_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        ___qtablewidgetitem2 = self.agents_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Hostname", None))
        ___qtablewidgetitem3 = self.agents_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        ___qtablewidgetitem4 = self.agents_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"RAM", None))
        ___qtablewidgetitem5 = self.agents_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Seen", None))
        self.refresh_table_button.setText(QCoreApplication.translate("MainWindow", u"[ Refresh ]", None))
        self.agents_headline_label.setText(QCoreApplication.translate("MainWindow", u"Agents", None))
        self.page_description_label.setText(QCoreApplication.translate("MainWindow", u"Manage connected machines", None))
        self.search_input_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
        self.refresh_agents_button.setText(QCoreApplication.translate("MainWindow", u"[ Refresh ]", None))
        self.back_to_agents_button.setText(QCoreApplication.translate("MainWindow", u"[ \u2190 Back to Agents ]", None))
        self.detail_top_agent_name_label.setText(QCoreApplication.translate("MainWindow", u"VPS Production ", None))
        self.detail_top_agent_status_label.setText(QCoreApplication.translate("MainWindow", u"\u25cf ON", None))
        self.overview_nav_button.setText(QCoreApplication.translate("MainWindow", u"[ Overview ]", None))
        self.perfomance_nav_button.setText(QCoreApplication.translate("MainWindow", u"[ Performance ]", None))
        self.hardware_nav_button.setText(QCoreApplication.translate("MainWindow", u"[ Hardware ]", None))
        self.storage_nav_button.setText(QCoreApplication.translate("MainWindow", u"[ Storage ]", None))
        self.network_nav_button.setText(QCoreApplication.translate("MainWindow", u"[ Network ]", None))
        self.commands_nav_button.setText(QCoreApplication.translate("MainWindow", u"[ Commands ]", None))
        self.overview_label.setText(QCoreApplication.translate("MainWindow", u"OVERVIEW ", None))
        self.cpu_label.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_load_label.setText(QCoreApplication.translate("MainWindow", u"23.4% ", None))
        self.ram_label.setText(QCoreApplication.translate("MainWindow", u"RAM", None))
        self.ram_load_label.setText(QCoreApplication.translate("MainWindow", u"41.2%", None))
        self.disk_label.setText(QCoreApplication.translate("MainWindow", u"DISK", None))
        self.disk_load_label.setText(QCoreApplication.translate("MainWindow", u"58.1%", None))
        self.uptime_label.setText(QCoreApplication.translate("MainWindow", u"UPTIME", None))
        self.up_time_label.setText(QCoreApplication.translate("MainWindow", u"3d 14h", None))
        self.system_status_label.setText(QCoreApplication.translate("MainWindow", u"SYSTEM STATUS", None))
        self.agent_row_label.setText(QCoreApplication.translate("MainWindow", u"Agent", None))
        self.last_seen_row_label.setText(QCoreApplication.translate("MainWindow", u"Last seen", None))
        self.version_row_label.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.hostname_row_label.setText(QCoreApplication.translate("MainWindow", u"Hostname", None))
        self.os_name_row_label.setText(QCoreApplication.translate("MainWindow", u"OS", None))
        self.agent_status_value_label.setText(QCoreApplication.translate("MainWindow", u"ONLINE", None))
        self.last_seen_value_label.setText(QCoreApplication.translate("MainWindow", u"2 sec ago", None))
        self.version_value_label.setText(QCoreApplication.translate("MainWindow", u"0.1.0", None))
        self.hostname_value_label.setText(QCoreApplication.translate("MainWindow", u"prod-01", None))
        self.os_name_value_label.setText(QCoreApplication.translate("MainWindow", u"Ubuntu 24.04", None))
        self.quick_actions_label.setText(QCoreApplication.translate("MainWindow", u"QUICK ACTIONS ", None))
        self.restart_all_docker_cont_quick_button.setText(QCoreApplication.translate("MainWindow", u"[ Restart All Docker Containers ]", None))
        self.stop_all_docker_cont_quick_button.setText(QCoreApplication.translate("MainWindow", u"[ Stop All Docker Containers ]", None))
        self.docker_ps_quick_button.setText(QCoreApplication.translate("MainWindow", u"[ Docker PS ]", None))
        self.reboot_quick_button.setText(QCoreApplication.translate("MainWindow", u"[ Reboot ] ", None))
        self.recent_commands_label.setText(QCoreApplication.translate("MainWindow", u"RECENT COMMANDS", None))
        self.perfomance_label.setText(QCoreApplication.translate("MainWindow", u"PERFOMANCE", None))
        self.compute_button.setText(QCoreApplication.translate("MainWindow", u"[ COMPUTE ]", None))
        self.storage_button.setText(QCoreApplication.translate("MainWindow", u"[ STORAGE ]", None))
        self.thermals_button.setText(QCoreApplication.translate("MainWindow", u"[ THERMALS ]", None))
        self.network_button.setText(QCoreApplication.translate("MainWindow", u"[ NETWORK ]", None))
        self.hardware_label.setText(QCoreApplication.translate("MainWindow", u"HARDWARE", None))
        self.cpu_info_label.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.model_row_label.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.cores_row_label.setText(QCoreApplication.translate("MainWindow", u"Cores", None))
        self.threads_row_label.setText(QCoreApplication.translate("MainWindow", u"Threads", None))
        self.frequency_row_label.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.architecture_row_label.setText(QCoreApplication.translate("MainWindow", u"Architecture", None))
        self.model_value_label.setText(QCoreApplication.translate("MainWindow", u"AMD EPYC 7763", None))
        self.cores_value_label.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.threads_value_label.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.frequency_value_label.setText(QCoreApplication.translate("MainWindow", u"2.45 GHz", None))
        self.architecture_value_label.setText(QCoreApplication.translate("MainWindow", u"x86_64", None))
        self.memory_info_label.setText(QCoreApplication.translate("MainWindow", u"MEMORY", None))
        self.model_row_label_2.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.cores_row_label_2.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.threads_row_label_2.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.model_value_label_2.setText(QCoreApplication.translate("MainWindow", u"16 GB", None))
        self.cores_value_label_2.setText(QCoreApplication.translate("MainWindow", u"DDR4 ", None))
        self.threads_value_label_2.setText(QCoreApplication.translate("MainWindow", u"3200 MHz", None))
        self.cpu_info_label_5.setText(QCoreApplication.translate("MainWindow", u"GPU", None))
        self.model_row_label_3.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.cores_row_label_5.setText(QCoreApplication.translate("MainWindow", u"VRAM", None))
        self.threads_row_label_3.setText(QCoreApplication.translate("MainWindow", u"Memory Type", None))
        self.model_value_label_3.setText(QCoreApplication.translate("MainWindow", u"NVIDIA RTX 3050", None))
        self.cores_value_label_5.setText(QCoreApplication.translate("MainWindow", u"4 GB", None))
        self.threads_value_label_3.setText(QCoreApplication.translate("MainWindow", u"GDDR6X", None))
        self.cpu_info_label_6.setText(QCoreApplication.translate("MainWindow", u"MOTHERBOARD", None))
        self.model_row_label_8.setText(QCoreApplication.translate("MainWindow", u"Vendor", None))
        self.cores_row_label_6.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.threads_row_label_8.setText(QCoreApplication.translate("MainWindow", u"Serial", None))
        self.architecture_row_label_8.setText(QCoreApplication.translate("MainWindow", u"Architecture", None))
        self.model_value_label_8.setText(QCoreApplication.translate("MainWindow", u"ASUS", None))
        self.cores_value_label_6.setText(QCoreApplication.translate("MainWindow", u"PRIME B550", None))
        self.threads_value_label_8.setText(QCoreApplication.translate("MainWindow", u"********", None))
        self.architecture_value_label_8.setText(QCoreApplication.translate("MainWindow", u"x86_64", None))
        self.cpu_info_label_8.setText(QCoreApplication.translate("MainWindow", u"BIOS", None))
        self.model_row_label_10.setText(QCoreApplication.translate("MainWindow", u"Vendor", None))
        self.cores_row_label_8.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.threads_row_label_10.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.model_value_label_10.setText(QCoreApplication.translate("MainWindow", u"AMD EPYC 7763", None))
        self.cores_value_label_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.threads_value_label_10.setText(QCoreApplication.translate("MainWindow", u"2026-01-15", None))
    # retranslateUi

