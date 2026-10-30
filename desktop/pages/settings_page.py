from __future__ import annotations

from PySide6.QtCore import QObject, QThread, Slot

from api.client import NexoraClient

from services.app_settings import DesktopPreferences, normalize_api_base_url
from services.stores.settings_store import DesktopSettingsStore
from services.workers.connection_worker import ConnectionTestWorker

from ui.main_window import Ui_MainWindow

from version import APP_VERSION


class SettingsController(QObject):
    """Loads, validates, persists, and applies desktop settings."""

    def __init__(
        self,
        ui: Ui_MainWindow,
        client: NexoraClient,
        agents_poller=None,
        settings_store: DesktopSettingsStore | None = None,
        parent: QObject | None = None,
    ) -> None:
        super().__init__(parent)

        self.ui = ui
        self.client = client
        self.agents_poller = agents_poller
        self.settings_store = settings_store or DesktopSettingsStore()

        self._connection_thread: QThread | None = None
        self._connection_worker: ConnectionTestWorker | None = None
        self._testing_base_url: str | None = None

        self._prepare_interval_options()
        self.load_settings()
        self._connect_signals()

    def _prepare_interval_options(self) -> None:
        combo = self.ui.preferences_refresh_interval_combo
        if combo.count() == 0:
            for seconds in (5, 10, 30, 60):
                combo.addItem(f"{seconds} seconds", seconds)
            return

        for index in range(combo.count()):
            if combo.itemData(index) is not None:
                continue
            text = combo.itemText(index)
            digits = "".join(char for char in text if char.isdigit())
            if digits:
                combo.setItemData(index, int(digits))

    def _connect_signals(self) -> None:
        self.ui.preferences_test_connection_button.clicked.connect(self.test_connection)
        self.ui.preferences_save_button.clicked.connect(self.save_settings)
        self.ui.preferences_reset_button.clicked.connect(self.restore_defaults)

        self.ui.preferences_endpoint_edit.textChanged.connect(
            self._mark_connection_untested
        )
        self.ui.preferences_endpoint_edit.textChanged.connect(self._mark_unsaved)
        self.ui.preferences_auto_refresh_checkbox.toggled.connect(self._mark_unsaved)
        self.ui.preferences_refresh_interval_combo.currentIndexChanged.connect(
            self._mark_unsaved
        )
        self.ui.preferences_request_timeout_spin.valueChanged.connect(
            self._mark_unsaved
        )
        self.ui.preferences_confirm_dangerous_checkbox.toggled.connect(
            self._mark_unsaved
        )
        self.ui.preferences_notify_failures_checkbox.toggled.connect(self._mark_unsaved)

    def load_settings(self) -> None:
        preferences = self.settings_store.load()

        self.ui.preferences_endpoint_edit.setText(preferences.api_base_url)

        self.ui.preferences_auto_refresh_checkbox.setChecked(
            preferences.auto_refresh_enabled
        )
        self.ui.preferences_request_timeout_spin.setValue(
            preferences.request_timeout_seconds
        )
        self.ui.preferences_confirm_dangerous_checkbox.setChecked(
            preferences.confirm_dangerous_commands
        )
        self.ui.preferences_notify_failures_checkbox.setChecked(
            preferences.notify_failures
        )
        self._select_refresh_interval(preferences.refresh_interval_seconds)
        self.ui.preferences_app_version_value.setText(
            f"NexoraControl Desktop · v{APP_VERSION}"
        )

        self._apply_preferences(preferences)
        self._set_connection_status(
            "neutral", "NOT TESTED", "Run Test connection to check this endpoint."
        )
        self._set_save_status("Settings loaded from this device.", "neutral")

    def _select_refresh_interval(self, seconds: int) -> None:
        combo = self.ui.preferences_refresh_interval_combo
        index = combo.findData(seconds)
        if index < 0:
            combo.addItem(f"{seconds} seconds", seconds)
            index = combo.findData(seconds)
        combo.setCurrentIndex(index)

    def _read_form(self) -> DesktopPreferences:
        api_url = normalize_api_base_url(self.ui.preferences_endpoint_edit.text())
        interval_data = self.ui.preferences_refresh_interval_combo.currentData()
        if interval_data is None:
            raise ValueError("Choose a dashboard refresh interval.")

        return DesktopPreferences(
            api_base_url=api_url,
            auto_refresh_enabled=self.ui.preferences_auto_refresh_checkbox.isChecked(),
            refresh_interval_seconds=int(interval_data),
            request_timeout_seconds=self.ui.preferences_request_timeout_spin.value(),
            confirm_dangerous_commands=self.ui.preferences_confirm_dangerous_checkbox.isChecked(),
            notify_failures=self.ui.preferences_notify_failures_checkbox.isChecked(),
        )

    def save_settings(self) -> None:
        try:
            preferences = self._read_form()
            self.settings_store.save(preferences)
        except (ValueError, RuntimeError) as exc:
            self._set_save_status(f"Could not save settings: {exc}", "error")
            return

        # Show the canonical URL saved by the store and apply it to the live app.
        self.ui.preferences_endpoint_edit.setText(preferences.api_base_url)
        self._apply_preferences(preferences)
        self._set_save_status("Settings saved and applied.", "saved")

    def restore_defaults(self) -> None:
        try:
            defaults = self.settings_store.restore_defaults()
        except (ValueError, RuntimeError) as exc:
            self._set_save_status(f"Could not restore defaults: {exc}", "error")
            return

        self.ui.preferences_endpoint_edit.setText(defaults.api_base_url)
        self.ui.preferences_auto_refresh_checkbox.setChecked(
            defaults.auto_refresh_enabled
        )
        self._select_refresh_interval(defaults.refresh_interval_seconds)
        self.ui.preferences_request_timeout_spin.setValue(
            defaults.request_timeout_seconds
        )
        self.ui.preferences_confirm_dangerous_checkbox.setChecked(
            defaults.confirm_dangerous_commands
        )
        self.ui.preferences_notify_failures_checkbox.setChecked(
            defaults.notify_failures
        )

        self._apply_preferences(defaults)
        self._set_save_status("Default settings restored and saved.", "saved")
        self._set_connection_status(
            "neutral", "NOT TESTED", "Run Test connection to check this endpoint."
        )

    def _apply_preferences(self, preferences: DesktopPreferences) -> None:
        # NexoraClient is shared by the pages, workers and pollers.
        self.client.base_url = preferences.api_base_url
        self.client.timeout_seconds = float(preferences.request_timeout_seconds)
        self.client.confirm_dangerous_commands = preferences.confirm_dangerous_commands
        self.client.notify_failures = preferences.notify_failures

        timer = getattr(self.agents_poller, "timer", None)
        if timer is None:
            return

        timer.setInterval(preferences.refresh_interval_seconds * 1000)
        if preferences.auto_refresh_enabled:
            if not timer.isActive():
                timer.start()
        elif timer.isActive():
            timer.stop()

    def test_connection(self) -> None:
        if self._connection_thread is not None:
            return

        try:
            base_url = normalize_api_base_url(self.ui.preferences_endpoint_edit.text())
        except ValueError as exc:
            self._set_connection_status("error", "INVALID URL", str(exc))
            return

        self._testing_base_url = base_url
        timeout = self.ui.preferences_request_timeout_spin.value()
        self.ui.preferences_test_connection_button.setEnabled(False)
        self._set_connection_status(
            "testing", "TESTING...", f"Checking {base_url}agents/"
        )

        worker = ConnectionTestWorker(
            base_url=base_url,
            timeout_seconds=timeout,
        )
        thread = QThread(self)
        worker.moveToThread(thread)
        thread.started.connect(worker.run)
        worker.result.connect(self._on_connection_test_result)
        worker.finished.connect(thread.quit)
        worker.finished.connect(worker.deleteLater)
        thread.finished.connect(self._on_connection_thread_finished)
        thread.finished.connect(thread.deleteLater)

        self._connection_worker = worker
        self._connection_thread = thread
        thread.start()

    def _on_connection_test_result(
        self, state: str, status_text: str, details: str
    ) -> None:
        # Ignore a result for a URL that the user has already changed.
        try:
            current_url = normalize_api_base_url(
                self.ui.preferences_endpoint_edit.text()
            )
        except ValueError:
            return

        if current_url != self._testing_base_url:
            return

        self._set_connection_status(state, status_text, details)

    @Slot()
    def _on_connection_thread_finished(self) -> None:
        self._connection_thread = None
        self._connection_worker = None
        self._testing_base_url = None
        self.ui.preferences_test_connection_button.setEnabled(True)

    def _mark_connection_untested(self, _text: str) -> None:
        self._set_connection_status(
            "neutral",
            "NOT TESTED",
            "The API URL changed. Test the new URL before relying on it.",
        )

    def _mark_unsaved(self, *_args) -> None:
        self._set_save_status("Unsaved changes.", "dirty")

    def _set_save_status(self, text: str, state: str) -> None:
        label = self.ui.preferences_save_status_label
        label.setText(text)
        label.setProperty("saveState", state)
        self._repolish(label)

    def _set_connection_status(self, state: str, label: str, details: str) -> None:
        status = self.ui.preferences_connection_status_label
        status.setText(label)
        status.setToolTip(details)
        status.setProperty("connectionState", state)
        self._repolish(status)

    @staticmethod
    def _repolish(widget) -> None:
        widget.style().unpolish(widget)
        widget.style().polish(widget)
        widget.update()
