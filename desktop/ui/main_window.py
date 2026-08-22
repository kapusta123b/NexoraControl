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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(993, 564)
        icon = QIcon()
        iconThemeName = u"camera-photo"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

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
"    transition: background-color 0.2s, color 0.2s;\n"
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
"	background-color: rgba(244, 244, 244, 164);\n"
"\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.central_content)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
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


        self.horizontalLayout.addWidget(self.left_panel)

        self.content_stack = QStackedWidget(self.central_content)
        self.content_stack.setObjectName(u"content_stack")
        self.content_stack.setMinimumSize(QSize(500, 411))
        self.content_stack.setMaximumSize(QSize(801, 623))
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
        self.agents_table.setMaximumSize(QSize(787, 282))
        self.agents_table.setStyleSheet(u"border-top-right: none;")
        self.agents_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.agents_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.agents_table.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.agents_table.horizontalHeader().setCascadingSectionResizes(True)
        self.agents_table.horizontalHeader().setMinimumSectionSize(20)
        self.agents_table.horizontalHeader().setDefaultSectionSize(130)
        self.agents_table.horizontalHeader().setHighlightSections(True)
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
        self.add_agent_button = QPushButton(self.dashboard_page)
        self.add_agent_button.setObjectName(u"add_agent_button")
        self.add_agent_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_agent_button.setLayoutDirection(Qt.LeftToRight)

        self.layout_buttons.addWidget(self.add_agent_button)

        self.refresh_table_button = QPushButton(self.dashboard_page)
        self.refresh_table_button.setObjectName(u"refresh_table_button")
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
        self.add_agent_button_2 = QPushButton(self.agents_page)
        self.add_agent_button_2.setObjectName(u"add_agent_button_2")
        self.add_agent_button_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.help_bar_layout.addWidget(self.add_agent_button_2)

        self.horizontalSpacer_3 = QSpacerItem(65, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.help_bar_layout.addItem(self.horizontalSpacer_3)

        self.search_input_line = QLineEdit(self.agents_page)
        self.search_input_line.setObjectName(u"search_input_line")
        self.search_input_line.setClearButtonEnabled(False)

        self.help_bar_layout.addWidget(self.search_input_line)

        self.verticalSpacer_3 = QSpacerItem(23, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.help_bar_layout.addItem(self.verticalSpacer_3)

        self.refresh_agents_button = QPushButton(self.agents_page)
        self.refresh_agents_button.setObjectName(u"refresh_agents_button")
        self.refresh_agents_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.help_bar_layout.addWidget(self.refresh_agents_button)

        self.horizontalSpacer_5 = QSpacerItem(39, 42, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.help_bar_layout.addItem(self.horizontalSpacer_5)


        self.agents_main_layout.addLayout(self.help_bar_layout)

        self.verticalSpacer_4 = QSpacerItem(20, 17, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.agents_main_layout.addItem(self.verticalSpacer_4)

        self.agent_list = QScrollArea(self.agents_page)
        self.agent_list.setObjectName(u"agent_list")
        self.agent_list.setMaximumSize(QSize(16777215, 350))
        self.agent_list.setStyleSheet(u"QScrollArea {\n"
"    border: none;\n"
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
"    border-radius: 4px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #242936;\n"
"    min-height: 20px;\n"
"    border-radius: 4px;\n"
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
        self.agent_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.agent_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.agent_list.setWidgetResizable(False)
        self.agent_list.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.agent_scroll = QWidget()
        self.agent_scroll.setObjectName(u"agent_scroll")
        self.agent_scroll.setGeometry(QRect(0, 0, 777, 500))
        self.agent_scroll.setMaximumSize(QSize(16777215, 1000000))
        self.agent_scroll.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.agent_scroll)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 0, 10, 0)
        self.agent_card = QWidget(self.agent_scroll)
        self.agent_card.setObjectName(u"agent_card")
        self.agent_card.setMinimumSize(QSize(0, 120))
        self.agent_card.setMaximumSize(QSize(16777215, 120))
        self.agent_card.setAcceptDrops(False)
        self.agent_card.setStyleSheet(u"\n"
"QWidget {\n"
"    background-color: #161920;\n"
"    border: 1px solid #242936;\n"
"    border-radius: 4px;\n"
"	border: none;\n"
"}\n"
"QLabel {\n"
"    color: #a5b4fc;\n"
"    border: none;\n"
"    background: transparent;\n"
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
"}")
        self.horizontalLayout_5 = QHBoxLayout(self.agent_card)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, 0, 10, 0)
        self.agent_information_widget = QWidget(self.agent_card)
        self.agent_information_widget.setObjectName(u"agent_information_widget")
        self.agent_information_widget.setMinimumSize(QSize(300, 0))
        self.agent_information_widget.setMaximumSize(QSize(400, 150))
        self.agent_information_widget.setStyleSheet(u"")
        self.horizontalLayout_8 = QHBoxLayout(self.agent_information_widget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.online_dot = QLabel(self.agent_information_widget)
        self.online_dot.setObjectName(u"online_dot")
        self.online_dot.setMaximumSize(QSize(20, 100))
        self.online_dot.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_8.addWidget(self.online_dot)

        self.system_information_widget = QWidget(self.agent_information_widget)
        self.system_information_widget.setObjectName(u"system_information_widget")
        self.verticalLayout_6 = QVBoxLayout(self.system_information_widget)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.vps_name_label = QLabel(self.system_information_widget)
        self.vps_name_label.setObjectName(u"vps_name_label")
        self.vps_name_label.setStyleSheet(u"font: 12pt;")
        self.vps_name_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_6.addWidget(self.vps_name_label)

        self.ip_os_label = QLabel(self.system_information_widget)
        self.ip_os_label.setObjectName(u"ip_os_label")
        self.ip_os_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_6.addWidget(self.ip_os_label)

        self.cpu_ram_label = QLabel(self.system_information_widget)
        self.cpu_ram_label.setObjectName(u"cpu_ram_label")
        self.cpu_ram_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_6.addWidget(self.cpu_ram_label)


        self.horizontalLayout_8.addWidget(self.system_information_widget)

        self.status_label = QLabel(self.agent_information_widget)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setStyleSheet(u"color: rgb(46, 194, 126);\n"
"\n"
"font: 12pt")
        self.status_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_8.addWidget(self.status_label)


        self.horizontalLayout_5.addWidget(self.agent_information_widget)

        self.spacer1 = QSpacerItem(200, 29, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.spacer1)

        self.right_widget = QWidget(self.agent_card)
        self.right_widget.setObjectName(u"right_widget")
        self.right_widget.setMaximumSize(QSize(150, 120))
        self.right_widget.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.right_widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 80, -1, -1)
        self.agent_open_button = QPushButton(self.right_widget)
        self.agent_open_button.setObjectName(u"agent_open_button")
        self.agent_open_button.setMaximumSize(QSize(104, 16777215))
        self.agent_open_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.agent_open_button)


        self.horizontalLayout_5.addWidget(self.right_widget)

        self.spacer2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.spacer2)


        self.verticalLayout_4.addWidget(self.agent_card)

        self.scroll_clamping_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.scroll_clamping_spacer)

        self.agent_list.setWidget(self.agent_scroll)

        self.agents_main_layout.addWidget(self.agent_list)


        self.verticalLayout_8.addLayout(self.agents_main_layout)

        self.content_stack.addWidget(self.agents_page)

        self.horizontalLayout.addWidget(self.content_stack)

        MainWindow.setCentralWidget(self.central_content)

        self.retranslateUi(MainWindow)

        self.content_stack.setCurrentIndex(0)


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
        self.add_agent_button.setText(QCoreApplication.translate("MainWindow", u"[ + Add Agent ]", None))
        self.refresh_table_button.setText(QCoreApplication.translate("MainWindow", u"[ Refresh ]", None))
        self.agents_headline_label.setText(QCoreApplication.translate("MainWindow", u"Agents", None))
        self.page_description_label.setText(QCoreApplication.translate("MainWindow", u"Manage connected machines", None))
        self.add_agent_button_2.setText(QCoreApplication.translate("MainWindow", u"[ + Add Agent ]", None))
        self.search_input_line.setPlaceholderText("")
        self.refresh_agents_button.setText(QCoreApplication.translate("MainWindow", u"[ Refresh ]", None))
        self.online_dot.setText(QCoreApplication.translate("MainWindow", u"\u25cf", None))
        self.vps_name_label.setText(QCoreApplication.translate("MainWindow", u"VPS Production", None))
        self.ip_os_label.setText(QCoreApplication.translate("MainWindow", u"1.2.3.4 \u00b7 Ubuntu 24.04", None))
        self.cpu_ram_label.setText(QCoreApplication.translate("MainWindow", u"CPU 23%   RAM 41%", None))
        self.status_label.setText(QCoreApplication.translate("MainWindow", u"ONLINE", None))
        self.agent_open_button.setText(QCoreApplication.translate("MainWindow", u"[ Open \u2192 ]", None))
    # retranslateUi

