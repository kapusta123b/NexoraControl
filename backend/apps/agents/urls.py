from django.urls import path

from apps.agents.api.views.agent import (
    AgentDetailView,
    AgentHeartbeatView,
    AgentListView,
)
from apps.agents.api.views.command import CommandBulkCreateView, CommandListView

app_name = "notes"

urlpatterns = [
    path("agents/", AgentListView.as_view(), name="agent-list"),
    path("agents/<int:pk>/", AgentDetailView.as_view(), name="agent-detail"),
    path(
        "agents/<int:pk>/heartbeat/",
        AgentHeartbeatView.as_view(),
        name="agent-detail-heartbeat",
    ),
    path(
        "agents/<int:pk>/commands/",
        CommandListView.as_view(),
        name="agent-commands",
    ),
    path(
        "agents/<int:pk>/commands/results/",
        CommandBulkCreateView.as_view(),
        name="agent-commands-results",
    ),
]
