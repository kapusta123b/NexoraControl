import uuid
from rest_framework import authentication, exceptions
from apps.agents.models import Agent

class AgentTokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization", "")
        
        if not auth_header.startswith("Bearer "):
            return None

        raw_token = auth_header.split(" ")[1].strip()

        try:
            token_uuid = uuid.UUID(raw_token)

        except ValueError:
            raise exceptions.AuthenticationFailed("Invalid token format (UUID required)")

        agent = Agent.objects.filter(token=token_uuid).first()

        if not agent:
            raise exceptions.AuthenticationFailed("Invalid or unknown agent token")

        return (agent, None)