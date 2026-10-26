from rest_framework import serializers

from apps.agents.models.metric import AgentMetric
from apps.agents.models.agent import Agent
from apps.agents.models.agent_information import AgentSystemInfo


class AgentDetailSerializer(serializers.ModelSerializer):
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


class AgentHeartbeatSerializer(serializers.ModelSerializer):
    uptime = serializers.FloatField()

    class Meta:
        model = AgentMetric

        fields = [
            "cpu_metrics",
            "memory_metrics",
            "storage_metrics",
            "network_metrics",
            "thermal_metrics",
            "gpu_metrics",
            "uptime",
        ]


class AgentSystemInfoSerializer(serializers.ModelSerializer):

    agent_id = serializers.CharField(source="agent.id", read_only=True)

    class Meta:
        model = AgentSystemInfo

        fields = [
            "agent_id",
            "cpu_info",
            "gpu_info",
            "memory_info",
            "motherboard_bios_info",
            "storage_info",
            "network_info",
        ]

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")

        if request and request.method == "GET":
            target = request.query_params.get("target_info")

            if target:
                if target not in fields:
                    raise serializers.ValidationError(
                        {"target_info": "Invalid hardware category."}
                    )

                return {target: fields[target]}

        return fields
