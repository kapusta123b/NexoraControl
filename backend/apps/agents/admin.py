from django.contrib import admin

from apps.agents.models.agent import Agent
from apps.agents.models.command import Command
from apps.agents.models.metric import AgentMetric
from apps.agents.models.agent_information import AgentSystemInfo

admin.site.register(Agent)
admin.site.register(Command)
admin.site.register(AgentMetric)
admin.site.register(AgentSystemInfo)
