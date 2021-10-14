from django.urls import re_path
from . import consumers


websocket_urlpatterns = [
    #Path that helps us give our chatrooms any name 
    #Docs for more info: https://docs.djangoproject.com/en/3.2/ref/urls/#re-path
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatRoomConsumer.as_asgi()),
]