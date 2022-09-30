from django.urls import re_path
from . import consumers

#Move to products
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatRoomConsumer.as_asgi()),
    re_path(r'ws/main/(?P<room_name>\w+)/$', consumers.ChatRoomConsumer.as_asgi()),
]