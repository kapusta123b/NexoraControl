import json

from channels.generic.websocket import AsyncWebsocketConsumer

class MonitoringConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.agent_id = self.scope['url_route']['kwargs']['agent_id']
        self.group_name = f"agent_{self.agent_id}"

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def send_agent_metrics(self, event):
        metrics_data = event['metrics']
        
        await self.send(text_data=json.dumps(metrics_data))