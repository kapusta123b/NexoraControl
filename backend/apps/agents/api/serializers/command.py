from rest_framework import serializers

from apps.agents.models.command import Command


class CommandListSerializer(serializers.ModelSerializer):

    output = serializers.ReadOnlyField()

    class Meta:
        model = Command

        fields = [
            "id",
            "command_type",
            "payload",
            "output",
            "status",
            "created_at",
        ]

        read_only_fields = ["id", "status", "created_at"]


class CommandPatchSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField()

    class Meta:

        model = Command

        fields = ["id", "status", "output"]
