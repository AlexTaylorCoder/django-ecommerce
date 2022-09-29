from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatRoomConsumer(AsyncWebsocketConsumer):
    #handles initial web socket connection
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat%s' % self.room_name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        ) 
        #Accepts connection from client
        await self.accept()
        
        #Sends message on connection to group with key of group_name 
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'tester_message',
                'tester':'First Message'
            }
        )
        #Sends message contained within group to client
    async def tester_message(self,event):
        tester = event['tester']
        await self.send(text_data=json.dumps({
            'tester':tester,
        }))
        #On leaving window destroys connection
    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    #Recieves message from client
    async def receive(self, text_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
    #Partitions to group 
        await self.channel_layer.group_send(
            self.room_group_name,
             {
                'type':'chat_message',
                'message':message,
            }
        )
    #Sends message to client
    async def chatroom_message(self,event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message':message,
        }))
