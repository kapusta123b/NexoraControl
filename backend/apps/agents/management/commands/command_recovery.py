from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db import transaction

from apps.agents.models.agent import Agent
from apps.agents.models.command import Command as AgentCommand


class Command(BaseCommand):
    def handle(self, *args, **options):

        with transaction.atomic():
            threshold = timezone.now() - timedelta(seconds=30)

            agents = Agent.objects.filter(
                status=Agent.Status.OFFLINE, last_seen__gte=threshold
            )

            updated_count = 0
            for agent in agents:
                res = AgentCommand.objects.filter(
                    agent=agent, status=AgentCommand.Status.RUNNING
                ).update(
                    status=AgentCommand.Status.FAILED,
                    output="Agent connection lost during command execution.",
                )
                updated_count += res

        self.stdout.write(
            self.style.SUCCESS(f"Command success recovery count: {updated_count}")
        )
