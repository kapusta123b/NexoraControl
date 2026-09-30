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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1187, 803)
        icon = QIcon()
        iconThemeName = u"camera-photo"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"../.designer/.designer/.designer/.designer/.designer/.designer/.designer/.designer/.designer/.designer/.designer/.designer/.designer/.designer/.designer/backup", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
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
"QTableWidget {\n"
"    background-color: #161b22;\n"
"    color: #e6edf3;\n"
"    border: 1px solid #30363d;\n"
"    gridline-color: #21262d;\n"
"    border-radius: 6px;\n"
"    outline: none;\n"
"}\n"
"\n"
"\n"
"QTableWidget::item {\n"
"    padding: 8px 12px;\n"
"    border-bottom: 1px solid #21262d;\n"
"}\n"
"\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #1f242c;\n"
"}\n"
"\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #1f6feb;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #11151c;\n"
" "
                        "   color: #58a6ff;\n"
"    padding: 10px 12px;\n"
"    border: none;\n"
"    border-bottom: 2px solid #30363d;\n"
"    font-weight: bold;\n"
"    font-size: 11px;\n"
"    text-transform: uppercase;\n"
"}\n"
"\n"
"\n"
"QTableWidget QProgressBar {\n"
"    border: 1px solid #1E2B3E;\n"
"    border-radius: 0px;\n"
"    background-color: #090C12;\n"
"    text-align: center;\n"
"    font-size: 11px;\n"
"    font-weight: bold;\n"
"    min-height: 18px; \n"
"    max-height: 22px;\n"
"}\n"
"\n"
"QTableWidget QProgressBar[load_level=\"low\"] {\n"
"    color: #8da2c0;\n"
"}\n"
"\n"
"QTableWidget QProgressBar[load_level=\"medium\"] {\n"
"    color: #a5b4fc;\n"
"}\n"
"\n"
"QTableWidget QProgressBar[load_level=\"high\"] {\n"
"    color: #e2a8b3;\n"
"}\n"
"\n"
"QTableWidget QProgressBar::chunk {\n"
"    border-radius: 0px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QTableWidget QProgressBar[load_level=\"low\"]::chunk {\n"
"    background-color: rgb(11, 22, 35); \n"
"}\n"
"\n"
"QTableWidget QProgressBar[load_level=\"medium\"]::chunk"
                        " {\n"
