from rest_framework.serializers import ModelSerializer

from apps.agents.models.agent import Agent


class AgentListCreateSerializer(ModelSerializer):

    class Meta:
        model = Agent
        fields = [
            "id",
            "name",
            "hostname",
            "ram_load",
            "cpu_load",
            "status",
            "last_seen",
        ]

        read_only_fields = [
            "id",
            "last_seen",
            "created_at",
            "ram_load",
            "cpu_load",
            "status",
        ]