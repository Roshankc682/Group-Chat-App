from django.db import models

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
# declare a new model with a name "MessageData"
class UserData(models.Model):
    username = models.CharField(max_length=15,unique=True)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.username


class MessageData(models.Model):
    username = models.CharField(max_length=15)
    message = models.TextField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True)

   
    # ovverride the save and send the message through channel
    def save(self, *args, **kwargs):
        # all channel layer imported
        channel_layer = get_channel_layer()
        data = json.dumps(*args)
        print("send data to scoket")
        print(data)
        # This channels will be hit after the saving is done
        async_to_sync(channel_layer.group_send)(
            'message_group',{
                # type is the function called from consumers
                'type':'send_notification',
                # this is the value send to send_notification function in consumer
                'value': data
            }
        )
        super(MessageData,self).save(*args,**kwargs)

    def __str__(self):
        return self.username