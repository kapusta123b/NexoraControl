from datetime import timedelta
import time

from django.utils import timezone

from apps.agents.models.agent import Agent


def check_agents():
    threshold = timezone.now() - timedelta(seconds=30)

    Agent.objects.filter(
        status=Agent.Status.ONLINE,
        last_seen__lt=threshold,
    ).update(status=Agent.Status.OFFLINE)


while True:
    check_agents()
    time.sleep(15)