import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class Agent(models.Model):
    class Status(models.TextChoices):
        OFFLINE = "OFF", _("Offline")
        ONLINE = "ON", _("Online")

    name = models.CharField(max_length=100, default="Server")
    hostname = models.CharField(max_length=100)
    ip = models.GenericIPAddressField(null=True, blank=True)
    os = models.CharField(max_length=30, null=True, blank=True)

    cpu_load = models.PositiveSmallIntegerField(null=True, blank=True)
    ram_load = models.PositiveSmallIntegerField(null=True, blank=True)

    status = models.CharField(
        max_length=3, choices=Status.choices, default=Status.OFFLINE
    )

    last_seen = models.DateTimeField(null=True, blank=True)
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def is_authenticated(self):
        return True

    def __str__(self):
        return f"{self.name} ({self.hostname})"
