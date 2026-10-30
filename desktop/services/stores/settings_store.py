from PySide6.QtCore import QSettings

from services.app_settings import (
    APPLICATION_NAME,
    ORGANIZATION_NAME,
    DesktopPreferences,
    normalize_api_base_url,
)


class DesktopSettingsStore:
<<<<<<< HEAD
=======
    """Persist desktop preferences in the current user's local settings store."""

>>>>>>> refs/remotes/origin/main
    def __init__(self, settings: QSettings | None = None) -> None:
        self.qsettings = (
            settings
            if settings is not None
            else QSettings(ORGANIZATION_NAME, APPLICATION_NAME)
        )

    @staticmethod
    def defaults() -> DesktopPreferences:
        return DesktopPreferences()

    def load(self) -> DesktopPreferences:
        defaults = self.defaults()

        raw_url = self.qsettings.value(
            "connection/api_base_url", defaults.api_base_url, type=str
        )
        try:
            api_base_url = normalize_api_base_url(raw_url)
        except (TypeError, ValueError):
            api_base_url = defaults.api_base_url

        try:
            interval = int(
                self.qsettings.value(
                    "refresh/interval_seconds", defaults.refresh_interval_seconds
                )
            )
        except (TypeError, ValueError):
            interval = defaults.refresh_interval_seconds
        if not 1 <= interval <= 300:
            interval = defaults.refresh_interval_seconds

        try:
            timeout = int(
                self.qsettings.value(
                    "network/request_timeout_seconds",
                    defaults.request_timeout_seconds,
                )
            )
        except (TypeError, ValueError):
            timeout = defaults.request_timeout_seconds
        timeout = max(3, min(timeout, 120))

        return DesktopPreferences(
            api_base_url=api_base_url,
            auto_refresh_enabled=self.qsettings.value(
                "refresh/auto_enabled", defaults.auto_refresh_enabled, type=bool
            ),
            refresh_interval_seconds=interval,
            request_timeout_seconds=timeout,
            confirm_dangerous_commands=self.qsettings.value(
                "safety/confirm_dangerous_commands",
                defaults.confirm_dangerous_commands,
                type=bool,
            ),
            notify_failures=self.qsettings.value(
                "safety/notify_failures", defaults.notify_failures, type=bool
            ),
        )

    def save(self, preferences: DesktopPreferences) -> None:
        api_base_url = normalize_api_base_url(preferences.api_base_url)

        if not 1 <= int(preferences.refresh_interval_seconds) <= 300:
            raise ValueError("Refresh interval must be between 1 and 300 seconds.")
        if not 3 <= int(preferences.request_timeout_seconds) <= 120:
            raise ValueError("Request timeout must be between 3 and 120 seconds.")

        self.qsettings.setValue("connection/api_base_url", api_base_url)
        self.qsettings.setValue(
            "refresh/auto_enabled", bool(preferences.auto_refresh_enabled)
        )
        self.qsettings.setValue(
            "refresh/interval_seconds", int(preferences.refresh_interval_seconds)
        )
        self.qsettings.setValue(
            "network/request_timeout_seconds", int(preferences.request_timeout_seconds)
        )
        self.qsettings.setValue(
            "safety/confirm_dangerous_commands",
            bool(preferences.confirm_dangerous_commands),
        )
<<<<<<< HEAD
        self.qsettings.setValue(
            "safety/notify_failures", bool(preferences.notify_failures)
        )
=======
        self.qsettings.setValue("safety/notify_failures", bool(preferences.notify_failures))
>>>>>>> refs/remotes/origin/main
        self.qsettings.sync()

        if self.qsettings.status() != QSettings.Status.NoError:
            raise RuntimeError(
                "Could not persist settings to the local settings store."
            )

    def restore_defaults(self) -> DesktopPreferences:
        defaults = self.defaults()
        self.save(defaults)
        return defaults

    def bool_value(self, key: str, default: bool = True) -> bool:
        return self.qsettings.value(key, default, type=bool)
