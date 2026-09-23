from django.db import models


class AgentMetricQuerySet(models.QuerySet):

    def by_date(self, from_date):
        if from_date:
            return self.filter(created_at__gte=from_date)

        return self


class AgentMetric(models.Model):
    agent = models.ForeignKey(
        "agents.Agent",
        related_name="metrics",
        on_delete=models.CASCADE,
    )

    cpu_metrics = models.JSONField(
        default=dict,
        blank=True,
    )

    memory_metrics = models.JSONField(
        default=dict,
        blank=True,
    )

    storage_metrics = models.JSONField(
        default=dict,
        blank=True,
    )

    network_metrics = models.JSONField(
        default=dict,
        blank=True,
    )

    thermal_metrics = models.JSONField(
        default=dict,
        blank=True,
    )

    gpu_metrics = models.JSONField(
        default=dict,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["agent", "-created_at"]),
        ]
