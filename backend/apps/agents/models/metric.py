from django.db import models


class AgentMetricQuerySet(models.QuerySet):

    def by_date(self, from_date):
        if from_date:
            return self.filter(created_at__gte=from_date)

        return self


class AgentMetric(models.Model):

    objects = AgentMetricQuerySet.as_manager()

    agent = models.ForeignKey(
        "agents.Agent", related_name="metrics", on_delete=models.CASCADE
    )

    cpu_load = models.PositiveSmallIntegerField(null=True)

    ram_load = models.PositiveSmallIntegerField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = "Metric"

        indexes = [
            models.Index(fields=["agent", "-created_at"]),
        ]
