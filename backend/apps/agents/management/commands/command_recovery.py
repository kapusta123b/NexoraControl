from datetime import timedelta

from django.utils import timezone

from django.db import transaction

from apps.agents.models.agent import Agent
from apps.agents.models.command import Command


@transaction.atomic
def recover_commands():

    threshold = timezone.now() - timedelta(seconds=30)

    agents = Agent.objects.filter(status=Agent.Status.OFFLINE, last_seen__gte=threshold)

    for agent in agents:
        Command.objects.filter(agent=agent, status=Command.Status.RUNNING).update(
            status=Command.Status.FAILED,
            output="Agent connection lost during command execution.",
        )