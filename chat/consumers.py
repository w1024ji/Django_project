
import json

from channels.generic.websocket import AsyncWebsocketConsumer

from channels.db import database_sync_to_async
from .models import ChatMessage
from django.utils import timezone




class ChatConsumer(AsyncWebsocketConsumer):
    #db_create
    @database_sync_to_async
    def get_previous_messages(self):
        return list(ChatMessage.objects.filter(room_name=self.room_name).values('message'))

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        # Accept the WebSocket connection
        await self.accept()

        #db_create
        previous_messages = await self.get_previous_messages()
        for message in previous_messages:
            await self.send(
                text_data=json.dumps({"message": f"{message['message']}"}))




    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

   # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
     #   message_style = text_data_json.get("style", "")  # 추가된 부분

        # Send message to room group
        # await self.channel_layer.group_send(
        #     self.room_group_name, {"type": "chat.message", "message": message, "style": message_style}
        # )

        #db_create
        # Save the message to the database
        await self.save_message_to_database(message)



        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message, "timestamp": timezone.now().isoformat()}
    #        self.room_group_name, {"type": "chat.message", "message": message}
        )

    @database_sync_to_async
    def save_message_to_database(self, message):
        ChatMessage.objects.create(room_name=self.room_name, message=message)



    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        # Send message to WebSocket with HTML tags
        await self.send(text_data=json.dumps({
            "message": message,
        }))



