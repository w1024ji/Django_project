
import json

from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from channels.db import database_sync_to_async
from .models import Chat, ChatRoom
from django.utils import timezone




class ChatConsumer(AsyncWebsocketConsumer):
    #db_create
    # @database_sync_to_async
    # def get_previous_messages(self):
    #     return list(ChatMessage.objects.filter(room_name=self.room_name).values('message', 'user'))

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
#        self.user = self.scope['user']

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Accept the WebSocket connection
        await self.accept()

        # #db_create
        # previous_messages = await self.get_previous_messages()
        # for message in previous_messages:
        #     await self.send(
        #         text_data=json.dumps({"message": f"{message['message']}", "username": message['username']}))
        #
        # @database_sync_to_async
        # def get_user(self, username):
        #     return User.objects.get(username=username)



    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

   # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        self.user_name = self.scope["user"].username
        self.user_id = self.scope["user"].id
        #username = text_data_json["username"]

        # user 생성
       # username = text_data_json['username']

     #   user = await self.get_user(username)

        room = await database_sync_to_async(ChatRoom.objects.get)(name=self.room_name)

        chat = Chat(
            user=self.scope['user'],
            message=message,
            room=room,
        )
        await database_sync_to_async(chat.save)()
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
                'user_id':self.user_id,
                'user_name':self.user_name,
            }
        )

        # db_create
        # await self.save_message_to_database(message,  self.scope['user'])

        # Save the message to the database
    #    await self.save_message_to_database(message, self.scope['user'])
        #        await self.save_message_to_database(message)

    async def chat_message(self, event):
        message=event['message']
        user_id=event['user_id']
        user_name=event['user_name']

        await self.send(text_data=json.dumps({
            'message':message,
            'user_id':user_id,
            'user_name': user_name
        }))






        # Send message to room group
    #     await self.channel_layer.group_send(
    #         self.room_group_name, {"type": "chat.message", "message": message,
    #                 "user_id": self.user_id, "user_name": self.user_name, "timestamp": timezone.now().isoformat()}
    #         #"username": self.user.username,
    # #        self.room_group_name, {"type": "chat.message", "message": message}
    #     )

#     @database_sync_to_async
#     def save_message_to_database(self, message, username):
#         ChatMessage.objects.create(
#             room_name=self.room_name,
#             message=message,
#             username=self.user_name
# #            username=self.user.username,
#         )
#
#     # Receive message from room group
#     async def chat_message(self, event):
#         message = event["message"]
#         user_id = event["user_id"]
#         user_name = event["user_name"]
#         # print(self.user.username)
#         # print(user_name)
#         # Send message to WebSocket with HTML tags
#         await self.send(text_data=json.dumps({
#             "message": message,
#             "user_id": user_id,
#             "user_name": user_name,
#         }))
#


