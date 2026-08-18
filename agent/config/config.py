from decouple import config

from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    api_url: str
    agent_id: int
    token: str
    heartbeat_interval: int = 5
    command_interval: int = 2


def load_settings() -> Settings:
    return Settings(
        api_url=config("NEXORA_API_URL"),
        agent_id=config("NEXORA_AGENT_ID", cast=int),
        token=config("NEXORA_TOKEN"),
        heartbeat_interval=config(
            "NEXORA_HEARTBEAT_INTERVAL",
            cast=int,
        ),
        command_interval=config(
            "NEXORA_COMMAND_INTERVAL",
            cast=int,
        ),
    )
