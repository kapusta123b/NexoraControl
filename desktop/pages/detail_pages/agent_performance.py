from api.client import NexoraClient

from .performance_pages.storage_page import PerformanceStoragePage
from .performance_pages.compute_page import PerformanceComputePage

from services.pollers.metrics_poller import AgentMetricPoller
from services.stores.metric_store import MetricStore

from ui.main_window import Ui_MainWindow

from PySide6.QtWidgets import QButtonGroup

from PySide6.QtCore import QObject


class DetailPerformanceController(QObject):

    def __init__(self, ui: Ui_MainWindow, client: NexoraClient):
        super().__init__()
        self.ui = ui
        self.client = client

        self.agent = {}

        self.current_page = None

        self.performance_store = MetricStore()
        self.performance_poller = AgentMetricPoller(self.client, self.performance_store)

        self.setup_connections()
        self.setup_pages()

    def setup_pages(self):
        self.compute_page = PerformanceComputePage(self.ui, self.performance_store)
        self.storage_page = PerformanceStoragePage(self.ui, self.performance_store)

    def setup_connections(self) -> None:
        self.performance_nav_group = QButtonGroup(self)
        self.performance_nav_group.setExclusive(True)

        self.nav_mapping = {
            self.ui.compute_button: (self.ui.compute_page, "resources"),
            self.ui.storage_button: (self.ui.storage_page, "storage"),
            self.ui.thermals_button: (self.ui.thermals_page, "thermals"),
            self.ui.network_button: (self.ui.network_page, "network"),
        }

        for button, metric_type in self.nav_mapping.items():
            self.performance_nav_group.addButton(button)

            button.clicked.connect(self.on_nav_button_clicked)

    def on_nav_button_clicked(self) -> None:
        clicked_button = self.sender()

        if clicked_button not in self.nav_mapping:
            return

        page_widget, metric_type = self.nav_mapping[clicked_button]

        if not self.current_page or self.current_page != clicked_button:
            self.current_page = clicked_button

            self.performance_poller.stop_polling()

            self.performance_poller.on_clicked(metric_type=metric_type)
            self.ui.performance_stacked_content.setCurrentWidget(page_widget)

    def activate(self) -> None:
        if self.agent:
            self.performance_poller.on_clicked(self.agent.get("id"))
