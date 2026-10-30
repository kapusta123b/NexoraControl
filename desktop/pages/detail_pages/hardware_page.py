from PySide6.QtCore import QObject

from api.client import NexoraClient

from services.utils.widgets_utils import (
    apply_style_for_tables,
    setup_table,
)

from services.stores.agent_store import AgentHardwareInfoStore

from services.pollers.hardware_poller import HardwarePoller

from ui.main_window import Ui_MainWindow


class DetailHardwareController(QObject):
    def __init__(self, ui: Ui_MainWindow, client: NexoraClient):
        super().__init__()

        self.ui = ui
        self.client = client

        self.hardware_store = AgentHardwareInfoStore()
        self.hardware_poller = HardwarePoller(self.client, self.hardware_store)

        self.agent = {}

        self._connect_signals()
        self._setup_style()

    def _connect_signals(self):
        self.hardware_store.system_info_changed.connect(self.table_manager)

        self.ui.hardware_refresh_inventory_button.clicked.connect(
            lambda: self.hardware_poller.refresh(force=True)
        )

    def _setup_style(self):
        tables = (
            self.ui.hardware_cpu_specifications_table,
            self.ui.hardware_gpu_inventory_table,
            self.ui.hardware_ram_modules_table,
            self.ui.hardware_bios_motherboard_table,
            self.ui.hardware_storage_devices_table,
            self.ui.hardware_network_adapters_table,
        )

        apply_style_for_tables(tables)

    def table_manager(self, system_info: dict[str, dict | list[dict] | str]):
        if not system_info:
            return

        setup_table(
            self.ui.hardware_cpu_specifications_table,
            system_info.get("cpu_info"),
            (
                "model",
                "architecture",
                "physical_cores",
                "logical_threads",
                "frequency",
                "l1_cache",
                "l2_cache",
                "l3_cache",
            ),
        )
        setup_table(
            self.ui.hardware_gpu_inventory_table,
            system_info.get("gpu_info"),
            ("device", "model", "vram", "driver_version", "interface"),
        )
        setup_table(
            self.ui.hardware_ram_modules_table,
            system_info.get("memory_info"),
            ("slot", "capacity"),
        )
        setup_table(
            self.ui.hardware_bios_motherboard_table,
            system_info.get("motherboard_bios_info"),
            (
                "board_vendor",
                "board_model",
                "bios_vendor",
                "bios_version",
                "release_date",
            ),
        )
        setup_table(
            self.ui.hardware_storage_devices_table,
            system_info.get("storage_info"),
            ("device", "model", "capacity", "interface"),
        )
        setup_table(
            self.ui.hardware_network_adapters_table,
            system_info.get("network_info"),
            ("interface", "model", "mac_adresses", "link_type", "status"),
        )

    def activate(self) -> None:
        if self.agent:
            self.hardware_poller.on_clicked(self.agent["id"])
