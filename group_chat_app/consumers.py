from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer

class MessageChannel(AsyncJsonWebsocketConsumer):
    async def connect(self, *args,**kwargs):
        self.room_name = "message_consumer"
        self.room_group_name = "message_group"
        await(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        # await self.send(text_data=json.dumps({'status': 'Connected to message app'}))

    async def receive(self,text_data):
        # print(text_data)
        # await self.send(text_data=json.dumps({'message': 'new channel got message'}))
        pass

    async def disconnect(self, *args,**kwargs):
        print("disconnected from message app")
        # pass

    
    async def send_notification(self,event):
        date = json.loads(event.get('value'))
        print(event)
        await self.send(text_data=json.dumps(date))