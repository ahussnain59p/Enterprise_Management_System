# chatapp/routing.py
# from django.urls import re_path
# from . import consumers

# websocket_urlpatterns = [
    # re_path(r'ws/chat/(?P<room_id>\d+)/$', consumers.ChatConsumer.as_asgi()),
# ]
from django.urls import path , include
from .consumers import ChatConsumer

# Here, "" is routing to the URL ChatConsumer which 
# will handle the chat functionality.
websocket_urlpatterns = [
    path("ws/chat/<room_id>" , ChatConsumer.as_asgi()), 
] 
