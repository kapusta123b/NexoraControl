from django.db import models
from django.utils.translation import gettext_lazy as _


class Command(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING"
        RUNNING = "RUNNING"
        SUCCESS = "SUCCESS"
        FAILED = "FAILED"

    agent = models.ForeignKey(
        "agents.Agent", on_delete=models.CASCADE, related_name="commands"
    )

    command_type = models.CharField(max_length=50)

    payload = models.JSONField(default=dict)

    output = models.TextField(null=True, max_length=10000)

    errors = models.JSONField(default=dict)

    status = models.CharField(choices=Status.choices, default=Status.PENDING)

    started_at = models.DateTimeField(null=True)

    finished_at = models.DateTimeField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
