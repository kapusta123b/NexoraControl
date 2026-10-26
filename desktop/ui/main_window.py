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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPlainTextEdit, QProgressBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget
from qfluentwidgets import (Pivot, SegmentedWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1267, 940)
        self.central_content = QWidget(MainWindow)
        self.central_content.setObjectName(u"central_content")
        self.central_content.setMinimumSize(QSize(1140, 680))
        self.central_content.setMaximumSize(QSize(16777215, 16777215))
        self.central_content.setStyleSheet(u"")
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
        self.left_panel.setMinimumSize(QSize(150, 550))
        self.left_panel.setMaximumSize(QSize(1312313, 16777215))
        self.left_panel_layout = QVBoxLayout(self.left_panel)
        self.left_panel_layout.setSpacing(9)
        self.left_panel_layout.setObjectName(u"left_panel_layout")
        self.left_panel_layout.setContentsMargins(10, 20, 10, 0)
        self.nexora_logo = QLabel(self.left_panel)
        self.nexora_logo.setObjectName(u"nexora_logo")
        self.nexora_logo.setWordWrap(True)

        self.left_panel_layout.addWidget(self.nexora_logo)

        self.sidebar_product_subtitle = QLabel(self.left_panel)
        self.sidebar_product_subtitle.setObjectName(u"sidebar_product_subtitle")

        self.left_panel_layout.addWidget(self.sidebar_product_subtitle)

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
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.dashboard_page_layout = QVBoxLayout(self.dashboard_page)
        self.dashboard_page_layout.setSpacing(0)
        self.dashboard_page_layout.setObjectName(u"dashboard_page_layout")
        self.dashboard_page_layout.setContentsMargins(0, 0, 0, 0)
        self.dashboard_layout = QVBoxLayout()
        self.dashboard_layout.setSpacing(13)
        self.dashboard_layout.setObjectName(u"dashboard_layout")
        self.dashboard_layout.setContentsMargins(6, 6, 6, 6)
        self.dashboard_label = QLabel(self.dashboard_page)
        self.dashboard_label.setObjectName(u"dashboard_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dashboard_label.sizePolicy().hasHeightForWidth())
        self.dashboard_label.setSizePolicy(sizePolicy1)
        self.dashboard_label.setMaximumSize(QSize(16777215, 28))

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
        self.cards_layout = QHBoxLayout(self.cards)
        self.cards_layout.setSpacing(16)
        self.cards_layout.setObjectName(u"cards_layout")
        self.cards_layout.setContentsMargins(0, 3, 0, 12)
        self.card_agents = QWidget(self.cards)
        self.card_agents.setObjectName(u"card_agents")
        self.card_agents.setMinimumSize(QSize(158, 84))
        self.card_agents.setMaximumSize(QSize(16777215, 98))
        self.card_agents_layout = QVBoxLayout(self.card_agents)
        self.card_agents_layout.setSpacing(3)
        self.card_agents_layout.setObjectName(u"card_agents_layout")
        self.card_agents_layout.setContentsMargins(16, 12, 16, 10)
        self.agent_label = QLabel(self.card_agents)
        self.agent_label.setObjectName(u"agent_label")
        self.agent_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.card_agents_layout.addWidget(self.agent_label)

        self.agents_count = QLabel(self.card_agents)
        self.agents_count.setObjectName(u"agents_count")
        self.agents_count.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.card_agents_layout.addWidget(self.agents_count)


        self.cards_layout.addWidget(self.card_agents)

        self.card_online = QWidget(self.cards)
        self.card_online.setObjectName(u"card_online")
        self.card_online.setMinimumSize(QSize(158, 84))
        self.card_online.setMaximumSize(QSize(16777215, 98))
        self.card_online_layout = QVBoxLayout(self.card_online)
        self.card_online_layout.setSpacing(3)
        self.card_online_layout.setObjectName(u"card_online_layout")
        self.card_online_layout.setContentsMargins(16, 12, 16, 10)
        self.online_label = QLabel(self.card_online)
        self.online_label.setObjectName(u"online_label")
        self.online_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.card_online_layout.addWidget(self.online_label)

        self.online_count = QLabel(self.card_online)
        self.online_count.setObjectName(u"online_count")
        self.online_count.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.card_online_layout.addWidget(self.online_count)


        self.cards_layout.addWidget(self.card_online)

        self.card_offline = QWidget(self.cards)
        self.card_offline.setObjectName(u"card_offline")
        self.card_offline.setMinimumSize(QSize(158, 84))
        self.card_offline.setMaximumSize(QSize(16777215, 98))
        self.card_offline_layout = QVBoxLayout(self.card_offline)
        self.card_offline_layout.setSpacing(3)
        self.card_offline_layout.setObjectName(u"card_offline_layout")
        self.card_offline_layout.setContentsMargins(16, 12, 16, 10)
        self.offline_label = QLabel(self.card_offline)
        self.offline_label.setObjectName(u"offline_label")
        self.offline_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.card_offline_layout.addWidget(self.offline_label)

        self.offline_count = QLabel(self.card_offline)
        self.offline_count.setObjectName(u"offline_count")
        self.offline_count.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.card_offline_layout.addWidget(self.offline_count)


        self.cards_layout.addWidget(self.card_offline)


        self.dashboard_layout.addWidget(self.cards)

        self.agents_label = QLabel(self.dashboard_page)
        self.agents_label.setObjectName(u"agents_label")
        self.agents_label.setEnabled(True)
        self.agents_label.setMaximumSize(QSize(16777215, 30))

        self.dashboard_layout.addWidget(self.agents_label)

        self.agents_table_legend_label = QLabel(self.dashboard_page)
        self.agents_table_legend_label.setObjectName(u"agents_table_legend_label")

        self.dashboard_layout.addWidget(self.agents_table_legend_label)

        self.line_4 = QFrame(self.dashboard_page)
        self.line_4.setObjectName(u"line_4")
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
        self.agents_table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.agents_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.agents_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.agents_table.setAlternatingRowColors(True)
        self.agents_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.agents_table.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.agents_table.setShowGrid(False)
        self.agents_table.setSortingEnabled(True)
        self.agents_table.setWordWrap(False)
        self.agents_table.horizontalHeader().setVisible(True)
        self.agents_table.horizontalHeader().setCascadingSectionResizes(True)
        self.agents_table.horizontalHeader().setMinimumSectionSize(20)
        self.agents_table.horizontalHeader().setDefaultSectionSize(120)
        self.agents_table.horizontalHeader().setHighlightSections(False)
        self.agents_table.horizontalHeader().setStretchLastSection(False)
        self.agents_table.verticalHeader().setVisible(False)
        self.agents_table.verticalHeader().setCascadingSectionResizes(False)
        self.agents_table.verticalHeader().setMinimumSectionSize(25)
        self.agents_table.verticalHeader().setDefaultSectionSize(48)
        self.agents_table.verticalHeader().setHighlightSections(True)
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
        self.agents_page_layout = QVBoxLayout(self.agents_page)
        self.agents_page_layout.setSpacing(0)
        self.agents_page_layout.setObjectName(u"agents_page_layout")
        self.agents_page_layout.setContentsMargins(6, 6, 0, 0)
        self.agents_main_layout = QVBoxLayout()
        self.agents_main_layout.setSpacing(4)
        self.agents_main_layout.setObjectName(u"agents_main_layout")
        self.agents_main_layout.setContentsMargins(0, 0, 0, 0)
        self.agents_headline_label = QLabel(self.agents_page)
        self.agents_headline_label.setObjectName(u"agents_headline_label")
        self.agents_headline_label.setMinimumSize(QSize(0, 0))
        self.agents_headline_label.setMaximumSize(QSize(16777215, 25))

        self.agents_main_layout.addWidget(self.agents_headline_label)

        self.page_description_label = QLabel(self.agents_page)
        self.page_description_label.setObjectName(u"page_description_label")
        self.page_description_label.setMinimumSize(QSize(0, 30))
        self.page_description_label.setMaximumSize(QSize(16777215, 30))

        self.agents_main_layout.addWidget(self.page_description_label)

        self.page_description_line = QFrame(self.agents_page)
        self.page_description_line.setObjectName(u"page_description_line")
        self.page_description_line.setFrameShape(QFrame.Shape.VLine)
        self.page_description_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.agents_main_layout.addWidget(self.page_description_line)

        self.line_8 = QFrame(self.agents_page)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.agents_main_layout.addWidget(self.line_8)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.agents_main_layout.addItem(self.verticalSpacer_4)

        self.help_bar_layout = QHBoxLayout()
        self.help_bar_layout.setSpacing(0)
        self.help_bar_layout.setObjectName(u"help_bar_layout")
        self.help_bar_layout.setContentsMargins(-1, -1, 6, -1)
        self.search_input_line = QLineEdit(self.agents_page)
        self.search_input_line.setObjectName(u"search_input_line")
        self.search_input_line.setClearButtonEnabled(False)

        self.help_bar_layout.addWidget(self.search_input_line)

        self.horizontalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.help_bar_layout.addItem(self.horizontalSpacer)

        self.refresh_agents_button = QPushButton(self.agents_page)
        self.refresh_agents_button.setObjectName(u"refresh_agents_button")
        self.refresh_agents_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.help_bar_layout.addWidget(self.refresh_agents_button)


        self.agents_main_layout.addLayout(self.help_bar_layout)

        self.agent_scroll_spacer = QSpacerItem(20, 19, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.agents_main_layout.addItem(self.agent_scroll_spacer)

        self.agent_list = QScrollArea(self.agents_page)
        self.agent_list.setObjectName(u"agent_list")
        self.agent_list.setMinimumSize(QSize(0, 600))
        self.agent_list.setMaximumSize(QSize(16777215, 16777215))
        self.agent_list.setLayoutDirection(Qt.LeftToRight)
        self.agent_list.setAutoFillBackground(False)
        self.agent_list.setFrameShape(QFrame.NoFrame)
        self.agent_list.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.agent_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.agent_list.setWidgetResizable(True)
        self.agent_scroll = QWidget()
        self.agent_scroll.setObjectName(u"agent_scroll")
        self.agent_scroll.setGeometry(QRect(0, 0, 100, 600))
        self.agent_scroll.setMaximumSize(QSize(16777215, 1000000))
        self.agent_scroll_layout = QVBoxLayout(self.agent_scroll)
        self.agent_scroll_layout.setSpacing(12)
        self.agent_scroll_layout.setObjectName(u"agent_scroll_layout")
        self.agent_scroll_layout.setContentsMargins(0, 0, 6, 10)
        self.agent_list.setWidget(self.agent_scroll)

        self.agents_main_layout.addWidget(self.agent_list)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.agents_main_layout.addItem(self.verticalSpacer)


        self.agents_page_layout.addLayout(self.agents_main_layout)

        self.content_stack.addWidget(self.agents_page)
        self.agent_detail_page = QWidget()
        self.agent_detail_page.setObjectName(u"agent_detail_page")
        self.agent_detail_page_layout = QVBoxLayout(self.agent_detail_page)
        self.agent_detail_page_layout.setSpacing(0)
        self.agent_detail_page_layout.setObjectName(u"agent_detail_page_layout")
        self.agent_detail_page_layout.setContentsMargins(0, 0, 0, 0)
        self.agent_detail_content = QWidget(self.agent_detail_page)
        self.agent_detail_content.setObjectName(u"agent_detail_content")
        self.agent_detail_content_layout = QVBoxLayout(self.agent_detail_content)
        self.agent_detail_content_layout.setObjectName(u"agent_detail_content_layout")
        self.agent_detail_content_layout.setContentsMargins(6, 6, 6, 6)
        self.detail_top_widget = QWidget(self.agent_detail_content)
        self.detail_top_widget.setObjectName(u"detail_top_widget")
        self.detail_top_widget.setMinimumSize(QSize(0, 0))
        self.detail_top_widget.setMaximumSize(QSize(16777215, 300))
        self.detail_top_widget_layout = QVBoxLayout(self.detail_top_widget)
        self.detail_top_widget_layout.setSpacing(10)
        self.detail_top_widget_layout.setObjectName(u"detail_top_widget_layout")
        self.detail_top_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.detail_top_layout = QHBoxLayout()
        self.detail_top_layout.setObjectName(u"detail_top_layout")
        self.back_to_agents_button = QPushButton(self.detail_top_widget)
        self.back_to_agents_button.setObjectName(u"back_to_agents_button")
        self.back_to_agents_button.setMinimumSize(QSize(104, 0))
        self.back_to_agents_button.setMaximumSize(QSize(138, 29))
        self.back_to_agents_button.setLayoutDirection(Qt.LeftToRight)
        self.back_to_agents_button.setCheckable(False)
        self.back_to_agents_button.setAutoRepeat(False)

        self.detail_top_layout.addWidget(self.back_to_agents_button)

        self.detail_top_center_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.detail_top_layout.addItem(self.detail_top_center_spacer)

        self.detail_top_agent_name_label = QLabel(self.detail_top_widget)
        self.detail_top_agent_name_label.setObjectName(u"detail_top_agent_name_label")
        self.detail_top_agent_name_label.setWordWrap(True)

        self.detail_top_layout.addWidget(self.detail_top_agent_name_label)

        self.detail_top_info_spacer = QSpacerItem(20, 28, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.detail_top_layout.addItem(self.detail_top_info_spacer)

        self.detail_top_agent_status_label = QLabel(self.detail_top_widget)
        self.detail_top_agent_status_label.setObjectName(u"detail_top_agent_status_label")

        self.detail_top_layout.addWidget(self.detail_top_agent_status_label)


        self.detail_top_widget_layout.addLayout(self.detail_top_layout)

        self.detail_top_navigation_layout = QHBoxLayout()
        self.detail_top_navigation_layout.setSpacing(8)
        self.detail_top_navigation_layout.setObjectName(u"detail_top_navigation_layout")
        self.detail_top_navigation_layout.setContentsMargins(0, 0, 0, 0)
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
        self.overview_detail_page_layout.setSpacing(12)
        self.overview_detail_page_layout.setObjectName(u"overview_detail_page_layout")
        self.overview_detail_page_layout.setContentsMargins(2, 8, 0, 5)
        self.overview_label = QLabel(self.overview_detail_page)
        self.overview_label.setObjectName(u"overview_label")
        self.overview_label.setMinimumSize(QSize(0, 0))

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
        self.overview_detail_scroll.setFrameShape(QFrame.NoFrame)
        self.overview_detail_scroll.setWidgetResizable(True)
        self.agent_detail_information = QWidget()
        self.agent_detail_information.setObjectName(u"agent_detail_information")
        self.agent_detail_information.setGeometry(QRect(0, 0, 513, 800))
        self.agent_detail_information.setMinimumSize(QSize(0, 800))
        self.agent_detail_information_layout = QVBoxLayout(self.agent_detail_information)
        self.agent_detail_information_layout.setSpacing(10)
        self.agent_detail_information_layout.setObjectName(u"agent_detail_information_layout")
        self.agent_detail_information_layout.setContentsMargins(0, 0, 6, 0)
        self.overview_widget = QWidget(self.agent_detail_information)
        self.overview_widget.setObjectName(u"overview_widget")
        self.overview_widget.setMaximumSize(QSize(16777215, 100))
        self.overview_layout = QHBoxLayout(self.overview_widget)
        self.overview_layout.setSpacing(14)
        self.overview_layout.setObjectName(u"overview_layout")
        self.overview_layout.setContentsMargins(2, 4, 5, 16)
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
        self.cpu_widget_layout = QVBoxLayout(self.cpu_widget)
        self.cpu_widget_layout.setObjectName(u"cpu_widget_layout")
        self.cpu_label = QLabel(self.cpu_widget)
        self.cpu_label.setObjectName(u"cpu_label")
        self.cpu_label.setAlignment(Qt.AlignCenter)

        self.cpu_widget_layout.addWidget(self.cpu_label)

        self.cpu_load_label = QLabel(self.cpu_widget)
        self.cpu_load_label.setObjectName(u"cpu_load_label")
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

        self.system_status_layout.addWidget(self.system_status_label)

        self.system_status_box_widget = QWidget(self.system_status_widget)
        self.system_status_box_widget.setObjectName(u"system_status_box_widget")
        self.system_status_box_widget.setMaximumSize(QSize(400, 300))
        self.system_status_box_widget_layout = QHBoxLayout(self.system_status_box_widget)
        self.system_status_box_widget_layout.setSpacing(0)
        self.system_status_box_widget_layout.setObjectName(u"system_status_box_widget_layout")
        self.system_status_box_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.system_status_box_layout = QHBoxLayout()
        self.system_status_box_layout.setObjectName(u"system_status_box_layout")
        self.system_status_rows_widget = QWidget(self.system_status_box_widget)
        self.system_status_rows_widget.setObjectName(u"system_status_rows_widget")
        self.system_status_rows_widget_layout = QVBoxLayout(self.system_status_rows_widget)
        self.system_status_rows_widget_layout.setSpacing(0)
        self.system_status_rows_widget_layout.setObjectName(u"system_status_rows_widget_layout")
        self.system_status_rows_widget_layout.setContentsMargins(10, 0, 0, 0)
        self.agent_row_label = QLabel(self.system_status_rows_widget)
        self.agent_row_label.setObjectName(u"agent_row_label")
        self.agent_row_label.setMargin(0)

        self.system_status_rows_widget_layout.addWidget(self.agent_row_label)

        self.last_seen_row_label = QLabel(self.system_status_rows_widget)
        self.last_seen_row_label.setObjectName(u"last_seen_row_label")
        self.last_seen_row_label.setMargin(0)

        self.system_status_rows_widget_layout.addWidget(self.last_seen_row_label)

        self.ip_row_label = QLabel(self.system_status_rows_widget)
        self.ip_row_label.setObjectName(u"ip_row_label")
        self.ip_row_label.setMargin(0)

        self.system_status_rows_widget_layout.addWidget(self.ip_row_label)

        self.hostname_row_label = QLabel(self.system_status_rows_widget)
        self.hostname_row_label.setObjectName(u"hostname_row_label")
        self.hostname_row_label.setMargin(0)

        self.system_status_rows_widget_layout.addWidget(self.hostname_row_label)

        self.os_name_row_label = QLabel(self.system_status_rows_widget)
        self.os_name_row_label.setObjectName(u"os_name_row_label")
        self.os_name_row_label.setMargin(0)

        self.system_status_rows_widget_layout.addWidget(self.os_name_row_label)


        self.system_status_box_layout.addWidget(self.system_status_rows_widget)

        self.system_status_values_widget = QWidget(self.system_status_box_widget)
        self.system_status_values_widget.setObjectName(u"system_status_values_widget")
        self.system_status_values_widget_layout = QVBoxLayout(self.system_status_values_widget)
        self.system_status_values_widget_layout.setSpacing(0)
        self.system_status_values_widget_layout.setObjectName(u"system_status_values_widget_layout")
        self.system_status_values_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.agent_status_value_label = QLabel(self.system_status_values_widget)
        self.agent_status_value_label.setObjectName(u"agent_status_value_label")

        self.system_status_values_widget_layout.addWidget(self.agent_status_value_label)

        self.last_seen_value_label = QLabel(self.system_status_values_widget)
        self.last_seen_value_label.setObjectName(u"last_seen_value_label")

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

        self.quick_actions_label = QLabel(self.agent_detail_information)
        self.quick_actions_label.setObjectName(u"quick_actions_label")
        self.quick_actions_label.setMaximumSize(QSize(16777215, 30))

        self.agent_detail_information_layout.addWidget(self.quick_actions_label)

        self.quick_actions_widget = QWidget(self.agent_detail_information)
        self.quick_actions_widget.setObjectName(u"quick_actions_widget")
        self.quick_actions_widget.setMinimumSize(QSize(0, 60))
        self.quick_actions_widget.setMaximumSize(QSize(16777215, 60))
        self.quick_actions_widget_layout = QVBoxLayout(self.quick_actions_widget)
        self.quick_actions_widget_layout.setSpacing(0)
        self.quick_actions_widget_layout.setObjectName(u"quick_actions_widget_layout")
        self.quick_actions_widget_layout.setContentsMargins(10, 0, 10, 0)
        self.quick_actions_buttons_widget = QWidget(self.quick_actions_widget)
        self.quick_actions_buttons_widget.setObjectName(u"quick_actions_buttons_widget")
        self.quick_actions_buttons_widget.setMaximumSize(QSize(16777215, 60))
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
        self.recent_commands_widget.setMaximumSize(QSize(500, 250))
        self.recent_commands_widget_layout = QVBoxLayout(self.recent_commands_widget)
        self.recent_commands_widget_layout.setSpacing(5)
        self.recent_commands_widget_layout.setObjectName(u"recent_commands_widget_layout")
        self.recent_commands_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.recent_commands_label = QLabel(self.recent_commands_widget)
        self.recent_commands_label.setObjectName(u"recent_commands_label")
        self.recent_commands_label.setMaximumSize(QSize(16777215, 30))

        self.recent_commands_widget_layout.addWidget(self.recent_commands_label)

        self.recent_command_box_widget = QWidget(self.recent_commands_widget)
        self.recent_command_box_widget.setObjectName(u"recent_command_box_widget")
        self.recent_command_box_widget.setMinimumSize(QSize(0, 0))
        self.recent_command_box_widget.setMaximumSize(QSize(16777215, 200))
        self.recent_command_box_layout = QVBoxLayout(self.recent_command_box_widget)
        self.recent_command_box_layout.setSpacing(0)
        self.recent_command_box_layout.setObjectName(u"recent_command_box_layout")
        self.recent_command_box_layout.setContentsMargins(0, 0, 0, 6)

        self.recent_commands_widget_layout.addWidget(self.recent_command_box_widget)


        self.agent_detail_information_layout.addWidget(self.recent_commands_widget)

        self.overview_detail_scroll.setWidget(self.agent_detail_information)

        self.overview_detail_page_layout.addWidget(self.overview_detail_scroll)

        self.agent_detail_stacked_content.addWidget(self.overview_detail_page)
        self.performance_detail_page = QWidget()
        self.performance_detail_page.setObjectName(u"performance_detail_page")
        self.performance_detail_page_layout = QVBoxLayout(self.performance_detail_page)
        self.performance_detail_page_layout.setSpacing(12)
        self.performance_detail_page_layout.setObjectName(u"performance_detail_page_layout")
        self.performance_detail_page_layout.setContentsMargins(0, 6, 0, 0)
        self.performance_label = QLabel(self.performance_detail_page)
        self.performance_label.setObjectName(u"performance_label")
        self.performance_label.setMinimumSize(QSize(0, 0))

        self.performance_detail_page_layout.addWidget(self.performance_label)

        self.performance_legend_label = QLabel(self.performance_detail_page)
        self.performance_legend_label.setObjectName(u"performance_legend_label")

        self.performance_detail_page_layout.addWidget(self.performance_legend_label)

        self.metric_buttons_layout = QHBoxLayout()
        self.metric_buttons_layout.setSpacing(2)
        self.metric_buttons_layout.setObjectName(u"metric_buttons_layout")
        self.metric_buttons_layout.setContentsMargins(-1, -1, 0, -1)
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

        self.performance_legend_line = QFrame(self.performance_detail_page)
        self.performance_legend_line.setObjectName(u"performance_legend_line")
        self.performance_legend_line.setFrameShape(QFrame.Shape.HLine)
        self.performance_legend_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.performance_detail_page_layout.addWidget(self.performance_legend_line)

        self.performance_detail_scroll = QScrollArea(self.performance_detail_page)
        self.performance_detail_scroll.setObjectName(u"performance_detail_scroll")
        self.performance_detail_scroll.setFrameShape(QFrame.NoFrame)
        self.performance_detail_scroll.setWidgetResizable(True)
        self.agent_performance_information = QWidget()
        self.agent_performance_information.setObjectName(u"agent_performance_information")
        self.agent_performance_information.setGeometry(QRect(0, 0, 930, 1207))
        self.agent_performance_information_layout = QVBoxLayout(self.agent_performance_information)
        self.agent_performance_information_layout.setSpacing(0)
        self.agent_performance_information_layout.setObjectName(u"agent_performance_information_layout")
        self.agent_performance_information_layout.setContentsMargins(0, 0, 6, 0)
        self.performance_content_widget = QWidget(self.agent_performance_information)
        self.performance_content_widget.setObjectName(u"performance_content_widget")
        self.performance_content_layout = QVBoxLayout(self.performance_content_widget)
        self.performance_content_layout.setSpacing(6)
        self.performance_content_layout.setObjectName(u"performance_content_layout")
        self.performance_content_layout.setContentsMargins(0, 0, 0, 0)
        self.performance_stacked_content = QStackedWidget(self.performance_content_widget)
        self.performance_stacked_content.setObjectName(u"performance_stacked_content")
        self.performance_compute_page = QWidget()
        self.performance_compute_page.setObjectName(u"performance_compute_page")
        self.compute_page_layout = QVBoxLayout(self.performance_compute_page)
        self.compute_page_layout.setSpacing(15)
        self.compute_page_layout.setObjectName(u"compute_page_layout")
        self.compute_page_layout.setContentsMargins(0, 0, 0, 0)
        self.compute_label = QLabel(self.performance_compute_page)
        self.compute_label.setObjectName(u"compute_label")

        self.compute_page_layout.addWidget(self.compute_label)

        self.compute_legend_label = QLabel(self.performance_compute_page)
        self.compute_legend_label.setObjectName(u"compute_legend_label")

        self.compute_page_layout.addWidget(self.compute_legend_label)

        self.compute_legend_line = QFrame(self.performance_compute_page)
        self.compute_legend_line.setObjectName(u"compute_legend_line")
        self.compute_legend_line.setFrameShape(QFrame.Shape.HLine)
        self.compute_legend_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.compute_page_layout.addWidget(self.compute_legend_line)

        self.compute_current_state_label = QLabel(self.performance_compute_page)
        self.compute_current_state_label.setObjectName(u"compute_current_state_label")

        self.compute_page_layout.addWidget(self.compute_current_state_label)

        self.compute_gauge_widget = QWidget(self.performance_compute_page)
        self.compute_gauge_widget.setObjectName(u"compute_gauge_widget")
        self.compute_gauge_layout = QHBoxLayout(self.compute_gauge_widget)
        self.compute_gauge_layout.setObjectName(u"compute_gauge_layout")
        self.compute_gauge_layout.setContentsMargins(-1, -1, -1, 1)

        self.compute_page_layout.addWidget(self.compute_gauge_widget)

        self.line_2 = QFrame(self.performance_compute_page)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.compute_page_layout.addWidget(self.line_2)

        self.cpu_ram_metric_label = QLabel(self.performance_compute_page)
        self.cpu_ram_metric_label.setObjectName(u"cpu_ram_metric_label")

        self.compute_page_layout.addWidget(self.cpu_ram_metric_label)

        self.cpu_ram_utilization_widget = QWidget(self.performance_compute_page)
        self.cpu_ram_utilization_widget.setObjectName(u"cpu_ram_utilization_widget")
        self.cpu_ram_utilization_widget.setMinimumSize(QSize(0, 300))
        self.cpu_ram_utilization_widget.setMaximumSize(QSize(16777215, 600))
        self.cpu_ram_utilization_layout = QHBoxLayout(self.cpu_ram_utilization_widget)
        self.cpu_ram_utilization_layout.setObjectName(u"cpu_ram_utilization_layout")
        self.cpu_ram_utilization_layout.setContentsMargins(0, 0, 0, 0)
        self.cpu_ram_metric_graph = PlotWidget(self.cpu_ram_utilization_widget)
        self.cpu_ram_metric_graph.setObjectName(u"cpu_ram_metric_graph")
        self.cpu_ram_metric_graph.setMinimumSize(QSize(0, 0))

        self.cpu_ram_utilization_layout.addWidget(self.cpu_ram_metric_graph)

        self.ram_utilization_widget = QWidget(self.cpu_ram_utilization_widget)
        self.ram_utilization_widget.setObjectName(u"ram_utilization_widget")
        self.ram_utilization_widget.setMinimumSize(QSize(0, 120))
        self.ram_utilization_widget.setMaximumSize(QSize(230, 16777215))
        self.ram_utilization_layout = QVBoxLayout(self.ram_utilization_widget)
        self.ram_utilization_layout.setObjectName(u"ram_utilization_layout")
        self.memory_label = QLabel(self.ram_utilization_widget)
        self.memory_label.setObjectName(u"memory_label")
        self.memory_label.setMaximumSize(QSize(16777215, 50))

        self.ram_utilization_layout.addWidget(self.memory_label)

        self.line_6 = QFrame(self.ram_utilization_widget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.ram_utilization_layout.addWidget(self.line_6)

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

        self.available_memory_layout = QHBoxLayout()
        self.available_memory_layout.setObjectName(u"available_memory_layout")
        self.available_memory_label = QLabel(self.ram_utilization_widget)
        self.available_memory_label.setObjectName(u"available_memory_label")

        self.available_memory_layout.addWidget(self.available_memory_label)

        self.available_memory_value_label = QLabel(self.ram_utilization_widget)
        self.available_memory_value_label.setObjectName(u"available_memory_value_label")

        self.available_memory_layout.addWidget(self.available_memory_value_label)


        self.memory_information_layout.addLayout(self.available_memory_layout)

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
        self.memory_progress_bar.setValue(0)

        self.ram_utilization_layout.addWidget(self.memory_progress_bar)


        self.cpu_ram_utilization_layout.addWidget(self.ram_utilization_widget)


        self.compute_page_layout.addWidget(self.cpu_ram_utilization_widget)

        self.line_3 = QFrame(self.performance_compute_page)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.compute_page_layout.addWidget(self.line_3)

        self.compute_load_average_label = QLabel(self.performance_compute_page)
        self.compute_load_average_label.setObjectName(u"compute_load_average_label")

        self.compute_page_layout.addWidget(self.compute_load_average_label)

        self.load_average_metric_graph = PlotWidget(self.performance_compute_page)
        self.load_average_metric_graph.setObjectName(u"load_average_metric_graph")
        self.load_average_metric_graph.setMinimumSize(QSize(0, 300))

        self.compute_page_layout.addWidget(self.load_average_metric_graph)

        self.line_5 = QFrame(self.performance_compute_page)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.compute_page_layout.addWidget(self.line_5)

        self.compute_cpu_cores_label = QLabel(self.performance_compute_page)
        self.compute_cpu_cores_label.setObjectName(u"compute_cpu_cores_label")

        self.compute_page_layout.addWidget(self.compute_cpu_cores_label)

        self.cpu_cores_metric_graph = PlotWidget(self.performance_compute_page)
        self.cpu_cores_metric_graph.setObjectName(u"cpu_cores_metric_graph")
        self.cpu_cores_metric_graph.setMinimumSize(QSize(0, 300))

        self.compute_page_layout.addWidget(self.cpu_cores_metric_graph)

        self.performance_stacked_content.addWidget(self.performance_compute_page)
        self.performance_storage_page = QWidget()
        self.performance_storage_page.setObjectName(u"performance_storage_page")
        self.storage_page_layout = QVBoxLayout(self.performance_storage_page)
        self.storage_page_layout.setSpacing(15)
        self.storage_page_layout.setObjectName(u"storage_page_layout")
        self.storage_page_layout.setContentsMargins(0, 0, 0, 0)
        self.storage_label = QLabel(self.performance_storage_page)
        self.storage_label.setObjectName(u"storage_label")
        self.storage_label.setMaximumSize(QSize(16777215, 40))

        self.storage_page_layout.addWidget(self.storage_label)

        self.storage_legend_label = QLabel(self.performance_storage_page)
        self.storage_legend_label.setObjectName(u"storage_legend_label")

        self.storage_page_layout.addWidget(self.storage_legend_label)

        self.storage_legend_line = QFrame(self.performance_storage_page)
        self.storage_legend_line.setObjectName(u"storage_legend_line")
        self.storage_legend_line.setFrameShape(QFrame.Shape.HLine)
        self.storage_legend_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.storage_page_layout.addWidget(self.storage_legend_line)

        self.current_storage_label = QLabel(self.performance_storage_page)
        self.current_storage_label.setObjectName(u"current_storage_label")
        self.current_storage_label.setMaximumSize(QSize(16777215, 30))

        self.storage_page_layout.addWidget(self.current_storage_label)

        self.storage_gauge_widget = QWidget(self.performance_storage_page)
        self.storage_gauge_widget.setObjectName(u"storage_gauge_widget")
        self.storage_gauge_layout = QHBoxLayout(self.storage_gauge_widget)
        self.storage_gauge_layout.setObjectName(u"storage_gauge_layout")
        self.storage_gauge_layout.setContentsMargins(-1, -1, -1, 1)

        self.storage_page_layout.addWidget(self.storage_gauge_widget)

        self.current_storage_line = QFrame(self.performance_storage_page)
        self.current_storage_line.setObjectName(u"current_storage_line")
        self.current_storage_line.setFrameShape(QFrame.Shape.HLine)
        self.current_storage_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.storage_page_layout.addWidget(self.current_storage_line)

        self.disk_io_layout = QHBoxLayout()
        self.disk_io_layout.setObjectName(u"disk_io_layout")
        self.disk_io_layout.setContentsMargins(0, 0, -1, -1)
        self.disk_io_label = QLabel(self.performance_storage_page)
        self.disk_io_label.setObjectName(u"disk_io_label")
        self.disk_io_label.setMinimumSize(QSize(0, 0))
        self.disk_io_label.setMaximumSize(QSize(100, 16777215))

        self.disk_io_layout.addWidget(self.disk_io_label)

        self.disk_io_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.disk_io_layout.addItem(self.disk_io_spacer)

        self.hardware_group_label_2 = QLabel(self.performance_storage_page)
        self.hardware_group_label_2.setObjectName(u"hardware_group_label_2")
        self.hardware_group_label_2.setMinimumSize(QSize(0, 0))
        self.hardware_group_label_2.setMaximumSize(QSize(120, 40))

        self.disk_io_layout.addWidget(self.hardware_group_label_2)

        self.disks_combo_box = QComboBox(self.performance_storage_page)
        self.disks_combo_box.setObjectName(u"disks_combo_box")
        self.disks_combo_box.setMinimumSize(QSize(0, 0))
        self.disks_combo_box.setMaximumSize(QSize(120, 16777215))
        self.disks_combo_box.setEditable(False)
        self.disks_combo_box.setMaxVisibleItems(4)
        self.disks_combo_box.setIconSize(QSize(16, 16))
        self.disks_combo_box.setFrame(True)

        self.disk_io_layout.addWidget(self.disks_combo_box)

        self.disk_data_unit_combo_box = QComboBox(self.performance_storage_page)
        self.disk_data_unit_combo_box.setObjectName(u"disk_data_unit_combo_box")
        self.disk_data_unit_combo_box.setMinimumSize(QSize(0, 0))
        self.disk_data_unit_combo_box.setMaximumSize(QSize(70, 16777215))
        self.disk_data_unit_combo_box.setEditable(False)
        self.disk_data_unit_combo_box.setInsertPolicy(QComboBox.NoInsert)

        self.disk_io_layout.addWidget(self.disk_data_unit_combo_box)


        self.storage_page_layout.addLayout(self.disk_io_layout)

        self.storage_disk_io_widget = QWidget(self.performance_storage_page)
        self.storage_disk_io_widget.setObjectName(u"storage_disk_io_widget")
        self.storage_disk_io_widget.setMinimumSize(QSize(0, 300))
        self.storage_disk_io_widget.setMaximumSize(QSize(16777215, 600))
        self.storage_disk_io_layout = QHBoxLayout(self.storage_disk_io_widget)
        self.storage_disk_io_layout.setObjectName(u"storage_disk_io_layout")
        self.storage_disk_io_layout.setContentsMargins(0, 0, 0, 0)
        self.disk_write_read_graph = PlotWidget(self.storage_disk_io_widget)
        self.disk_write_read_graph.setObjectName(u"disk_write_read_graph")
        self.disk_write_read_graph.setMinimumSize(QSize(0, 0))

        self.storage_disk_io_layout.addWidget(self.disk_write_read_graph)

        self.disk_io_summary_widget = QWidget(self.storage_disk_io_widget)
        self.disk_io_summary_widget.setObjectName(u"disk_io_summary_widget")
        self.disk_io_summary_widget.setMinimumSize(QSize(230, 120))
        self.disk_io_summary_widget.setMaximumSize(QSize(300, 16777215))
        self.disk_io_summary_layout = QVBoxLayout(self.disk_io_summary_widget)
        self.disk_io_summary_layout.setSpacing(0)
        self.disk_io_summary_layout.setObjectName(u"disk_io_summary_layout")
        self.disk_io_summary_layout.setContentsMargins(6, 6, 6, 6)
        self.disk_i_o_summary_label = QLabel(self.disk_io_summary_widget)
        self.disk_i_o_summary_label.setObjectName(u"disk_i_o_summary_label")
        self.disk_i_o_summary_label.setMaximumSize(QSize(16777215, 50))

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

        self.disk_read_information_layout.addWidget(self.disk_read_information_value)


        self.disk_capacity_information_layout.addLayout(self.disk_read_information_layout)

        self.disk_write_informatio_layout = QHBoxLayout()
        self.disk_write_informatio_layout.setObjectName(u"disk_write_informatio_layout")
        self.disk_write_information_label = QLabel(self.disk_io_summary_widget)
        self.disk_write_information_label.setObjectName(u"disk_write_information_label")

        self.disk_write_informatio_layout.addWidget(self.disk_write_information_label)

        self.disk_write_information_value = QLabel(self.disk_io_summary_widget)
        self.disk_write_information_value.setObjectName(u"disk_write_information_value")

        self.disk_write_informatio_layout.addWidget(self.disk_write_information_value)


        self.disk_capacity_information_layout.addLayout(self.disk_write_informatio_layout)

        self.disk_read_per_sec_information_layout = QHBoxLayout()
        self.disk_read_per_sec_information_layout.setObjectName(u"disk_read_per_sec_information_layout")
        self.disk_read_per_sec_information_label = QLabel(self.disk_io_summary_widget)
        self.disk_read_per_sec_information_label.setObjectName(u"disk_read_per_sec_information_label")

        self.disk_read_per_sec_information_layout.addWidget(self.disk_read_per_sec_information_label)

        self.disk_read_per_sec_information_value = QLabel(self.disk_io_summary_widget)
        self.disk_read_per_sec_information_value.setObjectName(u"disk_read_per_sec_information_value")

        self.disk_read_per_sec_information_layout.addWidget(self.disk_read_per_sec_information_value)


        self.disk_capacity_information_layout.addLayout(self.disk_read_per_sec_information_layout)

        self.disk_write_per_sec_information_layout = QHBoxLayout()
        self.disk_write_per_sec_information_layout.setObjectName(u"disk_write_per_sec_information_layout")
        self.disk_write_per_sec_information_label = QLabel(self.disk_io_summary_widget)
        self.disk_write_per_sec_information_label.setObjectName(u"disk_write_per_sec_information_label")

        self.disk_write_per_sec_information_layout.addWidget(self.disk_write_per_sec_information_label)

        self.disk_write_per_sec_information_value = QLabel(self.disk_io_summary_widget)
        self.disk_write_per_sec_information_value.setObjectName(u"disk_write_per_sec_information_value")

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

        self.disk_avg_latency_layout.addWidget(self.disk_avg_latency_value)


        self.disk_information_layout.addLayout(self.disk_avg_latency_layout)


        self.disk_io_summary_layout.addLayout(self.disk_information_layout)


        self.storage_disk_io_layout.addWidget(self.disk_io_summary_widget)


        self.storage_page_layout.addWidget(self.storage_disk_io_widget)

        self.disk_io_line = QFrame(self.performance_storage_page)
        self.disk_io_line.setObjectName(u"disk_io_line")
        self.disk_io_line.setFrameShape(QFrame.Shape.HLine)
        self.disk_io_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.storage_page_layout.addWidget(self.disk_io_line)

        self.file_systems_label = QLabel(self.performance_storage_page)
        self.file_systems_label.setObjectName(u"file_systems_label")

        self.storage_page_layout.addWidget(self.file_systems_label)

        self.file_systems_table = QTableWidget(self.performance_storage_page)
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
        self.file_systems_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.file_systems_table.setAlternatingRowColors(True)
        self.file_systems_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.file_systems_table.setShowGrid(False)
        self.file_systems_table.horizontalHeader().setCascadingSectionResizes(True)

        self.storage_page_layout.addWidget(self.file_systems_table)

        self.file_systems_line = QFrame(self.performance_storage_page)
        self.file_systems_line.setObjectName(u"file_systems_line")
        self.file_systems_line.setFrameShape(QFrame.Shape.HLine)
        self.file_systems_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.storage_page_layout.addWidget(self.file_systems_line)

        self.storage_devices_label = QLabel(self.performance_storage_page)
        self.storage_devices_label.setObjectName(u"storage_devices_label")

        self.storage_page_layout.addWidget(self.storage_devices_label)

        self.storage_devices_table = QTableWidget(self.performance_storage_page)
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
        self.storage_devices_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.storage_devices_table.setAlternatingRowColors(True)
        self.storage_devices_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.storage_devices_table.setShowGrid(False)
        self.storage_devices_table.horizontalHeader().setCascadingSectionResizes(True)

        self.storage_page_layout.addWidget(self.storage_devices_table)

        self.performance_stacked_content.addWidget(self.performance_storage_page)
        self.performance_thermal_page = QWidget()
        self.performance_thermal_page.setObjectName(u"performance_thermal_page")
        self.thermals_page_layout = QVBoxLayout(self.performance_thermal_page)
        self.thermals_page_layout.setSpacing(15)
        self.thermals_page_layout.setObjectName(u"thermals_page_layout")
        self.thermals_page_layout.setContentsMargins(0, 0, 0, 0)
        self.thermals_label = QLabel(self.performance_thermal_page)
        self.thermals_label.setObjectName(u"thermals_label")
        self.thermals_label.setMaximumSize(QSize(16777215, 40))

        self.thermals_page_layout.addWidget(self.thermals_label)

        self.thermals_legend_label = QLabel(self.performance_thermal_page)
        self.thermals_legend_label.setObjectName(u"thermals_legend_label")
        self.thermals_legend_label.setMaximumSize(QSize(16777215, 30))

        self.thermals_page_layout.addWidget(self.thermals_legend_label)

        self.thermal_legend_line = QFrame(self.performance_thermal_page)
        self.thermal_legend_line.setObjectName(u"thermal_legend_line")
        self.thermal_legend_line.setFrameShape(QFrame.Shape.HLine)
        self.thermal_legend_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.thermals_page_layout.addWidget(self.thermal_legend_line)

        self.current_thermals_label = QLabel(self.performance_thermal_page)
        self.current_thermals_label.setObjectName(u"current_thermals_label")
        self.current_thermals_label.setMaximumSize(QSize(16777215, 30))

        self.thermals_page_layout.addWidget(self.current_thermals_label)

        self.thermals_gauge_widget = QWidget(self.performance_thermal_page)
        self.thermals_gauge_widget.setObjectName(u"thermals_gauge_widget")
        self.thermals_gauge_layout = QHBoxLayout(self.thermals_gauge_widget)
        self.thermals_gauge_layout.setObjectName(u"thermals_gauge_layout")
        self.thermals_gauge_layout.setContentsMargins(-1, -1, -1, 1)

        self.thermals_page_layout.addWidget(self.thermals_gauge_widget)

        self.current_thermals_line = QFrame(self.performance_thermal_page)
        self.current_thermals_line.setObjectName(u"current_thermals_line")
        self.current_thermals_line.setFrameShape(QFrame.Shape.HLine)
        self.current_thermals_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.thermals_page_layout.addWidget(self.current_thermals_line)

        self.SegmentedWidget = SegmentedWidget(self.performance_thermal_page)
        self.SegmentedWidget.setObjectName(u"SegmentedWidget")
        self.SegmentedWidget.setStyleSheet(u"SegmentedWidget { background: #111B25; border: 1px solid #304452; border-radius: 2px; }\n"
"SegmentedWidget QPushButton { color: #BCD0DD; background: transparent; border: 0; }")

        self.thermals_page_layout.addWidget(self.SegmentedWidget)

        self.thermals_combo_box_layout = QHBoxLayout()
        self.thermals_combo_box_layout.setObjectName(u"thermals_combo_box_layout")
        self.thermals_combo_box_layout.setContentsMargins(0, 0, -1, -1)
        self.temperature_history_label = QLabel(self.performance_thermal_page)
        self.temperature_history_label.setObjectName(u"temperature_history_label")
        self.temperature_history_label.setMinimumSize(QSize(0, 0))
        self.temperature_history_label.setMaximumSize(QSize(16777215, 30))

        self.thermals_combo_box_layout.addWidget(self.temperature_history_label)

        self.thermals_combo_box_right_spacer = QSpacerItem(50, 35, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.thermals_combo_box_layout.addItem(self.thermals_combo_box_right_spacer)

        self.hardware_group_label = QLabel(self.performance_thermal_page)
        self.hardware_group_label.setObjectName(u"hardware_group_label")
        self.hardware_group_label.setMinimumSize(QSize(0, 0))
        self.hardware_group_label.setMaximumSize(QSize(120, 40))

        self.thermals_combo_box_layout.addWidget(self.hardware_group_label)

        self.hardware_group_combo_box = QComboBox(self.performance_thermal_page)
        self.hardware_group_combo_box.setObjectName(u"hardware_group_combo_box")
        self.hardware_group_combo_box.setMinimumSize(QSize(100, 0))
        self.hardware_group_combo_box.setMaximumSize(QSize(120, 16777215))
        self.hardware_group_combo_box.setIconSize(QSize(0, 0))

        self.thermals_combo_box_layout.addWidget(self.hardware_group_combo_box)

        self.thernals_combo_box_separate_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.thermals_combo_box_layout.addItem(self.thernals_combo_box_separate_spacer)

        self.sensor_name_label = QLabel(self.performance_thermal_page)
        self.sensor_name_label.setObjectName(u"sensor_name_label")
        self.sensor_name_label.setMaximumSize(QSize(60, 30))

        self.thermals_combo_box_layout.addWidget(self.sensor_name_label)

        self.thermal_sensor_name_combo_box = QComboBox(self.performance_thermal_page)
        self.thermal_sensor_name_combo_box.setObjectName(u"thermal_sensor_name_combo_box")
        self.thermal_sensor_name_combo_box.setMinimumSize(QSize(0, 0))
        self.thermal_sensor_name_combo_box.setMaximumSize(QSize(120, 30))
        self.thermal_sensor_name_combo_box.setEditable(False)
        self.thermal_sensor_name_combo_box.setInsertPolicy(QComboBox.NoInsert)

        self.thermals_combo_box_layout.addWidget(self.thermal_sensor_name_combo_box)


        self.thermals_page_layout.addLayout(self.thermals_combo_box_layout)

        self.thermals_graph = PlotWidget(self.performance_thermal_page)
        self.thermals_graph.setObjectName(u"thermals_graph")
        self.thermals_graph.setMinimumSize(QSize(0, 300))

        self.thermals_page_layout.addWidget(self.thermals_graph)

        self.thermals_graph_line = QFrame(self.performance_thermal_page)
        self.thermals_graph_line.setObjectName(u"thermals_graph_line")
        self.thermals_graph_line.setFrameShape(QFrame.Shape.HLine)
        self.thermals_graph_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.thermals_page_layout.addWidget(self.thermals_graph_line)

        self.sensors_label = QLabel(self.performance_thermal_page)
        self.sensors_label.setObjectName(u"sensors_label")
        self.sensors_label.setMaximumSize(QSize(16777215, 30))

        self.thermals_page_layout.addWidget(self.sensors_label)

        self.sensors_table = QTableWidget(self.performance_thermal_page)
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
        self.sensors_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.sensors_table.setAlternatingRowColors(True)
        self.sensors_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.sensors_table.setShowGrid(False)
        self.sensors_table.horizontalHeader().setCascadingSectionResizes(True)

        self.thermals_page_layout.addWidget(self.sensors_table)

        self.performance_stacked_content.addWidget(self.performance_thermal_page)
        self.performance_network_page = QWidget()
        self.performance_network_page.setObjectName(u"performance_network_page")
        self.network_page_layout = QVBoxLayout(self.performance_network_page)
        self.network_page_layout.setSpacing(15)
        self.network_page_layout.setObjectName(u"network_page_layout")
        self.network_page_layout.setContentsMargins(0, 0, 0, 0)
        self.network_label = QLabel(self.performance_network_page)
        self.network_label.setObjectName(u"network_label")
        self.network_label.setMaximumSize(QSize(16777215, 40))

        self.network_page_layout.addWidget(self.network_label)

        self.network_legend_label = QLabel(self.performance_network_page)
        self.network_legend_label.setObjectName(u"network_legend_label")
        self.network_legend_label.setMaximumSize(QSize(16777215, 30))

        self.network_page_layout.addWidget(self.network_legend_label)

        self.network_legend_line = QFrame(self.performance_network_page)
        self.network_legend_line.setObjectName(u"network_legend_line")
        self.network_legend_line.setFrameShape(QFrame.Shape.HLine)
        self.network_legend_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.network_page_layout.addWidget(self.network_legend_line)

        self.network_gauges_combo_box_layout = QHBoxLayout()
        self.network_gauges_combo_box_layout.setObjectName(u"network_gauges_combo_box_layout")
        self.network_gauges_combo_box_label = QLabel(self.performance_network_page)
        self.network_gauges_combo_box_label.setObjectName(u"network_gauges_combo_box_label")
        self.network_gauges_combo_box_label.setMaximumSize(QSize(16777215, 30))

        self.network_gauges_combo_box_layout.addWidget(self.network_gauges_combo_box_label)


        self.network_page_layout.addLayout(self.network_gauges_combo_box_layout)

        self.network_gauge_widget = QWidget(self.performance_network_page)
        self.network_gauge_widget.setObjectName(u"network_gauge_widget")
        self.network_gauge_layout = QHBoxLayout(self.network_gauge_widget)
        self.network_gauge_layout.setObjectName(u"network_gauge_layout")
        self.network_gauge_layout.setContentsMargins(-1, -1, -1, 1)

        self.network_page_layout.addWidget(self.network_gauge_widget)

        self.network_gauge_line = QFrame(self.performance_network_page)
        self.network_gauge_line.setObjectName(u"network_gauge_line")
        self.network_gauge_line.setFrameShape(QFrame.Shape.HLine)
        self.network_gauge_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.network_page_layout.addWidget(self.network_gauge_line)

        self.network_traffic_graph_combo_box_layout = QHBoxLayout()
        self.network_traffic_graph_combo_box_layout.setObjectName(u"network_traffic_graph_combo_box_layout")
        self.network_traffic_graph_combo_box_layout.setContentsMargins(0, 0, -1, -1)
        self.rx_tx_throughput_label = QLabel(self.performance_network_page)
        self.rx_tx_throughput_label.setObjectName(u"rx_tx_throughput_label")
        self.rx_tx_throughput_label.setMinimumSize(QSize(0, 0))
        self.rx_tx_throughput_label.setMaximumSize(QSize(16777215, 30))

        self.network_traffic_graph_combo_box_layout.addWidget(self.rx_tx_throughput_label)

        self.network_traffic_graph_combo_box_spacer = QSpacerItem(50, 35, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.network_traffic_graph_combo_box_layout.addItem(self.network_traffic_graph_combo_box_spacer)

        self.network_group_combo_box_legend_label = QLabel(self.performance_network_page)
        self.network_group_combo_box_legend_label.setObjectName(u"network_group_combo_box_legend_label")
        self.network_group_combo_box_legend_label.setMaximumSize(QSize(16777215, 30))

        self.network_traffic_graph_combo_box_layout.addWidget(self.network_group_combo_box_legend_label)

        self.network_traffic_graph_combo_box = QComboBox(self.performance_network_page)
        self.network_traffic_graph_combo_box.setObjectName(u"network_traffic_graph_combo_box")
        self.network_traffic_graph_combo_box.setMaximumSize(QSize(16777215, 16777215))
        self.network_traffic_graph_combo_box.setMaxVisibleItems(5)
        self.network_traffic_graph_combo_box.setFrame(True)

        self.network_traffic_graph_combo_box_layout.addWidget(self.network_traffic_graph_combo_box)

        self.network_traffic_unit_combo_box = QComboBox(self.performance_network_page)
        self.network_traffic_unit_combo_box.setObjectName(u"network_traffic_unit_combo_box")
        self.network_traffic_unit_combo_box.setMaximumSize(QSize(70, 16777215))

        self.network_traffic_graph_combo_box_layout.addWidget(self.network_traffic_unit_combo_box)


        self.network_page_layout.addLayout(self.network_traffic_graph_combo_box_layout)

        self.network_graph_toggle_buttons_widget = QWidget(self.performance_network_page)
        self.network_graph_toggle_buttons_widget.setObjectName(u"network_graph_toggle_buttons_widget")
        self.network_graph_toggle_buttons_layout = QHBoxLayout(self.network_graph_toggle_buttons_widget)
        self.network_graph_toggle_buttons_layout.setSpacing(10)
        self.network_graph_toggle_buttons_layout.setObjectName(u"network_graph_toggle_buttons_layout")
        self.network_graph_toggle_buttons_layout.setContentsMargins(5, 7, 5, 7)
        self.network_traffic_toggle_button = QPushButton(self.network_graph_toggle_buttons_widget)
        self.network_traffic_toggle_button.setObjectName(u"network_traffic_toggle_button")

        self.network_graph_toggle_buttons_layout.addWidget(self.network_traffic_toggle_button)

        self.network_packets_toggle_button = QPushButton(self.network_graph_toggle_buttons_widget)
        self.network_packets_toggle_button.setObjectName(u"network_packets_toggle_button")

        self.network_graph_toggle_buttons_layout.addWidget(self.network_packets_toggle_button)


        self.network_page_layout.addWidget(self.network_graph_toggle_buttons_widget)

        self.network_graph = PlotWidget(self.performance_network_page)
        self.network_graph.setObjectName(u"network_graph")
        self.network_graph.setMinimumSize(QSize(0, 300))

        self.network_page_layout.addWidget(self.network_graph)

        self.network_packets_graph_line = QFrame(self.performance_network_page)
        self.network_packets_graph_line.setObjectName(u"network_packets_graph_line")
        self.network_packets_graph_line.setFrameShape(QFrame.Shape.HLine)
        self.network_packets_graph_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.network_page_layout.addWidget(self.network_packets_graph_line)

        self.network_health_label = QLabel(self.performance_network_page)
        self.network_health_label.setObjectName(u"network_health_label")

        self.network_page_layout.addWidget(self.network_health_label)

        self.network_health_widget = QWidget(self.performance_network_page)
        self.network_health_widget.setObjectName(u"network_health_widget")
        self.network_health_layout = QHBoxLayout(self.network_health_widget)
        self.network_health_layout.setObjectName(u"network_health_layout")
        self.network_health_layout.setContentsMargins(0, 0, 0, 0)
        self.network_health_errors_widget = QWidget(self.network_health_widget)
        self.network_health_errors_widget.setObjectName(u"network_health_errors_widget")
        self.network_health_errors_widget.setMinimumSize(QSize(300, 200))
        self.network_health_errors_widget.setMaximumSize(QSize(16777215, 200))
        self.network_health_errors_layout = QVBoxLayout(self.network_health_errors_widget)
        self.network_health_errors_layout.setObjectName(u"network_health_errors_layout")
        self.network_health_errors_layout.setContentsMargins(5, 5, 5, 0)
        self.network_health_errors_label = QLabel(self.network_health_errors_widget)
        self.network_health_errors_label.setObjectName(u"network_health_errors_label")
        self.network_health_errors_label.setMaximumSize(QSize(16777215, 30))

        self.network_health_errors_layout.addWidget(self.network_health_errors_label)

        self.network_health_errors_line = QFrame(self.network_health_errors_widget)
        self.network_health_errors_line.setObjectName(u"network_health_errors_line")
        self.network_health_errors_line.setFrameShape(QFrame.Shape.HLine)
        self.network_health_errors_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.network_health_errors_layout.addWidget(self.network_health_errors_line)

        self.network_health_errors_content_widget = QWidget(self.network_health_errors_widget)
        self.network_health_errors_content_widget.setObjectName(u"network_health_errors_content_widget")
        self.network_health_errors_content_widget.setMinimumSize(QSize(0, 120))
        self.network_health_errors_content_widget.setMaximumSize(QSize(16777215, 120))
        self.network_health_errors_content_layout = QVBoxLayout(self.network_health_errors_content_widget)
        self.network_health_errors_content_layout.setObjectName(u"network_health_errors_content_layout")
        self.network_health_errors_content_layout.setContentsMargins(0, 0, 0, 0)
        self.network_health_errors_content_top_layout = QHBoxLayout()
        self.network_health_errors_content_top_layout.setObjectName(u"network_health_errors_content_top_layout")
        self.network_health_errors_content_top_layout.setContentsMargins(-1, -1, -1, 0)
        self.network_health_errors_content_top_rx_errors_label = QLabel(self.network_health_errors_content_widget)
        self.network_health_errors_content_top_rx_errors_label.setObjectName(u"network_health_errors_content_top_rx_errors_label")

        self.network_health_errors_content_top_layout.addWidget(self.network_health_errors_content_top_rx_errors_label)

        self.network_health_errors_content_top_rx_errors_value_label = QLabel(self.network_health_errors_content_widget)
        self.network_health_errors_content_top_rx_errors_value_label.setObjectName(u"network_health_errors_content_top_rx_errors_value_label")

        self.network_health_errors_content_top_layout.addWidget(self.network_health_errors_content_top_rx_errors_value_label)


        self.network_health_errors_content_layout.addLayout(self.network_health_errors_content_top_layout)

        self.network_health_errors_content_bottom_layout = QHBoxLayout()
        self.network_health_errors_content_bottom_layout.setObjectName(u"network_health_errors_content_bottom_layout")
        self.network_health_errors_content_bottom_layout.setContentsMargins(-1, -1, -1, 0)
        self.network_health_errors_content_bottom_tx_errors_label = QLabel(self.network_health_errors_content_widget)
        self.network_health_errors_content_bottom_tx_errors_label.setObjectName(u"network_health_errors_content_bottom_tx_errors_label")

        self.network_health_errors_content_bottom_layout.addWidget(self.network_health_errors_content_bottom_tx_errors_label)

        self.network_health_errors_content_bottom_tx_errors_value_label = QLabel(self.network_health_errors_content_widget)
        self.network_health_errors_content_bottom_tx_errors_value_label.setObjectName(u"network_health_errors_content_bottom_tx_errors_value_label")

        self.network_health_errors_content_bottom_layout.addWidget(self.network_health_errors_content_bottom_tx_errors_value_label)


        self.network_health_errors_content_layout.addLayout(self.network_health_errors_content_bottom_layout)


        self.network_health_errors_layout.addWidget(self.network_health_errors_content_widget)


        self.network_health_layout.addWidget(self.network_health_errors_widget)

        self.left_health_widget_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.network_health_layout.addItem(self.left_health_widget_spacer)

        self.network_health_drops_widget = QWidget(self.network_health_widget)
        self.network_health_drops_widget.setObjectName(u"network_health_drops_widget")
        self.network_health_drops_widget.setMinimumSize(QSize(300, 200))
        self.network_health_drops_widget.setMaximumSize(QSize(16777215, 200))
        self.network_health_drops_layout = QVBoxLayout(self.network_health_drops_widget)
        self.network_health_drops_layout.setObjectName(u"network_health_drops_layout")
        self.network_health_drops_layout.setContentsMargins(5, 5, 5, 0)
        self.network_health_drops_label = QLabel(self.network_health_drops_widget)
        self.network_health_drops_label.setObjectName(u"network_health_drops_label")
        self.network_health_drops_label.setMaximumSize(QSize(16777215, 30))

        self.network_health_drops_layout.addWidget(self.network_health_drops_label)

        self.network_health_drops_line = QFrame(self.network_health_drops_widget)
        self.network_health_drops_line.setObjectName(u"network_health_drops_line")
        self.network_health_drops_line.setFrameShape(QFrame.Shape.HLine)
        self.network_health_drops_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.network_health_drops_layout.addWidget(self.network_health_drops_line)

        self.network_health_drops_content_widget = QWidget(self.network_health_drops_widget)
        self.network_health_drops_content_widget.setObjectName(u"network_health_drops_content_widget")
        self.network_health_drops_content_widget.setMinimumSize(QSize(0, 120))
        self.network_health_drops_content_widget.setMaximumSize(QSize(16777215, 120))
        self.network_health_drops_content_layout = QVBoxLayout(self.network_health_drops_content_widget)
        self.network_health_drops_content_layout.setObjectName(u"network_health_drops_content_layout")
        self.network_health_drops_content_layout.setContentsMargins(0, 0, 0, 0)
        self.network_health_drops_content_top_layout = QHBoxLayout()
        self.network_health_drops_content_top_layout.setObjectName(u"network_health_drops_content_top_layout")
        self.network_health_drops_content_top_layout.setContentsMargins(-1, -1, -1, 0)
        self.network_health_drops_content_top_rx_drops_label = QLabel(self.network_health_drops_content_widget)
        self.network_health_drops_content_top_rx_drops_label.setObjectName(u"network_health_drops_content_top_rx_drops_label")

        self.network_health_drops_content_top_layout.addWidget(self.network_health_drops_content_top_rx_drops_label)

        self.network_health_drops_content_top_rx_drops_value_label = QLabel(self.network_health_drops_content_widget)
        self.network_health_drops_content_top_rx_drops_value_label.setObjectName(u"network_health_drops_content_top_rx_drops_value_label")

        self.network_health_drops_content_top_layout.addWidget(self.network_health_drops_content_top_rx_drops_value_label)


        self.network_health_drops_content_layout.addLayout(self.network_health_drops_content_top_layout)

        self.network_health_drops_content_bottom_layout = QHBoxLayout()
        self.network_health_drops_content_bottom_layout.setObjectName(u"network_health_drops_content_bottom_layout")
        self.network_health_drops_content_bottom_layout.setContentsMargins(-1, -1, -1, 0)
        self.network_health_drops_content_bottom_tx_drops_label = QLabel(self.network_health_drops_content_widget)
        self.network_health_drops_content_bottom_tx_drops_label.setObjectName(u"network_health_drops_content_bottom_tx_drops_label")

        self.network_health_drops_content_bottom_layout.addWidget(self.network_health_drops_content_bottom_tx_drops_label)

        self.network_health_drops_content_bottom_tx_drops_value_label = QLabel(self.network_health_drops_content_widget)
        self.network_health_drops_content_bottom_tx_drops_value_label.setObjectName(u"network_health_drops_content_bottom_tx_drops_value_label")

        self.network_health_drops_content_bottom_layout.addWidget(self.network_health_drops_content_bottom_tx_drops_value_label)


        self.network_health_drops_content_layout.addLayout(self.network_health_drops_content_bottom_layout)


        self.network_health_drops_layout.addWidget(self.network_health_drops_content_widget)


        self.network_health_layout.addWidget(self.network_health_drops_widget)

        self.right_health_widget_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.network_health_layout.addItem(self.right_health_widget_spacer)

        self.network_health_total_widget = QWidget(self.network_health_widget)
        self.network_health_total_widget.setObjectName(u"network_health_total_widget")
        self.network_health_total_widget.setMinimumSize(QSize(300, 200))
        self.network_health_total_widget.setMaximumSize(QSize(16777215, 200))
        self.network_health_total_layout = QVBoxLayout(self.network_health_total_widget)
        self.network_health_total_layout.setObjectName(u"network_health_total_layout")
        self.network_health_total_layout.setContentsMargins(5, 5, 5, 0)
        self.network_health_total_label = QLabel(self.network_health_total_widget)
        self.network_health_total_label.setObjectName(u"network_health_total_label")
        self.network_health_total_label.setMaximumSize(QSize(16777215, 30))

        self.network_health_total_layout.addWidget(self.network_health_total_label)

        self.network_health_total_line = QFrame(self.network_health_total_widget)
        self.network_health_total_line.setObjectName(u"network_health_total_line")
        self.network_health_total_line.setFrameShape(QFrame.Shape.HLine)
        self.network_health_total_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.network_health_total_layout.addWidget(self.network_health_total_line)

        self.network_health_total_content_widget = QWidget(self.network_health_total_widget)
        self.network_health_total_content_widget.setObjectName(u"network_health_total_content_widget")
        self.network_health_total_content_widget.setMinimumSize(QSize(0, 120))
        self.network_health_total_content_widget.setMaximumSize(QSize(16777215, 120))
        self.network_health_total_content_layout = QVBoxLayout(self.network_health_total_content_widget)
        self.network_health_total_content_layout.setSpacing(0)
        self.network_health_total_content_layout.setObjectName(u"network_health_total_content_layout")
        self.network_health_total_content_layout.setContentsMargins(0, 0, 0, 0)
        self.network_health_total_content_top_layout = QVBoxLayout()
        self.network_health_total_content_top_layout.setSpacing(0)
        self.network_health_total_content_top_layout.setObjectName(u"network_health_total_content_top_layout")
        self.network_health_total_content_top_layout.setContentsMargins(-1, -1, -1, 0)
        self.network_health_total_content_top_rx_packets_layout = QHBoxLayout()
        self.network_health_total_content_top_rx_packets_layout.setObjectName(u"network_health_total_content_top_rx_packets_layout")
        self.network_health_total_content_top_rx_packets_layout.setContentsMargins(-1, -1, -1, 0)
        self.network_health_total_content_top_rx_packets_label = QLabel(self.network_health_total_content_widget)
        self.network_health_total_content_top_rx_packets_label.setObjectName(u"network_health_total_content_top_rx_packets_label")

        self.network_health_total_content_top_rx_packets_layout.addWidget(self.network_health_total_content_top_rx_packets_label)

        self.network_health_total_content_top_rx_packets_value_label = QLabel(self.network_health_total_content_widget)
        self.network_health_total_content_top_rx_packets_value_label.setObjectName(u"network_health_total_content_top_rx_packets_value_label")

        self.network_health_total_content_top_rx_packets_layout.addWidget(self.network_health_total_content_top_rx_packets_value_label)


        self.network_health_total_content_top_layout.addLayout(self.network_health_total_content_top_rx_packets_layout)

        self.network_health_total_content_bottom_tx_packets_layout = QHBoxLayout()
        self.network_health_total_content_bottom_tx_packets_layout.setObjectName(u"network_health_total_content_bottom_tx_packets_layout")
        self.network_health_total_content_bottom_tx_packets_layout.setContentsMargins(-1, -1, -1, 0)
        self.network_health_total_content_top_tx_packets_label = QLabel(self.network_health_total_content_widget)
        self.network_health_total_content_top_tx_packets_label.setObjectName(u"network_health_total_content_top_tx_packets_label")

        self.network_health_total_content_bottom_tx_packets_layout.addWidget(self.network_health_total_content_top_tx_packets_label)

        self.network_health_total_content_top_tx_packets_value_label = QLabel(self.network_health_total_content_widget)
        self.network_health_total_content_top_tx_packets_value_label.setObjectName(u"network_health_total_content_top_tx_packets_value_label")

        self.network_health_total_content_bottom_tx_packets_layout.addWidget(self.network_health_total_content_top_tx_packets_value_label)


        self.network_health_total_content_top_layout.addLayout(self.network_health_total_content_bottom_tx_packets_layout)


        self.network_health_total_content_layout.addLayout(self.network_health_total_content_top_layout)

        self.network_health_total_content_bottom_layout = QVBoxLayout()
        self.network_health_total_content_bottom_layout.setSpacing(0)
        self.network_health_total_content_bottom_layout.setObjectName(u"network_health_total_content_bottom_layout")
        self.network_health_total_content_bottom_layout.setContentsMargins(-1, -1, -1, 0)
        self.network_health_total_content_bottom_rx_data_layout = QHBoxLayout()
        self.network_health_total_content_bottom_rx_data_layout.setObjectName(u"network_health_total_content_bottom_rx_data_layout")
        self.network_health_total_content_bottom_rx_data_layout.setContentsMargins(-1, -1, -1, 0)
        self.network_health_total_content_bottom_rx_data_label = QLabel(self.network_health_total_content_widget)
        self.network_health_total_content_bottom_rx_data_label.setObjectName(u"network_health_total_content_bottom_rx_data_label")

        self.network_health_total_content_bottom_rx_data_layout.addWidget(self.network_health_total_content_bottom_rx_data_label)

        self.network_health_total_content_bottom_rx_data_value_label = QLabel(self.network_health_total_content_widget)
        self.network_health_total_content_bottom_rx_data_value_label.setObjectName(u"network_health_total_content_bottom_rx_data_value_label")

        self.network_health_total_content_bottom_rx_data_layout.addWidget(self.network_health_total_content_bottom_rx_data_value_label)


        self.network_health_total_content_bottom_layout.addLayout(self.network_health_total_content_bottom_rx_data_layout)

        self.network_health_total_content_bottom_tx_data_layout = QHBoxLayout()
        self.network_health_total_content_bottom_tx_data_layout.setObjectName(u"network_health_total_content_bottom_tx_data_layout")
        self.network_health_total_content_bottom_tx_data_layout.setContentsMargins(-1, -1, -1, 0)
        self.network_health_total_content_bottom_tx_data_label = QLabel(self.network_health_total_content_widget)
        self.network_health_total_content_bottom_tx_data_label.setObjectName(u"network_health_total_content_bottom_tx_data_label")

        self.network_health_total_content_bottom_tx_data_layout.addWidget(self.network_health_total_content_bottom_tx_data_label)

        self.network_health_total_content_bottom_tx_data_value_label = QLabel(self.network_health_total_content_widget)
        self.network_health_total_content_bottom_tx_data_value_label.setObjectName(u"network_health_total_content_bottom_tx_data_value_label")

        self.network_health_total_content_bottom_tx_data_layout.addWidget(self.network_health_total_content_bottom_tx_data_value_label)


        self.network_health_total_content_bottom_layout.addLayout(self.network_health_total_content_bottom_tx_data_layout)


        self.network_health_total_content_layout.addLayout(self.network_health_total_content_bottom_layout)


        self.network_health_total_layout.addWidget(self.network_health_total_content_widget)


        self.network_health_layout.addWidget(self.network_health_total_widget)


        self.network_page_layout.addWidget(self.network_health_widget)

        self.network_health_line = QFrame(self.performance_network_page)
        self.network_health_line.setObjectName(u"network_health_line")
        self.network_health_line.setFrameShape(QFrame.Shape.HLine)
        self.network_health_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.network_page_layout.addWidget(self.network_health_line)

        self.network_interfaces_label = QLabel(self.performance_network_page)
        self.network_interfaces_label.setObjectName(u"network_interfaces_label")

        self.network_page_layout.addWidget(self.network_interfaces_label)

        self.network_interfaces_table = QTableWidget(self.performance_network_page)
        if (self.network_interfaces_table.columnCount() < 7):
            self.network_interfaces_table.setColumnCount(7)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.network_interfaces_table.setHorizontalHeaderItem(0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.network_interfaces_table.setHorizontalHeaderItem(1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.network_interfaces_table.setHorizontalHeaderItem(2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.network_interfaces_table.setHorizontalHeaderItem(3, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.network_interfaces_table.setHorizontalHeaderItem(4, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.network_interfaces_table.setHorizontalHeaderItem(5, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.network_interfaces_table.setHorizontalHeaderItem(6, __qtablewidgetitem28)
        self.network_interfaces_table.setObjectName(u"network_interfaces_table")
        self.network_interfaces_table.setMinimumSize(QSize(0, 200))
        self.network_interfaces_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.network_interfaces_table.setAlternatingRowColors(True)
        self.network_interfaces_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.network_interfaces_table.setShowGrid(False)
        self.network_interfaces_table.horizontalHeader().setCascadingSectionResizes(True)

        self.network_page_layout.addWidget(self.network_interfaces_table)

        self.performance_stacked_content.addWidget(self.performance_network_page)

        self.performance_content_layout.addWidget(self.performance_stacked_content)


        self.agent_performance_information_layout.addWidget(self.performance_content_widget)

        self.performance_detail_scroll.setWidget(self.agent_performance_information)

        self.performance_detail_page_layout.addWidget(self.performance_detail_scroll)

        self.agent_detail_stacked_content.addWidget(self.performance_detail_page)
        self.hardware_detail_page = QWidget()
        self.hardware_detail_page.setObjectName(u"hardware_detail_page")
        self.hardware_detail_page_layout = QVBoxLayout(self.hardware_detail_page)
        self.hardware_detail_page_layout.setSpacing(14)
        self.hardware_detail_page_layout.setObjectName(u"hardware_detail_page_layout")
        self.hardware_detail_page_layout.setContentsMargins(2, 8, 2, 5)
        self.hardware_label = QLabel(self.hardware_detail_page)
        self.hardware_label.setObjectName(u"hardware_label")
        self.hardware_label.setMinimumSize(QSize(0, 0))
        self.hardware_label.setMaximumSize(QSize(16777215, 28))

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
        self.hardware_info_scroll.setFrameShape(QFrame.NoFrame)
        self.hardware_info_scroll.setWidgetResizable(True)
        self.hardware_info_scroll_content = QWidget()
        self.hardware_info_scroll_content.setObjectName(u"hardware_info_scroll_content")
        self.hardware_info_scroll_content.setGeometry(QRect(0, 0, 129, 1228))
        self.hardware_info_scroll_content.setMinimumSize(QSize(0, 0))
        self.hardware_info_scroll_content_layout = QGridLayout(self.hardware_info_scroll_content)
        self.hardware_info_scroll_content_layout.setObjectName(u"hardware_info_scroll_content_layout")
        self.hardware_info_scroll_content_layout.setHorizontalSpacing(15)
        self.hardware_info_scroll_content_layout.setVerticalSpacing(20)
        self.hardware_info_scroll_content_layout.setContentsMargins(0, 0, 6, 0)
        self.hardware_storage_inventory_panel_layout = QVBoxLayout()
        self.hardware_storage_inventory_panel_layout.setSpacing(12)
        self.hardware_storage_inventory_panel_layout.setObjectName(u"hardware_storage_inventory_panel_layout")
        self.hardware_storage_inventory_panel_layout.setContentsMargins(0, 0, 0, 0)
        self.hardware_storage_inventory_panel_header = QLabel(self.hardware_info_scroll_content)
        self.hardware_storage_inventory_panel_header.setObjectName(u"hardware_storage_inventory_panel_header")

        self.hardware_storage_inventory_panel_layout.addWidget(self.hardware_storage_inventory_panel_header)

        self.hardware_storage_devices_table = QTableWidget(self.hardware_info_scroll_content)
        if (self.hardware_storage_devices_table.columnCount() < 4):
            self.hardware_storage_devices_table.setColumnCount(4)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.hardware_storage_devices_table.setHorizontalHeaderItem(0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.hardware_storage_devices_table.setHorizontalHeaderItem(1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.hardware_storage_devices_table.setHorizontalHeaderItem(2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.hardware_storage_devices_table.setHorizontalHeaderItem(3, __qtablewidgetitem32)
        self.hardware_storage_devices_table.setObjectName(u"hardware_storage_devices_table")
        self.hardware_storage_devices_table.setMinimumSize(QSize(0, 155))
        self.hardware_storage_devices_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.hardware_storage_devices_table.setAlternatingRowColors(True)
        self.hardware_storage_devices_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.hardware_storage_devices_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.hardware_storage_devices_table.setShowGrid(False)
        self.hardware_storage_devices_table.setRowCount(0)
        self.hardware_storage_devices_table.setColumnCount(4)

        self.hardware_storage_inventory_panel_layout.addWidget(self.hardware_storage_devices_table)


        self.hardware_info_scroll_content_layout.addLayout(self.hardware_storage_inventory_panel_layout, 5, 0, 1, 2)

        self.hardware_inventory_action_row = QHBoxLayout()
        self.hardware_inventory_action_row.setSpacing(8)
        self.hardware_inventory_action_row.setObjectName(u"hardware_inventory_action_row")
        self.hardware_inventory_action_row.setContentsMargins(0, 0, 0, 0)
        self.hardware_refresh_inventory_button = QPushButton(self.hardware_info_scroll_content)
        self.hardware_refresh_inventory_button.setObjectName(u"hardware_refresh_inventory_button")
        self.hardware_refresh_inventory_button.setMinimumSize(QSize(0, 0))
        self.hardware_refresh_inventory_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.hardware_inventory_action_row.addWidget(self.hardware_refresh_inventory_button)


        self.hardware_info_scroll_content_layout.addLayout(self.hardware_inventory_action_row, 0, 0, 1, 2)

        self.hardware_gpu_inventory_panel_layout = QVBoxLayout()
        self.hardware_gpu_inventory_panel_layout.setSpacing(12)
        self.hardware_gpu_inventory_panel_layout.setObjectName(u"hardware_gpu_inventory_panel_layout")
        self.hardware_gpu_inventory_panel_layout.setContentsMargins(0, 0, 0, 0)
        self.hardware_gpu_inventory_panel_header = QLabel(self.hardware_info_scroll_content)
        self.hardware_gpu_inventory_panel_header.setObjectName(u"hardware_gpu_inventory_panel_header")

        self.hardware_gpu_inventory_panel_layout.addWidget(self.hardware_gpu_inventory_panel_header)

        self.hardware_gpu_inventory_table = QTableWidget(self.hardware_info_scroll_content)
        if (self.hardware_gpu_inventory_table.columnCount() < 5):
            self.hardware_gpu_inventory_table.setColumnCount(5)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.hardware_gpu_inventory_table.setHorizontalHeaderItem(0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.hardware_gpu_inventory_table.setHorizontalHeaderItem(1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.hardware_gpu_inventory_table.setHorizontalHeaderItem(2, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.hardware_gpu_inventory_table.setHorizontalHeaderItem(3, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.hardware_gpu_inventory_table.setHorizontalHeaderItem(4, __qtablewidgetitem37)
        self.hardware_gpu_inventory_table.setObjectName(u"hardware_gpu_inventory_table")
        self.hardware_gpu_inventory_table.setMinimumSize(QSize(0, 155))
        self.hardware_gpu_inventory_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.hardware_gpu_inventory_table.setAlternatingRowColors(True)
        self.hardware_gpu_inventory_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.hardware_gpu_inventory_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.hardware_gpu_inventory_table.setShowGrid(False)
        self.hardware_gpu_inventory_table.setRowCount(0)
        self.hardware_gpu_inventory_table.setColumnCount(5)

        self.hardware_gpu_inventory_panel_layout.addWidget(self.hardware_gpu_inventory_table)


        self.hardware_info_scroll_content_layout.addLayout(self.hardware_gpu_inventory_panel_layout, 2, 0, 1, 2)

        self.hardware_bios_motherboard_inventory_panel_layout = QVBoxLayout()
        self.hardware_bios_motherboard_inventory_panel_layout.setSpacing(12)
        self.hardware_bios_motherboard_inventory_panel_layout.setObjectName(u"hardware_bios_motherboard_inventory_panel_layout")
        self.hardware_bios_motherboard_inventory_panel_layout.setContentsMargins(0, 0, 0, 0)
        self.hardware_bios_motherboard_panel_header = QLabel(self.hardware_info_scroll_content)
        self.hardware_bios_motherboard_panel_header.setObjectName(u"hardware_bios_motherboard_panel_header")

        self.hardware_bios_motherboard_inventory_panel_layout.addWidget(self.hardware_bios_motherboard_panel_header)

        self.hardware_bios_motherboard_table = QTableWidget(self.hardware_info_scroll_content)
        if (self.hardware_bios_motherboard_table.columnCount() < 5):
            self.hardware_bios_motherboard_table.setColumnCount(5)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.hardware_bios_motherboard_table.setHorizontalHeaderItem(0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.hardware_bios_motherboard_table.setHorizontalHeaderItem(1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.hardware_bios_motherboard_table.setHorizontalHeaderItem(2, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.hardware_bios_motherboard_table.setHorizontalHeaderItem(3, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.hardware_bios_motherboard_table.setHorizontalHeaderItem(4, __qtablewidgetitem42)
        self.hardware_bios_motherboard_table.setObjectName(u"hardware_bios_motherboard_table")
        self.hardware_bios_motherboard_table.setMinimumSize(QSize(0, 155))
        self.hardware_bios_motherboard_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.hardware_bios_motherboard_table.setAlternatingRowColors(True)
        self.hardware_bios_motherboard_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.hardware_bios_motherboard_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.hardware_bios_motherboard_table.setShowGrid(False)
        self.hardware_bios_motherboard_table.setRowCount(0)
        self.hardware_bios_motherboard_table.setColumnCount(5)

        self.hardware_bios_motherboard_inventory_panel_layout.addWidget(self.hardware_bios_motherboard_table)


        self.hardware_info_scroll_content_layout.addLayout(self.hardware_bios_motherboard_inventory_panel_layout, 4, 0, 1, 2)

        self.hardware_memory_inventory_panel_layout = QVBoxLayout()
        self.hardware_memory_inventory_panel_layout.setSpacing(12)
        self.hardware_memory_inventory_panel_layout.setObjectName(u"hardware_memory_inventory_panel_layout")
        self.hardware_memory_inventory_panel_layout.setContentsMargins(0, 0, 0, 0)
        self.hardware_ram_modules_panel_header = QLabel(self.hardware_info_scroll_content)
        self.hardware_ram_modules_panel_header.setObjectName(u"hardware_ram_modules_panel_header")

        self.hardware_memory_inventory_panel_layout.addWidget(self.hardware_ram_modules_panel_header)

        self.hardware_ram_modules_table = QTableWidget(self.hardware_info_scroll_content)
        if (self.hardware_ram_modules_table.columnCount() < 2):
            self.hardware_ram_modules_table.setColumnCount(2)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.hardware_ram_modules_table.setHorizontalHeaderItem(0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.hardware_ram_modules_table.setHorizontalHeaderItem(1, __qtablewidgetitem44)
        self.hardware_ram_modules_table.setObjectName(u"hardware_ram_modules_table")
        self.hardware_ram_modules_table.setMinimumSize(QSize(0, 155))
        self.hardware_ram_modules_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.hardware_ram_modules_table.setAlternatingRowColors(True)
        self.hardware_ram_modules_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.hardware_ram_modules_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.hardware_ram_modules_table.setShowGrid(False)
        self.hardware_ram_modules_table.setRowCount(0)
        self.hardware_ram_modules_table.setColumnCount(2)

        self.hardware_memory_inventory_panel_layout.addWidget(self.hardware_ram_modules_table)


        self.hardware_info_scroll_content_layout.addLayout(self.hardware_memory_inventory_panel_layout, 3, 0, 1, 2)

        self.hardware_network_inventory_panel_layout = QVBoxLayout()
        self.hardware_network_inventory_panel_layout.setSpacing(12)
        self.hardware_network_inventory_panel_layout.setObjectName(u"hardware_network_inventory_panel_layout")
        self.hardware_network_inventory_panel_layout.setContentsMargins(0, 10, 0, 0)
        self.hardware_network_inventory_panel_header = QLabel(self.hardware_info_scroll_content)
        self.hardware_network_inventory_panel_header.setObjectName(u"hardware_network_inventory_panel_header")

        self.hardware_network_inventory_panel_layout.addWidget(self.hardware_network_inventory_panel_header)

        self.hardware_network_adapters_table = QTableWidget(self.hardware_info_scroll_content)
        if (self.hardware_network_adapters_table.columnCount() < 5):
            self.hardware_network_adapters_table.setColumnCount(5)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.hardware_network_adapters_table.setHorizontalHeaderItem(0, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.hardware_network_adapters_table.setHorizontalHeaderItem(1, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.hardware_network_adapters_table.setHorizontalHeaderItem(2, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.hardware_network_adapters_table.setHorizontalHeaderItem(3, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.hardware_network_adapters_table.setHorizontalHeaderItem(4, __qtablewidgetitem49)
        self.hardware_network_adapters_table.setObjectName(u"hardware_network_adapters_table")
        self.hardware_network_adapters_table.setMinimumSize(QSize(0, 125))
        self.hardware_network_adapters_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.hardware_network_adapters_table.setAlternatingRowColors(True)
        self.hardware_network_adapters_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.hardware_network_adapters_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.hardware_network_adapters_table.setShowGrid(False)
        self.hardware_network_adapters_table.setRowCount(0)
        self.hardware_network_adapters_table.setColumnCount(5)

        self.hardware_network_inventory_panel_layout.addWidget(self.hardware_network_adapters_table)


        self.hardware_info_scroll_content_layout.addLayout(self.hardware_network_inventory_panel_layout, 6, 0, 1, 2)

        self.hardware_cpu_inventory_panel_layout = QVBoxLayout()
        self.hardware_cpu_inventory_panel_layout.setSpacing(12)
        self.hardware_cpu_inventory_panel_layout.setObjectName(u"hardware_cpu_inventory_panel_layout")
        self.hardware_cpu_inventory_panel_layout.setContentsMargins(0, 0, 0, 0)
        self.hardware_cpu_inventory_panel_header = QLabel(self.hardware_info_scroll_content)
        self.hardware_cpu_inventory_panel_header.setObjectName(u"hardware_cpu_inventory_panel_header")

        self.hardware_cpu_inventory_panel_layout.addWidget(self.hardware_cpu_inventory_panel_header)

        self.hardware_cpu_specifications_table = QTableWidget(self.hardware_info_scroll_content)
        if (self.hardware_cpu_specifications_table.columnCount() < 8):
            self.hardware_cpu_specifications_table.setColumnCount(8)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.hardware_cpu_specifications_table.setHorizontalHeaderItem(0, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.hardware_cpu_specifications_table.setHorizontalHeaderItem(1, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.hardware_cpu_specifications_table.setHorizontalHeaderItem(2, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.hardware_cpu_specifications_table.setHorizontalHeaderItem(3, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.hardware_cpu_specifications_table.setHorizontalHeaderItem(4, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.hardware_cpu_specifications_table.setHorizontalHeaderItem(5, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.hardware_cpu_specifications_table.setHorizontalHeaderItem(6, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.hardware_cpu_specifications_table.setHorizontalHeaderItem(7, __qtablewidgetitem57)
        self.hardware_cpu_specifications_table.setObjectName(u"hardware_cpu_specifications_table")
        self.hardware_cpu_specifications_table.setMinimumSize(QSize(0, 155))
        self.hardware_cpu_specifications_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.hardware_cpu_specifications_table.setAlternatingRowColors(True)
        self.hardware_cpu_specifications_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.hardware_cpu_specifications_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.hardware_cpu_specifications_table.setShowGrid(False)
        self.hardware_cpu_specifications_table.setRowCount(0)
        self.hardware_cpu_specifications_table.setColumnCount(8)

        self.hardware_cpu_inventory_panel_layout.addWidget(self.hardware_cpu_specifications_table)


        self.hardware_info_scroll_content_layout.addLayout(self.hardware_cpu_inventory_panel_layout, 1, 0, 1, 2)

        self.hardware_info_scroll.setWidget(self.hardware_info_scroll_content)

        self.hardware_detail_page_layout.addWidget(self.hardware_info_scroll)

        self.agent_detail_stacked_content.addWidget(self.hardware_detail_page)
        self.agent_commands_page = QWidget()
        self.agent_commands_page.setObjectName(u"agent_commands_page")
        self.agent_commands_page_host_layout = QVBoxLayout(self.agent_commands_page)
        self.agent_commands_page_host_layout.setSpacing(0)
        self.agent_commands_page_host_layout.setObjectName(u"agent_commands_page_host_layout")
        self.agent_commands_page_host_layout.setContentsMargins(0, 0, 0, 0)
        self.agent_commands_page_scroll = QScrollArea(self.agent_commands_page)
        self.agent_commands_page_scroll.setObjectName(u"agent_commands_page_scroll")
        self.agent_commands_page_scroll.setFrameShape(QFrame.NoFrame)
        self.agent_commands_page_scroll.setWidgetResizable(True)
        self.agent_commands_page_scroll_content = QWidget()
        self.agent_commands_page_scroll_content.setObjectName(u"agent_commands_page_scroll_content")
        self.agent_commands_page_scroll_content.setGeometry(QRect(0, 0, 1091, 1393))
        self.agent_commands_page_layout = QVBoxLayout(self.agent_commands_page_scroll_content)
        self.agent_commands_page_layout.setSpacing(16)
        self.agent_commands_page_layout.setObjectName(u"agent_commands_page_layout")
        self.agent_commands_page_layout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.agent_commands_page_layout.setContentsMargins(15, 15, 15, 18)
        self.agent_cmd_heading_row = QHBoxLayout()
        self.agent_cmd_heading_row.setSpacing(12)
        self.agent_cmd_heading_row.setObjectName(u"agent_cmd_heading_row")
        self.agent_cmd_heading_row.setContentsMargins(0, 0, 0, 0)
        self.agent_cmd_heading_text = QVBoxLayout()
        self.agent_cmd_heading_text.setSpacing(6)
        self.agent_cmd_heading_text.setObjectName(u"agent_cmd_heading_text")
        self.agent_cmd_heading_text.setContentsMargins(0, 0, 0, 0)
        self.agent_cmd_title = QLabel(self.agent_commands_page_scroll_content)
        self.agent_cmd_title.setObjectName(u"agent_cmd_title")

        self.agent_cmd_heading_text.addWidget(self.agent_cmd_title)

        self.agent_cmd_subtitle = QLabel(self.agent_commands_page_scroll_content)
        self.agent_cmd_subtitle.setObjectName(u"agent_cmd_subtitle")
        self.agent_cmd_subtitle.setWordWrap(True)

        self.agent_cmd_heading_text.addWidget(self.agent_cmd_subtitle)


        self.agent_cmd_heading_row.addLayout(self.agent_cmd_heading_text)

        self.spacer_auto_4 = QSpacerItem(5, 2, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.agent_cmd_heading_row.addItem(self.spacer_auto_4)

        self.agent_command_target_indicator = QLabel(self.agent_commands_page_scroll_content)
        self.agent_command_target_indicator.setObjectName(u"agent_command_target_indicator")

        self.agent_cmd_heading_row.addWidget(self.agent_command_target_indicator)

        self.agent_cmd_heading_row.setStretch(0, 4)
        self.agent_cmd_heading_row.setStretch(1, 1)

        self.agent_commands_page_layout.addLayout(self.agent_cmd_heading_row)

        self.line_14 = QFrame(self.agent_commands_page_scroll_content)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.Shape.HLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)

        self.agent_commands_page_layout.addWidget(self.line_14)

        self.agent_command_process_strip = QFrame(self.agent_commands_page_scroll_content)
        self.agent_command_process_strip.setObjectName(u"agent_command_process_strip")
        self.agent_command_process_strip_layout = QVBoxLayout(self.agent_command_process_strip)
        self.agent_command_process_strip_layout.setSpacing(0)
        self.agent_command_process_strip_layout.setObjectName(u"agent_command_process_strip_layout")
        self.agent_command_process_strip_layout.setContentsMargins(10, 10, 10, 10)
        self.agent_command_process_steps = QLabel(self.agent_command_process_strip)
        self.agent_command_process_steps.setObjectName(u"agent_command_process_steps")

        self.agent_command_process_strip_layout.addWidget(self.agent_command_process_steps)


        self.agent_commands_page_layout.addWidget(self.agent_command_process_strip)

        self.agent_cmd_top_layout = QHBoxLayout()
        self.agent_cmd_top_layout.setSpacing(12)
        self.agent_cmd_top_layout.setObjectName(u"agent_cmd_top_layout")
        self.agent_cmd_top_layout.setContentsMargins(0, 0, 0, 0)
        self.agent_command_form_panel = QFrame(self.agent_commands_page_scroll_content)
        self.agent_command_form_panel.setObjectName(u"agent_command_form_panel")
        self.agent_command_form_panel.setMinimumSize(QSize(425, 0))
        self.agent_command_form_panel.setMaximumSize(QSize(450, 2313123))
        self.agent_command_form_panel_host_layout = QVBoxLayout(self.agent_command_form_panel)
        self.agent_command_form_panel_host_layout.setSpacing(0)
        self.agent_command_form_panel_host_layout.setObjectName(u"agent_command_form_panel_host_layout")
        self.agent_command_form_panel_host_layout.setContentsMargins(0, 0, 0, 0)
        self.agent_command_form_panel_layout = QVBoxLayout()
        self.agent_command_form_panel_layout.setSpacing(12)
        self.agent_command_form_panel_layout.setObjectName(u"agent_command_form_panel_layout")
        self.agent_command_form_panel_layout.setContentsMargins(16, 15, 16, 16)
        self.widget = QWidget(self.agent_command_form_panel)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 400))
        self.widget.setMaximumSize(QSize(16777215, 400))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.agent_command_form_panel_header = QLabel(self.widget)
        self.agent_command_form_panel_header.setObjectName(u"agent_command_form_panel_header")

        self.verticalLayout.addWidget(self.agent_command_form_panel_header)

        self.agent_command_form_panel_caption = QLabel(self.widget)
        self.agent_command_form_panel_caption.setObjectName(u"agent_command_form_panel_caption")

        self.verticalLayout.addWidget(self.agent_command_form_panel_caption)

        self.agent_command_category_label = QLabel(self.widget)
        self.agent_command_category_label.setObjectName(u"agent_command_category_label")

        self.verticalLayout.addWidget(self.agent_command_category_label)

        self.agent_command_category_combo = QComboBox(self.widget)
        self.agent_command_category_combo.setObjectName(u"agent_command_category_combo")
        self.agent_command_category_combo.setMinimumSize(QSize(0, 43))

        self.verticalLayout.addWidget(self.agent_command_category_combo)

        self.agent_command_type_label = QLabel(self.widget)
        self.agent_command_type_label.setObjectName(u"agent_command_type_label")

        self.verticalLayout.addWidget(self.agent_command_type_label)

        self.agent_command_type_combo = QComboBox(self.widget)
        self.agent_command_type_combo.setObjectName(u"agent_command_type_combo")
        self.agent_command_type_combo.setMinimumSize(QSize(0, 43))

        self.verticalLayout.addWidget(self.agent_command_type_combo)

        self.agent_command_identity_card = QFrame(self.widget)
        self.agent_command_identity_card.setObjectName(u"agent_command_identity_card")
        self.agent_command_identity_card_layout = QVBoxLayout(self.agent_command_identity_card)
        self.agent_command_identity_card_layout.setSpacing(7)
        self.agent_command_identity_card_layout.setObjectName(u"agent_command_identity_card_layout")
        self.agent_command_identity_card_layout.setContentsMargins(12, 12, 12, 12)
        self.agent_command_risk_row = QHBoxLayout()
        self.agent_command_risk_row.setSpacing(8)
        self.agent_command_risk_row.setObjectName(u"agent_command_risk_row")
        self.agent_command_risk_row.setContentsMargins(0, 0, 0, 0)
        self.agent_command_display_title = QLabel(self.agent_command_identity_card)
        self.agent_command_display_title.setObjectName(u"agent_command_display_title")

        self.agent_command_risk_row.addWidget(self.agent_command_display_title)

        self.spacer_auto_5 = QSpacerItem(18, 1, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.agent_command_risk_row.addItem(self.spacer_auto_5)

        self.agent_command_risk_badge = QLabel(self.agent_command_identity_card)
        self.agent_command_risk_badge.setObjectName(u"agent_command_risk_badge")

        self.agent_command_risk_row.addWidget(self.agent_command_risk_badge)


        self.agent_command_identity_card_layout.addLayout(self.agent_command_risk_row)

        self.agent_command_command_key = QLabel(self.agent_command_identity_card)
        self.agent_command_command_key.setObjectName(u"agent_command_command_key")

        self.agent_command_identity_card_layout.addWidget(self.agent_command_command_key)

        self.agent_command_description = QLabel(self.agent_command_identity_card)
        self.agent_command_description.setObjectName(u"agent_command_description")
        self.agent_command_description.setWordWrap(True)

        self.agent_command_identity_card_layout.addWidget(self.agent_command_description)


        self.verticalLayout.addWidget(self.agent_command_identity_card)


        self.agent_command_form_panel_layout.addWidget(self.widget)

        self.agent_command_parameters_heading = QHBoxLayout()
        self.agent_command_parameters_heading.setSpacing(8)
        self.agent_command_parameters_heading.setObjectName(u"agent_command_parameters_heading")
        self.agent_command_parameters_heading.setContentsMargins(0, 0, 0, 0)
        self.agent_command_fields_label = QLabel(self.agent_command_form_panel)
        self.agent_command_fields_label.setObjectName(u"agent_command_fields_label")

        self.agent_command_parameters_heading.addWidget(self.agent_command_fields_label)

        self.agent_command_fields_count = QLabel(self.agent_command_form_panel)
        self.agent_command_fields_count.setObjectName(u"agent_command_fields_count")

        self.agent_command_parameters_heading.addWidget(self.agent_command_fields_count)

        self.agent_command_parameters_heading.setStretch(0, 4)

        self.agent_command_form_panel_layout.addLayout(self.agent_command_parameters_heading)

        self.agent_command_fields_container = QFrame(self.agent_command_form_panel)
        self.agent_command_fields_container.setObjectName(u"agent_command_fields_container")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.agent_command_fields_container.sizePolicy().hasHeightForWidth())
        self.agent_command_fields_container.setSizePolicy(sizePolicy2)
        self.agent_command_fields_container.setMinimumSize(QSize(0, 0))
        self.agent_command_fields_container.setFrameShape(QFrame.NoFrame)
        self.agent_command_fields_layout = QVBoxLayout(self.agent_command_fields_container)
        self.agent_command_fields_layout.setSpacing(9)
        self.agent_command_fields_layout.setObjectName(u"agent_command_fields_layout")
        self.agent_command_fields_layout.setContentsMargins(12, 12, 12, 12)

        self.agent_command_form_panel_layout.addWidget(self.agent_command_fields_container)

        self.agent_command_payload_label = QLabel(self.agent_command_form_panel)
        self.agent_command_payload_label.setObjectName(u"agent_command_payload_label")

        self.agent_command_form_panel_layout.addWidget(self.agent_command_payload_label)

        self.agent_command_raw_mode_checkbox = QCheckBox(self.agent_command_form_panel)
        self.agent_command_raw_mode_checkbox.setObjectName(u"agent_command_raw_mode_checkbox")

        self.agent_command_form_panel_layout.addWidget(self.agent_command_raw_mode_checkbox)

        self.agent_command_payload_editor = QPlainTextEdit(self.agent_command_form_panel)
        self.agent_command_payload_editor.setObjectName(u"agent_command_payload_editor")
        self.agent_command_payload_editor.setMinimumSize(QSize(0, 120))
        self.agent_command_payload_editor.setMaximumSize(QSize(16777215, 200))
        self.agent_command_payload_editor.setFocusPolicy(Qt.ClickFocus)
        self.agent_command_payload_editor.setReadOnly(True)

        self.agent_command_form_panel_layout.addWidget(self.agent_command_payload_editor)


        self.agent_command_form_panel_host_layout.addLayout(self.agent_command_form_panel_layout)


        self.agent_cmd_top_layout.addWidget(self.agent_command_form_panel)

        self.agent_command_inspection_stack_layout = QVBoxLayout()
        self.agent_command_inspection_stack_layout.setSpacing(12)
        self.agent_command_inspection_stack_layout.setObjectName(u"agent_command_inspection_stack_layout")
        self.agent_command_inspection_stack_layout.setContentsMargins(0, 0, 0, 0)
        self.agent_command_review_panel = QFrame(self.agent_commands_page_scroll_content)
        self.agent_command_review_panel.setObjectName(u"agent_command_review_panel")
        self.agent_command_review_panel_layout = QVBoxLayout(self.agent_command_review_panel)
        self.agent_command_review_panel_layout.setSpacing(12)
        self.agent_command_review_panel_layout.setObjectName(u"agent_command_review_panel_layout")
        self.agent_command_review_panel_layout.setContentsMargins(16, 15, 16, 16)
        self.agent_command_review_header = QLabel(self.agent_command_review_panel)
        self.agent_command_review_header.setObjectName(u"agent_command_review_header")

        self.agent_command_review_panel_layout.addWidget(self.agent_command_review_header)

        self.agent_command_review_caption = QLabel(self.agent_command_review_panel)
        self.agent_command_review_caption.setObjectName(u"agent_command_review_caption")
        self.agent_command_review_caption.setWordWrap(True)

        self.agent_command_review_panel_layout.addWidget(self.agent_command_review_caption)

        self.agent_command_review_target = QLabel(self.agent_command_review_panel)
        self.agent_command_review_target.setObjectName(u"agent_command_review_target")

        self.agent_command_review_panel_layout.addWidget(self.agent_command_review_target)

        self.agent_command_review_operation = QLabel(self.agent_command_review_panel)
        self.agent_command_review_operation.setObjectName(u"agent_command_review_operation")

        self.agent_command_review_panel_layout.addWidget(self.agent_command_review_operation)

        self.agent_command_review_payload_label = QLabel(self.agent_command_review_panel)
        self.agent_command_review_payload_label.setObjectName(u"agent_command_review_payload_label")

        self.agent_command_review_panel_layout.addWidget(self.agent_command_review_payload_label)

        self.agent_command_request_preview = QPlainTextEdit(self.agent_command_review_panel)
        self.agent_command_request_preview.setObjectName(u"agent_command_request_preview")
        self.agent_command_request_preview.setMinimumSize(QSize(0, 155))
        self.agent_command_request_preview.setFocusPolicy(Qt.ClickFocus)
        self.agent_command_request_preview.setReadOnly(True)

        self.agent_command_review_panel_layout.addWidget(self.agent_command_request_preview)

        self.agent_command_validation_status = QLabel(self.agent_command_review_panel)
        self.agent_command_validation_status.setObjectName(u"agent_command_validation_status")
        self.agent_command_validation_status.setWordWrap(True)

        self.agent_command_review_panel_layout.addWidget(self.agent_command_validation_status)

        self.agent_command_risk_confirmation_checkbox = QCheckBox(self.agent_command_review_panel)
        self.agent_command_risk_confirmation_checkbox.setObjectName(u"agent_command_risk_confirmation_checkbox")
        self.agent_command_risk_confirmation_checkbox.setVisible(False)

        self.agent_command_review_panel_layout.addWidget(self.agent_command_risk_confirmation_checkbox)

        self.agent_command_action_row = QHBoxLayout()
        self.agent_command_action_row.setSpacing(8)
        self.agent_command_action_row.setObjectName(u"agent_command_action_row")
        self.agent_command_action_row.setContentsMargins(0, 0, 0, 0)
        self.agent_command_validate_button = QPushButton(self.agent_command_review_panel)
        self.agent_command_validate_button.setObjectName(u"agent_command_validate_button")
        self.agent_command_validate_button.setMinimumSize(QSize(0, 39))
        self.agent_command_validate_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.agent_command_action_row.addWidget(self.agent_command_validate_button)

        self.agent_command_execute_button = QPushButton(self.agent_command_review_panel)
        self.agent_command_execute_button.setObjectName(u"agent_command_execute_button")
        self.agent_command_execute_button.setMinimumSize(QSize(0, 39))
        self.agent_command_execute_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.agent_command_action_row.addWidget(self.agent_command_execute_button)


        self.agent_command_review_panel_layout.addLayout(self.agent_command_action_row)


        self.agent_command_inspection_stack_layout.addWidget(self.agent_command_review_panel)

        self.agent_command_output_panel = QFrame(self.agent_commands_page_scroll_content)
        self.agent_command_output_panel.setObjectName(u"agent_command_output_panel")
        self.agent_command_output_panel_host_layout = QVBoxLayout(self.agent_command_output_panel)
        self.agent_command_output_panel_host_layout.setSpacing(0)
        self.agent_command_output_panel_host_layout.setObjectName(u"agent_command_output_panel_host_layout")
        self.agent_command_output_panel_host_layout.setContentsMargins(0, 0, 0, 0)
        self.agent_command_output_panel_layout = QVBoxLayout()
        self.agent_command_output_panel_layout.setSpacing(10)
        self.agent_command_output_panel_layout.setObjectName(u"agent_command_output_panel_layout")
        self.agent_command_output_panel_layout.setContentsMargins(15, 14, 15, 15)
        self.agent_command_output_panel_header = QLabel(self.agent_command_output_panel)
        self.agent_command_output_panel_header.setObjectName(u"agent_command_output_panel_header")

        self.agent_command_output_panel_layout.addWidget(self.agent_command_output_panel_header)

        self.agent_command_output_panel_caption = QLabel(self.agent_command_output_panel)
        self.agent_command_output_panel_caption.setObjectName(u"agent_command_output_panel_caption")
        self.agent_command_output_panel_caption.setWordWrap(True)

        self.agent_command_output_panel_layout.addWidget(self.agent_command_output_panel_caption)

        self.agent_command_result_summary = QLabel(self.agent_command_output_panel)
        self.agent_command_result_summary.setObjectName(u"agent_command_result_summary")

        self.agent_command_output_panel_layout.addWidget(self.agent_command_result_summary)

        self.agent_command_result_status_row = QHBoxLayout()
        self.agent_command_result_status_row.setSpacing(8)
        self.agent_command_result_status_row.setObjectName(u"agent_command_result_status_row")
        self.agent_command_result_status_row.setContentsMargins(0, 0, 0, 0)
        self.agent_command_result_status = QLabel(self.agent_command_output_panel)
        self.agent_command_result_status.setObjectName(u"agent_command_result_status")

        self.agent_command_result_status_row.addWidget(self.agent_command_result_status)

        self.agent_command_result_duration = QLabel(self.agent_command_output_panel)
        self.agent_command_result_duration.setObjectName(u"agent_command_result_duration")

        self.agent_command_result_status_row.addWidget(self.agent_command_result_duration)


        self.agent_command_output_panel_layout.addLayout(self.agent_command_result_status_row)

        self.agent_command_result_tabs = QTabWidget(self.agent_command_output_panel)
        self.agent_command_result_tabs.setObjectName(u"agent_command_result_tabs")
        self.agent_command_result_tabs.setMinimumSize(QSize(0, 210))
        self.agent_command_stdout_tab = QWidget()
        self.agent_command_stdout_tab.setObjectName(u"agent_command_stdout_tab")
        self.agent_command_stdout_tab_layout = QVBoxLayout(self.agent_command_stdout_tab)
        self.agent_command_stdout_tab_layout.setSpacing(0)
        self.agent_command_stdout_tab_layout.setObjectName(u"agent_command_stdout_tab_layout")
        self.agent_command_stdout_tab_layout.setContentsMargins(6, 6, 6, 6)
        self.agent_command_output_view = QPlainTextEdit(self.agent_command_stdout_tab)
        self.agent_command_output_view.setObjectName(u"agent_command_output_view")
        self.agent_command_output_view.setMinimumSize(QSize(0, 105))
        self.agent_command_output_view.setReadOnly(True)

        self.agent_command_stdout_tab_layout.addWidget(self.agent_command_output_view)

        self.agent_command_result_tabs.addTab(self.agent_command_stdout_tab, "")
        self.agent_command_stderr_tab = QWidget()
        self.agent_command_stderr_tab.setObjectName(u"agent_command_stderr_tab")
        self.agent_command_stderr_tab_layout = QVBoxLayout(self.agent_command_stderr_tab)
        self.agent_command_stderr_tab_layout.setSpacing(0)
        self.agent_command_stderr_tab_layout.setObjectName(u"agent_command_stderr_tab_layout")
        self.agent_command_stderr_tab_layout.setContentsMargins(6, 6, 6, 6)
        self.agent_command_stderr_view = QPlainTextEdit(self.agent_command_stderr_tab)
        self.agent_command_stderr_view.setObjectName(u"agent_command_stderr_view")
        self.agent_command_stderr_view.setMinimumSize(QSize(0, 150))
        self.agent_command_stderr_view.setFocusPolicy(Qt.ClickFocus)
        self.agent_command_stderr_view.setReadOnly(True)

        self.agent_command_stderr_tab_layout.addWidget(self.agent_command_stderr_view)

        self.agent_command_result_tabs.addTab(self.agent_command_stderr_tab, "")

        self.agent_command_output_panel_layout.addWidget(self.agent_command_result_tabs)

        self.agent_command_copy_output_button = QPushButton(self.agent_command_output_panel)
        self.agent_command_copy_output_button.setObjectName(u"agent_command_copy_output_button")
        self.agent_command_copy_output_button.setMinimumSize(QSize(0, 39))
        self.agent_command_copy_output_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.agent_command_output_panel_layout.addWidget(self.agent_command_copy_output_button)


        self.agent_command_output_panel_host_layout.addLayout(self.agent_command_output_panel_layout)


        self.agent_command_inspection_stack_layout.addWidget(self.agent_command_output_panel)


        self.agent_cmd_top_layout.addLayout(self.agent_command_inspection_stack_layout)

        self.agent_cmd_top_layout.setStretch(0, 6)
        self.agent_cmd_top_layout.setStretch(1, 5)

        self.agent_commands_page_layout.addLayout(self.agent_cmd_top_layout)

        self.agent_command_recent_section_label = QLabel(self.agent_commands_page_scroll_content)
        self.agent_command_recent_section_label.setObjectName(u"agent_command_recent_section_label")

        self.agent_commands_page_layout.addWidget(self.agent_command_recent_section_label)

        self.agent_command_history_panel = QFrame(self.agent_commands_page_scroll_content)
        self.agent_command_history_panel.setObjectName(u"agent_command_history_panel")
        self.agent_command_history_panel_host_layout = QVBoxLayout(self.agent_command_history_panel)
        self.agent_command_history_panel_host_layout.setSpacing(0)
        self.agent_command_history_panel_host_layout.setObjectName(u"agent_command_history_panel_host_layout")
        self.agent_command_history_panel_host_layout.setContentsMargins(0, 0, 0, 0)
        self.agent_command_history_panel_layout = QVBoxLayout()
        self.agent_command_history_panel_layout.setSpacing(10)
        self.agent_command_history_panel_layout.setObjectName(u"agent_command_history_panel_layout")
        self.agent_command_history_panel_layout.setContentsMargins(15, 14, 15, 15)
        self.agent_command_history_panel_header = QLabel(self.agent_command_history_panel)
        self.agent_command_history_panel_header.setObjectName(u"agent_command_history_panel_header")

        self.agent_command_history_panel_layout.addWidget(self.agent_command_history_panel_header)

        self.agent_cmd_history_toolbar_layout = QHBoxLayout()
        self.agent_cmd_history_toolbar_layout.setSpacing(8)
        self.agent_cmd_history_toolbar_layout.setObjectName(u"agent_cmd_history_toolbar_layout")
        self.agent_cmd_history_toolbar_layout.setContentsMargins(0, 0, 0, 0)
        self.agent_command_history_search = QLineEdit(self.agent_command_history_panel)
        self.agent_command_history_search.setObjectName(u"agent_command_history_search")
        self.agent_command_history_search.setClearButtonEnabled(True)

        self.agent_cmd_history_toolbar_layout.addWidget(self.agent_command_history_search)

        self.agent_command_status_filter_combo = QComboBox(self.agent_command_history_panel)
        self.agent_command_status_filter_combo.addItem("")
        self.agent_command_status_filter_combo.addItem("")
        self.agent_command_status_filter_combo.addItem("")
        self.agent_command_status_filter_combo.addItem("")
        self.agent_command_status_filter_combo.addItem("")
        self.agent_command_status_filter_combo.setObjectName(u"agent_command_status_filter_combo")
        self.agent_command_status_filter_combo.setMinimumSize(QSize(0, 43))

        self.agent_cmd_history_toolbar_layout.addWidget(self.agent_command_status_filter_combo)

        self.agent_command_history_refresh_button = QPushButton(self.agent_command_history_panel)
        self.agent_command_history_refresh_button.setObjectName(u"agent_command_history_refresh_button")
        self.agent_command_history_refresh_button.setMinimumSize(QSize(0, 39))
        self.agent_command_history_refresh_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.agent_cmd_history_toolbar_layout.addWidget(self.agent_command_history_refresh_button)

        self.agent_cmd_history_toolbar_layout.setStretch(0, 3)
        self.agent_cmd_history_toolbar_layout.setStretch(1, 1)

        self.agent_command_history_panel_layout.addLayout(self.agent_cmd_history_toolbar_layout)

        self.agent_command_history_table = QTableWidget(self.agent_command_history_panel)
        if (self.agent_command_history_table.columnCount() < 6):
            self.agent_command_history_table.setColumnCount(6)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.agent_command_history_table.setHorizontalHeaderItem(0, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.agent_command_history_table.setHorizontalHeaderItem(1, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.agent_command_history_table.setHorizontalHeaderItem(2, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.agent_command_history_table.setHorizontalHeaderItem(3, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.agent_command_history_table.setHorizontalHeaderItem(4, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.agent_command_history_table.setHorizontalHeaderItem(5, __qtablewidgetitem63)
        self.agent_command_history_table.setObjectName(u"agent_command_history_table")
        self.agent_command_history_table.setMinimumSize(QSize(0, 175))
        self.agent_command_history_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.agent_command_history_table.setAlternatingRowColors(True)
        self.agent_command_history_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.agent_command_history_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.agent_command_history_table.setShowGrid(False)
        self.agent_command_history_table.setWordWrap(False)
        self.agent_command_history_table.setRowCount(0)
        self.agent_command_history_table.setColumnCount(6)
        self.agent_command_history_table.horizontalHeader().setVisible(True)
        self.agent_command_history_table.horizontalHeader().setCascadingSectionResizes(False)
        self.agent_command_history_table.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.agent_command_history_table.horizontalHeader().setStretchLastSection(False)
        self.agent_command_history_table.verticalHeader().setCascadingSectionResizes(True)
        self.agent_command_history_table.verticalHeader().setProperty(u"showSortIndicator", False)
        self.agent_command_history_table.verticalHeader().setStretchLastSection(False)

        self.agent_command_history_panel_layout.addWidget(self.agent_command_history_table)


        self.agent_command_history_panel_host_layout.addLayout(self.agent_command_history_panel_layout)


        self.agent_commands_page_layout.addWidget(self.agent_command_history_panel)

        self.spacer_auto_6 = QSpacerItem(5, 2, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.agent_commands_page_layout.addItem(self.spacer_auto_6)

        self.agent_commands_page_scroll.setWidget(self.agent_commands_page_scroll_content)

        self.agent_commands_page_host_layout.addWidget(self.agent_commands_page_scroll)

        self.agent_detail_stacked_content.addWidget(self.agent_commands_page)

        self.agent_detail_content_layout.addWidget(self.agent_detail_stacked_content)


        self.agent_detail_page_layout.addWidget(self.agent_detail_content)

        self.content_stack.addWidget(self.agent_detail_page)
        self.fleet_commands_page = QWidget()
        self.fleet_commands_page.setObjectName(u"fleet_commands_page")
        self.fleet_commands_page_host_layout = QVBoxLayout(self.fleet_commands_page)
        self.fleet_commands_page_host_layout.setSpacing(0)
        self.fleet_commands_page_host_layout.setObjectName(u"fleet_commands_page_host_layout")
        self.fleet_commands_page_host_layout.setContentsMargins(0, 0, 0, 0)
        self.fleet_commands_page_scroll = QScrollArea(self.fleet_commands_page)
        self.fleet_commands_page_scroll.setObjectName(u"fleet_commands_page_scroll")
        self.fleet_commands_page_scroll.setFrameShape(QFrame.NoFrame)
        self.fleet_commands_page_scroll.setWidgetResizable(True)
        self.fleet_commands_page_scroll_content = QWidget()
        self.fleet_commands_page_scroll_content.setObjectName(u"fleet_commands_page_scroll_content")
        self.fleet_commands_page_scroll_content.setGeometry(QRect(0, -434, 1103, 1374))
        self.fleet_commands_page_layout = QVBoxLayout(self.fleet_commands_page_scroll_content)
        self.fleet_commands_page_layout.setSpacing(16)
        self.fleet_commands_page_layout.setObjectName(u"fleet_commands_page_layout")
        self.fleet_commands_page_layout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.fleet_commands_page_layout.setContentsMargins(15, 15, 15, 18)
        self.fleet_cmd_heading_row = QHBoxLayout()
        self.fleet_cmd_heading_row.setSpacing(12)
        self.fleet_cmd_heading_row.setObjectName(u"fleet_cmd_heading_row")
        self.fleet_cmd_heading_row.setContentsMargins(0, 0, 0, 0)
        self.fleet_cmd_heading_text = QVBoxLayout()
        self.fleet_cmd_heading_text.setSpacing(6)
        self.fleet_cmd_heading_text.setObjectName(u"fleet_cmd_heading_text")
        self.fleet_cmd_heading_text.setContentsMargins(0, 0, 0, 0)
        self.fleet_cmd_title = QLabel(self.fleet_commands_page_scroll_content)
        self.fleet_cmd_title.setObjectName(u"fleet_cmd_title")

        self.fleet_cmd_heading_text.addWidget(self.fleet_cmd_title)

        self.fleet_cmd_subtitle = QLabel(self.fleet_commands_page_scroll_content)
        self.fleet_cmd_subtitle.setObjectName(u"fleet_cmd_subtitle")
        self.fleet_cmd_subtitle.setWordWrap(True)

        self.fleet_cmd_heading_text.addWidget(self.fleet_cmd_subtitle)


        self.fleet_cmd_heading_row.addLayout(self.fleet_cmd_heading_text)

        self.spacer_auto_1 = QSpacerItem(5, 2, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.fleet_cmd_heading_row.addItem(self.spacer_auto_1)

        self.fleet_command_workspace_status = QLabel(self.fleet_commands_page_scroll_content)
        self.fleet_command_workspace_status.setObjectName(u"fleet_command_workspace_status")

        self.fleet_cmd_heading_row.addWidget(self.fleet_command_workspace_status)

        self.fleet_cmd_refresh_button = QPushButton(self.fleet_commands_page_scroll_content)
        self.fleet_cmd_refresh_button.setObjectName(u"fleet_cmd_refresh_button")
        self.fleet_cmd_refresh_button.setMinimumSize(QSize(0, 39))
        self.fleet_cmd_refresh_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.fleet_cmd_heading_row.addWidget(self.fleet_cmd_refresh_button)

        self.fleet_cmd_heading_row.setStretch(0, 4)
        self.fleet_cmd_heading_row.setStretch(1, 1)

        self.fleet_commands_page_layout.addLayout(self.fleet_cmd_heading_row)

        self.line_7 = QFrame(self.fleet_commands_page_scroll_content)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.fleet_commands_page_layout.addWidget(self.line_7)

        self.fleet_command_process_strip = QFrame(self.fleet_commands_page_scroll_content)
        self.fleet_command_process_strip.setObjectName(u"fleet_command_process_strip")
        self.fleet_command_process_strip_layout = QVBoxLayout(self.fleet_command_process_strip)
        self.fleet_command_process_strip_layout.setSpacing(0)
        self.fleet_command_process_strip_layout.setObjectName(u"fleet_command_process_strip_layout")
        self.fleet_command_process_strip_layout.setContentsMargins(10, 10, 10, 10)
        self.fleet_command_process_steps = QLabel(self.fleet_command_process_strip)
        self.fleet_command_process_steps.setObjectName(u"fleet_command_process_steps")

        self.fleet_command_process_strip_layout.addWidget(self.fleet_command_process_steps)


        self.fleet_commands_page_layout.addWidget(self.fleet_command_process_strip)

        self.fleet_cmd_upper_layout = QHBoxLayout()
        self.fleet_cmd_upper_layout.setSpacing(6)
        self.fleet_cmd_upper_layout.setObjectName(u"fleet_cmd_upper_layout")
        self.fleet_cmd_upper_layout.setContentsMargins(0, 0, 0, 0)
        self.fleet_command_library_panel = QFrame(self.fleet_commands_page_scroll_content)
        self.fleet_command_library_panel.setObjectName(u"fleet_command_library_panel")
        self.fleet_command_library_panel.setMinimumSize(QSize(230, 0))
        self.fleet_command_library_panel.setMaximumSize(QSize(340, 16777215))
        self.fleet_command_library_panel_host_layout = QVBoxLayout(self.fleet_command_library_panel)
        self.fleet_command_library_panel_host_layout.setSpacing(0)
        self.fleet_command_library_panel_host_layout.setObjectName(u"fleet_command_library_panel_host_layout")
        self.fleet_command_library_panel_host_layout.setContentsMargins(0, 0, 0, 0)
        self.fleet_command_library_panel_layout = QVBoxLayout()
        self.fleet_command_library_panel_layout.setSpacing(11)
        self.fleet_command_library_panel_layout.setObjectName(u"fleet_command_library_panel_layout")
        self.fleet_command_library_panel_layout.setContentsMargins(6, 15, 6, 15)
        self.fleet_command_library_panel_header = QLabel(self.fleet_command_library_panel)
        self.fleet_command_library_panel_header.setObjectName(u"fleet_command_library_panel_header")

        self.fleet_command_library_panel_layout.addWidget(self.fleet_command_library_panel_header)

        self.fleet_command_library_panel_caption = QLabel(self.fleet_command_library_panel)
        self.fleet_command_library_panel_caption.setObjectName(u"fleet_command_library_panel_caption")
        self.fleet_command_library_panel_caption.setWordWrap(True)

        self.fleet_command_library_panel_layout.addWidget(self.fleet_command_library_panel_caption)

        self.fleet_command_search = QLineEdit(self.fleet_command_library_panel)
        self.fleet_command_search.setObjectName(u"fleet_command_search")
        self.fleet_command_search.setMinimumSize(QSize(0, 43))

        self.fleet_command_library_panel_layout.addWidget(self.fleet_command_search)

        self.fleet_command_category = QComboBox(self.fleet_command_library_panel)
        self.fleet_command_category.addItem("")
        self.fleet_command_category.setObjectName(u"fleet_command_category")
        self.fleet_command_category.setMinimumSize(QSize(0, 43))

        self.fleet_command_library_panel_layout.addWidget(self.fleet_command_category)

        self.fleet_command_catalog_table = QTableWidget(self.fleet_command_library_panel)
        if (self.fleet_command_catalog_table.columnCount() < 3):
            self.fleet_command_catalog_table.setColumnCount(3)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.fleet_command_catalog_table.setHorizontalHeaderItem(0, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.fleet_command_catalog_table.setHorizontalHeaderItem(1, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.fleet_command_catalog_table.setHorizontalHeaderItem(2, __qtablewidgetitem66)
        self.fleet_command_catalog_table.setObjectName(u"fleet_command_catalog_table")
        self.fleet_command_catalog_table.setMinimumSize(QSize(0, 0))
        self.fleet_command_catalog_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.fleet_command_catalog_table.setAlternatingRowColors(True)
        self.fleet_command_catalog_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.fleet_command_catalog_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.fleet_command_catalog_table.setShowGrid(False)
        self.fleet_command_catalog_table.setWordWrap(False)
        self.fleet_command_catalog_table.setRowCount(0)
        self.fleet_command_catalog_table.setColumnCount(3)

        self.fleet_command_library_panel_layout.addWidget(self.fleet_command_catalog_table)

        self.fleet_command_library_help = QLabel(self.fleet_command_library_panel)
        self.fleet_command_library_help.setObjectName(u"fleet_command_library_help")
        self.fleet_command_library_help.setWordWrap(True)

        self.fleet_command_library_panel_layout.addWidget(self.fleet_command_library_help)


        self.fleet_command_library_panel_host_layout.addLayout(self.fleet_command_library_panel_layout)


        self.fleet_cmd_upper_layout.addWidget(self.fleet_command_library_panel)

        self.fleet_command_execution_panel = QFrame(self.fleet_commands_page_scroll_content)
        self.fleet_command_execution_panel.setObjectName(u"fleet_command_execution_panel")
        self.fleet_command_execution_panel.setMinimumSize(QSize(355, 0))
        self.fleet_command_execution_panel_host_layout = QVBoxLayout(self.fleet_command_execution_panel)
        self.fleet_command_execution_panel_host_layout.setSpacing(0)
        self.fleet_command_execution_panel_host_layout.setObjectName(u"fleet_command_execution_panel_host_layout")
        self.fleet_command_execution_panel_host_layout.setContentsMargins(0, 0, 0, 0)
        self.fleet_command_execution_panel_layout = QVBoxLayout()
        self.fleet_command_execution_panel_layout.setSpacing(12)
        self.fleet_command_execution_panel_layout.setObjectName(u"fleet_command_execution_panel_layout")
        self.fleet_command_execution_panel_layout.setContentsMargins(16, 15, 16, 16)
        self.fleet_command_execution_panel_header = QLabel(self.fleet_command_execution_panel)
        self.fleet_command_execution_panel_header.setObjectName(u"fleet_command_execution_panel_header")

        self.fleet_command_execution_panel_layout.addWidget(self.fleet_command_execution_panel_header)

        self.fleet_command_execution_panel_caption = QLabel(self.fleet_command_execution_panel)
        self.fleet_command_execution_panel_caption.setObjectName(u"fleet_command_execution_panel_caption")

        self.fleet_command_execution_panel_layout.addWidget(self.fleet_command_execution_panel_caption)

        self.fleet_command_target_label = QLabel(self.fleet_command_execution_panel)
        self.fleet_command_target_label.setObjectName(u"fleet_command_target_label")

        self.fleet_command_execution_panel_layout.addWidget(self.fleet_command_target_label)

        self.fleet_command_target_combo = QComboBox(self.fleet_command_execution_panel)
        self.fleet_command_target_combo.setObjectName(u"fleet_command_target_combo")
        self.fleet_command_target_combo.setMinimumSize(QSize(0, 43))

        self.fleet_command_execution_panel_layout.addWidget(self.fleet_command_target_combo)

        self.fleet_command_category_label = QLabel(self.fleet_command_execution_panel)
        self.fleet_command_category_label.setObjectName(u"fleet_command_category_label")

        self.fleet_command_execution_panel_layout.addWidget(self.fleet_command_category_label)

        self.fleet_command_category_combo = QComboBox(self.fleet_command_execution_panel)
        self.fleet_command_category_combo.setObjectName(u"fleet_command_category_combo")
        self.fleet_command_category_combo.setMinimumSize(QSize(0, 43))

        self.fleet_command_execution_panel_layout.addWidget(self.fleet_command_category_combo)

        self.fleet_command_selected_label = QLabel(self.fleet_command_execution_panel)
        self.fleet_command_selected_label.setObjectName(u"fleet_command_selected_label")

        self.fleet_command_execution_panel_layout.addWidget(self.fleet_command_selected_label)

        self.fleet_command_type_combo = QComboBox(self.fleet_command_execution_panel)
        self.fleet_command_type_combo.setObjectName(u"fleet_command_type_combo")
        self.fleet_command_type_combo.setMinimumSize(QSize(0, 43))

        self.fleet_command_execution_panel_layout.addWidget(self.fleet_command_type_combo)

        self.fleet_command_identity_card = QFrame(self.fleet_command_execution_panel)
        self.fleet_command_identity_card.setObjectName(u"fleet_command_identity_card")
        self.fleet_command_identity_card_layout = QVBoxLayout(self.fleet_command_identity_card)
        self.fleet_command_identity_card_layout.setSpacing(7)
        self.fleet_command_identity_card_layout.setObjectName(u"fleet_command_identity_card_layout")
        self.fleet_command_identity_card_layout.setContentsMargins(12, 12, 12, 12)
        self.fleet_command_risk_row = QHBoxLayout()
        self.fleet_command_risk_row.setSpacing(8)
        self.fleet_command_risk_row.setObjectName(u"fleet_command_risk_row")
        self.fleet_command_risk_row.setContentsMargins(0, 0, 0, 0)
        self.fleet_command_display_title = QLabel(self.fleet_command_identity_card)
        self.fleet_command_display_title.setObjectName(u"fleet_command_display_title")

        self.fleet_command_risk_row.addWidget(self.fleet_command_display_title)

        self.spacer_auto_2 = QSpacerItem(18, 1, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.fleet_command_risk_row.addItem(self.spacer_auto_2)

        self.fleet_command_risk_badge = QLabel(self.fleet_command_identity_card)
        self.fleet_command_risk_badge.setObjectName(u"fleet_command_risk_badge")

        self.fleet_command_risk_row.addWidget(self.fleet_command_risk_badge)


        self.fleet_command_identity_card_layout.addLayout(self.fleet_command_risk_row)

        self.fleet_command_command_key = QLabel(self.fleet_command_identity_card)
        self.fleet_command_command_key.setObjectName(u"fleet_command_command_key")

        self.fleet_command_identity_card_layout.addWidget(self.fleet_command_command_key)

        self.fleet_command_description = QLabel(self.fleet_command_identity_card)
        self.fleet_command_description.setObjectName(u"fleet_command_description")
        self.fleet_command_description.setWordWrap(True)

        self.fleet_command_identity_card_layout.addWidget(self.fleet_command_description)


        self.fleet_command_execution_panel_layout.addWidget(self.fleet_command_identity_card)

        self.fleet_command_parameters_heading = QHBoxLayout()
        self.fleet_command_parameters_heading.setSpacing(8)
        self.fleet_command_parameters_heading.setObjectName(u"fleet_command_parameters_heading")
        self.fleet_command_parameters_heading.setContentsMargins(0, 0, 0, 0)
        self.fleet_command_fields_label = QLabel(self.fleet_command_execution_panel)
        self.fleet_command_fields_label.setObjectName(u"fleet_command_fields_label")

        self.fleet_command_parameters_heading.addWidget(self.fleet_command_fields_label)

        self.fleet_command_fields_count = QLabel(self.fleet_command_execution_panel)
        self.fleet_command_fields_count.setObjectName(u"fleet_command_fields_count")

        self.fleet_command_parameters_heading.addWidget(self.fleet_command_fields_count)

        self.fleet_command_parameters_heading.setStretch(0, 4)
        self.fleet_command_parameters_heading.setStretch(1, 2)

        self.fleet_command_execution_panel_layout.addLayout(self.fleet_command_parameters_heading)

        self.fleet_command_fields_container = QFrame(self.fleet_command_execution_panel)
        self.fleet_command_fields_container.setObjectName(u"fleet_command_fields_container")
        sizePolicy2.setHeightForWidth(self.fleet_command_fields_container.sizePolicy().hasHeightForWidth())
        self.fleet_command_fields_container.setSizePolicy(sizePolicy2)
        self.fleet_command_fields_container.setMinimumSize(QSize(0, 64))
        self.fleet_command_fields_container.setFrameShape(QFrame.NoFrame)
        self.fleet_command_fields_layout = QVBoxLayout(self.fleet_command_fields_container)
        self.fleet_command_fields_layout.setSpacing(9)
        self.fleet_command_fields_layout.setObjectName(u"fleet_command_fields_layout")
        self.fleet_command_fields_layout.setContentsMargins(12, 12, 12, 12)

        self.fleet_command_execution_panel_layout.addWidget(self.fleet_command_fields_container)

        self.fleet_command_payload_label = QLabel(self.fleet_command_execution_panel)
        self.fleet_command_payload_label.setObjectName(u"fleet_command_payload_label")

        self.fleet_command_execution_panel_layout.addWidget(self.fleet_command_payload_label)

        self.fleet_command_raw_mode_checkbox = QCheckBox(self.fleet_command_execution_panel)
        self.fleet_command_raw_mode_checkbox.setObjectName(u"fleet_command_raw_mode_checkbox")

        self.fleet_command_execution_panel_layout.addWidget(self.fleet_command_raw_mode_checkbox)

        self.fleet_command_payload_editor = QPlainTextEdit(self.fleet_command_execution_panel)
        self.fleet_command_payload_editor.setObjectName(u"fleet_command_payload_editor")
        self.fleet_command_payload_editor.setMinimumSize(QSize(0, 96))
        self.fleet_command_payload_editor.setMaximumSize(QSize(16777215, 138))
        self.fleet_command_payload_editor.setReadOnly(True)

        self.fleet_command_execution_panel_layout.addWidget(self.fleet_command_payload_editor)


        self.fleet_command_execution_panel_host_layout.addLayout(self.fleet_command_execution_panel_layout)


        self.fleet_cmd_upper_layout.addWidget(self.fleet_command_execution_panel)

        self.fleet_command_review_panel = QFrame(self.fleet_commands_page_scroll_content)
        self.fleet_command_review_panel.setObjectName(u"fleet_command_review_panel")
        self.fleet_command_review_panel.setMinimumSize(QSize(268, 0))
        self.fleet_command_review_panel_layout = QVBoxLayout(self.fleet_command_review_panel)
        self.fleet_command_review_panel_layout.setSpacing(12)
        self.fleet_command_review_panel_layout.setObjectName(u"fleet_command_review_panel_layout")
        self.fleet_command_review_panel_layout.setContentsMargins(16, 15, 16, 16)
        self.fleet_command_review_header = QLabel(self.fleet_command_review_panel)
        self.fleet_command_review_header.setObjectName(u"fleet_command_review_header")

        self.fleet_command_review_panel_layout.addWidget(self.fleet_command_review_header)

        self.fleet_command_review_caption = QLabel(self.fleet_command_review_panel)
        self.fleet_command_review_caption.setObjectName(u"fleet_command_review_caption")
        self.fleet_command_review_caption.setWordWrap(True)

        self.fleet_command_review_panel_layout.addWidget(self.fleet_command_review_caption)

        self.fleet_command_review_target = QLabel(self.fleet_command_review_panel)
        self.fleet_command_review_target.setObjectName(u"fleet_command_review_target")

        self.fleet_command_review_panel_layout.addWidget(self.fleet_command_review_target)

        self.fleet_command_review_operation = QLabel(self.fleet_command_review_panel)
        self.fleet_command_review_operation.setObjectName(u"fleet_command_review_operation")

        self.fleet_command_review_panel_layout.addWidget(self.fleet_command_review_operation)

        self.fleet_command_review_payload_label = QLabel(self.fleet_command_review_panel)
        self.fleet_command_review_payload_label.setObjectName(u"fleet_command_review_payload_label")

        self.fleet_command_review_panel_layout.addWidget(self.fleet_command_review_payload_label)

        self.fleet_command_request_preview = QPlainTextEdit(self.fleet_command_review_panel)
        self.fleet_command_request_preview.setObjectName(u"fleet_command_request_preview")
        self.fleet_command_request_preview.setMinimumSize(QSize(0, 155))
        self.fleet_command_request_preview.setReadOnly(True)

        self.fleet_command_review_panel_layout.addWidget(self.fleet_command_request_preview)

        self.fleet_command_validation_status = QLabel(self.fleet_command_review_panel)
        self.fleet_command_validation_status.setObjectName(u"fleet_command_validation_status")
        self.fleet_command_validation_status.setWordWrap(True)

        self.fleet_command_review_panel_layout.addWidget(self.fleet_command_validation_status)

        self.fleet_command_risk_confirmation_checkbox = QCheckBox(self.fleet_command_review_panel)
        self.fleet_command_risk_confirmation_checkbox.setObjectName(u"fleet_command_risk_confirmation_checkbox")
        self.fleet_command_risk_confirmation_checkbox.setVisible(False)

        self.fleet_command_review_panel_layout.addWidget(self.fleet_command_risk_confirmation_checkbox)

        self.fleet_cmd_action_layout = QHBoxLayout()
        self.fleet_cmd_action_layout.setSpacing(8)
        self.fleet_cmd_action_layout.setObjectName(u"fleet_cmd_action_layout")
        self.fleet_cmd_action_layout.setContentsMargins(0, 0, 0, 0)
        self.fleet_command_validate_button = QPushButton(self.fleet_command_review_panel)
        self.fleet_command_validate_button.setObjectName(u"fleet_command_validate_button")
        self.fleet_command_validate_button.setMinimumSize(QSize(0, 39))
        self.fleet_command_validate_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.fleet_cmd_action_layout.addWidget(self.fleet_command_validate_button)

        self.fleet_command_execute_button = QPushButton(self.fleet_command_review_panel)
        self.fleet_command_execute_button.setObjectName(u"fleet_command_execute_button")
        self.fleet_command_execute_button.setMinimumSize(QSize(0, 39))
        self.fleet_command_execute_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.fleet_cmd_action_layout.addWidget(self.fleet_command_execute_button)


        self.fleet_command_review_panel_layout.addLayout(self.fleet_cmd_action_layout)


        self.fleet_cmd_upper_layout.addWidget(self.fleet_command_review_panel)

        self.fleet_cmd_upper_layout.setStretch(0, 3)
        self.fleet_cmd_upper_layout.setStretch(1, 5)
        self.fleet_cmd_upper_layout.setStretch(2, 4)

        self.fleet_commands_page_layout.addLayout(self.fleet_cmd_upper_layout)

        self.fleet_command_recent_section_label = QLabel(self.fleet_commands_page_scroll_content)
        self.fleet_command_recent_section_label.setObjectName(u"fleet_command_recent_section_label")

        self.fleet_commands_page_layout.addWidget(self.fleet_command_recent_section_label)

        self.fleet_cmd_bottom_layout = QHBoxLayout()
        self.fleet_cmd_bottom_layout.setSpacing(12)
        self.fleet_cmd_bottom_layout.setObjectName(u"fleet_cmd_bottom_layout")
        self.fleet_cmd_bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.fleet_command_history_panel = QFrame(self.fleet_commands_page_scroll_content)
        self.fleet_command_history_panel.setObjectName(u"fleet_command_history_panel")
        self.fleet_command_history_panel.setMaximumSize(QSize(620, 16777215))
        self.fleet_command_history_panel_host_layout = QVBoxLayout(self.fleet_command_history_panel)
        self.fleet_command_history_panel_host_layout.setSpacing(0)
        self.fleet_command_history_panel_host_layout.setObjectName(u"fleet_command_history_panel_host_layout")
        self.fleet_command_history_panel_host_layout.setContentsMargins(0, 0, 0, 0)
        self.fleet_command_history_panel_layout = QVBoxLayout()
        self.fleet_command_history_panel_layout.setSpacing(10)
        self.fleet_command_history_panel_layout.setObjectName(u"fleet_command_history_panel_layout")
        self.fleet_command_history_panel_layout.setContentsMargins(15, 14, 15, 15)
        self.fleet_command_history_panel_header = QLabel(self.fleet_command_history_panel)
        self.fleet_command_history_panel_header.setObjectName(u"fleet_command_history_panel_header")

        self.fleet_command_history_panel_layout.addWidget(self.fleet_command_history_panel_header)

        self.fleet_command_history_panel_caption = QLabel(self.fleet_command_history_panel)
        self.fleet_command_history_panel_caption.setObjectName(u"fleet_command_history_panel_caption")
        self.fleet_command_history_panel_caption.setWordWrap(True)

        self.fleet_command_history_panel_layout.addWidget(self.fleet_command_history_panel_caption)

        self.fleet_cmd_hist_toolbar_layout = QHBoxLayout()
        self.fleet_cmd_hist_toolbar_layout.setSpacing(8)
        self.fleet_cmd_hist_toolbar_layout.setObjectName(u"fleet_cmd_hist_toolbar_layout")
        self.fleet_cmd_hist_toolbar_layout.setContentsMargins(0, 0, 0, 0)
        self.fleet_command_history_search = QLineEdit(self.fleet_command_history_panel)
        self.fleet_command_history_search.setObjectName(u"fleet_command_history_search")
        self.fleet_command_history_search.setClearButtonEnabled(True)

        self.fleet_cmd_hist_toolbar_layout.addWidget(self.fleet_command_history_search)

        self.fleet_command_history_status_combo = QComboBox(self.fleet_command_history_panel)
        self.fleet_command_history_status_combo.addItem("")
        self.fleet_command_history_status_combo.addItem("")
        self.fleet_command_history_status_combo.addItem("")
        self.fleet_command_history_status_combo.addItem("")
        self.fleet_command_history_status_combo.addItem("")
        self.fleet_command_history_status_combo.addItem("")
        self.fleet_command_history_status_combo.setObjectName(u"fleet_command_history_status_combo")
        self.fleet_command_history_status_combo.setMinimumSize(QSize(0, 43))

        self.fleet_cmd_hist_toolbar_layout.addWidget(self.fleet_command_history_status_combo)

        self.fleet_command_history_refresh_button = QPushButton(self.fleet_command_history_panel)
        self.fleet_command_history_refresh_button.setObjectName(u"fleet_command_history_refresh_button")
        self.fleet_command_history_refresh_button.setMinimumSize(QSize(0, 39))
        self.fleet_command_history_refresh_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.fleet_cmd_hist_toolbar_layout.addWidget(self.fleet_command_history_refresh_button)

        self.fleet_cmd_hist_toolbar_layout.setStretch(0, 3)
        self.fleet_cmd_hist_toolbar_layout.setStretch(1, 1)

        self.fleet_command_history_panel_layout.addLayout(self.fleet_cmd_hist_toolbar_layout)

        self.fleet_command_history_table = QTableWidget(self.fleet_command_history_panel)
        if (self.fleet_command_history_table.columnCount() < 6):
            self.fleet_command_history_table.setColumnCount(6)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.fleet_command_history_table.setHorizontalHeaderItem(0, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.fleet_command_history_table.setHorizontalHeaderItem(1, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.fleet_command_history_table.setHorizontalHeaderItem(2, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.fleet_command_history_table.setHorizontalHeaderItem(3, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.fleet_command_history_table.setHorizontalHeaderItem(4, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.fleet_command_history_table.setHorizontalHeaderItem(5, __qtablewidgetitem72)
        self.fleet_command_history_table.setObjectName(u"fleet_command_history_table")
        self.fleet_command_history_table.setMinimumSize(QSize(0, 175))
        self.fleet_command_history_table.setMaximumSize(QSize(650, 16777215))
        self.fleet_command_history_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.fleet_command_history_table.setAlternatingRowColors(True)
        self.fleet_command_history_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.fleet_command_history_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.fleet_command_history_table.setShowGrid(False)
        self.fleet_command_history_table.setWordWrap(False)
        self.fleet_command_history_table.setRowCount(0)
        self.fleet_command_history_table.setColumnCount(6)

        self.fleet_command_history_panel_layout.addWidget(self.fleet_command_history_table)


        self.fleet_command_history_panel_host_layout.addLayout(self.fleet_command_history_panel_layout)


        self.fleet_cmd_bottom_layout.addWidget(self.fleet_command_history_panel)

        self.fleet_command_result_panel = QFrame(self.fleet_commands_page_scroll_content)
        self.fleet_command_result_panel.setObjectName(u"fleet_command_result_panel")
        self.fleet_command_result_panel.setMinimumSize(QSize(320, 0))
        self.fleet_command_result_panel_host_layout = QVBoxLayout(self.fleet_command_result_panel)
        self.fleet_command_result_panel_host_layout.setSpacing(0)
        self.fleet_command_result_panel_host_layout.setObjectName(u"fleet_command_result_panel_host_layout")
        self.fleet_command_result_panel_host_layout.setContentsMargins(0, 0, 0, 0)
        self.fleet_command_result_panel_layout = QVBoxLayout()
        self.fleet_command_result_panel_layout.setSpacing(10)
        self.fleet_command_result_panel_layout.setObjectName(u"fleet_command_result_panel_layout")
        self.fleet_command_result_panel_layout.setContentsMargins(15, 14, 15, 15)
        self.fleet_command_result_panel_header = QLabel(self.fleet_command_result_panel)
        self.fleet_command_result_panel_header.setObjectName(u"fleet_command_result_panel_header")

        self.fleet_command_result_panel_layout.addWidget(self.fleet_command_result_panel_header)

        self.fleet_command_result_panel_caption = QLabel(self.fleet_command_result_panel)
        self.fleet_command_result_panel_caption.setObjectName(u"fleet_command_result_panel_caption")
        self.fleet_command_result_panel_caption.setWordWrap(True)

        self.fleet_command_result_panel_layout.addWidget(self.fleet_command_result_panel_caption)

        self.fleet_command_result_metadata = QLabel(self.fleet_command_result_panel)
        self.fleet_command_result_metadata.setObjectName(u"fleet_command_result_metadata")

        self.fleet_command_result_panel_layout.addWidget(self.fleet_command_result_metadata)

        self.fleet_command_result_status_row = QHBoxLayout()
        self.fleet_command_result_status_row.setSpacing(8)
        self.fleet_command_result_status_row.setObjectName(u"fleet_command_result_status_row")
        self.fleet_command_result_status_row.setContentsMargins(0, 0, 0, 0)
        self.fleet_command_result_status = QLabel(self.fleet_command_result_panel)
        self.fleet_command_result_status.setObjectName(u"fleet_command_result_status")

        self.fleet_command_result_status_row.addWidget(self.fleet_command_result_status)

        self.fleet_command_result_duration = QLabel(self.fleet_command_result_panel)
        self.fleet_command_result_duration.setObjectName(u"fleet_command_result_duration")

        self.fleet_command_result_status_row.addWidget(self.fleet_command_result_duration)


        self.fleet_command_result_panel_layout.addLayout(self.fleet_command_result_status_row)

        self.fleet_command_result_tabs = QTabWidget(self.fleet_command_result_panel)
        self.fleet_command_result_tabs.setObjectName(u"fleet_command_result_tabs")
        self.fleet_command_result_tabs.setMinimumSize(QSize(0, 210))
        self.fleet_command_stdout_tab = QWidget()
        self.fleet_command_stdout_tab.setObjectName(u"fleet_command_stdout_tab")
        self.fleet_command_stdout_tab_layout = QVBoxLayout(self.fleet_command_stdout_tab)
        self.fleet_command_stdout_tab_layout.setSpacing(0)
        self.fleet_command_stdout_tab_layout.setObjectName(u"fleet_command_stdout_tab_layout")
        self.fleet_command_stdout_tab_layout.setContentsMargins(6, 6, 6, 6)
        self.fleet_command_output_view = QPlainTextEdit(self.fleet_command_stdout_tab)
        self.fleet_command_output_view.setObjectName(u"fleet_command_output_view")
        self.fleet_command_output_view.setMinimumSize(QSize(0, 105))
        self.fleet_command_output_view.setReadOnly(True)

        self.fleet_command_stdout_tab_layout.addWidget(self.fleet_command_output_view)

        self.fleet_command_result_tabs.addTab(self.fleet_command_stdout_tab, "")
        self.fleet_command_stderr_tab = QWidget()
        self.fleet_command_stderr_tab.setObjectName(u"fleet_command_stderr_tab")
        self.fleet_command_stderr_tab_layout = QVBoxLayout(self.fleet_command_stderr_tab)
        self.fleet_command_stderr_tab_layout.setSpacing(0)
        self.fleet_command_stderr_tab_layout.setObjectName(u"fleet_command_stderr_tab_layout")
        self.fleet_command_stderr_tab_layout.setContentsMargins(6, 6, 6, 6)
        self.fleet_command_stderr_view = QPlainTextEdit(self.fleet_command_stderr_tab)
        self.fleet_command_stderr_view.setObjectName(u"fleet_command_stderr_view")
        self.fleet_command_stderr_view.setMinimumSize(QSize(0, 150))
        self.fleet_command_stderr_view.setReadOnly(True)

        self.fleet_command_stderr_tab_layout.addWidget(self.fleet_command_stderr_view)

        self.fleet_command_result_tabs.addTab(self.fleet_command_stderr_tab, "")

        self.fleet_command_result_panel_layout.addWidget(self.fleet_command_result_tabs)

        self.fleet_command_copy_output_button = QPushButton(self.fleet_command_result_panel)
        self.fleet_command_copy_output_button.setObjectName(u"fleet_command_copy_output_button")
        self.fleet_command_copy_output_button.setMinimumSize(QSize(0, 39))
        self.fleet_command_copy_output_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.fleet_command_result_panel_layout.addWidget(self.fleet_command_copy_output_button)


        self.fleet_command_result_panel_host_layout.addLayout(self.fleet_command_result_panel_layout)


        self.fleet_cmd_bottom_layout.addWidget(self.fleet_command_result_panel)

        self.fleet_cmd_bottom_layout.setStretch(0, 7)
        self.fleet_cmd_bottom_layout.setStretch(1, 5)

        self.fleet_commands_page_layout.addLayout(self.fleet_cmd_bottom_layout)

        self.spacer_auto_3 = QSpacerItem(5, 2, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.fleet_commands_page_layout.addItem(self.spacer_auto_3)

        self.fleet_commands_page_scroll.setWidget(self.fleet_commands_page_scroll_content)

        self.fleet_commands_page_host_layout.addWidget(self.fleet_commands_page_scroll)

        self.content_stack.addWidget(self.fleet_commands_page)
        self.fleet_logs_page = QWidget()
        self.fleet_logs_page.setObjectName(u"fleet_logs_page")
        self.fleet_logs_page_host_layout = QVBoxLayout(self.fleet_logs_page)
        self.fleet_logs_page_host_layout.setSpacing(0)
        self.fleet_logs_page_host_layout.setObjectName(u"fleet_logs_page_host_layout")
        self.fleet_logs_page_host_layout.setContentsMargins(0, 0, 0, 0)
        self.fleet_logs_page_scroll = QScrollArea(self.fleet_logs_page)
        self.fleet_logs_page_scroll.setObjectName(u"fleet_logs_page_scroll")
        self.fleet_logs_page_scroll.setFrameShape(QFrame.NoFrame)
        self.fleet_logs_page_scroll.setWidgetResizable(True)
        self.fleet_logs_page_scroll_content = QWidget()
        self.fleet_logs_page_scroll_content.setObjectName(u"fleet_logs_page_scroll_content")
        self.fleet_logs_page_scroll_content.setGeometry(QRect(0, 0, 387, 828))
        self.fleet_logs_page_layout = QVBoxLayout(self.fleet_logs_page_scroll_content)
        self.fleet_logs_page_layout.setSpacing(10)
        self.fleet_logs_page_layout.setObjectName(u"fleet_logs_page_layout")
        self.fleet_logs_page_layout.setContentsMargins(6, 6, 6, 0)
        self.fleet_logs_heading_row = QHBoxLayout()
        self.fleet_logs_heading_row.setSpacing(12)
        self.fleet_logs_heading_row.setObjectName(u"fleet_logs_heading_row")
        self.fleet_logs_heading_row.setContentsMargins(0, 0, 6, 0)
        self.fleet_logs_heading_text = QVBoxLayout()
        self.fleet_logs_heading_text.setSpacing(4)
        self.fleet_logs_heading_text.setObjectName(u"fleet_logs_heading_text")
        self.fleet_logs_heading_text.setContentsMargins(0, 0, 0, 0)
        self.fleet_logs_title = QLabel(self.fleet_logs_page_scroll_content)
        self.fleet_logs_title.setObjectName(u"fleet_logs_title")

        self.fleet_logs_heading_text.addWidget(self.fleet_logs_title)

        self.fleet_logs_subtitle = QLabel(self.fleet_logs_page_scroll_content)
        self.fleet_logs_subtitle.setObjectName(u"fleet_logs_subtitle")
        self.fleet_logs_subtitle.setWordWrap(True)

        self.fleet_logs_heading_text.addWidget(self.fleet_logs_subtitle)


        self.fleet_logs_heading_row.addLayout(self.fleet_logs_heading_text)

        self.fleet_logs_heading_spacer = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.fleet_logs_heading_row.addItem(self.fleet_logs_heading_spacer)

        self.fleet_logs_refresh_button = QPushButton(self.fleet_logs_page_scroll_content)
        self.fleet_logs_refresh_button.setObjectName(u"fleet_logs_refresh_button")
        self.fleet_logs_refresh_button.setMinimumSize(QSize(0, 0))
        self.fleet_logs_refresh_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.fleet_logs_heading_row.addWidget(self.fleet_logs_refresh_button)

        self.fleet_logs_export_button = QPushButton(self.fleet_logs_page_scroll_content)
        self.fleet_logs_export_button.setObjectName(u"fleet_logs_export_button")
        self.fleet_logs_export_button.setMinimumSize(QSize(0, 0))
        self.fleet_logs_export_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.fleet_logs_heading_row.addWidget(self.fleet_logs_export_button)


        self.fleet_logs_page_layout.addLayout(self.fleet_logs_heading_row)

        self.line_11 = QFrame(self.fleet_logs_page_scroll_content)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.fleet_logs_page_layout.addWidget(self.line_11)

        self.fleet_logs_filters_panel = QFrame(self.fleet_logs_page_scroll_content)
        self.fleet_logs_filters_panel.setObjectName(u"fleet_logs_filters_panel")
        self.fleet_logs_filters_panel_host_layout = QVBoxLayout(self.fleet_logs_filters_panel)
        self.fleet_logs_filters_panel_host_layout.setObjectName(u"fleet_logs_filters_panel_host_layout")
        self.fleet_logs_filters_panel_host_layout.setContentsMargins(0, 0, 0, 0)
        self.fleet_logs_filters_panel_layout = QVBoxLayout()
        self.fleet_logs_filters_panel_layout.setSpacing(12)
        self.fleet_logs_filters_panel_layout.setObjectName(u"fleet_logs_filters_panel_layout")
        self.fleet_logs_filters_panel_layout.setContentsMargins(6, 6, 6, 6)
        self.fleet_logs_filters_panel_header = QLabel(self.fleet_logs_filters_panel)
        self.fleet_logs_filters_panel_header.setObjectName(u"fleet_logs_filters_panel_header")

        self.fleet_logs_filters_panel_layout.addWidget(self.fleet_logs_filters_panel_header)

        self.fleet_logs_filters_row = QHBoxLayout()
        self.fleet_logs_filters_row.setSpacing(9)
        self.fleet_logs_filters_row.setObjectName(u"fleet_logs_filters_row")
        self.fleet_logs_filters_row.setContentsMargins(0, 0, 0, 0)
        self.fleet_logs_search = QLineEdit(self.fleet_logs_filters_panel)
        self.fleet_logs_search.setObjectName(u"fleet_logs_search")
        self.fleet_logs_search.setMinimumSize(QSize(0, 0))

        self.fleet_logs_filters_row.addWidget(self.fleet_logs_search)

        self.fleet_logs_agent_combo = QComboBox(self.fleet_logs_filters_panel)
        self.fleet_logs_agent_combo.addItem("")
        self.fleet_logs_agent_combo.setObjectName(u"fleet_logs_agent_combo")
        self.fleet_logs_agent_combo.setMinimumSize(QSize(0, 0))

        self.fleet_logs_filters_row.addWidget(self.fleet_logs_agent_combo)

        self.fleet_logs_level_combo = QComboBox(self.fleet_logs_filters_panel)
        self.fleet_logs_level_combo.addItem("")
        self.fleet_logs_level_combo.addItem("")
        self.fleet_logs_level_combo.addItem("")
        self.fleet_logs_level_combo.addItem("")
        self.fleet_logs_level_combo.addItem("")
        self.fleet_logs_level_combo.setObjectName(u"fleet_logs_level_combo")
        self.fleet_logs_level_combo.setMinimumSize(QSize(0, 0))

        self.fleet_logs_filters_row.addWidget(self.fleet_logs_level_combo)

        self.fleet_logs_source_combo = QComboBox(self.fleet_logs_filters_panel)
        self.fleet_logs_source_combo.addItem("")
        self.fleet_logs_source_combo.addItem("")
        self.fleet_logs_source_combo.addItem("")
        self.fleet_logs_source_combo.addItem("")
        self.fleet_logs_source_combo.setObjectName(u"fleet_logs_source_combo")
        self.fleet_logs_source_combo.setMinimumSize(QSize(0, 0))

        self.fleet_logs_filters_row.addWidget(self.fleet_logs_source_combo)


        self.fleet_logs_filters_panel_layout.addLayout(self.fleet_logs_filters_row)


        self.fleet_logs_filters_panel_host_layout.addLayout(self.fleet_logs_filters_panel_layout)


        self.fleet_logs_page_layout.addWidget(self.fleet_logs_filters_panel)

        self.line_12 = QFrame(self.fleet_logs_page_scroll_content)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.fleet_logs_page_layout.addWidget(self.line_12)

        self.fleet_logs_table_panel = QFrame(self.fleet_logs_page_scroll_content)
        self.fleet_logs_table_panel.setObjectName(u"fleet_logs_table_panel")
        self.fleet_logs_table_panel_host_layout = QVBoxLayout(self.fleet_logs_table_panel)
        self.fleet_logs_table_panel_host_layout.setObjectName(u"fleet_logs_table_panel_host_layout")
        self.fleet_logs_table_panel_host_layout.setContentsMargins(0, 0, 0, 0)
        self.fleet_logs_table_panel_layout = QVBoxLayout()
        self.fleet_logs_table_panel_layout.setSpacing(12)
        self.fleet_logs_table_panel_layout.setObjectName(u"fleet_logs_table_panel_layout")
        self.fleet_logs_table_panel_layout.setContentsMargins(6, 6, 6, 6)
        self.fleet_logs_table_panel_header = QLabel(self.fleet_logs_table_panel)
        self.fleet_logs_table_panel_header.setObjectName(u"fleet_logs_table_panel_header")

        self.fleet_logs_table_panel_layout.addWidget(self.fleet_logs_table_panel_header)

        self.fleet_logs_table_panel_caption = QLabel(self.fleet_logs_table_panel)
        self.fleet_logs_table_panel_caption.setObjectName(u"fleet_logs_table_panel_caption")

        self.fleet_logs_table_panel_layout.addWidget(self.fleet_logs_table_panel_caption)

        self.fleet_logs_table = QTableWidget(self.fleet_logs_table_panel)
        if (self.fleet_logs_table.columnCount() < 5):
            self.fleet_logs_table.setColumnCount(5)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.fleet_logs_table.setHorizontalHeaderItem(0, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.fleet_logs_table.setHorizontalHeaderItem(1, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.fleet_logs_table.setHorizontalHeaderItem(2, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.fleet_logs_table.setHorizontalHeaderItem(3, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.fleet_logs_table.setHorizontalHeaderItem(4, __qtablewidgetitem77)
        self.fleet_logs_table.setObjectName(u"fleet_logs_table")
        self.fleet_logs_table.setMinimumSize(QSize(0, 260))
        self.fleet_logs_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.fleet_logs_table.setAlternatingRowColors(True)
        self.fleet_logs_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.fleet_logs_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.fleet_logs_table.setShowGrid(False)
        self.fleet_logs_table.setWordWrap(False)
        self.fleet_logs_table.setRowCount(0)
        self.fleet_logs_table.setColumnCount(5)

        self.fleet_logs_table_panel_layout.addWidget(self.fleet_logs_table)


        self.fleet_logs_table_panel_host_layout.addLayout(self.fleet_logs_table_panel_layout)


        self.fleet_logs_page_layout.addWidget(self.fleet_logs_table_panel)

        self.line_13 = QFrame(self.fleet_logs_page_scroll_content)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.Shape.HLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)

        self.fleet_logs_page_layout.addWidget(self.line_13)

        self.fleet_logs_details_panel = QFrame(self.fleet_logs_page_scroll_content)
        self.fleet_logs_details_panel.setObjectName(u"fleet_logs_details_panel")
        self.fleet_logs_details_panel_host_layout = QVBoxLayout(self.fleet_logs_details_panel)
        self.fleet_logs_details_panel_host_layout.setObjectName(u"fleet_logs_details_panel_host_layout")
        self.fleet_logs_details_panel_host_layout.setContentsMargins(0, 0, 0, 0)
        self.fleet_logs_details_panel_layout = QVBoxLayout()
        self.fleet_logs_details_panel_layout.setSpacing(12)
        self.fleet_logs_details_panel_layout.setObjectName(u"fleet_logs_details_panel_layout")
        self.fleet_logs_details_panel_layout.setContentsMargins(6, 6, 6, 6)
        self.fleet_logs_details_panel_header = QLabel(self.fleet_logs_details_panel)
        self.fleet_logs_details_panel_header.setObjectName(u"fleet_logs_details_panel_header")

        self.fleet_logs_details_panel_layout.addWidget(self.fleet_logs_details_panel_header)

        self.fleet_logs_event_metadata = QLabel(self.fleet_logs_details_panel)
        self.fleet_logs_event_metadata.setObjectName(u"fleet_logs_event_metadata")

        self.fleet_logs_details_panel_layout.addWidget(self.fleet_logs_event_metadata)

        self.fleet_logs_details_view = QPlainTextEdit(self.fleet_logs_details_panel)
        self.fleet_logs_details_view.setObjectName(u"fleet_logs_details_view")
        self.fleet_logs_details_view.setMinimumSize(QSize(0, 105))
        self.fleet_logs_details_view.setReadOnly(True)

        self.fleet_logs_details_panel_layout.addWidget(self.fleet_logs_details_view)

        self.fleet_logs_details_actions = QHBoxLayout()
        self.fleet_logs_details_actions.setSpacing(10)
        self.fleet_logs_details_actions.setObjectName(u"fleet_logs_details_actions")
        self.fleet_logs_details_actions.setContentsMargins(0, 0, 0, 0)
        self.fleet_logs_copy_button = QPushButton(self.fleet_logs_details_panel)
        self.fleet_logs_copy_button.setObjectName(u"fleet_logs_copy_button")
        self.fleet_logs_copy_button.setMinimumSize(QSize(0, 0))
        self.fleet_logs_copy_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.fleet_logs_details_actions.addWidget(self.fleet_logs_copy_button)

        self.fleet_logs_clear_filters_button = QPushButton(self.fleet_logs_details_panel)
        self.fleet_logs_clear_filters_button.setObjectName(u"fleet_logs_clear_filters_button")
        self.fleet_logs_clear_filters_button.setMinimumSize(QSize(0, 0))
        self.fleet_logs_clear_filters_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.fleet_logs_details_actions.addWidget(self.fleet_logs_clear_filters_button)


        self.fleet_logs_details_panel_layout.addLayout(self.fleet_logs_details_actions)


        self.fleet_logs_details_panel_host_layout.addLayout(self.fleet_logs_details_panel_layout)


        self.fleet_logs_page_layout.addWidget(self.fleet_logs_details_panel)

        self.fleet_logs_page_scroll.setWidget(self.fleet_logs_page_scroll_content)

        self.fleet_logs_page_host_layout.addWidget(self.fleet_logs_page_scroll)

        self.content_stack.addWidget(self.fleet_logs_page)
        self.preferences_page = QWidget()
        self.preferences_page.setObjectName(u"preferences_page")
        self.preferences_page_host_layout = QVBoxLayout(self.preferences_page)
        self.preferences_page_host_layout.setSpacing(0)
        self.preferences_page_host_layout.setObjectName(u"preferences_page_host_layout")
        self.preferences_page_host_layout.setContentsMargins(0, 0, 0, 0)
        self.preferences_page_scroll = QScrollArea(self.preferences_page)
        self.preferences_page_scroll.setObjectName(u"preferences_page_scroll")
        self.preferences_page_scroll.setFrameShape(QFrame.NoFrame)
        self.preferences_page_scroll.setWidgetResizable(True)
        self.preferences_page_scroll_content = QWidget()
        self.preferences_page_scroll_content.setObjectName(u"preferences_page_scroll_content")
        self.preferences_page_scroll_content.setGeometry(QRect(0, 0, 391, 382))
        self.preferences_page_layout = QVBoxLayout(self.preferences_page_scroll_content)
        self.preferences_page_layout.setSpacing(17)
        self.preferences_page_layout.setObjectName(u"preferences_page_layout")
        self.preferences_page_layout.setContentsMargins(6, 6, 0, 0)
        self.prefs_heading_row = QHBoxLayout()
        self.prefs_heading_row.setSpacing(0)
        self.prefs_heading_row.setObjectName(u"prefs_heading_row")
        self.prefs_heading_row.setContentsMargins(0, 0, 0, 0)
        self.prefs_heading_text = QVBoxLayout()
        self.prefs_heading_text.setSpacing(4)
        self.prefs_heading_text.setObjectName(u"prefs_heading_text")
        self.prefs_heading_text.setContentsMargins(0, 0, 0, 0)
        self.prefs_title = QLabel(self.preferences_page_scroll_content)
        self.prefs_title.setObjectName(u"prefs_title")

        self.prefs_heading_text.addWidget(self.prefs_title)

        self.prefs_subtitle = QLabel(self.preferences_page_scroll_content)
        self.prefs_subtitle.setObjectName(u"prefs_subtitle")
        self.prefs_subtitle.setWordWrap(True)

        self.prefs_heading_text.addWidget(self.prefs_subtitle)


        self.prefs_heading_row.addLayout(self.prefs_heading_text)

        self.prefs_heading_spacer = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.prefs_heading_row.addItem(self.prefs_heading_spacer)


        self.preferences_page_layout.addLayout(self.prefs_heading_row)

        self.line_10 = QFrame(self.preferences_page_scroll_content)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.preferences_page_layout.addWidget(self.line_10)

        self.preferences_connection_panel = QFrame(self.preferences_page_scroll_content)
        self.preferences_connection_panel.setObjectName(u"preferences_connection_panel")
        self.preferences_connection_panel.setMaximumSize(QSize(820, 16777215))
        self.preferences_connection_panel_host_layout = QVBoxLayout(self.preferences_connection_panel)
        self.preferences_connection_panel_host_layout.setObjectName(u"preferences_connection_panel_host_layout")
        self.preferences_connection_panel_host_layout.setContentsMargins(0, 0, 0, 0)
        self.preferences_connection_panel_layout = QVBoxLayout()
        self.preferences_connection_panel_layout.setSpacing(12)
        self.preferences_connection_panel_layout.setObjectName(u"preferences_connection_panel_layout")
        self.preferences_connection_panel_layout.setContentsMargins(12, 12, 12, 12)
        self.preferences_connection_panel_header = QLabel(self.preferences_connection_panel)
        self.preferences_connection_panel_header.setObjectName(u"preferences_connection_panel_header")

        self.preferences_connection_panel_layout.addWidget(self.preferences_connection_panel_header)

        self.preferences_connection_panel_caption = QLabel(self.preferences_connection_panel)
        self.preferences_connection_panel_caption.setObjectName(u"preferences_connection_panel_caption")

        self.preferences_connection_panel_layout.addWidget(self.preferences_connection_panel_caption)

        self.preferences_endpoint_label = QLabel(self.preferences_connection_panel)
        self.preferences_endpoint_label.setObjectName(u"preferences_endpoint_label")

        self.preferences_connection_panel_layout.addWidget(self.preferences_endpoint_label)

        self.preferences_endpoint_edit = QLineEdit(self.preferences_connection_panel)
        self.preferences_endpoint_edit.setObjectName(u"preferences_endpoint_edit")
        self.preferences_endpoint_edit.setMinimumSize(QSize(0, 0))

        self.preferences_connection_panel_layout.addWidget(self.preferences_endpoint_edit)

        self.preferences_interval_label = QLabel(self.preferences_connection_panel)
        self.preferences_interval_label.setObjectName(u"preferences_interval_label")

        self.preferences_connection_panel_layout.addWidget(self.preferences_interval_label)

        self.preferences_refresh_interval_combo = QComboBox(self.preferences_connection_panel)
        self.preferences_refresh_interval_combo.addItem("")
        self.preferences_refresh_interval_combo.addItem("")
        self.preferences_refresh_interval_combo.addItem("")
        self.preferences_refresh_interval_combo.addItem("")
        self.preferences_refresh_interval_combo.setObjectName(u"preferences_refresh_interval_combo")
        self.preferences_refresh_interval_combo.setMinimumSize(QSize(0, 0))

        self.preferences_connection_panel_layout.addWidget(self.preferences_refresh_interval_combo)


        self.preferences_connection_panel_host_layout.addLayout(self.preferences_connection_panel_layout)


        self.preferences_page_layout.addWidget(self.preferences_connection_panel)

        self.preferences_save_button = QPushButton(self.preferences_page_scroll_content)
        self.preferences_save_button.setObjectName(u"preferences_save_button")
        self.preferences_save_button.setMinimumSize(QSize(150, 0))
        self.preferences_save_button.setMaximumSize(QSize(190, 34))
        self.preferences_save_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.preferences_page_layout.addWidget(self.preferences_save_button)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.preferences_page_layout.addItem(self.verticalSpacer_3)

        self.preferences_page_scroll.setWidget(self.preferences_page_scroll_content)

        self.preferences_page_host_layout.addWidget(self.preferences_page_scroll)

        self.content_stack.addWidget(self.preferences_page)
        self.application_about_page = QWidget()
        self.application_about_page.setObjectName(u"application_about_page")
        self.application_about_page_host_layout = QVBoxLayout(self.application_about_page)
        self.application_about_page_host_layout.setSpacing(0)
        self.application_about_page_host_layout.setObjectName(u"application_about_page_host_layout")
        self.application_about_page_host_layout.setContentsMargins(0, 0, 0, 0)
        self.application_about_page_scroll = QScrollArea(self.application_about_page)
        self.application_about_page_scroll.setObjectName(u"application_about_page_scroll")
        self.application_about_page_scroll.setFrameShape(QFrame.NoFrame)
        self.application_about_page_scroll.setWidgetResizable(True)
        self.application_about_page_scroll_content = QWidget()
        self.application_about_page_scroll_content.setObjectName(u"application_about_page_scroll_content")
        self.application_about_page_scroll_content.setGeometry(QRect(0, 0, 303, 323))
        self.application_about_page_layout = QVBoxLayout(self.application_about_page_scroll_content)
        self.application_about_page_layout.setSpacing(6)
        self.application_about_page_layout.setObjectName(u"application_about_page_layout")
        self.application_about_page_layout.setContentsMargins(6, 6, 6, 6)
        self.about_heading_row = QHBoxLayout()
        self.about_heading_row.setSpacing(12)
        self.about_heading_row.setObjectName(u"about_heading_row")
        self.about_heading_row.setContentsMargins(0, 0, 0, 0)
        self.about_heading_text = QVBoxLayout()
        self.about_heading_text.setSpacing(4)
        self.about_heading_text.setObjectName(u"about_heading_text")
        self.about_heading_text.setContentsMargins(0, 0, 0, 0)
        self.about_title = QLabel(self.application_about_page_scroll_content)
        self.about_title.setObjectName(u"about_title")
        self.about_title.setMaximumSize(QSize(16777215, 50))

        self.about_heading_text.addWidget(self.about_title)

        self.about_subtitle = QLabel(self.application_about_page_scroll_content)
        self.about_subtitle.setObjectName(u"about_subtitle")
        self.about_subtitle.setMaximumSize(QSize(16777215, 50))
        self.about_subtitle.setWordWrap(True)

        self.about_heading_text.addWidget(self.about_subtitle)


        self.about_heading_row.addLayout(self.about_heading_text)

        self.about_heading_spacer = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.about_heading_row.addItem(self.about_heading_spacer)


        self.application_about_page_layout.addLayout(self.about_heading_row)

        self.line_9 = QFrame(self.application_about_page_scroll_content)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.application_about_page_layout.addWidget(self.line_9)

        self.about_identity_panel = QFrame(self.application_about_page_scroll_content)
        self.about_identity_panel.setObjectName(u"about_identity_panel")
        self.about_identity_panel.setMaximumSize(QSize(820, 16777215))
        self.about_identity_panel_host_layout = QVBoxLayout(self.about_identity_panel)
        self.about_identity_panel_host_layout.setObjectName(u"about_identity_panel_host_layout")
        self.about_identity_panel_host_layout.setContentsMargins(0, 0, 0, 0)
        self.about_identity_panel_layout = QVBoxLayout()
        self.about_identity_panel_layout.setSpacing(12)
        self.about_identity_panel_layout.setObjectName(u"about_identity_panel_layout")
        self.about_identity_panel_layout.setContentsMargins(6, 10, 0, 0)
        self.about_identity_panel_header = QLabel(self.about_identity_panel)
        self.about_identity_panel_header.setObjectName(u"about_identity_panel_header")

        self.about_identity_panel_layout.addWidget(self.about_identity_panel_header)

        self.about_identity_panel_caption = QLabel(self.about_identity_panel)
        self.about_identity_panel_caption.setObjectName(u"about_identity_panel_caption")

        self.about_identity_panel_layout.addWidget(self.about_identity_panel_caption)

        self.about_description = QLabel(self.about_identity_panel)
        self.about_description.setObjectName(u"about_description")
        self.about_description.setWordWrap(True)

        self.about_identity_panel_layout.addWidget(self.about_description)

        self.about_version_value = QLabel(self.about_identity_panel)
        self.about_version_value.setObjectName(u"about_version_value")

        self.about_identity_panel_layout.addWidget(self.about_version_value)

        self.about_backend_value = QLabel(self.about_identity_panel)
        self.about_backend_value.setObjectName(u"about_backend_value")

        self.about_identity_panel_layout.addWidget(self.about_backend_value)

        self.about_client_value = QLabel(self.about_identity_panel)
        self.about_client_value.setObjectName(u"about_client_value")

        self.about_identity_panel_layout.addWidget(self.about_client_value)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.about_identity_panel_layout.addItem(self.verticalSpacer_2)


        self.about_identity_panel_host_layout.addLayout(self.about_identity_panel_layout)


        self.application_about_page_layout.addWidget(self.about_identity_panel)

        self.application_about_page_scroll.setWidget(self.application_about_page_scroll_content)

        self.application_about_page_host_layout.addWidget(self.application_about_page_scroll)

        self.content_stack.addWidget(self.application_about_page)

        self.central_content_layout.addWidget(self.content_stack)

        MainWindow.setCentralWidget(self.central_content)

        self.retranslateUi(MainWindow)

        self.content_stack.setCurrentIndex(3)
        self.agent_detail_stacked_content.setCurrentIndex(3)
        self.performance_stacked_content.setCurrentIndex(2)
        self.agent_command_result_tabs.setCurrentIndex(0)
        self.fleet_command_result_tabs.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"NexoraControl \u2014 Infrastructure Console", None))
        self.nexora_logo.setText(QCoreApplication.translate("MainWindow", u"NEXORA", None))
        self.sidebar_product_subtitle.setText(QCoreApplication.translate("MainWindow", u"SYSTEM OPERATIONS", None))
        self.dashboard_button.setText(QCoreApplication.translate("MainWindow", u"  Overview", None))
        self.agents_button.setText(QCoreApplication.translate("MainWindow", u"  Agents", None))
        self.commands_button.setText(QCoreApplication.translate("MainWindow", u"  Commands", None))
        self.logs_button.setText(QCoreApplication.translate("MainWindow", u"  Logs", None))
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"  Settings", None))
        self.about_button.setText(QCoreApplication.translate("MainWindow", u"  About", None))
        self.dashboard_label.setText(QCoreApplication.translate("MainWindow", u"Fleet overview", None))
        self.dashboard_legend_label.setText(QCoreApplication.translate("MainWindow", u"Registered nodes  /  Current connectivity", None))
        self.agent_label.setText(QCoreApplication.translate("MainWindow", u"Agents", None))
        self.agents_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.online_label.setText(QCoreApplication.translate("MainWindow", u"Online", None))
        self.online_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.offline_label.setText(QCoreApplication.translate("MainWindow", u"Offline", None))
        self.offline_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.agents_label.setText(QCoreApplication.translate("MainWindow", u"Agent registry", None))
        self.agents_table_legend_label.setText(QCoreApplication.translate("MainWindow", u"Hosts, connectivity and last contact", None))
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
        self.refresh_table_button.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.agents_headline_label.setText(QCoreApplication.translate("MainWindow", u"Agents", None))
        self.page_description_label.setText(QCoreApplication.translate("MainWindow", u"Managed hosts and agent connectivity", None))
        self.search_input_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search agents by name, hostname or address", None))
        self.refresh_agents_button.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.back_to_agents_button.setText(QCoreApplication.translate("MainWindow", u"\u2190  Agents", None))
        self.detail_top_agent_name_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.detail_top_agent_status_label.setText(QCoreApplication.translate("MainWindow", u"\u25cb OFFLINE", None))
        self.overview_nav_button.setText(QCoreApplication.translate("MainWindow", u"Overview", None))
        self.performance_nav_button.setText(QCoreApplication.translate("MainWindow", u"Performance", None))
        self.hardware_nav_button.setText(QCoreApplication.translate("MainWindow", u"Hardware", None))
        self.commands_nav_button.setText(QCoreApplication.translate("MainWindow", u"Commands", None))
        self.overview_label.setText(QCoreApplication.translate("MainWindow", u"Overview", None))
        self.overview_legend_label.setText(QCoreApplication.translate("MainWindow", u"Host resources, connection details and recent activity", None))
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
        self.quick_actions_label.setText(QCoreApplication.translate("MainWindow", u"Quick actions", None))
        self.restart_all_docker_cont_quick_button.setText(QCoreApplication.translate("MainWindow", u"Restart containers", None))
        self.stop_all_docker_cont_quick_button.setText(QCoreApplication.translate("MainWindow", u"Stop containers", None))
        self.docker_ps_quick_button.setText(QCoreApplication.translate("MainWindow", u"List containers", None))
        self.reboot_quick_button.setText(QCoreApplication.translate("MainWindow", u"Reboot host", None))
        self.recent_commands_label.setText(QCoreApplication.translate("MainWindow", u"Recent executions", None))
        self.performance_label.setText(QCoreApplication.translate("MainWindow", u"Performance", None))
        self.performance_legend_label.setText(QCoreApplication.translate("MainWindow", u"Resource telemetry and historical measurements", None))
        self.compute_button.setText(QCoreApplication.translate("MainWindow", u"Compute", None))
        self.storage_button.setText(QCoreApplication.translate("MainWindow", u"Storage", None))
        self.thermals_button.setText(QCoreApplication.translate("MainWindow", u"Thermals", None))
        self.network_button.setText(QCoreApplication.translate("MainWindow", u"Network", None))
        self.compute_label.setText(QCoreApplication.translate("MainWindow", u"Compute", None))
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
        self.storage_label.setText(QCoreApplication.translate("MainWindow", u"Storage", None))
        self.storage_legend_label.setText(QCoreApplication.translate("MainWindow", u"Disk capacity, I/O activity and storage devices", None))
        self.current_storage_label.setText(QCoreApplication.translate("MainWindow", u"CURRENT STORAGE", None))
        self.disk_io_label.setText(QCoreApplication.translate("MainWindow", u"DISK I/O", None))
        self.hardware_group_label_2.setText(QCoreApplication.translate("MainWindow", u"DISK MOUNT", None))
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
        self.thermals_label.setText(QCoreApplication.translate("MainWindow", u"Thermal sensors", None))
        self.thermals_legend_label.setText(QCoreApplication.translate("MainWindow", u"Temperature sensors and thermal activity", None))
        self.current_thermals_label.setText(QCoreApplication.translate("MainWindow", u"CURRENT THERMALS", None))
        self.temperature_history_label.setText(QCoreApplication.translate("MainWindow", u"TEMPERATURE HISTORY", None))
        self.hardware_group_label.setText(QCoreApplication.translate("MainWindow", u"HARDWARE GROUP", None))
        self.hardware_group_combo_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"GROUP", None))
        self.sensor_name_label.setText(QCoreApplication.translate("MainWindow", u"SENSOR", None))
        self.thermal_sensor_name_combo_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NAME", None))
        self.sensors_label.setText(QCoreApplication.translate("MainWindow", u"SENSORS", None))
        ___qtablewidgetitem17 = self.sensors_table.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"GROUP", None))
        ___qtablewidgetitem18 = self.sensors_table.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"SENSOR", None))
        ___qtablewidgetitem19 = self.sensors_table.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"HIGH", None))
        ___qtablewidgetitem20 = self.sensors_table.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"CRITICAL", None))
        ___qtablewidgetitem21 = self.sensors_table.horizontalHeaderItem(4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"CURRENT", None))
        self.network_label.setText(QCoreApplication.translate("MainWindow", u"Network", None))
        self.network_legend_label.setText(QCoreApplication.translate("MainWindow", u"Network traffic, packets and interface statistics", None))
        self.network_gauges_combo_box_label.setText(QCoreApplication.translate("MainWindow", u"CURRENT NETWORK", None))
        self.rx_tx_throughput_label.setText(QCoreApplication.translate("MainWindow", u"RX TX TRAFFIC / PACKETS", None))
        self.network_group_combo_box_legend_label.setText(QCoreApplication.translate("MainWindow", u"NETWORK GROUP", None))
        self.network_traffic_graph_combo_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"GROUP", None))
        self.network_traffic_unit_combo_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UNIT", None))
        self.network_traffic_toggle_button.setText(QCoreApplication.translate("MainWindow", u"Traffic", None))
        self.network_packets_toggle_button.setText(QCoreApplication.translate("MainWindow", u"Packets", None))
        self.network_health_label.setText(QCoreApplication.translate("MainWindow", u"NETWORK IO IN TOTAL", None))
        self.network_health_errors_label.setText(QCoreApplication.translate("MainWindow", u"ERRORS", None))
        self.network_health_errors_content_top_rx_errors_label.setText(QCoreApplication.translate("MainWindow", u"RX errors", None))
        self.network_health_errors_content_top_rx_errors_value_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.network_health_errors_content_bottom_tx_errors_label.setText(QCoreApplication.translate("MainWindow", u"TX errors", None))
        self.network_health_errors_content_bottom_tx_errors_value_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.network_health_drops_label.setText(QCoreApplication.translate("MainWindow", u"DROPS", None))
        self.network_health_drops_content_top_rx_drops_label.setText(QCoreApplication.translate("MainWindow", u"RX drops", None))
        self.network_health_drops_content_top_rx_drops_value_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.network_health_drops_content_bottom_tx_drops_label.setText(QCoreApplication.translate("MainWindow", u"TX drops", None))
        self.network_health_drops_content_bottom_tx_drops_value_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.network_health_total_label.setText(QCoreApplication.translate("MainWindow", u"NETWORK DATA", None))
        self.network_health_total_content_top_rx_packets_label.setText(QCoreApplication.translate("MainWindow", u"RX packets", None))
        self.network_health_total_content_top_rx_packets_value_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.network_health_total_content_top_tx_packets_label.setText(QCoreApplication.translate("MainWindow", u"TX packets", None))
        self.network_health_total_content_top_tx_packets_value_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.network_health_total_content_bottom_rx_data_label.setText(QCoreApplication.translate("MainWindow", u"RX data", None))
        self.network_health_total_content_bottom_rx_data_value_label.setText(QCoreApplication.translate("MainWindow", u"0 MB", None))
        self.network_health_total_content_bottom_tx_data_label.setText(QCoreApplication.translate("MainWindow", u"TX data", None))
        self.network_health_total_content_bottom_tx_data_value_label.setText(QCoreApplication.translate("MainWindow", u"0 MB", None))
        self.network_interfaces_label.setText(QCoreApplication.translate("MainWindow", u"NETWORK INTERFACES", None))
        ___qtablewidgetitem22 = self.network_interfaces_table.horizontalHeaderItem(0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"INTERFACE", None))
        ___qtablewidgetitem23 = self.network_interfaces_table.horizontalHeaderItem(1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"TRAFFIC RX", None))
        ___qtablewidgetitem24 = self.network_interfaces_table.horizontalHeaderItem(2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"TRAFFIC TX", None))
        ___qtablewidgetitem25 = self.network_interfaces_table.horizontalHeaderItem(3)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"PACKETS RX", None))
        ___qtablewidgetitem26 = self.network_interfaces_table.horizontalHeaderItem(4)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"PACKETS TX", None))
        ___qtablewidgetitem27 = self.network_interfaces_table.horizontalHeaderItem(5)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"ERROR IN / ERROR OUT", None))
        ___qtablewidgetitem28 = self.network_interfaces_table.horizontalHeaderItem(6)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"DROPS IN/ DROPS OUT", None))
        self.hardware_label.setText(QCoreApplication.translate("MainWindow", u"Hardware", None))
        self.hardware_legend_label.setText(QCoreApplication.translate("MainWindow", u"Static component specifications and system identification", None))
        self.hardware_storage_inventory_panel_header.setText(QCoreApplication.translate("MainWindow", u"Storage devices", None))
        ___qtablewidgetitem29 = self.hardware_storage_devices_table.horizontalHeaderItem(0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"DEVICE", None))
        ___qtablewidgetitem30 = self.hardware_storage_devices_table.horizontalHeaderItem(1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"MODEL", None))
        ___qtablewidgetitem31 = self.hardware_storage_devices_table.horizontalHeaderItem(2)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"CAPACITY", None))
        ___qtablewidgetitem32 = self.hardware_storage_devices_table.horizontalHeaderItem(3)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"INTERFACE", None))
        self.hardware_refresh_inventory_button.setText(QCoreApplication.translate("MainWindow", u"Refresh inventory", None))
        self.hardware_gpu_inventory_panel_header.setText(QCoreApplication.translate("MainWindow", u"GPU Inventory", None))
        ___qtablewidgetitem33 = self.hardware_gpu_inventory_table.horizontalHeaderItem(0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"DEVICE", None))
        ___qtablewidgetitem34 = self.hardware_gpu_inventory_table.horizontalHeaderItem(1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"MODEL", None))
        ___qtablewidgetitem35 = self.hardware_gpu_inventory_table.horizontalHeaderItem(2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"VRAM", None))
        ___qtablewidgetitem36 = self.hardware_gpu_inventory_table.horizontalHeaderItem(3)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"DRIVER VERSION", None))
        ___qtablewidgetitem37 = self.hardware_gpu_inventory_table.horizontalHeaderItem(4)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"INTERFACE", None))
        self.hardware_bios_motherboard_panel_header.setText(QCoreApplication.translate("MainWindow", u"Motherboard & BIOS", None))
        ___qtablewidgetitem38 = self.hardware_bios_motherboard_table.horizontalHeaderItem(0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"BOARD VENDOR", None))
        ___qtablewidgetitem39 = self.hardware_bios_motherboard_table.horizontalHeaderItem(1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"BOARD MODEL", None))
        ___qtablewidgetitem40 = self.hardware_bios_motherboard_table.horizontalHeaderItem(2)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"BIOS VENDOR", None))
        ___qtablewidgetitem41 = self.hardware_bios_motherboard_table.horizontalHeaderItem(3)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"BIOS VERSION", None))
        ___qtablewidgetitem42 = self.hardware_bios_motherboard_table.horizontalHeaderItem(4)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"RELEASE DATE", None))
        self.hardware_ram_modules_panel_header.setText(QCoreApplication.translate("MainWindow", u"Memory Section", None))
        ___qtablewidgetitem43 = self.hardware_ram_modules_table.horizontalHeaderItem(0)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"SLOT", None))
        ___qtablewidgetitem44 = self.hardware_ram_modules_table.horizontalHeaderItem(1)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"CAPACITY", None))
        self.hardware_network_inventory_panel_header.setText(QCoreApplication.translate("MainWindow", u"Network adapters", None))
        ___qtablewidgetitem45 = self.hardware_network_adapters_table.horizontalHeaderItem(0)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"INTERFACE", None))
        ___qtablewidgetitem46 = self.hardware_network_adapters_table.horizontalHeaderItem(1)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"MODEL", None))
        ___qtablewidgetitem47 = self.hardware_network_adapters_table.horizontalHeaderItem(2)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"MAC ADDRESS", None))
        ___qtablewidgetitem48 = self.hardware_network_adapters_table.horizontalHeaderItem(3)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"LINK TYPE", None))
        ___qtablewidgetitem49 = self.hardware_network_adapters_table.horizontalHeaderItem(4)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"STATUS", None))
        self.hardware_cpu_inventory_panel_header.setText(QCoreApplication.translate("MainWindow", u"CPU Inventory", None))
        ___qtablewidgetitem50 = self.hardware_cpu_specifications_table.horizontalHeaderItem(0)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"MODEL", None))
        ___qtablewidgetitem51 = self.hardware_cpu_specifications_table.horizontalHeaderItem(1)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"ARCHITECTURE", None))
        ___qtablewidgetitem52 = self.hardware_cpu_specifications_table.horizontalHeaderItem(2)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"PHYSICAL CORES", None))
        ___qtablewidgetitem53 = self.hardware_cpu_specifications_table.horizontalHeaderItem(3)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"LOGICAL THREADS", None))
        ___qtablewidgetitem54 = self.hardware_cpu_specifications_table.horizontalHeaderItem(4)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"FREQUENCY", None))
        ___qtablewidgetitem55 = self.hardware_cpu_specifications_table.horizontalHeaderItem(5)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"L1 CACHE", None))
        ___qtablewidgetitem56 = self.hardware_cpu_specifications_table.horizontalHeaderItem(6)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"L2 CACHE", None))
        ___qtablewidgetitem57 = self.hardware_cpu_specifications_table.horizontalHeaderItem(7)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"L3 CACHE", None))
        self.agent_cmd_title.setText(QCoreApplication.translate("MainWindow", u"Agent Commands", None))
        self.agent_cmd_subtitle.setText(QCoreApplication.translate("MainWindow", u"One target. Typed parameters. Controlled execution.", None))
        self.agent_command_target_indicator.setText(QCoreApplication.translate("MainWindow", u"TARGET  /  Select an agent from the Agents page", None))
        self.agent_command_process_steps.setText(QCoreApplication.translate("MainWindow", u"01  SELECT OPERATION     /     02  CONFIGURE FIELDS     /     03  VALIDATE & QUEUE     /     04  INSPECT RESULT", None))
        self.agent_command_form_panel_header.setText(QCoreApplication.translate("MainWindow", u"01  /  COMMAND BUILDER", None))
        self.agent_command_form_panel_caption.setText(QCoreApplication.translate("MainWindow", u"The target is the currently opened agent. Parameters are local.", None))
        self.agent_command_category_label.setText(QCoreApplication.translate("MainWindow", u"CATEGORY", None))
        self.agent_command_category_combo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"All categories", None))
        self.agent_command_type_label.setText(QCoreApplication.translate("MainWindow", u"OPERATION", None))
        self.agent_command_type_combo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select command\u2026", None))
        self.agent_command_display_title.setText(QCoreApplication.translate("MainWindow", u"No given command", None))
        self.agent_command_risk_badge.setText("")
        self.agent_command_command_key.setText(QCoreApplication.translate("MainWindow", u"Please select a command above", None))
        self.agent_command_description.setText("")
        self.agent_command_fields_label.setText(QCoreApplication.translate("MainWindow", u"PARAMETERS", None))
        self.agent_command_fields_count.setText("")
