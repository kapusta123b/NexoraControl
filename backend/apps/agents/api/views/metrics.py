from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.agents.selectors.metrics import (
    get_resource_metrics,
    get_storage_metrics,
    get_thermal_metrics,
)


class AgentResourceMetricHistoryView(APIView):
    def get(self, request, pk):
        resource_metrics = get_resource_metrics(request, pk)

        return Response(resource_metrics, status=status.HTTP_200_OK)


class AgentStorageMetricHistoryView(APIView):
    def get(self, request, pk):
        storage_metrics = get_storage_metrics(request, pk)

        return Response(storage_metrics, status=status.HTTP_200_OK)


class AgentThermalMetricHistoryView(APIView):
    def get(self, request, pk):
        thermal_metrics = get_thermal_metrics(request, pk)

        return Response(thermal_metrics, status=status.HTTP_200_OK)
