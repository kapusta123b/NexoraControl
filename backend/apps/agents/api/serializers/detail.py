from rest_framework.serializers import ModelSerializer

from apps.agents.models.metric import AgentMetric
from apps.agents.models.agent import Agent


class AgentDetailSerializer(ModelSerializer):
    class Meta:
        model = Agent

        fields = [
            "id",
            "name",
            "hostname",
            "ip",
            "os",
            "cpu_load",
            "ram_load",
            "last_seen",
            "status",
        ]

        read_only_fields = [
            "id",
            "ip",
            "os",
            "last_seen",
            "created_at",
            "ram_load",
            "cpu_load",
            "disc_load",
            "status",
        ]


class AgentHeartbeatSerializer(ModelSerializer):
    class Meta:
        model = AgentMetric

        fields = [
            "cpu_metrics",
            "memory_metrics",
            "storage_metrics",
            "network_metrics",
            "thermal_metrics",
            "gpu_metrics",
        ]
