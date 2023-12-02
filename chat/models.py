from django.db import models
from django.contrib.auth.models import User


class ChatRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)  # 예시로 'name'을 사용

class Chat(models.Model):
#    room_name = models.CharField(max_length=255, null=True, blank=True)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)  # 이제 room이 외래 키로 참조함
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # User 모델과의 연결
#    style = models.TextField(default="")

    # def __str__(self):
    #     return f'{self.user.username}: {self.message}'

