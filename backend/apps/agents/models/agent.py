import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Agent(models.Model):
    class Status(models.TextChoices):
        OFFLINE = "OFF", _("Offline")
        ONLINE = "ON", _("Online")

    name = models.CharField(default="Server")

    hostname = models.CharField(max_length=100)

    cpu_load = models.PositiveSmallIntegerField(null=True)

    ram_load = models.PositiveSmallIntegerField(null=True)

    disc_load = models.PositiveSmallIntegerField(null=True)

    status = models.CharField(choices=Status.choices, default=Status.OFFLINE)

    last_seen = models.DateTimeField(
        null=True,
        blank=True,
    )

    token = models.UUIDField(default=uuid.uuid4, unique=True)

    