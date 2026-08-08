from django.contrib import admin

from apps.agents.models.agent import Agent
from apps.agents.models.command import Command




admin.site.register(Agent)
admin.site.register(Command)
