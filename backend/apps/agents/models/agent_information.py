from django.db import models


class AgentSystemInfo(models.Model):

    agent = models.OneToOneField(
        "agents.Agent", related_name="system_info", on_delete=models.CASCADE
    )

    cpu_info = models.JSONField(
        default=dict,
        blank=True,
    )

    gpu_info = models.JSONField(
        default=dict,
        blank=True,
    )

    memory_info = models.JSONField(
        default=dict,
        blank=True,
    )

    motherboard_bios_info = models.JSONField(
        default=dict,
        blank=True,
    )

    storage_info = models.JSONField(
        default=dict,
        blank=True,
    )

    network_info = models.JSONField(
        default=dict,
        blank=True,
    )
