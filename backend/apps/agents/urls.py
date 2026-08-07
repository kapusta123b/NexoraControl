from django.urls import path

from apps.agents.api.views import agent

app_name = 'notes'

urlpatterns = [
    path('agents', agent.AgentListView.as_view(), name='agents-list'),
    path('agents/<int:pk>', agent.AgentDetailView.as_view(), name='agent-detail'),
    path('agents/<int:pk>/heartbeat', agent.AgentHeartbeatView.as_view(), name='agent-detail-heartbeat')
]
