from rest_framework.serializers import ModelSerializer

from apps.agents.models.agent import Agent


class AgentDetailSerializer(ModelSerializer):
    class Meta:
        model = Agent

        fields = [
            "id",
            "name",
            "hostname",
            "cpu_load",
            "ram_load",
            "disc_load",
            "last_seen",
            "status",
        ]

        read_only_fields = [
            "id",
            "last_seen",
            "created_at",
            "cpu_load",
            "ram_load",
            "disc_load",
            "status",
        ]


class AgentHeartbeatSerializer(ModelSerializer):
    class Meta:
        model = Agent

        fields = [
            "cpu_load",
            "ram_load",
            "disc_load",
        ]
