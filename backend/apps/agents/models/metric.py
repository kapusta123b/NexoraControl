from django.db import models


class AgentMetricQuerySet(models.QuerySet):

    def by_date(self, from_date):
        if from_date:
            return self.filter(created_at__gte=from_date)

        return self


class AgentMetric(models.Model):
    objects = AgentMetricQuerySet.as_manager()

    agent = models.ForeignKey(
        "agents.Agent",
        related_name="metrics",
        on_delete=models.CASCADE,
    )

    # CPU
    cpu_load = models.FloatField(
        null=True,
        blank=True,
    )

    #                   core1 core2 core3
    # cpu cores load -> [25.2, 65.3,  48.6]
    cpu_load_per_core = models.JSONField(
        default=list,
        blank=True,
    )

    # cpu load average per 1m, 5m, 15m -> [1, 2.3, 3.8]
    load_average = models.JSONField(
        default=list,
        blank=True
    )

    # Memory
    ram_load = models.FloatField(
        null=True,
        blank=True,
    )

    ram_used_bytes = models.BigIntegerField(
        null=True,
        blank=True,
    )

    ram_available_bytes = models.BigIntegerField(
        null=True,
        blank=True,
    )

    swap_used_bytes = models.BigIntegerField(
        null=True,
        blank=True,
    )

    swap_available_bytes = models.BigIntegerField(
        null=True,
        blank=True,
    )

    # Storage
    disk_usage = models.FloatField(
        null=True,
        blank=True,
    )

    disk_read_bytes = models.BigIntegerField(
        null=True,
        blank=True,
    )

    disk_write_bytes = models.BigIntegerField(
        null=True,
        blank=True,
    )

    # Network
    network_rx_bytes = models.BigIntegerField(
        null=True,
        blank=True,
    )

    network_tx_bytes = models.BigIntegerField(
        null=True,
        blank=True,
    )

    network_rx_packets = models.BigIntegerField(
        null=True,
        blank=True,
    )

    network_tx_packets = models.BigIntegerField(
        null=True,
        blank=True,
    )

    network_errors = models.BigIntegerField(
        null=True,
        blank=True,
    )

    network_drops = models.BigIntegerField(
        null=True,
        blank=True,
    )

    # Thermals
    temperatures = models.JSONField(
        default=dict,
        blank=True,
    )

    # GPU
    gpu_load = models.FloatField(
        null=True,
        blank=True,
    )

    gpu_memory_used_bytes = models.BigIntegerField(
        null=True,
        blank=True,
    )

    gpu_memory_total_bytes = models.BigIntegerField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "Metric"
        verbose_name_plural = "Metrics"

        indexes = [
            models.Index(
                fields=["agent", "-created_at"],
            ),
        ]
