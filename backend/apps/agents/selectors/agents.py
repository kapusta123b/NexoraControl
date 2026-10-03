from django.db import transaction
from apps.agents.models import Agent


def register_new_agent(validated_data: dict) -> tuple[int, str]:
    with transaction.atomic():
        agent = Agent.objects.create(**validated_data)

    return agent.id, str(agent.token)


