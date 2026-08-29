from django.contrib import admin

from apps.agents.models.agent import Agent
from apps.agents.models.command import Command
from apps.agents.models.metric import AgentMetric




admin.site.register(Agent)
admin.site.register(Command)
admin.site.register(AgentMetric)

