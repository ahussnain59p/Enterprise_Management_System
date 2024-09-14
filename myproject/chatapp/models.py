# chatapp/models.py
from djongo import models
class Message(models.Model):
    room_id = models.IntegerField()
    text = models.TextField()
    senderid= models.TextField()
    receiverid=models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Message in Room {self.room_id} at {self.timestamp}'
class ChatRoom(models.Model):
    name = models.TextField()
    description = models.TextField()
    room_id = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Message in Room {self.room_id} at {self.timestamp}'