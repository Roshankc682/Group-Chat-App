import os
from django.urls import path
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'group_chat_app.settings')
from group_chat_app.consumers import *
from channels.auth import AuthMiddlewareStack
application = get_asgi_application()

ws_patterns = [
    path('ws/message_recieve/',MessageChannel),
    
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(ws_patterns)
})