"    background-color: rgb(24, 22, 46); \n"
"}\n"
"\n"
"QTableWidget QProgressBar[load_level=\"high\"]::chunk {\n"
"    background-color: rgb(46, 18, 25); \n"
"}\n"
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
"\n"
"QFrame[frameShape=\"4\"] {\n"
"    background-color: #1E2633;\n"
"    border: none;\n"
"    max-height: 1px;\n"
"    min-height: 1px;\n"
"}\n"
"\n"
"\n"
"QFrame[frameShape=\"5\"] {\n"
"    background-color: #1E2633;\n"
"    border: none;\n"
"    max-width: 1px;\n"
"    min-width: 1px;\n"
"}\n"
"")
        self.central_content_layout = QHBoxLayout(self.central_content)
        self.central_content_layout.setSpacing(0)
        self.central_content_layout.setObjectName(u"central_content_layout")
        self.central_content_layout.setContentsMargins(0, 0, 0, 0)
        self.left_panel = QWidget(self.central_content)
        self.left_panel.setObjectName(u"left_panel")
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
"\n"
"QFrame[frameShape=\"4\"] {\n"
"    background-color: #1E2633;\n"
"    border: none;\n"
"    max-height: 1px;\n"
"    min-height: 1px;\n"
"}\n"
"\n"
"\n"
"QFrame[frameShape=\"5\"] {\n"
"    background-color: #1E2633;\n"
"    border: none;\n"
"    max-width: 1px;\n"
"    min-width: 1px;\n"
"}")
        self.left_panel_layout = QVBoxLayout(self.left_panel)
        self.left_panel_layout.setObjectName(u"left_panel_layout")
        self.nexora_logo = QLabel(self.left_panel)
        self.nexora_logo.setObjectName(u"nexora_logo")
        self.nexora_logo.setStyleSheet(u"QLabel {\n"
"    color: #58a6ff;\n"
"    font: 800 25pt;\n"
"    letter-spacing: 2px;\n"
" 	margin-left: 2px;\n"
"}")
        self.nexora_logo.setWordWrap(True)

        self.left_panel_layout.addWidget(self.nexora_logo)

        self.dashboard_button = QPushButton(self.left_panel)
        self.dashboard_button.setObjectName(u"dashboard_button")
        self.dashboard_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dashboard_button.setCheckable(True)

        self.left_panel_layout.addWidget(self.dashboard_button)

        self.agents_button = QPushButton(self.left_panel)
        self.agents_button.setObjectName(u"agents_button")
        self.agents_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.agents_button.setCheckable(True)

        self.left_panel_layout.addWidget(self.agents_button)

        self.commands_button = QPushButton(self.left_panel)
        self.commands_button.setObjectName(u"commands_button")
        self.commands_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.commands_button.setCheckable(True)

        self.left_panel_layout.addWidget(self.commands_button)

        self.logs_button = QPushButton(self.left_panel)
        self.logs_button.setObjectName(u"logs_button")
        self.logs_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.logs_button.setCheckable(True)

        self.left_panel_layout.addWidget(self.logs_button)

        self.line = QFrame(self.left_panel)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.left_panel_layout.addWidget(self.line)

        self.settings_button = QPushButton(self.left_panel)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.settings_button.setCheckable(True)

        self.left_panel_layout.addWidget(self.settings_button)

        self.about_button = QPushButton(self.left_panel)
        self.about_button.setObjectName(u"about_button")
        self.about_button.setCursor(QCursor(Qt.CursorShape.WhatsThisCursor))
        self.about_button.setCheckable(True)
        self.about_button.setChecked(False)
        self.about_button.setAutoRepeat(False)

        self.left_panel_layout.addWidget(self.about_button)

        self.bottom_spacer = QSpacerItem(20, 200, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.left_panel_layout.addItem(self.bottom_spacer)


        self.central_content_layout.addWidget(self.left_panel)

        self.content_stack = QStackedWidget(self.central_content)
        self.content_stack.setObjectName(u"content_stack")
        self.content_stack.setMinimumSize(QSize(500, 411))
        self.content_stack.setMaximumSize(QSize(16777215, 16777215))
        self.content_stack.setStyleSheet(u"QWidget {\n"
"\n"
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
        self.dashboard_page_layout = QVBoxLayout(self.dashboard_page)
        self.dashboard_page_layout.setObjectName(u"dashboard_page_layout")
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
"	font: 600 17pt;\n"
"}")

        self.dashboard_layout.addWidget(self.dashboard_label)

        self.dashboard_legend_label = QLabel(self.dashboard_page)
        self.dashboard_legend_label.setObjectName(u"dashboard_legend_label")

        self.dashboard_layout.addWidget(self.dashboard_legend_label)

        self.dashboard_line = QFrame(self.dashboard_page)
        self.dashboard_line.setObjectName(u"dashboard_line")
        self.dashboard_line.setFrameShape(QFrame.Shape.HLine)
        self.dashboard_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.dashboard_layout.addWidget(self.dashboard_line)

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
        self.cards_layout = QHBoxLayout(self.cards)
        self.cards_layout.setSpacing(6)
        self.cards_layout.setObjectName(u"cards_layout")
        self.cards_layout.setContentsMargins(0, 0, 0, 0)
        self.card_agents = QWidget(self.cards)
        self.card_agents.setObjectName(u"card_agents")
        self.card_agents.setMaximumSize(QSize(16777215, 65))
        self.card_agents.setStyleSheet(u"")
        self.card_agents_layout = QVBoxLayout(self.card_agents)
        self.card_agents_layout.setObjectName(u"card_agents_layout")
        self.agent_label = QLabel(self.card_agents)
        self.agent_label.setObjectName(u"agent_label")
        self.agent_label.setAlignment(Qt.AlignCenter)

        self.card_agents_layout.addWidget(self.agent_label)

        self.agents_count = QLabel(self.card_agents)
        self.agents_count.setObjectName(u"agents_count")
        self.agents_count.setAlignment(Qt.AlignCenter)

        self.card_agents_layout.addWidget(self.agents_count)


        self.cards_layout.addWidget(self.card_agents)

        self.card_online = QWidget(self.cards)
        self.card_online.setObjectName(u"card_online")
        self.card_online.setMaximumSize(QSize(16777215, 65))
        self.card_online.setStyleSheet(u"")
        self.card_online_layout = QVBoxLayout(self.card_online)
        self.card_online_layout.setObjectName(u"card_online_layout")
        self.online_label = QLabel(self.card_online)
        self.online_label.setObjectName(u"online_label")
        self.online_label.setAlignment(Qt.AlignCenter)

        self.card_online_layout.addWidget(self.online_label)

        self.online_count = QLabel(self.card_online)
        self.online_count.setObjectName(u"online_count")
        self.online_count.setStyleSheet(u"QLabel { \n"
"	color: #4caf50;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QLabel[agent_status=\"online\"] {\n"
"    color: #4caf50;\n"
"}\n"
"QLabel[agent_status=\"offline\"] {\n"
"    color: #f44336;\n"
"}")
        self.online_count.setAlignment(Qt.AlignCenter)

        self.card_online_layout.addWidget(self.online_count)


        self.cards_layout.addWidget(self.card_online)

        self.card_offline = QWidget(self.cards)
        self.card_offline.setObjectName(u"card_offline")
        self.card_offline.setMaximumSize(QSize(16777215, 65))
        self.card_offline.setStyleSheet(u"")
        self.card_offline_layout = QVBoxLayout(self.card_offline)
        self.card_offline_layout.setObjectName(u"card_offline_layout")
        self.offline_label = QLabel(self.card_offline)
        self.offline_label.setObjectName(u"offline_label")
        self.offline_label.setAlignment(Qt.AlignCenter)

        self.card_offline_layout.addWidget(self.offline_label)

        self.offline_count = QLabel(self.card_offline)
        self.offline_count.setObjectName(u"offline_count")
        self.offline_count.setStyleSheet(u"QLabel {\n"
"    color: #f44336;\n"
"    font-weight: bold;\n"
"}")
        self.offline_count.setAlignment(Qt.AlignCenter)

        self.card_offline_layout.addWidget(self.offline_count)


        self.cards_layout.addWidget(self.card_offline)


        self.dashboard_layout.addWidget(self.cards)

        self.agents_label = QLabel(self.dashboard_page)
        self.agents_label.setObjectName(u"agents_label")
        self.agents_label.setEnabled(True)
        self.agents_label.setMaximumSize(QSize(16777215, 30))
        self.agents_label.setStyleSheet(u"QLabel {\n"
"	font: 600 17pt;\n"
"}")

        self.dashboard_layout.addWidget(self.agents_label)

        self.agents_table_legend_label = QLabel(self.dashboard_page)
        self.agents_table_legend_label.setObjectName(u"agents_table_legend_label")

        self.dashboard_layout.addWidget(self.agents_table_legend_label)

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

        self.refresh_button_bottom_spacer = QSpacerItem(20, 64, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.dashboard_layout.addItem(self.refresh_button_bottom_spacer)


        self.dashboard_page_layout.addLayout(self.dashboard_layout)

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
        self.agents_page_layout = QVBoxLayout(self.agents_page)
        self.agents_page_layout.setSpacing(6)
        self.agents_page_layout.setObjectName(u"agents_page_layout")
        self.agents_main_layout = QVBoxLayout()
        self.agents_main_layout.setSpacing(0)
        self.agents_main_layout.setObjectName(u"agents_main_layout")
        self.agents_headline_label = QLabel(self.agents_page)
        self.agents_headline_label.setObjectName(u"agents_headline_label")
        self.agents_headline_label.setMinimumSize(QSize(0, 0))
        self.agents_headline_label.setMaximumSize(QSize(16777215, 25))
        self.agents_headline_label.setStyleSheet(u"QLabel {\n"
"	font: 600 17pt;\n"
"}")

        self.agents_main_layout.addWidget(self.agents_headline_label)

        self.page_description_label = QLabel(self.agents_page)
        self.page_description_label.setObjectName(u"page_description_label")
        self.page_description_label.setMinimumSize(QSize(0, 30))
        self.page_description_label.setMaximumSize(QSize(16777215, 30))

        self.agents_main_layout.addWidget(self.page_description_label)

        self.page_description_line = QFrame(self.agents_page)
        self.page_description_line.setObjectName(u"page_description_line")
        self.page_description_line.setFrameShape(QFrame.Shape.HLine)
        self.page_description_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.agents_main_layout.addWidget(self.page_description_line)

        self.input_line_top_spacer = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.agents_main_layout.addItem(self.input_line_top_spacer)

        self.help_bar_layout = QHBoxLayout()
        self.help_bar_layout.setSpacing(0)
        self.help_bar_layout.setObjectName(u"help_bar_layout")
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

        self.help_bar_right_spacer = QSpacerItem(17, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.help_bar_layout.addItem(self.help_bar_right_spacer)


        self.agents_main_layout.addLayout(self.help_bar_layout)

        self.agent_list = QScrollArea(self.agents_page)
        self.agent_list.setObjectName(u"agent_list")
        self.agent_list.setMinimumSize(QSize(0, 600))
        self.agent_list.setMaximumSize(QSize(16777215, 16777215))
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
"    width: 8px;\n"
"    margin: 0px 0px 0px 0px;\n"
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
        self.agent_scroll.setGeometry(QRect(0, 0, 988, 600))
        self.agent_scroll.setMaximumSize(QSize(16777215, 1000000))
        self.agent_scroll.setStyleSheet(u"")
        self.agent_scroll_layout = QVBoxLayout(self.agent_scroll)
        self.agent_scroll_layout.setSpacing(12)
        self.agent_scroll_layout.setObjectName(u"agent_scroll_layout")
        self.agent_scroll_layout.setContentsMargins(0, 0, 0, 10)
        self.agent_scroll_spacer = QSpacerItem(20, 19, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.agent_scroll_layout.addItem(self.agent_scroll_spacer)

        self.agent_list.setWidget(self.agent_scroll)

        self.agents_main_layout.addWidget(self.agent_list)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.agents_main_layout.addItem(self.verticalSpacer)


        self.agents_page_layout.addLayout(self.agents_main_layout)

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
        self.agent_detail_page_layout = QVBoxLayout(self.agent_detail_page)
        self.agent_detail_page_layout.setSpacing(0)
        self.agent_detail_page_layout.setObjectName(u"agent_detail_page_layout")
        self.agent_detail_page_layout.setContentsMargins(0, 0, 0, 0)
        self.agent_detail_content = QWidget(self.agent_detail_page)
        self.agent_detail_content.setObjectName(u"agent_detail_content")
        self.agent_detail_content_layout = QVBoxLayout(self.agent_detail_content)
        self.agent_detail_content_layout.setObjectName(u"agent_detail_content_layout")
        self.detail_top_widget = QWidget(self.agent_detail_content)
        self.detail_top_widget.setObjectName(u"detail_top_widget")
        self.detail_top_widget.setMinimumSize(QSize(0, 0))
        self.detail_top_widget.setMaximumSize(QSize(16777215, 300))
        self.detail_top_widget.setStyleSheet(u"")
        self.detail_top_widget_layout = QVBoxLayout(self.detail_top_widget)
        self.detail_top_widget_layout.setSpacing(10)
        self.detail_top_widget_layout.setObjectName(u"detail_top_widget_layout")
        self.detail_top_widget_layout.setContentsMargins(0, 0, 0, 0)
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

        self.detail_top_center_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.detail_top_layout.addItem(self.detail_top_center_spacer)

        self.detail_top_agent_name_label = QLabel(self.detail_top_widget)
        self.detail_top_agent_name_label.setObjectName(u"detail_top_agent_name_label")
        self.detail_top_agent_name_label.setStyleSheet(u"font: 300 italic 12pt ;")
        self.detail_top_agent_name_label.setWordWrap(True)

        self.detail_top_layout.addWidget(self.detail_top_agent_name_label)

        self.detail_top_info_spacer = QSpacerItem(28, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.detail_top_layout.addItem(self.detail_top_info_spacer)

        self.detail_top_agent_status_label = QLabel(self.detail_top_widget)
        self.detail_top_agent_status_label.setObjectName(u"detail_top_agent_status_label")
        self.detail_top_agent_status_label.setStyleSheet(u"QLabel[agent_status=\"online\"] {\n"
"    color: #4caf50;\n"
"}\n"
"QLabel[agent_status=\"offline\"] {\n"
"    color: #f44336;\n"
"}")

        self.detail_top_layout.addWidget(self.detail_top_agent_status_label)


        self.detail_top_widget_layout.addLayout(self.detail_top_layout)

        self.detail_top_navigation_layout = QHBoxLayout()
        self.detail_top_navigation_layout.setSpacing(2)
        self.detail_top_navigation_layout.setObjectName(u"detail_top_navigation_layout")
        self.detail_top_navigation_layout.setContentsMargins(0, 10, 0, 10)
        self.overview_nav_button = QPushButton(self.detail_top_widget)
        self.overview_nav_button.setObjectName(u"overview_nav_button")
        self.overview_nav_button.setCheckable(True)
        self.overview_nav_button.setChecked(False)

        self.detail_top_navigation_layout.addWidget(self.overview_nav_button)

        self.performance_nav_button = QPushButton(self.detail_top_widget)
        self.performance_nav_button.setObjectName(u"performance_nav_button")
        self.performance_nav_button.setCheckable(True)
        self.performance_nav_button.setChecked(False)

        self.detail_top_navigation_layout.addWidget(self.performance_nav_button)

        self.hardware_nav_button = QPushButton(self.detail_top_widget)
        self.hardware_nav_button.setObjectName(u"hardware_nav_button")
        self.hardware_nav_button.setCheckable(True)
        self.hardware_nav_button.setChecked(False)

        self.detail_top_navigation_layout.addWidget(self.hardware_nav_button)

        self.commands_nav_button = QPushButton(self.detail_top_widget)
        self.commands_nav_button.setObjectName(u"commands_nav_button")
        self.commands_nav_button.setCheckable(True)
        self.commands_nav_button.setChecked(False)

        self.detail_top_navigation_layout.addWidget(self.commands_nav_button)


        self.detail_top_widget_layout.addLayout(self.detail_top_navigation_layout)


        self.agent_detail_content_layout.addWidget(self.detail_top_widget)

        self.detail_top_line = QFrame(self.agent_detail_content)
        self.detail_top_line.setObjectName(u"detail_top_line")
        self.detail_top_line.setFrameShape(QFrame.Shape.HLine)
        self.detail_top_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.agent_detail_content_layout.addWidget(self.detail_top_line)

        self.agent_detail_stacked_content = QStackedWidget(self.agent_detail_content)
        self.agent_detail_stacked_content.setObjectName(u"agent_detail_stacked_content")
        self.overview_detail_page = QWidget()
        self.overview_detail_page.setObjectName(u"overview_detail_page")
        self.overview_detail_page_layout = QVBoxLayout(self.overview_detail_page)
        self.overview_detail_page_layout.setObjectName(u"overview_detail_page_layout")
        self.overview_detail_page_layout.setContentsMargins(0, -1, -1, -1)
        self.overview_label = QLabel(self.overview_detail_page)
        self.overview_label.setObjectName(u"overview_label")
        self.overview_label.setMinimumSize(QSize(0, 0))
        self.overview_label.setStyleSheet(u"QLabel {\n"
"	font: 600 17pt;\n"
"}")
        self.overview_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.overview_detail_page_layout.addWidget(self.overview_label)

        self.overview_legend_label = QLabel(self.overview_detail_page)
        self.overview_legend_label.setObjectName(u"overview_legend_label")

        self.overview_detail_page_layout.addWidget(self.overview_legend_label)

        self.overview_legend_line = QFrame(self.overview_detail_page)
        self.overview_legend_line.setObjectName(u"overview_legend_line")
        self.overview_legend_line.setFrameShape(QFrame.Shape.HLine)
        self.overview_legend_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.overview_detail_page_layout.addWidget(self.overview_legend_line)

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
        self.agent_detail_information.setGeometry(QRect(0, 0, 977, 700))
        self.agent_detail_information.setMinimumSize(QSize(0, 700))
        self.agent_detail_information_layout = QVBoxLayout(self.agent_detail_information)
        self.agent_detail_information_layout.setSpacing(5)
        self.agent_detail_information_layout.setObjectName(u"agent_detail_information_layout")
        self.agent_detail_information_layout.setContentsMargins(0, 0, 0, 0)
        self.overview_widget = QWidget(self.agent_detail_information)
        self.overview_widget.setObjectName(u"overview_widget")
        self.overview_widget.setMaximumSize(QSize(16777215, 100))
        self.overview_widget.setStyleSheet(u"#uptime_widget, #ram_widget, #disk_widget, #cpu_widget {\n"
"	background-color: #161b22;\n"
"	border: 1px solid #30363d;\n"
"}\n"
"\n"
"\n"
"QLabel {\n"
"	background-color: transparent;\n"
"}")
        self.overview_layout = QHBoxLayout(self.overview_widget)
        self.overview_layout.setSpacing(0)
        self.overview_layout.setObjectName(u"overview_layout")
        self.overview_layout.setContentsMargins(0, 0, 0, 0)
        self.resource_boxes_widget = QWidget(self.overview_widget)
        self.resource_boxes_widget.setObjectName(u"resource_boxes_widget")
        self.resource_boxes_widget.setMaximumSize(QSize(16777215, 70))
        self.resource_boxes_widget.setStyleSheet(u"#cpu_label, #ram_label, #disk_label, #uptime_label {\n"
"	color: #8b949e;\n"
"}")
        self.resource_boxes_layout = QHBoxLayout(self.resource_boxes_widget)
        self.resource_boxes_layout.setSpacing(100)
        self.resource_boxes_layout.setObjectName(u"resource_boxes_layout")
        self.resource_boxes_layout.setContentsMargins(0, 0, 0, 0)
        self.cpu_widget = QWidget(self.resource_boxes_widget)
        self.cpu_widget.setObjectName(u"cpu_widget")
        self.cpu_widget.setMinimumSize(QSize(0, 60))
        self.cpu_widget.setMaximumSize(QSize(140, 90))
        self.cpu_widget_layout = QVBoxLayout(self.cpu_widget)
        self.cpu_widget_layout.setObjectName(u"cpu_widget_layout")
        self.cpu_label = QLabel(self.cpu_widget)
        self.cpu_label.setObjectName(u"cpu_label")
        self.cpu_label.setStyleSheet(u"")
        self.cpu_label.setAlignment(Qt.AlignCenter)

        self.cpu_widget_layout.addWidget(self.cpu_label)

        self.cpu_load_label = QLabel(self.cpu_widget)
        self.cpu_load_label.setObjectName(u"cpu_load_label")
        self.cpu_load_label.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"\n"
"}\n"
"\n"
"QLabel[load_level=\"low\"] {\n"
"    color: #4caf50;\n"
"}\n"
"QLabel[load_level=\"medium\"] {\n"
"    color: #ff9800;\n"
"}\n"
"QLabel[load_level=\"high\"] {\n"
"    color: #f44336;\n"
"}")
        self.cpu_load_label.setAlignment(Qt.AlignCenter)

        self.cpu_widget_layout.addWidget(self.cpu_load_label)


        self.resource_boxes_layout.addWidget(self.cpu_widget)

        self.ram_widget = QWidget(self.resource_boxes_widget)
        self.ram_widget.setObjectName(u"ram_widget")
        self.ram_widget.setMinimumSize(QSize(0, 60))
        self.ram_widget.setMaximumSize(QSize(140, 90))
        self.ram_widget_layout = QVBoxLayout(self.ram_widget)
        self.ram_widget_layout.setObjectName(u"ram_widget_layout")
        self.ram_label = QLabel(self.ram_widget)
        self.ram_label.setObjectName(u"ram_label")
        self.ram_label.setAlignment(Qt.AlignCenter)

        self.ram_widget_layout.addWidget(self.ram_label)

        self.ram_load_label = QLabel(self.ram_widget)
        self.ram_load_label.setObjectName(u"ram_load_label")
        self.ram_load_label.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"\n"
"}\n"
"QLabel[load_level=\"low\"] {\n"
"    color: #4caf50;\n"
"}\n"
"QLabel[load_level=\"medium\"] {\n"
"    color: #ff9800;\n"
"}\n"
"QLabel[load_level=\"high\"] {\n"
"    color: #f44336;\n"
"}")
        self.ram_load_label.setAlignment(Qt.AlignCenter)

        self.ram_widget_layout.addWidget(self.ram_load_label)


        self.resource_boxes_layout.addWidget(self.ram_widget)

        self.disk_widget = QWidget(self.resource_boxes_widget)
        self.disk_widget.setObjectName(u"disk_widget")
        self.disk_widget.setMinimumSize(QSize(0, 60))
        self.disk_widget.setMaximumSize(QSize(140, 90))
        self.disk_widget_layout = QVBoxLayout(self.disk_widget)
        self.disk_widget_layout.setObjectName(u"disk_widget_layout")
        self.disk_label = QLabel(self.disk_widget)
        self.disk_label.setObjectName(u"disk_label")
        self.disk_label.setAlignment(Qt.AlignCenter)

        self.disk_widget_layout.addWidget(self.disk_label)

        self.disk_load_label = QLabel(self.disk_widget)
        self.disk_load_label.setObjectName(u"disk_load_label")
        self.disk_load_label.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"\n"
"}")
        self.disk_load_label.setAlignment(Qt.AlignCenter)

        self.disk_widget_layout.addWidget(self.disk_load_label)


        self.resource_boxes_layout.addWidget(self.disk_widget)

        self.uptime_widget = QWidget(self.resource_boxes_widget)
        self.uptime_widget.setObjectName(u"uptime_widget")
        self.uptime_widget.setMinimumSize(QSize(0, 60))
        self.uptime_widget.setMaximumSize(QSize(140, 90))
        self.uptime_widget_layout = QVBoxLayout(self.uptime_widget)
        self.uptime_widget_layout.setObjectName(u"uptime_widget_layout")
        self.uptime_label = QLabel(self.uptime_widget)
        self.uptime_label.setObjectName(u"uptime_label")
        self.uptime_label.setAlignment(Qt.AlignCenter)

        self.uptime_widget_layout.addWidget(self.uptime_label)

        self.up_time_label = QLabel(self.uptime_widget)
        self.up_time_label.setObjectName(u"up_time_label")
        self.up_time_label.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"\n"
"}")
        self.up_time_label.setAlignment(Qt.AlignCenter)

        self.uptime_widget_layout.addWidget(self.up_time_label)


        self.resource_boxes_layout.addWidget(self.uptime_widget)


        self.overview_layout.addWidget(self.resource_boxes_widget)


        self.agent_detail_information_layout.addWidget(self.overview_widget)

        self.system_status_widget = QWidget(self.agent_detail_information)
        self.system_status_widget.setObjectName(u"system_status_widget")
        self.system_status_widget.setMinimumSize(QSize(0, 250))
        self.system_status_widget.setMaximumSize(QSize(16777215, 350))
        self.system_status_layout = QVBoxLayout(self.system_status_widget)
        self.system_status_layout.setObjectName(u"system_status_layout")
        self.system_status_layout.setContentsMargins(0, 0, 0, 0)
        self.system_status_label = QLabel(self.system_status_widget)
        self.system_status_label.setObjectName(u"system_status_label")
        self.system_status_label.setMaximumSize(QSize(16777215, 40))
        self.system_status_label.setStyleSheet(u"")

        self.system_status_layout.addWidget(self.system_status_label)

        self.system_status_box_widget = QWidget(self.system_status_widget)
        self.system_status_box_widget.setObjectName(u"system_status_box_widget")
        self.system_status_box_widget.setMaximumSize(QSize(400, 300))
        self.system_status_box_widget.setStyleSheet(u"#system_status_box_widget {\n"
"    background-color: #161b22;\n"
"	border: 1px solid #30363d;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"#system_status_box_widget QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.system_status_box_widget_layout = QHBoxLayout(self.system_status_box_widget)
        self.system_status_box_widget_layout.setSpacing(0)
        self.system_status_box_widget_layout.setObjectName(u"system_status_box_widget_layout")
        self.system_status_box_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.system_status_box_layout = QHBoxLayout()
        self.system_status_box_layout.setObjectName(u"system_status_box_layout")
        self.system_status_rows_widget = QWidget(self.system_status_box_widget)
        self.system_status_rows_widget.setObjectName(u"system_status_rows_widget")
        self.system_status_rows_widget.setStyleSheet(u"QLabel {\n"
"	font: 200 11pt;\n"
"	margin-left: 20px;\n"
"}")
        self.system_status_rows_widget_layout = QVBoxLayout(self.system_status_rows_widget)
        self.system_status_rows_widget_layout.setSpacing(0)
        self.system_status_rows_widget_layout.setObjectName(u"system_status_rows_widget_layout")
        self.system_status_rows_widget_layout.setContentsMargins(10, 0, 0, 0)
        self.agent_row_label = QLabel(self.system_status_rows_widget)
        self.agent_row_label.setObjectName(u"agent_row_label")
        self.agent_row_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.agent_row_label.setMargin(0)

        self.system_status_rows_widget_layout.addWidget(self.agent_row_label)

        self.last_seen_row_label = QLabel(self.system_status_rows_widget)
        self.last_seen_row_label.setObjectName(u"last_seen_row_label")
        self.last_seen_row_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.last_seen_row_label.setMargin(0)

        self.system_status_rows_widget_layout.addWidget(self.last_seen_row_label)

        self.ip_row_label = QLabel(self.system_status_rows_widget)
        self.ip_row_label.setObjectName(u"ip_row_label")
        self.ip_row_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ip_row_label.setMargin(0)

        self.system_status_rows_widget_layout.addWidget(self.ip_row_label)

        self.hostname_row_label = QLabel(self.system_status_rows_widget)
        self.hostname_row_label.setObjectName(u"hostname_row_label")
        self.hostname_row_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.hostname_row_label.setMargin(0)

        self.system_status_rows_widget_layout.addWidget(self.hostname_row_label)

        self.os_name_row_label = QLabel(self.system_status_rows_widget)
        self.os_name_row_label.setObjectName(u"os_name_row_label")
        self.os_name_row_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.os_name_row_label.setMargin(0)

        self.system_status_rows_widget_layout.addWidget(self.os_name_row_label)


        self.system_status_box_layout.addWidget(self.system_status_rows_widget)

        self.system_status_values_widget = QWidget(self.system_status_box_widget)
        self.system_status_values_widget.setObjectName(u"system_status_values_widget")
        self.system_status_values_widget.setStyleSheet(u"")
        self.system_status_values_widget_layout = QVBoxLayout(self.system_status_values_widget)
        self.system_status_values_widget_layout.setSpacing(0)
        self.system_status_values_widget_layout.setObjectName(u"system_status_values_widget_layout")
        self.system_status_values_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.agent_status_value_label = QLabel(self.system_status_values_widget)
        self.agent_status_value_label.setObjectName(u"agent_status_value_label")
        self.agent_status_value_label.setStyleSheet(u"QLabel[agent_status=\"online\"] {\n"
"    color: #4caf50;\n"
"}\n"
"QLabel[agent_status=\"offline\"] {\n"
"    color: #f44336;\n"
"}")

        self.system_status_values_widget_layout.addWidget(self.agent_status_value_label)

        self.last_seen_value_label = QLabel(self.system_status_values_widget)
        self.last_seen_value_label.setObjectName(u"last_seen_value_label")
        self.last_seen_value_label.setStyleSheet(u"")

        self.system_status_values_widget_layout.addWidget(self.last_seen_value_label)

        self.ip_value_label = QLabel(self.system_status_values_widget)
        self.ip_value_label.setObjectName(u"ip_value_label")

        self.system_status_values_widget_layout.addWidget(self.ip_value_label)

        self.hostname_value_label = QLabel(self.system_status_values_widget)
        self.hostname_value_label.setObjectName(u"hostname_value_label")

        self.system_status_values_widget_layout.addWidget(self.hostname_value_label)

        self.os_name_value_label = QLabel(self.system_status_values_widget)
        self.os_name_value_label.setObjectName(u"os_name_value_label")

        self.system_status_values_widget_layout.addWidget(self.os_name_value_label)


        self.system_status_box_layout.addWidget(self.system_status_values_widget)


        self.system_status_box_widget_layout.addLayout(self.system_status_box_layout)


        self.system_status_layout.addWidget(self.system_status_box_widget)


        self.agent_detail_information_layout.addWidget(self.system_status_widget)

        self.quick_actions_widget = QWidget(self.agent_detail_information)
        self.quick_actions_widget.setObjectName(u"quick_actions_widget")
        self.quick_actions_widget.setMinimumSize(QSize(0, 80))
        self.quick_actions_widget.setMaximumSize(QSize(16777215, 100))
        self.quick_actions_widget_layout = QVBoxLayout(self.quick_actions_widget)
        self.quick_actions_widget_layout.setSpacing(0)
        self.quick_actions_widget_layout.setObjectName(u"quick_actions_widget_layout")
        self.quick_actions_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.quick_actions_label = QLabel(self.quick_actions_widget)
        self.quick_actions_label.setObjectName(u"quick_actions_label")
        self.quick_actions_label.setMaximumSize(QSize(16777215, 30))
        self.quick_actions_label.setStyleSheet(u"")

        self.quick_actions_widget_layout.addWidget(self.quick_actions_label)

        self.quick_actions_buttons_widget = QWidget(self.quick_actions_widget)
        self.quick_actions_buttons_widget.setObjectName(u"quick_actions_buttons_widget")
        self.quick_actions_buttons_widget.setMaximumSize(QSize(16777215, 40))
        self.quick_actions_buttons_layout = QHBoxLayout(self.quick_actions_buttons_widget)
        self.quick_actions_buttons_layout.setSpacing(10)
        self.quick_actions_buttons_layout.setObjectName(u"quick_actions_buttons_layout")
        self.quick_actions_buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.restart_all_docker_cont_quick_button = QPushButton(self.quick_actions_buttons_widget)
        self.restart_all_docker_cont_quick_button.setObjectName(u"restart_all_docker_cont_quick_button")

        self.quick_actions_buttons_layout.addWidget(self.restart_all_docker_cont_quick_button)

        self.stop_all_docker_cont_quick_button = QPushButton(self.quick_actions_buttons_widget)
        self.stop_all_docker_cont_quick_button.setObjectName(u"stop_all_docker_cont_quick_button")

        self.quick_actions_buttons_layout.addWidget(self.stop_all_docker_cont_quick_button)

        self.docker_ps_quick_button = QPushButton(self.quick_actions_buttons_widget)
        self.docker_ps_quick_button.setObjectName(u"docker_ps_quick_button")

        self.quick_actions_buttons_layout.addWidget(self.docker_ps_quick_button)

        self.reboot_quick_button = QPushButton(self.quick_actions_buttons_widget)
        self.reboot_quick_button.setObjectName(u"reboot_quick_button")

        self.quick_actions_buttons_layout.addWidget(self.reboot_quick_button)


        self.quick_actions_widget_layout.addWidget(self.quick_actions_buttons_widget)


        self.agent_detail_information_layout.addWidget(self.quick_actions_widget)

        self.recent_commands_widget = QWidget(self.agent_detail_information)
        self.recent_commands_widget.setObjectName(u"recent_commands_widget")
        self.recent_commands_widget.setMaximumSize(QSize(16777215, 200))
        self.recent_commands_widget.setStyleSheet(u"#recent_command_box_widget {\n"
"    background-color: #161b22;\n"
"	border: 1px solid #30363d;\n"
"\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"#recent_command_box_widget QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.recent_commands_widget_layout = QVBoxLayout(self.recent_commands_widget)
        self.recent_commands_widget_layout.setSpacing(5)
        self.recent_commands_widget_layout.setObjectName(u"recent_commands_widget_layout")
        self.recent_commands_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.recent_commands_label = QLabel(self.recent_commands_widget)
        self.recent_commands_label.setObjectName(u"recent_commands_label")
        self.recent_commands_label.setMaximumSize(QSize(16777215, 30))
        self.recent_commands_label.setStyleSheet(u"")

        self.recent_commands_widget_layout.addWidget(self.recent_commands_label)

        self.recent_command_box_widget = QWidget(self.recent_commands_widget)
        self.recent_command_box_widget.setObjectName(u"recent_command_box_widget")
        self.recent_command_box_widget.setMaximumSize(QSize(550, 150))
        self.recent_command_box_widget.setStyleSheet(u"QLabel {\n"
"	font: 300 10.5pt\n"
"}")
        self.recent_command_box_layout = QVBoxLayout(self.recent_command_box_widget)
        self.recent_command_box_layout.setObjectName(u"recent_command_box_layout")
        self.recent_command_box_layout.setContentsMargins(9, -1, -1, -1)

        self.recent_commands_widget_layout.addWidget(self.recent_command_box_widget)


        self.agent_detail_information_layout.addWidget(self.recent_commands_widget)

        self.overview_detail_scroll.setWidget(self.agent_detail_information)

        self.overview_detail_page_layout.addWidget(self.overview_detail_scroll)

        self.agent_detail_stacked_content.addWidget(self.overview_detail_page)
        self.performance_detail_page = QWidget()
        self.performance_detail_page.setObjectName(u"performance_detail_page")
        self.performance_detail_page_layout = QVBoxLayout(self.performance_detail_page)
        self.performance_detail_page_layout.setSpacing(9)
        self.performance_detail_page_layout.setObjectName(u"performance_detail_page_layout")
        self.performance_detail_page_layout.setContentsMargins(0, 5, 0, 0)
        self.performance_label = QLabel(self.performance_detail_page)
        self.performance_label.setObjectName(u"performance_label")
        self.performance_label.setMinimumSize(QSize(0, 0))
        self.performance_label.setStyleSheet(u"QLabel {\n"
"	font: 600 17pt;\n"
"\n"
"}")
        self.performance_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.performance_detail_page_layout.addWidget(self.performance_label)

        self.performance_legend_label = QLabel(self.performance_detail_page)
        self.performance_legend_label.setObjectName(u"performance_legend_label")

        self.performance_detail_page_layout.addWidget(self.performance_legend_label)

        self.performance_legend_line = QFrame(self.performance_detail_page)
        self.performance_legend_line.setObjectName(u"performance_legend_line")
        self.performance_legend_line.setFrameShape(QFrame.Shape.HLine)
        self.performance_legend_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.performance_detail_page_layout.addWidget(self.performance_legend_line)

        self.metric_buttons_layout = QHBoxLayout()
        self.metric_buttons_layout.setSpacing(2)
        self.metric_buttons_layout.setObjectName(u"metric_buttons_layout")
        self.compute_button = QPushButton(self.performance_detail_page)
        self.compute_button.setObjectName(u"compute_button")

        self.metric_buttons_layout.addWidget(self.compute_button)

        self.storage_button = QPushButton(self.performance_detail_page)
        self.storage_button.setObjectName(u"storage_button")

        self.metric_buttons_layout.addWidget(self.storage_button)

        self.thermals_button = QPushButton(self.performance_detail_page)
        self.thermals_button.setObjectName(u"thermals_button")

        self.metric_buttons_layout.addWidget(self.thermals_button)

        self.network_button = QPushButton(self.performance_detail_page)
        self.network_button.setObjectName(u"network_button")

        self.metric_buttons_layout.addWidget(self.network_button)


        self.performance_detail_page_layout.addLayout(self.metric_buttons_layout)

        self.performance_detail_scroll = QScrollArea(self.performance_detail_page)
        self.performance_detail_scroll.setObjectName(u"performance_detail_scroll")
        self.performance_detail_scroll.setStyleSheet(u"QScrollArea {\n"
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
        self.performance_detail_scroll.setWidgetResizable(True)
        self.agent_performance_information = QWidget()
        self.agent_performance_information.setObjectName(u"agent_performance_information")
        self.agent_performance_information.setGeometry(QRect(0, 0, 986, 1190))
        self.agent_performance_information_layout = QVBoxLayout(self.agent_performance_information)
        self.agent_performance_information_layout.setSpacing(0)
        self.agent_performance_information_layout.setObjectName(u"agent_performance_information_layout")
        self.agent_performance_information_layout.setContentsMargins(0, 0, 0, 0)
        self.performance_content_widget = QWidget(self.agent_performance_information)
        self.performance_content_widget.setObjectName(u"performance_content_widget")
        self.performance_content_widget.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	margin-top: 5px;\n"
"	margin-bottom: 5px;\n"
"}")
        self.performance_content_layout = QVBoxLayout(self.performance_content_widget)
        self.performance_content_layout.setSpacing(6)
        self.performance_content_layout.setObjectName(u"performance_content_layout")
        self.performance_content_layout.setContentsMargins(0, 0, 0, 0)
        self.performance_stacked_content = QStackedWidget(self.performance_content_widget)
        self.performance_stacked_content.setObjectName(u"performance_stacked_content")
        self.performance_stacked_content.setStyleSheet(u"#perfomance_stacked_content {\n"
"    background-color: transparent;\n"
"    border: 1px solid #1E2633;\n"
"	border-radius: 2px\n"
"\n"
"}\n"
"\n"
"QComboBox {\n"
"    color: #a5b4fc; \n"
"    background-color: transparent;\n"
"    border: 1px solid #242936;\n"
"    border-radius: 4px;\n"
"    padding: 6px 0px 6px 15px;	\n"
"    font-size: 12px;\n"
"    min-width: 100px;\n"
"}\n"
"QComboBox:hover {\n"
"    background-color: #1e2230;\n"
"    border-color: #38bdf8;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QComboBox:on { \n"
"    background-color: #0f111a;\n"
"    border-color: #58a6ff;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QComboBox QAbstractItemView,\n"
"QComboBox QListView {\n"
"    background-color: #161920;\n"
"    border: 1px solid #242936; \n"
"    border-radius: 4px;\n"
"    padding: 0px !important;\n"
"    margin: 0px !important;\n"
"    outline: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    min-height: 28px;\n"
"    padding-left: 12px;\n"
"    padding-right: 12px;\n"
"    color: #a5b4fc;\n"
"   "
                        " background-color: transparent;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover,\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: #1e2230 !important;\n"
"    color: #ffffff !important;\n"
"}\n"
"\n"
"\n"
"QComboBox QScrollBar:vertical {\n"
"    background-color: #161920;\n"
"    width: 8px;\n"
"    margin: 0px;\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox QScrollBar::handle:vertical {\n"
"    background-color: #242936; \n"
"    border-radius: 4px;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QComboBox QScrollBar::handle:vertical:hover {\n"
"    background-color: #38bdf8;\n"
"}\n"
"\n"
"QComboBox QScrollBar::add-line:vertical,\n"
"QComboBox QScrollBar::sub-line:vertical,\n"
"QComboBox QScrollBar::up-arrow:vertical, \n"
"QComboBox QScrollBar::down-arrow:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"    height: 0px;\n"
"    width: 0px;\n"
"}")
        self.compute_page = QWidget()
        self.compute_page.setObjectName(u"compute_page")
        self.compute_page_layout = QVBoxLayout(self.compute_page)
        self.compute_page_layout.setSpacing(15)
        self.compute_page_layout.setObjectName(u"compute_page_layout")
        self.compute_page_layout.setContentsMargins(6, 6, 6, 6)
        self.compute_label = QLabel(self.compute_page)
        self.compute_label.setObjectName(u"compute_label")
        self.compute_label.setStyleSheet(u"QLabel {\n"
"	font: 350 italic 15pt;\n"
"	margin-left: 0px;\n"
"}")

        self.compute_page_layout.addWidget(self.compute_label)

        self.compute_legend_label = QLabel(self.compute_page)
        self.compute_legend_label.setObjectName(u"compute_legend_label")

        self.compute_page_layout.addWidget(self.compute_legend_label)

        self.compute_legend_line = QFrame(self.compute_page)
        self.compute_legend_line.setObjectName(u"compute_legend_line")
        self.compute_legend_line.setFrameShape(QFrame.Shape.HLine)
        self.compute_legend_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.compute_page_layout.addWidget(self.compute_legend_line)

        self.compute_current_state_label = QLabel(self.compute_page)
        self.compute_current_state_label.setObjectName(u"compute_current_state_label")

        self.compute_page_layout.addWidget(self.compute_current_state_label)

        self.compute_gauge_widget = QWidget(self.compute_page)
        self.compute_gauge_widget.setObjectName(u"compute_gauge_widget")
        self.compute_gauge_widget.setStyleSheet(u"#compute_gauge_widget {\n"
"	border: 1px solid #1E2633;\n"
"}")
        self.compute_gauge_layout = QHBoxLayout(self.compute_gauge_widget)
        self.compute_gauge_layout.setObjectName(u"compute_gauge_layout")
        self.compute_gauge_layout.setContentsMargins(-1, -1, -1, 1)

        self.compute_page_layout.addWidget(self.compute_gauge_widget)

        self.cpu_ram_metric_label = QLabel(self.compute_page)
        self.cpu_ram_metric_label.setObjectName(u"cpu_ram_metric_label")

        self.compute_page_layout.addWidget(self.cpu_ram_metric_label)

        self.cpu_ram_utilization_widget = QWidget(self.compute_page)
        self.cpu_ram_utilization_widget.setObjectName(u"cpu_ram_utilization_widget")
        self.cpu_ram_utilization_widget.setMinimumSize(QSize(0, 300))
        self.cpu_ram_utilization_widget.setMaximumSize(QSize(16777215, 600))
        self.cpu_ram_utilization_layout = QHBoxLayout(self.cpu_ram_utilization_widget)
        self.cpu_ram_utilization_layout.setObjectName(u"cpu_ram_utilization_layout")
        self.cpu_ram_utilization_layout.setContentsMargins(0, 0, 0, 0)
        self.cpu_ram_metric_graph = PlotWidget(self.cpu_ram_utilization_widget)
        self.cpu_ram_metric_graph.setObjectName(u"cpu_ram_metric_graph")
        self.cpu_ram_metric_graph.setMinimumSize(QSize(0, 0))
        self.cpu_ram_metric_graph.setStyleSheet(u"QWidget {\n"
"    background-color: transparent;\n"
"    border: 1px solid #30363d;\n"
"    border-radius: 8px;\n"
"	border-top-right-radius: 0px; \n"
"	border-bottom-right-radius: 0px;\n"
"}")

        self.cpu_ram_utilization_layout.addWidget(self.cpu_ram_metric_graph)

        self.ram_utilization_widget = QWidget(self.cpu_ram_utilization_widget)
        self.ram_utilization_widget.setObjectName(u"ram_utilization_widget")
        self.ram_utilization_widget.setMinimumSize(QSize(0, 120))
        self.ram_utilization_widget.setMaximumSize(QSize(200, 16777215))
        self.ram_utilization_widget.setStyleSheet(u"#ram_utilization_widget {\n"
"	border: 1px solid #30363d;\n"
"	border-radius: 8px;\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"Line {\n"
"    background-color: #1E2633;\n"
"    border: none;\n"
"    max-height: 1px;\n"
"}")
        self.ram_utilization_layout = QVBoxLayout(self.ram_utilization_widget)
        self.ram_utilization_layout.setObjectName(u"ram_utilization_layout")
        self.memory_label = QLabel(self.ram_utilization_widget)
        self.memory_label.setObjectName(u"memory_label")
        self.memory_label.setMaximumSize(QSize(16777215, 50))
        self.memory_label.setStyleSheet(u"font: 200 italic 11pt;")

        self.ram_utilization_layout.addWidget(self.memory_label)

        self.memory_information_layout = QVBoxLayout()
        self.memory_information_layout.setObjectName(u"memory_information_layout")
        self.used_memory_layout = QHBoxLayout()
        self.used_memory_layout.setObjectName(u"used_memory_layout")
        self.used_memory_label = QLabel(self.ram_utilization_widget)
        self.used_memory_label.setObjectName(u"used_memory_label")

        self.used_memory_layout.addWidget(self.used_memory_label)

        self.used_memory_value_label = QLabel(self.ram_utilization_widget)
        self.used_memory_value_label.setObjectName(u"used_memory_value_label")

        self.used_memory_layout.addWidget(self.used_memory_value_label)


        self.memory_information_layout.addLayout(self.used_memory_layout)

        self.memory_layout_top_line = QFrame(self.ram_utilization_widget)
        self.memory_layout_top_line.setObjectName(u"memory_layout_top_line")
        self.memory_layout_top_line.setFrameShape(QFrame.Shape.HLine)
        self.memory_layout_top_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.memory_information_layout.addWidget(self.memory_layout_top_line)

        self.available_memory_layout = QHBoxLayout()
        self.available_memory_layout.setObjectName(u"available_memory_layout")
        self.available_memory_label = QLabel(self.ram_utilization_widget)
        self.available_memory_label.setObjectName(u"available_memory_label")

        self.available_memory_layout.addWidget(self.available_memory_label)

        self.available_memory_value_label = QLabel(self.ram_utilization_widget)
        self.available_memory_value_label.setObjectName(u"available_memory_value_label")

        self.available_memory_layout.addWidget(self.available_memory_value_label)


        self.memory_information_layout.addLayout(self.available_memory_layout)

        self.memory_layout_bottom_line = QFrame(self.ram_utilization_widget)
        self.memory_layout_bottom_line.setObjectName(u"memory_layout_bottom_line")
        self.memory_layout_bottom_line.setFrameShape(QFrame.Shape.HLine)
        self.memory_layout_bottom_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.memory_information_layout.addWidget(self.memory_layout_bottom_line)

        self.swap_memory_layout = QHBoxLayout()
        self.swap_memory_layout.setObjectName(u"swap_memory_layout")
        self.swap_memory_label = QLabel(self.ram_utilization_widget)
        self.swap_memory_label.setObjectName(u"swap_memory_label")

        self.swap_memory_layout.addWidget(self.swap_memory_label)

        self.swap_memory_value_label = QLabel(self.ram_utilization_widget)
        self.swap_memory_value_label.setObjectName(u"swap_memory_value_label")

        self.swap_memory_layout.addWidget(self.swap_memory_value_label)


        self.memory_information_layout.addLayout(self.swap_memory_layout)


        self.ram_utilization_layout.addLayout(self.memory_information_layout)

        self.memory_progress_bar = QProgressBar(self.ram_utilization_widget)
        self.memory_progress_bar.setObjectName(u"memory_progress_bar")
        self.memory_progress_bar.setStyleSheet(u"QProgressBar {\n"
"    border: 1px solid #1E2B3E;\n"
"    border-radius: 0px;\n"
"    background-color: #090C12;\n"
"    text-align: center;\n"
"    color: #a5b4fc;\n"
"	font-size: 11px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"\n"
"	background-color: rgba(11, 22, 35, 255);\n"
"    border-radius: 0px;\n"
"    margin: 1px;\n"
"}")
        self.memory_progress_bar.setValue(0)

        self.ram_utilization_layout.addWidget(self.memory_progress_bar)


        self.cpu_ram_utilization_layout.addWidget(self.ram_utilization_widget)


        self.compute_page_layout.addWidget(self.cpu_ram_utilization_widget)

        self.compute_load_average_label = QLabel(self.compute_page)
        self.compute_load_average_label.setObjectName(u"compute_load_average_label")

        self.compute_page_layout.addWidget(self.compute_load_average_label)

        self.load_average_metric_graph = PlotWidget(self.compute_page)
        self.load_average_metric_graph.setObjectName(u"load_average_metric_graph")
        self.load_average_metric_graph.setMinimumSize(QSize(0, 300))
        self.load_average_metric_graph.setStyleSheet(u"QWidget {\n"
"    background-color: transparent;\n"
"    border: 1px solid #30363d;\n"
"    border-radius: 8px;\n"
"\n"
"\n"
"	border-top-right-radius: 0px; \n"
"	border-bottom-right-radius: 0px;\n"
"}")

        self.compute_page_layout.addWidget(self.load_average_metric_graph)

        self.compute_cpu_cores_label = QLabel(self.compute_page)
        self.compute_cpu_cores_label.setObjectName(u"compute_cpu_cores_label")

        self.compute_page_layout.addWidget(self.compute_cpu_cores_label)

        self.cpu_cores_metric_graph = PlotWidget(self.compute_page)
        self.cpu_cores_metric_graph.setObjectName(u"cpu_cores_metric_graph")
        self.cpu_cores_metric_graph.setMinimumSize(QSize(0, 300))
        self.cpu_cores_metric_graph.setStyleSheet(u"QWidget {\n"
"    background-color: transparent;\n"
"    border: 1px solid #30363d;\n"
"    border-radius: 8px;\n"
"\n"
"\n"
"	border-top-right-radius: 0px; \n"
"	border-bottom-right-radius: 0px;\n"
"}")

        self.compute_page_layout.addWidget(self.cpu_cores_metric_graph)

        self.performance_stacked_content.addWidget(self.compute_page)
        self.storage_page = QWidget()
        self.storage_page.setObjectName(u"storage_page")
        self.storage_page.setStyleSheet(u"")
        self.storage_page_layout = QVBoxLayout(self.storage_page)
        self.storage_page_layout.setSpacing(15)
        self.storage_page_layout.setObjectName(u"storage_page_layout")
        self.storage_page_layout.setContentsMargins(6, 6, 6, 6)
        self.storage_label = QLabel(self.storage_page)
        self.storage_label.setObjectName(u"storage_label")
        self.storage_label.setMaximumSize(QSize(16777215, 40))
        self.storage_label.setStyleSheet(u"QLabel {\n"
"	font: 350 italic 15pt;\n"
"	margin-left: 0px;\n"
"}")

        self.storage_page_layout.addWidget(self.storage_label)

        self.storage_legend_label = QLabel(self.storage_page)
        self.storage_legend_label.setObjectName(u"storage_legend_label")

        self.storage_page_layout.addWidget(self.storage_legend_label)

        self.storage_legend_line = QFrame(self.storage_page)
        self.storage_legend_line.setObjectName(u"storage_legend_line")
        self.storage_legend_line.setFrameShape(QFrame.Shape.HLine)
        self.storage_legend_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.storage_page_layout.addWidget(self.storage_legend_line)

        self.current_storage_label = QLabel(self.storage_page)
        self.current_storage_label.setObjectName(u"current_storage_label")
        self.current_storage_label.setMaximumSize(QSize(16777215, 30))

        self.storage_page_layout.addWidget(self.current_storage_label)

        self.storage_gauge_widget = QWidget(self.storage_page)
        self.storage_gauge_widget.setObjectName(u"storage_gauge_widget")
        self.storage_gauge_widget.setStyleSheet(u"#storage_gauge_widget {\n"
"	border: 1px solid #1E2633;\n"
"}")
        self.storage_gauge_layout = QHBoxLayout(self.storage_gauge_widget)
        self.storage_gauge_layout.setObjectName(u"storage_gauge_layout")
        self.storage_gauge_layout.setContentsMargins(-1, -1, -1, 1)

        self.storage_page_layout.addWidget(self.storage_gauge_widget)

        self.current_storage_line = QFrame(self.storage_page)
        self.current_storage_line.setObjectName(u"current_storage_line")
        self.current_storage_line.setFrameShape(QFrame.Shape.HLine)
        self.current_storage_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.storage_page_layout.addWidget(self.current_storage_line)

        self.disk_io_layout = QHBoxLayout()
        self.disk_io_layout.setObjectName(u"disk_io_layout")
        self.disk_io_layout.setContentsMargins(0, 0, -1, -1)
        self.disk_io_label = QLabel(self.storage_page)
        self.disk_io_label.setObjectName(u"disk_io_label")
        self.disk_io_label.setMinimumSize(QSize(0, 0))
        self.disk_io_label.setMaximumSize(QSize(100, 16777215))

        self.disk_io_layout.addWidget(self.disk_io_label)

        self.disk_io_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.disk_io_layout.addItem(self.disk_io_spacer)

        self.disks_combo_box = QComboBox(self.storage_page)
        self.disks_combo_box.setObjectName(u"disks_combo_box")
        self.disks_combo_box.setMinimumSize(QSize(117, 0))
        self.disks_combo_box.setMaximumSize(QSize(120, 16777215))
        self.disks_combo_box.setEditable(False)
        self.disks_combo_box.setMaxVisibleItems(4)
        self.disks_combo_box.setIconSize(QSize(16, 16))
        self.disks_combo_box.setFrame(True)

        self.disk_io_layout.addWidget(self.disks_combo_box)

        self.disk_data_unit_combo_box = QComboBox(self.storage_page)
        self.disk_data_unit_combo_box.setObjectName(u"disk_data_unit_combo_box")
        self.disk_data_unit_combo_box.setMinimumSize(QSize(117, 0))
        self.disk_data_unit_combo_box.setMaximumSize(QSize(70, 16777215))
        self.disk_data_unit_combo_box.setEditable(False)
        self.disk_data_unit_combo_box.setInsertPolicy(QComboBox.InsertAtCurrent)

        self.disk_io_layout.addWidget(self.disk_data_unit_combo_box)


        self.storage_page_layout.addLayout(self.disk_io_layout)

        self.storage_disk_io_widget = QWidget(self.storage_page)
        self.storage_disk_io_widget.setObjectName(u"storage_disk_io_widget")
        self.storage_disk_io_widget.setMinimumSize(QSize(0, 300))
        self.storage_disk_io_widget.setMaximumSize(QSize(16777215, 600))
        self.storage_disk_io_layout = QHBoxLayout(self.storage_disk_io_widget)
        self.storage_disk_io_layout.setObjectName(u"storage_disk_io_layout")
        self.storage_disk_io_layout.setContentsMargins(0, 0, 0, 0)
        self.disk_write_read_graph = PlotWidget(self.storage_disk_io_widget)
        self.disk_write_read_graph.setObjectName(u"disk_write_read_graph")
        self.disk_write_read_graph.setMinimumSize(QSize(0, 0))
        self.disk_write_read_graph.setStyleSheet(u"QWidget {\n"
"    background-color: transparent;\n"
"    border: 1px solid #30363d;\n"
"    border-radius: 8px;\n"
"	border-top-right-radius: 0px; \n"
"	border-bottom-right-radius: 0px;\n"
"}")

        self.storage_disk_io_layout.addWidget(self.disk_write_read_graph)

        self.disk_io_summary_widget = QWidget(self.storage_disk_io_widget)
        self.disk_io_summary_widget.setObjectName(u"disk_io_summary_widget")
        self.disk_io_summary_widget.setMinimumSize(QSize(230, 120))
        self.disk_io_summary_widget.setMaximumSize(QSize(300, 16777215))
        self.disk_io_summary_widget.setStyleSheet(u"#disk_io_summary_widget {\n"
"	border: 1px solid #30363d;\n"
"	border-radius: 8px;\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"Line {\n"
"    background-color: #1E2633;\n"
"    border: none;\n"
"    max-height: 1px;\n"
"}")
        self.disk_io_summary_layout = QVBoxLayout(self.disk_io_summary_widget)
        self.disk_io_summary_layout.setSpacing(0)
        self.disk_io_summary_layout.setObjectName(u"disk_io_summary_layout")
        self.disk_io_summary_layout.setContentsMargins(6, 6, 6, 6)
        self.disk_i_o_summary_label = QLabel(self.disk_io_summary_widget)
        self.disk_i_o_summary_label.setObjectName(u"disk_i_o_summary_label")
        self.disk_i_o_summary_label.setMaximumSize(QSize(16777215, 50))
        self.disk_i_o_summary_label.setStyleSheet(u"font: 200 italic 11pt;")

        self.disk_io_summary_layout.addWidget(self.disk_i_o_summary_label)

        self.disk_information_layout = QVBoxLayout()
        self.disk_information_layout.setSpacing(0)
        self.disk_information_layout.setObjectName(u"disk_information_layout")
        self.disk_i_o_summary_line = QFrame(self.disk_io_summary_widget)
        self.disk_i_o_summary_line.setObjectName(u"disk_i_o_summary_line")
        self.disk_i_o_summary_line.setFrameShape(QFrame.Shape.HLine)
        self.disk_i_o_summary_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.disk_information_layout.addWidget(self.disk_i_o_summary_line)

        self.disk_capacity_information_layout = QVBoxLayout()
        self.disk_capacity_information_layout.setSpacing(0)
        self.disk_capacity_information_layout.setObjectName(u"disk_capacity_information_layout")
        self.disk_read_information_layout = QHBoxLayout()
        self.disk_read_information_layout.setObjectName(u"disk_read_information_layout")
        self.disk_read_information_label = QLabel(self.disk_io_summary_widget)
        self.disk_read_information_label.setObjectName(u"disk_read_information_label")

        self.disk_read_information_layout.addWidget(self.disk_read_information_label)

        self.disk_read_information_value = QLabel(self.disk_io_summary_widget)
        self.disk_read_information_value.setObjectName(u"disk_read_information_value")
        self.disk_read_information_value.setAlignment(Qt.AlignCenter)

        self.disk_read_information_layout.addWidget(self.disk_read_information_value)


        self.disk_capacity_information_layout.addLayout(self.disk_read_information_layout)

        self.disk_write_informatio_layout = QHBoxLayout()
        self.disk_write_informatio_layout.setObjectName(u"disk_write_informatio_layout")
        self.disk_write_information_label = QLabel(self.disk_io_summary_widget)
        self.disk_write_information_label.setObjectName(u"disk_write_information_label")

        self.disk_write_informatio_layout.addWidget(self.disk_write_information_label)

        self.disk_write_information_value = QLabel(self.disk_io_summary_widget)
        self.disk_write_information_value.setObjectName(u"disk_write_information_value")
        self.disk_write_information_value.setAlignment(Qt.AlignCenter)

        self.disk_write_informatio_layout.addWidget(self.disk_write_information_value)


        self.disk_capacity_information_layout.addLayout(self.disk_write_informatio_layout)

        self.disk_read_per_sec_information_layout = QHBoxLayout()
        self.disk_read_per_sec_information_layout.setObjectName(u"disk_read_per_sec_information_layout")
        self.disk_read_per_sec_information_label = QLabel(self.disk_io_summary_widget)
        self.disk_read_per_sec_information_label.setObjectName(u"disk_read_per_sec_information_label")

        self.disk_read_per_sec_information_layout.addWidget(self.disk_read_per_sec_information_label)

        self.disk_read_per_sec_information_value = QLabel(self.disk_io_summary_widget)
        self.disk_read_per_sec_information_value.setObjectName(u"disk_read_per_sec_information_value")
        self.disk_read_per_sec_information_value.setAlignment(Qt.AlignCenter)

        self.disk_read_per_sec_information_layout.addWidget(self.disk_read_per_sec_information_value)


        self.disk_capacity_information_layout.addLayout(self.disk_read_per_sec_information_layout)

        self.disk_write_per_sec_information_layout = QHBoxLayout()
        self.disk_write_per_sec_information_layout.setObjectName(u"disk_write_per_sec_information_layout")
        self.disk_write_per_sec_information_label = QLabel(self.disk_io_summary_widget)
        self.disk_write_per_sec_information_label.setObjectName(u"disk_write_per_sec_information_label")

        self.disk_write_per_sec_information_layout.addWidget(self.disk_write_per_sec_information_label)

        self.disk_write_per_sec_information_value = QLabel(self.disk_io_summary_widget)
        self.disk_write_per_sec_information_value.setObjectName(u"disk_write_per_sec_information_value")
        self.disk_write_per_sec_information_value.setAlignment(Qt.AlignCenter)

        self.disk_write_per_sec_information_layout.addWidget(self.disk_write_per_sec_information_value)


        self.disk_capacity_information_layout.addLayout(self.disk_write_per_sec_information_layout)


        self.disk_information_layout.addLayout(self.disk_capacity_information_layout)

        self.disk_avg_latency_layout = QHBoxLayout()
        self.disk_avg_latency_layout.setSpacing(0)
        self.disk_avg_latency_layout.setObjectName(u"disk_avg_latency_layout")
        self.disk_avg_latency_label = QLabel(self.disk_io_summary_widget)
        self.disk_avg_latency_label.setObjectName(u"disk_avg_latency_label")
        self.disk_avg_latency_label.setMaximumSize(QSize(16777215, 60))

        self.disk_avg_latency_layout.addWidget(self.disk_avg_latency_label)

        self.disk_avg_latency_value = QLabel(self.disk_io_summary_widget)
        self.disk_avg_latency_value.setObjectName(u"disk_avg_latency_value")
        self.disk_avg_latency_value.setMaximumSize(QSize(16777215, 60))
        self.disk_avg_latency_value.setAlignment(Qt.AlignCenter)

        self.disk_avg_latency_layout.addWidget(self.disk_avg_latency_value)


        self.disk_information_layout.addLayout(self.disk_avg_latency_layout)


        self.disk_io_summary_layout.addLayout(self.disk_information_layout)


        self.storage_disk_io_layout.addWidget(self.disk_io_summary_widget)


        self.storage_page_layout.addWidget(self.storage_disk_io_widget)

        self.disk_io_line = QFrame(self.storage_page)
        self.disk_io_line.setObjectName(u"disk_io_line")
        self.disk_io_line.setFrameShape(QFrame.Shape.HLine)
        self.disk_io_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.storage_page_layout.addWidget(self.disk_io_line)

        self.file_systems_label = QLabel(self.storage_page)
        self.file_systems_label.setObjectName(u"file_systems_label")

        self.storage_page_layout.addWidget(self.file_systems_label)

        self.file_systems_table = QTableWidget(self.storage_page)
        if (self.file_systems_table.columnCount() < 6):
            self.file_systems_table.setColumnCount(6)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.file_systems_table.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.file_systems_table.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.file_systems_table.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.file_systems_table.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.file_systems_table.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.file_systems_table.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        self.file_systems_table.setObjectName(u"file_systems_table")
        self.file_systems_table.horizontalHeader().setCascadingSectionResizes(True)

        self.storage_page_layout.addWidget(self.file_systems_table)

        self.file_systems_line = QFrame(self.storage_page)
        self.file_systems_line.setObjectName(u"file_systems_line")
        self.file_systems_line.setFrameShape(QFrame.Shape.HLine)
        self.file_systems_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.storage_page_layout.addWidget(self.file_systems_line)

        self.storage_devices_label = QLabel(self.storage_page)
        self.storage_devices_label.setObjectName(u"storage_devices_label")

        self.storage_page_layout.addWidget(self.storage_devices_label)

        self.storage_devices_table = QTableWidget(self.storage_page)
        if (self.storage_devices_table.columnCount() < 5):
            self.storage_devices_table.setColumnCount(5)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.storage_devices_table.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.storage_devices_table.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.storage_devices_table.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.storage_devices_table.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.storage_devices_table.setHorizontalHeaderItem(4, __qtablewidgetitem16)
        self.storage_devices_table.setObjectName(u"storage_devices_table")
        self.storage_devices_table.horizontalHeader().setCascadingSectionResizes(True)

        self.storage_page_layout.addWidget(self.storage_devices_table)

        self.performance_stacked_content.addWidget(self.storage_page)
        self.thermals_page = QWidget()
        self.thermals_page.setObjectName(u"thermals_page")
        self.thermals_page_layout = QVBoxLayout(self.thermals_page)
        self.thermals_page_layout.setSpacing(15)
        self.thermals_page_layout.setObjectName(u"thermals_page_layout")
        self.thermals_page_layout.setContentsMargins(6, 6, 6, 6)
        self.thermals_label = QLabel(self.thermals_page)
        self.thermals_label.setObjectName(u"thermals_label")
        self.thermals_label.setMaximumSize(QSize(16777215, 40))
        self.thermals_label.setStyleSheet(u"QLabel {\n"
"	font: 350 italic 15pt;\n"
"	margin-left: 0px;\n"
"}")
        self.thermals_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.thermals_page_layout.addWidget(self.thermals_label)

        self.thermals_legend_label = QLabel(self.thermals_page)
        self.thermals_legend_label.setObjectName(u"thermals_legend_label")
        self.thermals_legend_label.setMaximumSize(QSize(16777215, 30))

        self.thermals_page_layout.addWidget(self.thermals_legend_label)

        self.thermal_legend_line = QFrame(self.thermals_page)
        self.thermal_legend_line.setObjectName(u"thermal_legend_line")
        self.thermal_legend_line.setFrameShape(QFrame.Shape.HLine)
        self.thermal_legend_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.thermals_page_layout.addWidget(self.thermal_legend_line)

        self.current_thermals_label = QLabel(self.thermals_page)
        self.current_thermals_label.setObjectName(u"current_thermals_label")
        self.current_thermals_label.setMaximumSize(QSize(16777215, 30))

        self.thermals_page_layout.addWidget(self.current_thermals_label)

        self.thermals_gauge_widget = QWidget(self.thermals_page)
        self.thermals_gauge_widget.setObjectName(u"thermals_gauge_widget")
        self.thermals_gauge_widget.setStyleSheet(u"#thermals_gauge_widget {\n"
"	border: 1px solid #1E2633;\n"
"}")
        self.thermals_gauge_layout = QHBoxLayout(self.thermals_gauge_widget)
        self.thermals_gauge_layout.setObjectName(u"thermals_gauge_layout")
        self.thermals_gauge_layout.setContentsMargins(-1, -1, -1, 1)

        self.thermals_page_layout.addWidget(self.thermals_gauge_widget)

        self.current_thermals_line = QFrame(self.thermals_page)
        self.current_thermals_line.setObjectName(u"current_thermals_line")
        self.current_thermals_line.setFrameShape(QFrame.Shape.HLine)
        self.current_thermals_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.thermals_page_layout.addWidget(self.current_thermals_line)

        self.thermals_combo_box_layout = QHBoxLayout()
        self.thermals_combo_box_layout.setObjectName(u"thermals_combo_box_layout")
        self.thermals_combo_box_layout.setContentsMargins(0, 0, -1, -1)
        self.temperature_history_label = QLabel(self.thermals_page)
        self.temperature_history_label.setObjectName(u"temperature_history_label")
        self.temperature_history_label.setMinimumSize(QSize(0, 0))
        self.temperature_history_label.setMaximumSize(QSize(16777215, 30))

        self.thermals_combo_box_layout.addWidget(self.temperature_history_label)

        self.thermals_combo_box_right_spacer = QSpacerItem(35, 50, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.thermals_combo_box_layout.addItem(self.thermals_combo_box_right_spacer)

        self.sensor_group_label = QLabel(self.thermals_page)
        self.sensor_group_label.setObjectName(u"sensor_group_label")
        self.sensor_group_label.setMinimumSize(QSize(0, 0))
        self.sensor_group_label.setMaximumSize(QSize(100, 40))

        self.thermals_combo_box_layout.addWidget(self.sensor_group_label)

        self.sensor_group_combo_box = QComboBox(self.thermals_page)
        self.sensor_group_combo_box.setObjectName(u"sensor_group_combo_box")
        self.sensor_group_combo_box.setMinimumSize(QSize(117, 0))
        self.sensor_group_combo_box.setMaximumSize(QSize(120, 30))
        self.sensor_group_combo_box.setEditable(False)
        self.sensor_group_combo_box.setMaxVisibleItems(4)
        self.sensor_group_combo_box.setIconSize(QSize(16, 16))
        self.sensor_group_combo_box.setFrame(True)

        self.thermals_combo_box_layout.addWidget(self.sensor_group_combo_box)

        self.thernals_combo_box_separate_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.thermals_combo_box_layout.addItem(self.thernals_combo_box_separate_spacer)

        self.sensor_name_label = QLabel(self.thermals_page)
        self.sensor_name_label.setObjectName(u"sensor_name_label")
        self.sensor_name_label.setMaximumSize(QSize(60, 30))

        self.thermals_combo_box_layout.addWidget(self.sensor_name_label)

        self.thermal_sensor_name_combo_box = QComboBox(self.thermals_page)
        self.thermal_sensor_name_combo_box.setObjectName(u"thermal_sensor_name_combo_box")
        self.thermal_sensor_name_combo_box.setMinimumSize(QSize(117, 0))
        self.thermal_sensor_name_combo_box.setMaximumSize(QSize(70, 30))
        self.thermal_sensor_name_combo_box.setEditable(False)
        self.thermal_sensor_name_combo_box.setInsertPolicy(QComboBox.InsertAtCurrent)

        self.thermals_combo_box_layout.addWidget(self.thermal_sensor_name_combo_box)


        self.thermals_page_layout.addLayout(self.thermals_combo_box_layout)

        self.thermals_graph = PlotWidget(self.thermals_page)
        self.thermals_graph.setObjectName(u"thermals_graph")
        self.thermals_graph.setMinimumSize(QSize(0, 300))
        self.thermals_graph.setStyleSheet(u"QWidget {\n"
"    background-color: transparent;\n"
"    border: 1px solid #30363d;\n"
"    border-radius: 8px;\n"
"	border-bottom-left-radius: 0px; \n"
"	border-bottom-right-radius: 0px;\n"
"}")

        self.thermals_page_layout.addWidget(self.thermals_graph)

        self.thermals_graph_line = QFrame(self.thermals_page)
        self.thermals_graph_line.setObjectName(u"thermals_graph_line")
        self.thermals_graph_line.setFrameShape(QFrame.Shape.HLine)
        self.thermals_graph_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.thermals_page_layout.addWidget(self.thermals_graph_line)

        self.sensors_label = QLabel(self.thermals_page)
        self.sensors_label.setObjectName(u"sensors_label")
        self.sensors_label.setMaximumSize(QSize(16777215, 30))

        self.thermals_page_layout.addWidget(self.sensors_label)

        self.sensors_table = QTableWidget(self.thermals_page)
        if (self.sensors_table.columnCount() < 5):
            self.sensors_table.setColumnCount(5)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.sensors_table.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.sensors_table.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.sensors_table.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.sensors_table.setHorizontalHeaderItem(3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.sensors_table.setHorizontalHeaderItem(4, __qtablewidgetitem21)
        self.sensors_table.setObjectName(u"sensors_table")
        self.sensors_table.horizontalHeader().setCascadingSectionResizes(True)

        self.thermals_page_layout.addWidget(self.sensors_table)

        self.performance_stacked_content.addWidget(self.thermals_page)
        self.network_page = QWidget()
        self.network_page.setObjectName(u"network_page")
        self.network_page_layout = QVBoxLayout(self.network_page)
        self.network_page_layout.setObjectName(u"network_page_layout")
        self.performance_stacked_content.addWidget(self.network_page)

        self.performance_content_layout.addWidget(self.performance_stacked_content)


        self.agent_performance_information_layout.addWidget(self.performance_content_widget)

        self.performance_detail_scroll.setWidget(self.agent_performance_information)

        self.performance_detail_page_layout.addWidget(self.performance_detail_scroll)

        self.agent_detail_stacked_content.addWidget(self.performance_detail_page)
        self.hardware_detail_page = QWidget()
        self.hardware_detail_page.setObjectName(u"hardware_detail_page")
        self.hardware_detail_page_layout = QVBoxLayout(self.hardware_detail_page)
        self.hardware_detail_page_layout.setObjectName(u"hardware_detail_page_layout")
        self.hardware_detail_page_layout.setContentsMargins(0, -1, -1, -1)
        self.hardware_label = QLabel(self.hardware_detail_page)
        self.hardware_label.setObjectName(u"hardware_label")
        self.hardware_label.setMinimumSize(QSize(0, 0))
        self.hardware_label.setMaximumSize(QSize(16777215, 30))
        self.hardware_label.setStyleSheet(u"QLabel {\n"
"	font: 600 17pt;\n"
"}\n"
"")
        self.hardware_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.hardware_detail_page_layout.addWidget(self.hardware_label)

        self.hardware_legend_label = QLabel(self.hardware_detail_page)
        self.hardware_legend_label.setObjectName(u"hardware_legend_label")

        self.hardware_detail_page_layout.addWidget(self.hardware_legend_label)

        self.hardware_legend_line = QFrame(self.hardware_detail_page)
        self.hardware_legend_line.setObjectName(u"hardware_legend_line")
        self.hardware_legend_line.setFrameShape(QFrame.Shape.HLine)
        self.hardware_legend_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.hardware_detail_page_layout.addWidget(self.hardware_legend_line)

        self.hardware_info_scroll = QScrollArea(self.hardware_detail_page)
        self.hardware_info_scroll.setObjectName(u"hardware_info_scroll")
        self.hardware_info_scroll.setStyleSheet(u"QScrollArea {\n"
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
        self.hardware_info_scroll.setWidgetResizable(True)
        self.hardware_info_scroll_content = QWidget()
        self.hardware_info_scroll_content.setObjectName(u"hardware_info_scroll_content")
        self.hardware_info_scroll_content.setGeometry(QRect(0, 0, 977, 910))
        self.hardware_info_scroll_content.setMinimumSize(QSize(0, 0))
        self.hardware_info_scroll_content_layout = QVBoxLayout(self.hardware_info_scroll_content)
        self.hardware_info_scroll_content_layout.setSpacing(0)
        self.hardware_info_scroll_content_layout.setObjectName(u"hardware_info_scroll_content_layout")
        self.hardware_info_scroll_content_layout.setContentsMargins(0, 0, 0, 0)
        self.cpu_info_widget = QWidget(self.hardware_info_scroll_content)
        self.cpu_info_widget.setObjectName(u"cpu_info_widget")
        self.cpu_info_widget.setMinimumSize(QSize(0, 250))
        self.cpu_info_widget.setMaximumSize(QSize(16777215, 350))
        self.cpu_info_widget_layout = QVBoxLayout(self.cpu_info_widget)
        self.cpu_info_widget_layout.setObjectName(u"cpu_info_widget_layout")
        self.cpu_info_widget_layout.setContentsMargins(5, 0, 0, 0)
        self.cpu_info_label = QLabel(self.cpu_info_widget)
        self.cpu_info_label.setObjectName(u"cpu_info_label")
        self.cpu_info_label.setMaximumSize(QSize(16777215, 40))
        self.cpu_info_label.setStyleSheet(u"")

        self.cpu_info_widget_layout.addWidget(self.cpu_info_label)

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
        self.cpu_info_box_widget_layout = QHBoxLayout(self.cpu_info_box_widget)
        self.cpu_info_box_widget_layout.setSpacing(0)
        self.cpu_info_box_widget_layout.setObjectName(u"cpu_info_box_widget_layout")
        self.cpu_info_box_widget_layout.setContentsMargins(5, 0, 0, 0)
        self.cpu_info_box_layout = QHBoxLayout()
        self.cpu_info_box_layout.setObjectName(u"cpu_info_box_layout")
        self.cpu_info_rows_widget = QWidget(self.cpu_info_box_widget)
        self.cpu_info_rows_widget.setObjectName(u"cpu_info_rows_widget")
        self.cpu_info_rows_widget.setStyleSheet(u"QLabel {\n"
"	font: 200 12pt;\n"
"	margin-left: 20px;\n"
"}")
        self.cpu_info_rows_widget_layout = QVBoxLayout(self.cpu_info_rows_widget)
        self.cpu_info_rows_widget_layout.setSpacing(0)
        self.cpu_info_rows_widget_layout.setObjectName(u"cpu_info_rows_widget_layout")
        self.cpu_info_rows_widget_layout.setContentsMargins(10, 0, 0, 0)
        self.model_row_label = QLabel(self.cpu_info_rows_widget)
        self.model_row_label.setObjectName(u"model_row_label")
        self.model_row_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.model_row_label.setMargin(0)

        self.cpu_info_rows_widget_layout.addWidget(self.model_row_label)

        self.cores_row_label = QLabel(self.cpu_info_rows_widget)
        self.cores_row_label.setObjectName(u"cores_row_label")
        self.cores_row_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.cores_row_label.setMargin(0)

        self.cpu_info_rows_widget_layout.addWidget(self.cores_row_label)

        self.threads_row_label = QLabel(self.cpu_info_rows_widget)
        self.threads_row_label.setObjectName(u"threads_row_label")
        self.threads_row_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.threads_row_label.setMargin(0)

        self.cpu_info_rows_widget_layout.addWidget(self.threads_row_label)

        self.frequency_row_label = QLabel(self.cpu_info_rows_widget)
        self.frequency_row_label.setObjectName(u"frequency_row_label")
        self.frequency_row_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.frequency_row_label.setMargin(0)

        self.cpu_info_rows_widget_layout.addWidget(self.frequency_row_label)

        self.architecture_row_label = QLabel(self.cpu_info_rows_widget)
        self.architecture_row_label.setObjectName(u"architecture_row_label")
        self.architecture_row_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.architecture_row_label.setMargin(0)

        self.cpu_info_rows_widget_layout.addWidget(self.architecture_row_label)


        self.cpu_info_box_layout.addWidget(self.cpu_info_rows_widget)

        self.cpu_info_values_widget = QWidget(self.cpu_info_box_widget)
        self.cpu_info_values_widget.setObjectName(u"cpu_info_values_widget")
        self.cpu_info_values_widget.setStyleSheet(u"")
        self.cpu_info_values_widget_layout = QVBoxLayout(self.cpu_info_values_widget)
        self.cpu_info_values_widget_layout.setSpacing(0)
        self.cpu_info_values_widget_layout.setObjectName(u"cpu_info_values_widget_layout")
        self.cpu_info_values_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.model_value_label = QLabel(self.cpu_info_values_widget)
        self.model_value_label.setObjectName(u"model_value_label")

        self.cpu_info_values_widget_layout.addWidget(self.model_value_label)

        self.cores_value_label = QLabel(self.cpu_info_values_widget)
        self.cores_value_label.setObjectName(u"cores_value_label")

        self.cpu_info_values_widget_layout.addWidget(self.cores_value_label)

        self.threads_value_label = QLabel(self.cpu_info_values_widget)
        self.threads_value_label.setObjectName(u"threads_value_label")

        self.cpu_info_values_widget_layout.addWidget(self.threads_value_label)

        self.frequency_value_label = QLabel(self.cpu_info_values_widget)
        self.frequency_value_label.setObjectName(u"frequency_value_label")

        self.cpu_info_values_widget_layout.addWidget(self.frequency_value_label)

        self.architecture_value_label = QLabel(self.cpu_info_values_widget)
        self.architecture_value_label.setObjectName(u"architecture_value_label")

        self.cpu_info_values_widget_layout.addWidget(self.architecture_value_label)


        self.cpu_info_box_layout.addWidget(self.cpu_info_values_widget)


        self.cpu_info_box_widget_layout.addLayout(self.cpu_info_box_layout)


        self.cpu_info_widget_layout.addWidget(self.cpu_info_box_widget)


        self.hardware_info_scroll_content_layout.addWidget(self.cpu_info_widget)

        self.memory_info_widget = QWidget(self.hardware_info_scroll_content)
        self.memory_info_widget.setObjectName(u"memory_info_widget")
        self.memory_info_widget.setMinimumSize(QSize(0, 180))
        self.memory_info_widget.setMaximumSize(QSize(16777215, 350))
        self.memory_info_widget_layout = QVBoxLayout(self.memory_info_widget)
        self.memory_info_widget_layout.setObjectName(u"memory_info_widget_layout")
        self.memory_info_widget_layout.setContentsMargins(5, 0, 0, 0)
        self.memory_info_label = QLabel(self.memory_info_widget)
        self.memory_info_label.setObjectName(u"memory_info_label")
        self.memory_info_label.setMaximumSize(QSize(16777215, 40))
        self.memory_info_label.setStyleSheet(u"")

        self.memory_info_widget_layout.addWidget(self.memory_info_label)

        self.memory_info_box_widget = QWidget(self.memory_info_widget)
        self.memory_info_box_widget.setObjectName(u"memory_info_box_widget")
        self.memory_info_box_widget.setMaximumSize(QSize(500, 100))
        self.memory_info_box_widget.setStyleSheet(u"#memory_info_box_widget {\n"
"    background-color: #161b22;\n"
"	border: 1px solid #30363d;\n"
"	margin-left: 5px;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"#memory_info_box_widget QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.memory_info_box_widget_layout = QHBoxLayout(self.memory_info_box_widget)
        self.memory_info_box_widget_layout.setSpacing(0)
        self.memory_info_box_widget_layout.setObjectName(u"memory_info_box_widget_layout")
        self.memory_info_box_widget_layout.setContentsMargins(5, 0, 0, 0)
        self.memory_info_box_layout = QHBoxLayout()
        self.memory_info_box_layout.setObjectName(u"memory_info_box_layout")
        self.memory_info_columns_widget = QWidget(self.memory_info_box_widget)
        self.memory_info_columns_widget.setObjectName(u"memory_info_columns_widget")
        self.memory_info_columns_widget.setStyleSheet(u"QLabel {\n"
"	font: 200 12pt;\n"
"	margin-left: 20px;\n"
"}")
        self.memory_info_columns_widget_layout = QVBoxLayout(self.memory_info_columns_widget)
        self.memory_info_columns_widget_layout.setSpacing(0)
        self.memory_info_columns_widget_layout.setObjectName(u"memory_info_columns_widget_layout")
        self.memory_info_columns_widget_layout.setContentsMargins(10, 0, 0, 0)
        self.memory_total_row_label = QLabel(self.memory_info_columns_widget)
        self.memory_total_row_label.setObjectName(u"memory_total_row_label")
        self.memory_total_row_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.memory_total_row_label.setMargin(0)

        self.memory_info_columns_widget_layout.addWidget(self.memory_total_row_label)

        self.memory_type_row_label = QLabel(self.memory_info_columns_widget)
        self.memory_type_row_label.setObjectName(u"memory_type_row_label")
        self.memory_type_row_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.memory_type_row_label.setMargin(0)

        self.memory_info_columns_widget_layout.addWidget(self.memory_type_row_label)

        self.memory_speed_row_label = QLabel(self.memory_info_columns_widget)
        self.memory_speed_row_label.setObjectName(u"memory_speed_row_label")
        self.memory_speed_row_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.memory_speed_row_label.setMargin(0)

        self.memory_info_columns_widget_layout.addWidget(self.memory_speed_row_label)


        self.memory_info_box_layout.addWidget(self.memory_info_columns_widget)

        self.memory_info_values_widget = QWidget(self.memory_info_box_widget)
        self.memory_info_values_widget.setObjectName(u"memory_info_values_widget")
        self.memory_info_values_widget.setStyleSheet(u"")
        self.memory_info_values_widget_layout = QVBoxLayout(self.memory_info_values_widget)
        self.memory_info_values_widget_layout.setSpacing(0)
        self.memory_info_values_widget_layout.setObjectName(u"memory_info_values_widget_layout")
        self.memory_info_values_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.memory_total_value_label = QLabel(self.memory_info_values_widget)
        self.memory_total_value_label.setObjectName(u"memory_total_value_label")

        self.memory_info_values_widget_layout.addWidget(self.memory_total_value_label)

        self.memory_type_value_label = QLabel(self.memory_info_values_widget)
        self.memory_type_value_label.setObjectName(u"memory_type_value_label")

        self.memory_info_values_widget_layout.addWidget(self.memory_type_value_label)

        self.memory_speed_value_label = QLabel(self.memory_info_values_widget)
        self.memory_speed_value_label.setObjectName(u"memory_speed_value_label")

        self.memory_info_values_widget_layout.addWidget(self.memory_speed_value_label)


        self.memory_info_box_layout.addWidget(self.memory_info_values_widget)


        self.memory_info_box_widget_layout.addLayout(self.memory_info_box_layout)


        self.memory_info_widget_layout.addWidget(self.memory_info_box_widget)


        self.hardware_info_scroll_content_layout.addWidget(self.memory_info_widget)

        self.gpu_info_widget = QWidget(self.hardware_info_scroll_content)
        self.gpu_info_widget.setObjectName(u"gpu_info_widget")
        self.gpu_info_widget.setMinimumSize(QSize(0, 150))
        self.gpu_info_widget.setMaximumSize(QSize(16777215, 350))
        self.gpu_info_widget_layout = QVBoxLayout(self.gpu_info_widget)
        self.gpu_info_widget_layout.setObjectName(u"gpu_info_widget_layout")
        self.gpu_info_widget_layout.setContentsMargins(5, 0, 0, 0)
        self.gpu_info_label = QLabel(self.gpu_info_widget)
        self.gpu_info_label.setObjectName(u"gpu_info_label")
        self.gpu_info_label.setMaximumSize(QSize(16777215, 40))
        self.gpu_info_label.setStyleSheet(u"")

        self.gpu_info_widget_layout.addWidget(self.gpu_info_label)

        self.gpu_info_box_widget = QWidget(self.gpu_info_widget)
        self.gpu_info_box_widget.setObjectName(u"gpu_info_box_widget")
        self.gpu_info_box_widget.setMaximumSize(QSize(500, 100))
        self.gpu_info_box_widget.setStyleSheet(u"#gpu_info_box_widget {\n"
"    background-color: #161b22;\n"
"	border: 1px solid #30363d;\n"
"	margin-left: 5px;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"#gpu_info_box_widget QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.gpu_info_box_widget_layout = QHBoxLayout(self.gpu_info_box_widget)
        self.gpu_info_box_widget_layout.setSpacing(0)
        self.gpu_info_box_widget_layout.setObjectName(u"gpu_info_box_widget_layout")
        self.gpu_info_box_widget_layout.setContentsMargins(5, 0, 0, 0)
        self.gpu_info_box_layout = QHBoxLayout()
        self.gpu_info_box_layout.setObjectName(u"gpu_info_box_layout")
        self.gpu_info_columns_widget = QWidget(self.gpu_info_box_widget)
        self.gpu_info_columns_widget.setObjectName(u"gpu_info_columns_widget")
        self.gpu_info_columns_widget.setStyleSheet(u"QLabel {\n"
"	font: 200 12pt;\n"
"	margin-left: 20px;\n"
"}")
        self.gpu_info_columns_widget_layout = QVBoxLayout(self.gpu_info_columns_widget)
        self.gpu_info_columns_widget_layout.setSpacing(0)
        self.gpu_info_columns_widget_layout.setObjectName(u"gpu_info_columns_widget_layout")
        self.gpu_info_columns_widget_layout.setContentsMargins(10, 0, 0, 0)
        self.gpu_model_type_row_label = QLabel(self.gpu_info_columns_widget)
        self.gpu_model_type_row_label.setObjectName(u"gpu_model_type_row_label")
        self.gpu_model_type_row_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gpu_model_type_row_label.setMargin(0)

        self.gpu_info_columns_widget_layout.addWidget(self.gpu_model_type_row_label)

        self.gpu_vram_row_label = QLabel(self.gpu_info_columns_widget)
        self.gpu_vram_row_label.setObjectName(u"gpu_vram_row_label")
        self.gpu_vram_row_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gpu_vram_row_label.setMargin(0)

        self.gpu_info_columns_widget_layout.addWidget(self.gpu_vram_row_label)

        self.gpu_memory_type_row_label = QLabel(self.gpu_info_columns_widget)
        self.gpu_memory_type_row_label.setObjectName(u"gpu_memory_type_row_label")
        self.gpu_memory_type_row_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gpu_memory_type_row_label.setMargin(0)

        self.gpu_info_columns_widget_layout.addWidget(self.gpu_memory_type_row_label)


        self.gpu_info_box_layout.addWidget(self.gpu_info_columns_widget)

        self.gpu_info_values_widget = QWidget(self.gpu_info_box_widget)
        self.gpu_info_values_widget.setObjectName(u"gpu_info_values_widget")
        self.gpu_info_values_widget.setStyleSheet(u"")
        self.gpu_info_values_widget_layout = QVBoxLayout(self.gpu_info_values_widget)
        self.gpu_info_values_widget_layout.setSpacing(0)
        self.gpu_info_values_widget_layout.setObjectName(u"gpu_info_values_widget_layout")
        self.gpu_info_values_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.gpu_model_type_value_label = QLabel(self.gpu_info_values_widget)
        self.gpu_model_type_value_label.setObjectName(u"gpu_model_type_value_label")

        self.gpu_info_values_widget_layout.addWidget(self.gpu_model_type_value_label)

        self.gpu_vram_value_label = QLabel(self.gpu_info_values_widget)
        self.gpu_vram_value_label.setObjectName(u"gpu_vram_value_label")

        self.gpu_info_values_widget_layout.addWidget(self.gpu_vram_value_label)

        self.gpu_memory_type_value_label = QLabel(self.gpu_info_values_widget)
        self.gpu_memory_type_value_label.setObjectName(u"gpu_memory_type_value_label")

        self.gpu_info_values_widget_layout.addWidget(self.gpu_memory_type_value_label)


        self.gpu_info_box_layout.addWidget(self.gpu_info_values_widget)


        self.gpu_info_box_widget_layout.addLayout(self.gpu_info_box_layout)


        self.gpu_info_widget_layout.addWidget(self.gpu_info_box_widget)


        self.hardware_info_scroll_content_layout.addWidget(self.gpu_info_widget)

        self.motherboard_info_widget = QWidget(self.hardware_info_scroll_content)
        self.motherboard_info_widget.setObjectName(u"motherboard_info_widget")
        self.motherboard_info_widget.setMinimumSize(QSize(0, 180))
        self.motherboard_info_widget.setMaximumSize(QSize(16777215, 350))
        self.motherboard_info_widget_layout = QVBoxLayout(self.motherboard_info_widget)
        self.motherboard_info_widget_layout.setObjectName(u"motherboard_info_widget_layout")
        self.motherboard_info_widget_layout.setContentsMargins(5, 0, 0, 0)
        self.motherboard_info_label = QLabel(self.motherboard_info_widget)
        self.motherboard_info_label.setObjectName(u"motherboard_info_label")
        self.motherboard_info_label.setMaximumSize(QSize(16777215, 40))
        self.motherboard_info_label.setStyleSheet(u"")

        self.motherboard_info_widget_layout.addWidget(self.motherboard_info_label)

        self.motherboard_info_box_widget = QWidget(self.motherboard_info_widget)
        self.motherboard_info_box_widget.setObjectName(u"motherboard_info_box_widget")
        self.motherboard_info_box_widget.setMaximumSize(QSize(500, 150))
        self.motherboard_info_box_widget.setStyleSheet(u"#motherboard_info_box_widget {\n"
"    background-color: #161b22;\n"
"	border: 1px solid #30363d;\n"
"	margin-left: 5px;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"#motherboard_info_box_widget QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.motherboard_info_box_widget_layout = QHBoxLayout(self.motherboard_info_box_widget)
        self.motherboard_info_box_widget_layout.setSpacing(0)
        self.motherboard_info_box_widget_layout.setObjectName(u"motherboard_info_box_widget_layout")
        self.motherboard_info_box_widget_layout.setContentsMargins(5, 0, 0, 0)
        self.motherboard_info_box_layout = QHBoxLayout()
        self.motherboard_info_box_layout.setObjectName(u"motherboard_info_box_layout")
        self.motherboard_info_columns_widget = QWidget(self.motherboard_info_box_widget)
        self.motherboard_info_columns_widget.setObjectName(u"motherboard_info_columns_widget")
        self.motherboard_info_columns_widget.setStyleSheet(u"QLabel {\n"
"	font: 200 12pt;\n"
"	margin-left: 20px;\n"
"}")
        self.motherboard_info_columns_widget_layout = QVBoxLayout(self.motherboard_info_columns_widget)
        self.motherboard_info_columns_widget_layout.setSpacing(0)
        self.motherboard_info_columns_widget_layout.setObjectName(u"motherboard_info_columns_widget_layout")
        self.motherboard_info_columns_widget_layout.setContentsMargins(10, 0, 0, 0)
        self.motherboard_vendor_column_label = QLabel(self.motherboard_info_columns_widget)
        self.motherboard_vendor_column_label.setObjectName(u"motherboard_vendor_column_label")
        self.motherboard_vendor_column_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.motherboard_vendor_column_label.setMargin(0)

        self.motherboard_info_columns_widget_layout.addWidget(self.motherboard_vendor_column_label)

        self.motherboard_model_column_label = QLabel(self.motherboard_info_columns_widget)
        self.motherboard_model_column_label.setObjectName(u"motherboard_model_column_label")
        self.motherboard_model_column_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.motherboard_model_column_label.setMargin(0)

        self.motherboard_info_columns_widget_layout.addWidget(self.motherboard_model_column_label)

        self.motherboard_serial_column_label = QLabel(self.motherboard_info_columns_widget)
        self.motherboard_serial_column_label.setObjectName(u"motherboard_serial_column_label")
        self.motherboard_serial_column_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.motherboard_serial_column_label.setMargin(0)

        self.motherboard_info_columns_widget_layout.addWidget(self.motherboard_serial_column_label)

        self.motherboard_architecture_column_label = QLabel(self.motherboard_info_columns_widget)
        self.motherboard_architecture_column_label.setObjectName(u"motherboard_architecture_column_label")
        self.motherboard_architecture_column_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.motherboard_architecture_column_label.setMargin(0)

        self.motherboard_info_columns_widget_layout.addWidget(self.motherboard_architecture_column_label)


        self.motherboard_info_box_layout.addWidget(self.motherboard_info_columns_widget)

        self.motherboard_info_values_widget = QWidget(self.motherboard_info_box_widget)
        self.motherboard_info_values_widget.setObjectName(u"motherboard_info_values_widget")
        self.motherboard_info_values_widget.setStyleSheet(u"")
        self.motherboard_info_values_widget_layout = QVBoxLayout(self.motherboard_info_values_widget)
        self.motherboard_info_values_widget_layout.setSpacing(0)
        self.motherboard_info_values_widget_layout.setObjectName(u"motherboard_info_values_widget_layout")
        self.motherboard_info_values_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.motherboard_vendor_value_label = QLabel(self.motherboard_info_values_widget)
        self.motherboard_vendor_value_label.setObjectName(u"motherboard_vendor_value_label")

        self.motherboard_info_values_widget_layout.addWidget(self.motherboard_vendor_value_label)

        self.motherboard_model_value_label = QLabel(self.motherboard_info_values_widget)
        self.motherboard_model_value_label.setObjectName(u"motherboard_model_value_label")

        self.motherboard_info_values_widget_layout.addWidget(self.motherboard_model_value_label)

        self.motherboard_serial_value_label = QLabel(self.motherboard_info_values_widget)
        self.motherboard_serial_value_label.setObjectName(u"motherboard_serial_value_label")

        self.motherboard_info_values_widget_layout.addWidget(self.motherboard_serial_value_label)

        self.motherboard_architecture_value_label = QLabel(self.motherboard_info_values_widget)
        self.motherboard_architecture_value_label.setObjectName(u"motherboard_architecture_value_label")

        self.motherboard_info_values_widget_layout.addWidget(self.motherboard_architecture_value_label)


        self.motherboard_info_box_layout.addWidget(self.motherboard_info_values_widget)


        self.motherboard_info_box_widget_layout.addLayout(self.motherboard_info_box_layout)


        self.motherboard_info_widget_layout.addWidget(self.motherboard_info_box_widget)


        self.hardware_info_scroll_content_layout.addWidget(self.motherboard_info_widget)

        self.bios_info_widget = QWidget(self.hardware_info_scroll_content)
        self.bios_info_widget.setObjectName(u"bios_info_widget")
        self.bios_info_widget.setMinimumSize(QSize(0, 150))
        self.bios_info_widget.setMaximumSize(QSize(16777215, 350))
        self.bios_info_widget_layout = QVBoxLayout(self.bios_info_widget)
        self.bios_info_widget_layout.setObjectName(u"bios_info_widget_layout")
        self.bios_info_widget_layout.setContentsMargins(5, 0, 0, 0)
        self.bios_info_label = QLabel(self.bios_info_widget)
        self.bios_info_label.setObjectName(u"bios_info_label")
        self.bios_info_label.setMaximumSize(QSize(16777215, 40))
        self.bios_info_label.setStyleSheet(u"")

        self.bios_info_widget_layout.addWidget(self.bios_info_label)

        self.bios_info_box_widget = QWidget(self.bios_info_widget)
        self.bios_info_box_widget.setObjectName(u"bios_info_box_widget")
        self.bios_info_box_widget.setMaximumSize(QSize(500, 100))
        self.bios_info_box_widget.setStyleSheet(u"#bios_info_box_widget {\n"
"    background-color: #161b22;\n"
"	border: 1px solid #30363d;\n"
"	margin-left: 5px;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"#bios_info_box_widget QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.bios_info_box_widget_layout = QHBoxLayout(self.bios_info_box_widget)
        self.bios_info_box_widget_layout.setSpacing(0)
        self.bios_info_box_widget_layout.setObjectName(u"bios_info_box_widget_layout")
        self.bios_info_box_widget_layout.setContentsMargins(5, 0, 0, 0)
        self.bios_info_box_layout = QHBoxLayout()
        self.bios_info_box_layout.setObjectName(u"bios_info_box_layout")
        self.bios_info_columns_widget = QWidget(self.bios_info_box_widget)
        self.bios_info_columns_widget.setObjectName(u"bios_info_columns_widget")
        self.bios_info_columns_widget.setStyleSheet(u"QLabel {\n"
"	font: 200 12pt;\n"
"	margin-left: 20px;\n"
"}")
        self.bios_info_columns_widget_layout = QVBoxLayout(self.bios_info_columns_widget)
        self.bios_info_columns_widget_layout.setSpacing(0)
        self.bios_info_columns_widget_layout.setObjectName(u"bios_info_columns_widget_layout")
        self.bios_info_columns_widget_layout.setContentsMargins(10, 0, 0, 0)
        self.bios_vendor_row_label = QLabel(self.bios_info_columns_widget)
        self.bios_vendor_row_label.setObjectName(u"bios_vendor_row_label")
        self.bios_vendor_row_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.bios_vendor_row_label.setMargin(0)

        self.bios_info_columns_widget_layout.addWidget(self.bios_vendor_row_label)

        self.bios_version_row_label = QLabel(self.bios_info_columns_widget)
        self.bios_version_row_label.setObjectName(u"bios_version_row_label")
        self.bios_version_row_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.bios_version_row_label.setMargin(0)

        self.bios_info_columns_widget_layout.addWidget(self.bios_version_row_label)

        self.bios_date_row_label = QLabel(self.bios_info_columns_widget)
        self.bios_date_row_label.setObjectName(u"bios_date_row_label")
        self.bios_date_row_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.bios_date_row_label.setMargin(0)

        self.bios_info_columns_widget_layout.addWidget(self.bios_date_row_label)


        self.bios_info_box_layout.addWidget(self.bios_info_columns_widget)

        self.bios_info_values_widget = QWidget(self.bios_info_box_widget)
        self.bios_info_values_widget.setObjectName(u"bios_info_values_widget")
        self.bios_info_values_widget.setStyleSheet(u"")
        self.bios_info_values_widget_layout = QVBoxLayout(self.bios_info_values_widget)
        self.bios_info_values_widget_layout.setSpacing(0)
        self.bios_info_values_widget_layout.setObjectName(u"bios_info_values_widget_layout")
        self.bios_info_values_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.bios_vendor_value_label = QLabel(self.bios_info_values_widget)
        self.bios_vendor_value_label.setObjectName(u"bios_vendor_value_label")

        self.bios_info_values_widget_layout.addWidget(self.bios_vendor_value_label)

        self.bios_version_value_label = QLabel(self.bios_info_values_widget)
        self.bios_version_value_label.setObjectName(u"bios_version_value_label")

        self.bios_info_values_widget_layout.addWidget(self.bios_version_value_label)

        self.bios_date_value_label = QLabel(self.bios_info_values_widget)
        self.bios_date_value_label.setObjectName(u"bios_date_value_label")

        self.bios_info_values_widget_layout.addWidget(self.bios_date_value_label)


        self.bios_info_box_layout.addWidget(self.bios_info_values_widget)


        self.bios_info_box_widget_layout.addLayout(self.bios_info_box_layout)


        self.bios_info_widget_layout.addWidget(self.bios_info_box_widget)


        self.hardware_info_scroll_content_layout.addWidget(self.bios_info_widget)

        self.hardware_info_scroll.setWidget(self.hardware_info_scroll_content)

        self.hardware_detail_page_layout.addWidget(self.hardware_info_scroll)

        self.agent_detail_stacked_content.addWidget(self.hardware_detail_page)

        self.agent_detail_content_layout.addWidget(self.agent_detail_stacked_content)


        self.agent_detail_page_layout.addWidget(self.agent_detail_content)

        self.content_stack.addWidget(self.agent_detail_page)

        self.central_content_layout.addWidget(self.content_stack)

        MainWindow.setCentralWidget(self.central_content)

        self.retranslateUi(MainWindow)

        self.content_stack.setCurrentIndex(2)
        self.agent_detail_stacked_content.setCurrentIndex(0)
        self.performance_stacked_content.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"NexoraControl", None))
        self.nexora_logo.setText(QCoreApplication.translate("MainWindow", u"NEXORA", None))
        self.dashboard_button.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.agents_button.setText(QCoreApplication.translate("MainWindow", u"Agents", None))
        self.commands_button.setText(QCoreApplication.translate("MainWindow", u"Commands", None))
        self.logs_button.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.about_button.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.dashboard_label.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.dashboard_legend_label.setText(QCoreApplication.translate("MainWindow", u"Fleet availability metrics", None))
        self.agent_label.setText(QCoreApplication.translate("MainWindow", u"Agents", None))
        self.agents_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.online_label.setText(QCoreApplication.translate("MainWindow", u"Online", None))
        self.online_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.offline_label.setText(QCoreApplication.translate("MainWindow", u"Offline", None))
        self.offline_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.agents_label.setText(QCoreApplication.translate("MainWindow", u"AGENTS", None))
        self.agents_table_legend_label.setText(QCoreApplication.translate("MainWindow", u"Endpoint telemetry, host metrics and execution status", None))
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
        self.agents_headline_label.setText(QCoreApplication.translate("MainWindow", u"AGENTS", None))
        self.page_description_label.setText(QCoreApplication.translate("MainWindow", u"Manage connected machines", None))
        self.search_input_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
        self.refresh_agents_button.setText(QCoreApplication.translate("MainWindow", u"[ Refresh ]", None))
        self.back_to_agents_button.setText(QCoreApplication.translate("MainWindow", u"[ \u2190 Back to Agents ]", None))
        self.detail_top_agent_name_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.detail_top_agent_status_label.setText(QCoreApplication.translate("MainWindow", u"\u25cb OFFLINE", None))
        self.overview_nav_button.setText(QCoreApplication.translate("MainWindow", u"[ Overview ]", None))
        self.performance_nav_button.setText(QCoreApplication.translate("MainWindow", u"[ Performance ]", None))
        self.hardware_nav_button.setText(QCoreApplication.translate("MainWindow", u"[ Hardware ]", None))
        self.commands_nav_button.setText(QCoreApplication.translate("MainWindow", u"[ Commands ]", None))
        self.overview_label.setText(QCoreApplication.translate("MainWindow", u"OVERVIEW", None))
        self.overview_legend_label.setText(QCoreApplication.translate("MainWindow", u"System health, resource utilization and real-time activity summary", None))
        self.cpu_label.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_load_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.ram_label.setText(QCoreApplication.translate("MainWindow", u"RAM", None))
        self.ram_load_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.disk_label.setText(QCoreApplication.translate("MainWindow", u"DISK", None))
        self.disk_load_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.uptime_label.setText(QCoreApplication.translate("MainWindow", u"UPTIME", None))
        self.up_time_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.system_status_label.setText(QCoreApplication.translate("MainWindow", u"SYSTEM STATUS", None))
        self.agent_row_label.setText(QCoreApplication.translate("MainWindow", u"Agent", None))
        self.last_seen_row_label.setText(QCoreApplication.translate("MainWindow", u"Last seen", None))
        self.ip_row_label.setText(QCoreApplication.translate("MainWindow", u"IP", None))
        self.hostname_row_label.setText(QCoreApplication.translate("MainWindow", u"Hostname", None))
        self.os_name_row_label.setText(QCoreApplication.translate("MainWindow", u"OS", None))
        self.agent_status_value_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.last_seen_value_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.ip_value_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.hostname_value_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.os_name_value_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.quick_actions_label.setText(QCoreApplication.translate("MainWindow", u"QUICK ACTIONS ", None))
        self.restart_all_docker_cont_quick_button.setText(QCoreApplication.translate("MainWindow", u"[ Restart All Docker Containers ]", None))
        self.stop_all_docker_cont_quick_button.setText(QCoreApplication.translate("MainWindow", u"[ Stop All Docker Containers ]", None))
        self.docker_ps_quick_button.setText(QCoreApplication.translate("MainWindow", u"[ Docker PS ]", None))
        self.reboot_quick_button.setText(QCoreApplication.translate("MainWindow", u"[ Reboot ] ", None))
        self.recent_commands_label.setText(QCoreApplication.translate("MainWindow", u"RECENT COMMANDS", None))
        self.performance_label.setText(QCoreApplication.translate("MainWindow", u"PERFORMANCE", None))
        self.performance_legend_label.setText(QCoreApplication.translate("MainWindow", u"Real-time resource tracking, system workloads and efficiency metrics", None))
        self.compute_button.setText(QCoreApplication.translate("MainWindow", u"[ COMPUTE ]", None))
        self.storage_button.setText(QCoreApplication.translate("MainWindow", u"[ STORAGE ]", None))
        self.thermals_button.setText(QCoreApplication.translate("MainWindow", u"[ THERMALS ]", None))
        self.network_button.setText(QCoreApplication.translate("MainWindow", u"[ NETWORK ]", None))
        self.compute_label.setText(QCoreApplication.translate("MainWindow", u"COMPUTE", None))
        self.compute_legend_label.setText(QCoreApplication.translate("MainWindow", u"Processor load, per-core performance and system memory tracking", None))
        self.compute_current_state_label.setText(QCoreApplication.translate("MainWindow", u"CURRENT STATE", None))
        self.cpu_ram_metric_label.setText(QCoreApplication.translate("MainWindow", u"CPU / RAM UTILIZATION", None))
        self.memory_label.setText(QCoreApplication.translate("MainWindow", u"MEMORY", None))
        self.used_memory_label.setText(QCoreApplication.translate("MainWindow", u"Used", None))
        self.used_memory_value_label.setText(QCoreApplication.translate("MainWindow", u"0 GB", None))
        self.available_memory_label.setText(QCoreApplication.translate("MainWindow", u"Available", None))
        self.available_memory_value_label.setText(QCoreApplication.translate("MainWindow", u"0 GB", None))
        self.swap_memory_label.setText(QCoreApplication.translate("MainWindow", u"Swap", None))
        self.swap_memory_value_label.setText(QCoreApplication.translate("MainWindow", u"0.0 GB", None))
        self.compute_load_average_label.setText(QCoreApplication.translate("MainWindow", u"LOAD AVERAGE", None))
        self.compute_cpu_cores_label.setText(QCoreApplication.translate("MainWindow", u"CPU CORES", None))
        self.storage_label.setText(QCoreApplication.translate("MainWindow", u"STORAGE", None))
        self.storage_legend_label.setText(QCoreApplication.translate("MainWindow", u"Disk capacity, I/O activity and storage devices", None))
        self.current_storage_label.setText(QCoreApplication.translate("MainWindow", u"CURRENT STORAGE", None))
        self.disk_io_label.setText(QCoreApplication.translate("MainWindow", u"DISK I/O", None))
        self.disks_combo_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ALL DISKS", None))
        self.disk_data_unit_combo_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UNIT", None))
        self.disk_i_o_summary_label.setText(QCoreApplication.translate("MainWindow", u"I/O SUMMARY", None))
        self.disk_read_information_label.setText(QCoreApplication.translate("MainWindow", u"Read", None))
        self.disk_read_information_value.setText(QCoreApplication.translate("MainWindow", u"0.0 MB/s", None))
        self.disk_write_information_label.setText(QCoreApplication.translate("MainWindow", u"Write", None))
        self.disk_write_information_value.setText(QCoreApplication.translate("MainWindow", u"0.0 MB/s", None))
        self.disk_read_per_sec_information_label.setText(QCoreApplication.translate("MainWindow", u"Read IOPS", None))
        self.disk_read_per_sec_information_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.disk_write_per_sec_information_label.setText(QCoreApplication.translate("MainWindow", u"Write IOPS", None))
        self.disk_write_per_sec_information_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.disk_avg_latency_label.setText(QCoreApplication.translate("MainWindow", u"Avg latency", None))
        self.disk_avg_latency_value.setText(QCoreApplication.translate("MainWindow", u"0 ms", None))
        self.file_systems_label.setText(QCoreApplication.translate("MainWindow", u"FILESYSTEMS", None))
        ___qtablewidgetitem6 = self.file_systems_table.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"MOUNT", None))
        ___qtablewidgetitem7 = self.file_systems_table.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"DEVICE", None))
        ___qtablewidgetitem8 = self.file_systems_table.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"TYPE", None))
        ___qtablewidgetitem9 = self.file_systems_table.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"USED", None))
        ___qtablewidgetitem10 = self.file_systems_table.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"AVAILABLE", None))
        ___qtablewidgetitem11 = self.file_systems_table.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"USAGE", None))
        self.storage_devices_label.setText(QCoreApplication.translate("MainWindow", u"STORAGE DEVICES", None))
        ___qtablewidgetitem12 = self.storage_devices_table.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"DEVICE", None))
        ___qtablewidgetitem13 = self.storage_devices_table.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"MODEL", None))
        ___qtablewidgetitem14 = self.storage_devices_table.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"TYPE", None))
        ___qtablewidgetitem15 = self.storage_devices_table.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"CAPACITY", None))
        ___qtablewidgetitem16 = self.storage_devices_table.horizontalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"STATUS", None))
        self.thermals_label.setText(QCoreApplication.translate("MainWindow", u"THERMALS", None))
        self.thermals_legend_label.setText(QCoreApplication.translate("MainWindow", u"Temperature sensors and thermal activity", None))
        self.current_thermals_label.setText(QCoreApplication.translate("MainWindow", u"CURRENT THERMALS", None))
        self.temperature_history_label.setText(QCoreApplication.translate("MainWindow", u"TEMPERATURE HISTORY", None))
        self.sensor_group_label.setText(QCoreApplication.translate("MainWindow", u"SENSOR GROUP", None))
        self.sensor_group_combo_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"GROUP", None))
        self.sensor_name_label.setText(QCoreApplication.translate("MainWindow", u"SENSOR", None))
        self.thermal_sensor_name_combo_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NAME", None))
        self.sensors_label.setText(QCoreApplication.translate("MainWindow", u"SENSORS", None))
        ___qtablewidgetitem17 = self.sensors_table.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"GROUP", None))
        ___qtablewidgetitem18 = self.sensors_table.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"SENSOR", None))
        ___qtablewidgetitem19 = self.sensors_table.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"CURRENT", None))
        ___qtablewidgetitem20 = self.sensors_table.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"HIGH", None))
        ___qtablewidgetitem21 = self.sensors_table.horizontalHeaderItem(4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"CRITICAL", None))
        self.hardware_label.setText(QCoreApplication.translate("MainWindow", u"HARDWARE", None))
        self.hardware_legend_label.setText(QCoreApplication.translate("MainWindow", u"Component specifications, hardware model data and system architecture", None))
        self.cpu_info_label.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.model_row_label.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.cores_row_label.setText(QCoreApplication.translate("MainWindow", u"Cores", None))
        self.threads_row_label.setText(QCoreApplication.translate("MainWindow", u"Threads", None))
        self.frequency_row_label.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.architecture_row_label.setText(QCoreApplication.translate("MainWindow", u"Architecture", None))
        self.model_value_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.cores_value_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.threads_value_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.frequency_value_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.architecture_value_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.memory_info_label.setText(QCoreApplication.translate("MainWindow", u"MEMORY", None))
        self.memory_total_row_label.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.memory_type_row_label.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.memory_speed_row_label.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.memory_total_value_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.memory_type_value_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.memory_speed_value_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.gpu_info_label.setText(QCoreApplication.translate("MainWindow", u"GPU", None))
        self.gpu_model_type_row_label.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.gpu_vram_row_label.setText(QCoreApplication.translate("MainWindow", u"VRAM", None))
        self.gpu_memory_type_row_label.setText(QCoreApplication.translate("MainWindow", u"Memory Type", None))
        self.gpu_model_type_value_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.gpu_vram_value_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.gpu_memory_type_value_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.motherboard_info_label.setText(QCoreApplication.translate("MainWindow", u"MOTHERBOARD", None))
        self.motherboard_vendor_column_label.setText(QCoreApplication.translate("MainWindow", u"Vendor", None))
        self.motherboard_model_column_label.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.motherboard_serial_column_label.setText(QCoreApplication.translate("MainWindow", u"Serial", None))
        self.motherboard_architecture_column_label.setText(QCoreApplication.translate("MainWindow", u"Architecture", None))
        self.motherboard_vendor_value_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.motherboard_model_value_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.motherboard_serial_value_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.motherboard_architecture_value_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.bios_info_label.setText(QCoreApplication.translate("MainWindow", u"BIOS", None))
        self.bios_vendor_row_label.setText(QCoreApplication.translate("MainWindow", u"Vendor", None))
        self.bios_version_row_label.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.bios_date_row_label.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.bios_vendor_value_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.bios_version_value_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.bios_date_value_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
    # retranslateUi

