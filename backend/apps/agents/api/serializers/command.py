from rest_framework import serializers

from apps.agents.models.command import Command


class CommandListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Command

        fields = [
            "id",
            "command_type",
            "payload",
            "output",
            "status",
            "created_at",
            "started_at",
            "finished_at",
        ]

        read_only_fields = [
            "id",
            "status",
            "created_at",
            "output",
            "started_at",
            "finished_at",
        ]


class CommandPendingListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Command

        fields = [
            "id",
            "command_type",
            "payload",
        ]


class CommandPatchSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField()

    finished_at = serializers.DateTimeField()

    class Meta:

        model = Command

        fields = ["id", "status", "output", "finished_at"]
