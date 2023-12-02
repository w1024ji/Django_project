# chat/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Chat, ChatRoom
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


# def index(request):
#     return render(request, "chat/index.html")
#
#
# def room(request, room_name):
#     room = get_object_or_404(ChatRoom, name=room_name)
#
#     # 방에 속한 메시지 가져오기
#     messages = ChatMessage.objects.filter(room=room)
#
#     return render(request, "chat/room.html", {"room_name": room_name})

class Index(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'chat/index.html')


class Room(LoginRequiredMixin, View):
    def get(self, request, room_name):
        room = ChatRoom.objects.filter(name=room_name).first()
        chats = []

        if room:
            chats = Chat.objects.filter(room=room)
        else:
            room = ChatRoom(name=room_name)
            room.save()

        return render(request, 'chat/room.html', {'room_name': room_name, 'chats': chats})