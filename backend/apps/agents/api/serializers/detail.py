from apps.agents.models.metric import AgentMetric

from rest_framework.serializers import ModelSerializer

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
            # CPU
            "cpu_load",
            "cpu_load_per_core",
            "load_average",
            
            # MEMORY
            "ram_load",
            "ram_used_bytes",
            "ram_available_bytes",
            "swap_used_bytes",
            "swap_available_bytes",
        ]
