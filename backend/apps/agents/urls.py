from django.urls import path

from apps.agents.api.views.agent import (
    AgentDetailView,
    AgentHeartbeatView,
    AgentListView,
)
from apps.agents.api.views.commands import (
    CommandBulkUpdateView,
    CommandListView,
    CommandPendingListView,
)
from apps.agents.api.views.metrics import (
    AgentResourceMetricHistoryView,
    AgentStorageMetricHistoryView,
    AgentThermalMetricHistoryView,
)

app_name = "agents"

url_metrics = [
    path(
        "agents/<int:pk>/metrics/resource/",
        AgentResourceMetricHistoryView.as_view(),
        name="agent-metrics-resource-history",
    ),
    path(
        "agents/<int:pk>/metrics/storage/",
        AgentStorageMetricHistoryView.as_view(),
        name="agent-metrics-storage-history",
    ),
    path(
        "agents/<int:pk>/metrics/thermal/",
        AgentThermalMetricHistoryView.as_view(),
        name="agent-metrics-thermal-history",
    ),
]

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
        "agents/<int:pk>/commands/pending/",
        CommandPendingListView.as_view(),
        name="agent-commands-pending",
    ),
    path(
        "agents/<int:pk>/commands/results/",
        CommandBulkUpdateView.as_view(),
        name="agent-commands-results",
    ),
] + url_metrics
