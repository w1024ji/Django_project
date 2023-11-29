from django.db import models


class ChatMessage(models.Model):
    room_name = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
#    style = models.TextField(default="")