#if QT_CONFIG(tooltip)
        self.agent_command_fields_container.setToolTip(QCoreApplication.translate("MainWindow", u"Dynamic command parameter area.", None))
#endif // QT_CONFIG(tooltip)
        self.agent_command_payload_label.setText(QCoreApplication.translate("MainWindow", u"ADVANCED  /  RAW JSON PAYLOAD", None))
        self.agent_command_raw_mode_checkbox.setText(QCoreApplication.translate("MainWindow", u"Edit raw JSON instead of generated fields", None))
        self.agent_command_payload_editor.setPlainText("")
        self.agent_command_payload_editor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}", None))
        self.agent_command_review_header.setText(QCoreApplication.translate("MainWindow", u"02  /  EXECUTION REVIEW", None))
        self.agent_command_review_caption.setText(QCoreApplication.translate("MainWindow", u"Validate the exact request before it enters the agent queue.", None))
        self.agent_command_review_target.setText(QCoreApplication.translate("MainWindow", u"TARGET  /  Current agent", None))
        self.agent_command_review_operation.setText(QCoreApplication.translate("MainWindow", u"COMMAND  /  docker_logs", None))
        self.agent_command_review_payload_label.setText(QCoreApplication.translate("MainWindow", u"HTTP REQUEST PREVIEW", None))
        self.agent_command_request_preview.setPlainText("")
        self.agent_command_request_preview.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}", None))
        self.agent_command_validation_status.setText(QCoreApplication.translate("MainWindow", u"NOT VALIDATED   \u00b7   Complete parameters first.", None))
        self.agent_command_risk_confirmation_checkbox.setText(QCoreApplication.translate("MainWindow", u"I understand this operation may disrupt the target.", None))
        self.agent_command_validate_button.setText(QCoreApplication.translate("MainWindow", u"Validate inputs", None))
        self.agent_command_execute_button.setText(QCoreApplication.translate("MainWindow", u"Queue command  \u2192", None))
        self.agent_command_output_panel_header.setText(QCoreApplication.translate("MainWindow", u"EXECUTION INSPECTOR", None))
        self.agent_command_output_panel_caption.setText(QCoreApplication.translate("MainWindow", u"Select an execution from history to inspect its response.", None))
        self.agent_command_result_summary.setText(QCoreApplication.translate("MainWindow", u"No execution selected", None))
        self.agent_command_result_status.setText(QCoreApplication.translate("MainWindow", u"STATUS  /  \u2014", None))
        self.agent_command_result_duration.setText(QCoreApplication.translate("MainWindow", u"DURATION  /  \u2014", None))
        self.agent_command_output_view.setPlaceholderText(QCoreApplication.translate("MainWindow", u"No stdout captured for the selected execution.", None))
        self.agent_command_result_tabs.setTabText(self.agent_command_result_tabs.indexOf(self.agent_command_stdout_tab), QCoreApplication.translate("MainWindow", u"STDOUT", None))
        self.agent_command_stderr_view.setPlaceholderText(QCoreApplication.translate("MainWindow", u"No stderr captured for the selected execution.", None))
        self.agent_command_result_tabs.setTabText(self.agent_command_result_tabs.indexOf(self.agent_command_stderr_tab), QCoreApplication.translate("MainWindow", u"STDERR", None))
        self.agent_command_copy_output_button.setText(QCoreApplication.translate("MainWindow", u"Copy output", None))
        self.agent_command_recent_section_label.setText(QCoreApplication.translate("MainWindow", u"03  /  AGENT COMMAND HISTORY", None))
        self.agent_command_history_panel_header.setText(QCoreApplication.translate("MainWindow", u"EXECUTION HISTORY", None))
        self.agent_command_history_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search command ID, operation or target\u2026", None))
        self.agent_command_status_filter_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"All statuses", None))
        self.agent_command_status_filter_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Pending", None))
        self.agent_command_status_filter_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"Running", None))
        self.agent_command_status_filter_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"Success", None))
        self.agent_command_status_filter_combo.setItemText(4, QCoreApplication.translate("MainWindow", u"Failed", None))

        self.agent_command_history_refresh_button.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        ___qtablewidgetitem58 = self.agent_command_history_table.horizontalHeaderItem(0)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        ___qtablewidgetitem59 = self.agent_command_history_table.horizontalHeaderItem(1)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"COMMAND", None))
        ___qtablewidgetitem60 = self.agent_command_history_table.horizontalHeaderItem(2)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"STATUS", None))
        ___qtablewidgetitem61 = self.agent_command_history_table.horizontalHeaderItem(3)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"CREATED", None))
        ___qtablewidgetitem62 = self.agent_command_history_table.horizontalHeaderItem(4)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"STARTED", None))
        ___qtablewidgetitem63 = self.agent_command_history_table.horizontalHeaderItem(5)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"FINISHED", None))
        self.fleet_cmd_title.setText(QCoreApplication.translate("MainWindow", u"Command Center", None))
        self.fleet_cmd_subtitle.setText(QCoreApplication.translate("MainWindow", u"Find an operation, build a valid request, verify, then queue.", None))
        self.fleet_command_workspace_status.setText(QCoreApplication.translate("MainWindow", u"LOCAL COMMAND REGISTRY  /  SINGLE TARGET", None))
        self.fleet_cmd_refresh_button.setText(QCoreApplication.translate("MainWindow", u"Refresh agents", None))
        self.fleet_command_process_steps.setText(QCoreApplication.translate("MainWindow", u"01  SELECT OPERATION     /     02  CONFIGURE FIELDS     /     03  VALIDATE & QUEUE     /     04  INSPECT RESULT", None))
        self.fleet_command_library_panel_header.setText(QCoreApplication.translate("MainWindow", u"01  /  COMMAND LIBRARY", None))
        self.fleet_command_library_panel_caption.setText(QCoreApplication.translate("MainWindow", u"Operations defined inside your desktop application.", None))
        self.fleet_command_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search operations or descriptions\u2026", None))
        self.fleet_command_category.setItemText(0, QCoreApplication.translate("MainWindow", u"All categories", None))

        self.fleet_command_category.setPlaceholderText("")
        ___qtablewidgetitem64 = self.fleet_command_catalog_table.horizontalHeaderItem(0)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"OPERATION", None))
        ___qtablewidgetitem65 = self.fleet_command_catalog_table.horizontalHeaderItem(1)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"CATEGORY", None))
        ___qtablewidgetitem66 = self.fleet_command_catalog_table.horizontalHeaderItem(2)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"RISK", None))
        self.fleet_command_library_help.setText(QCoreApplication.translate("MainWindow", u"Choose a command to view its title, description, settings, and risks..", None))
        self.fleet_command_execution_panel_header.setText(QCoreApplication.translate("MainWindow", u"02  /  COMMAND BUILDER", None))
        self.fleet_command_execution_panel_caption.setText(QCoreApplication.translate("MainWindow", u"Choose a target, inspect the command, then configure its inputs.", None))
        self.fleet_command_target_label.setText(QCoreApplication.translate("MainWindow", u"TARGET AGENT   *", None))
        self.fleet_command_target_combo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select a managed agent\u2026", None))
        self.fleet_command_category_label.setText(QCoreApplication.translate("MainWindow", u"CATEGORY", None))
        self.fleet_command_category_combo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"All categories", None))
        self.fleet_command_selected_label.setText(QCoreApplication.translate("MainWindow", u"OPERATION", None))
        self.fleet_command_type_combo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select command\u2026", None))
        self.fleet_command_display_title.setText(QCoreApplication.translate("MainWindow", u"No given command", None))
        self.fleet_command_risk_badge.setText("")
        self.fleet_command_command_key.setText(QCoreApplication.translate("MainWindow", u"Please select a command above", None))
        self.fleet_command_description.setText("")
        self.fleet_command_fields_label.setText(QCoreApplication.translate("MainWindow", u"PARAMETERS", None))
        self.fleet_command_fields_count.setText(QCoreApplication.translate("MainWindow", u"2 FIELDS   \u00b7   1 REQUIRED", None))
#if QT_CONFIG(tooltip)
        self.fleet_command_fields_container.setToolTip(QCoreApplication.translate("MainWindow", u"Dynamic command parameter area. Add fields to the existing fleet_command_fields_layout at runtime; no fixed schema widgets are included.", None))
#endif // QT_CONFIG(tooltip)
        self.fleet_command_payload_label.setText(QCoreApplication.translate("MainWindow", u"ADVANCED  /  RAW JSON PAYLOAD", None))
        self.fleet_command_raw_mode_checkbox.setText(QCoreApplication.translate("MainWindow", u"Edit raw JSON instead of generated fields", None))
        self.fleet_command_payload_editor.setPlainText("")
        self.fleet_command_payload_editor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}", None))
        self.fleet_command_review_header.setText(QCoreApplication.translate("MainWindow", u"03  /  EXECUTION REVIEW", None))
        self.fleet_command_review_caption.setText(QCoreApplication.translate("MainWindow", u"Validate the exact request before it enters the agent queue.", None))
        self.fleet_command_review_target.setText(QCoreApplication.translate("MainWindow", u"TARGET  /  Not selected", None))
        self.fleet_command_review_operation.setText(QCoreApplication.translate("MainWindow", u"COMMAND  /  docker_logs", None))
        self.fleet_command_review_payload_label.setText(QCoreApplication.translate("MainWindow", u"HTTP REQUEST PREVIEW", None))
        self.fleet_command_request_preview.setPlainText("")
        self.fleet_command_request_preview.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}", None))
        self.fleet_command_validation_status.setText(QCoreApplication.translate("MainWindow", u"NOT VALIDATED   \u00b7   Complete parameters first.", None))
        self.fleet_command_risk_confirmation_checkbox.setText(QCoreApplication.translate("MainWindow", u"I understand this operation may disrupt the target.", None))
        self.fleet_command_validate_button.setText(QCoreApplication.translate("MainWindow", u"Validate inputs", None))
        self.fleet_command_execute_button.setText(QCoreApplication.translate("MainWindow", u"Queue command  \u2192", None))
        self.fleet_command_recent_section_label.setText(QCoreApplication.translate("MainWindow", u"04  /  RECENT OPERATIONS", None))
        self.fleet_command_history_panel_header.setText(QCoreApplication.translate("MainWindow", u"EXECUTION HISTORY", None))
        self.fleet_command_history_panel_caption.setText(QCoreApplication.translate("MainWindow", u"Commands submitted across selected targets. Inspect any execution on the right.", None))
        self.fleet_command_history_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search command ID, operation or target\u2026", None))
        self.fleet_command_history_status_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"All statuses", None))
        self.fleet_command_history_status_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Pending", None))
        self.fleet_command_history_status_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"Running", None))
        self.fleet_command_history_status_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"Success", None))
        self.fleet_command_history_status_combo.setItemText(4, QCoreApplication.translate("MainWindow", u"Failed", None))
        self.fleet_command_history_status_combo.setItemText(5, QCoreApplication.translate("MainWindow", u"Cancelled", None))

        self.fleet_command_history_refresh_button.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        ___qtablewidgetitem67 = self.fleet_command_history_table.horizontalHeaderItem(0)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        ___qtablewidgetitem68 = self.fleet_command_history_table.horizontalHeaderItem(1)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"COMMAND", None))
        ___qtablewidgetitem69 = self.fleet_command_history_table.horizontalHeaderItem(2)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"STATUS", None))
        ___qtablewidgetitem70 = self.fleet_command_history_table.horizontalHeaderItem(3)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"CREATED", None))
        ___qtablewidgetitem71 = self.fleet_command_history_table.horizontalHeaderItem(4)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"STARTED", None))
        ___qtablewidgetitem72 = self.fleet_command_history_table.horizontalHeaderItem(5)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"FINISHED", None))
        self.fleet_command_result_panel_header.setText(QCoreApplication.translate("MainWindow", u"EXECUTION INSPECTOR", None))
        self.fleet_command_result_panel_caption.setText(QCoreApplication.translate("MainWindow", u"Select an execution from history to inspect its response.", None))
        self.fleet_command_result_metadata.setText(QCoreApplication.translate("MainWindow", u"No execution selected", None))
        self.fleet_command_result_status.setText(QCoreApplication.translate("MainWindow", u"STATUS  /  \u2014", None))
        self.fleet_command_result_duration.setText(QCoreApplication.translate("MainWindow", u"DURATION  /  \u2014", None))
        self.fleet_command_output_view.setPlaceholderText(QCoreApplication.translate("MainWindow", u"No stdout captured for the selected execution.", None))
        self.fleet_command_result_tabs.setTabText(self.fleet_command_result_tabs.indexOf(self.fleet_command_stdout_tab), QCoreApplication.translate("MainWindow", u"STDOUT", None))
        self.fleet_command_stderr_view.setPlaceholderText(QCoreApplication.translate("MainWindow", u"No stderr captured for the selected execution.", None))
        self.fleet_command_result_tabs.setTabText(self.fleet_command_result_tabs.indexOf(self.fleet_command_stderr_tab), QCoreApplication.translate("MainWindow", u"STDERR", None))
        self.fleet_command_copy_output_button.setText(QCoreApplication.translate("MainWindow", u"Copy output", None))
        self.fleet_logs_title.setText(QCoreApplication.translate("MainWindow", u"Activity & logs", None))
        self.fleet_logs_subtitle.setText(QCoreApplication.translate("MainWindow", u"Explore machine events, command execution records and operational history.", None))
        self.fleet_logs_refresh_button.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.fleet_logs_export_button.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.fleet_logs_filters_panel_header.setText(QCoreApplication.translate("MainWindow", u"Event filters", None))
        self.fleet_logs_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search events or command output", None))
        self.fleet_logs_agent_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"All agents", None))

        self.fleet_logs_level_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"All levels", None))
        self.fleet_logs_level_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Info", None))
        self.fleet_logs_level_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"Warning", None))
        self.fleet_logs_level_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"Error", None))
        self.fleet_logs_level_combo.setItemText(4, QCoreApplication.translate("MainWindow", u"Critical", None))

        self.fleet_logs_source_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"All sources", None))
        self.fleet_logs_source_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Agent", None))
        self.fleet_logs_source_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"Commands", None))
        self.fleet_logs_source_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"System", None))

        self.fleet_logs_table_panel_header.setText(QCoreApplication.translate("MainWindow", u"Event log", None))
        self.fleet_logs_table_panel_caption.setText(QCoreApplication.translate("MainWindow", u"Newest records appear first. Select an event to inspect details.", None))
        ___qtablewidgetitem73 = self.fleet_logs_table.horizontalHeaderItem(0)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"TIMESTAMP", None))
        ___qtablewidgetitem74 = self.fleet_logs_table.horizontalHeaderItem(1)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"AGENT", None))
        ___qtablewidgetitem75 = self.fleet_logs_table.horizontalHeaderItem(2)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"SOURCE", None))
        ___qtablewidgetitem76 = self.fleet_logs_table.horizontalHeaderItem(3)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"LEVEL", None))
        ___qtablewidgetitem77 = self.fleet_logs_table.horizontalHeaderItem(4)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"EVENT / MESSAGE", None))
        self.fleet_logs_details_panel_header.setText(QCoreApplication.translate("MainWindow", u"Event details", None))
        self.fleet_logs_event_metadata.setText(QCoreApplication.translate("MainWindow", u"No event selected", None))
        self.fleet_logs_details_view.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select a row to inspect full details.", None))
        self.fleet_logs_copy_button.setText(QCoreApplication.translate("MainWindow", u"Copy details", None))
        self.fleet_logs_clear_filters_button.setText(QCoreApplication.translate("MainWindow", u"Clear filters", None))
        self.prefs_title.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.prefs_subtitle.setText(QCoreApplication.translate("MainWindow", u"Configure local presentation and connectivity. Settings require application wiring.", None))
        self.preferences_connection_panel_header.setText(QCoreApplication.translate("MainWindow", u"CONNECTION", None))
        self.preferences_connection_panel_caption.setText(QCoreApplication.translate("MainWindow", u"Specify the API endpoint and the preferred UI refresh interval.", None))
        self.preferences_endpoint_label.setText(QCoreApplication.translate("MainWindow", u"BACKEND URL", None))
        self.preferences_endpoint_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"https://example.com/api/v1/", None))
        self.preferences_interval_label.setText(QCoreApplication.translate("MainWindow", u"REFRESH INTERVAL", None))
        self.preferences_refresh_interval_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"5 seconds", None))
        self.preferences_refresh_interval_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"10 seconds", None))
        self.preferences_refresh_interval_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"30 seconds", None))
        self.preferences_refresh_interval_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"60 seconds", None))

        self.preferences_save_button.setText(QCoreApplication.translate("MainWindow", u"Save preferences", None))
        self.about_title.setText(QCoreApplication.translate("MainWindow", u"About NexoraControl", None))
        self.about_subtitle.setText(QCoreApplication.translate("MainWindow", u"Distributed agent monitoring, remote operations and infrastructure observability.", None))
        self.about_identity_panel_header.setText(QCoreApplication.translate("MainWindow", u"NexoraControl / Desktop", None))
        self.about_identity_panel_caption.setText(QCoreApplication.translate("MainWindow", u"Agent-based infrastructure workspace", None))
        self.about_description.setText(QCoreApplication.translate("MainWindow", u"Manage connected machines, inspect hardware inventory, review performance, and track commands from a single desktop interface.", None))
        self.about_version_value.setText(QCoreApplication.translate("MainWindow", u"Version: provided by application", None))
        self.about_backend_value.setText(QCoreApplication.translate("MainWindow", u"Backend: Django REST Framework  /  PostgreSQL", None))
        self.about_client_value.setText(QCoreApplication.translate("MainWindow", u"Desktop: PySide6  /  Qt", None))
    # retranslateUi

