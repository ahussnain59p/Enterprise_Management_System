import json
import os
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
from pymongo.errors import ServerSelectionTimeoutError
import logging
load_dotenv()
MONGO_DB_HOST = os.getenv('MONGO_DB_HOST')
MONGO_DB_PORT = int(os.getenv('MONGO_DB_PORT'))  # Ensure port is an integer
MONGO_DB_NAME = os.getenv('MONGO_DB_NAME')
MONGO_DB_URI = os.getenv("MONGO_DB_URI")
logger = logging.getLogger(__name__)
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f'chat_{self.room_name}'
        logger.info(f"WebSocket connected for room: {self.room_name}")
        # Initialize MongoDB client and connection
        self.client = MongoClient(MONGO_DB_HOST, MONGO_DB_PORT, serverSelectionTimeoutMS=5000)
        try:
            self.client.server_info()
            logger.info("Connected to MongoDB successfully.")
        except ServerSelectionTimeoutError as err:
            logger.error(f"Failed to connect to MongoDB: {err}")
        self.db = self.client[MONGO_DB_NAME]
        self.collection = self.db['CHATMSGS1']
        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
    async def disconnect(self, close_code):
        logger.info(f"WebSocket disconnected for room: {self.room_name}")
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        # Close MongoDB connection
        self.client.close()
    async def receive(self, text_data):
        data = json.loads(text_data)
        message_type = data.get('type', 'chat')
        if message_type == 'chat':
            await self.handle_chat_message(data)
        elif message_type == 'history':
            await self.handle_message_history(data)
        elif message_type == 'edit':
            await self.handle_edit_message(data)
        elif message_type == 'delete':
            await self.handle_delete_message(data)
        else:
            logger.warning(f"Unknown message type received: {message_type}")
    async def handle_chat_message(self, data):
     message = data.get('message')
     provided_room_id = data.get('room_id')
     senderid = data.get('senderid')
     receiverid = data.get('receiverid')
     if not all([message, provided_room_id, senderid, receiverid]):
        logger.error(f"Missing fields in chat message data: {data}")
        return
     existing_room = self.collection.find_one({
            '$or': [
                {'$and': [{'senderid': senderid}, {'receiverid': receiverid}]},
                {'$and': [{'senderid': receiverid}, {'receiverid': senderid}]}
            ]
        })
     if existing_room:
        # Use the existing room_id if it matches
        room_id = existing_room['room_id']
        print("Room Exists")
     else:
        # Insert a new room with the provided room_id if it does not exist
        room_id = provided_room_id
        print("Room Does not exist")
     # Prepare the message object with the correct room_id
     message_obj = {
        'room_id': room_id,
        'text': message,
        'senderid': senderid,
        'receiverid': receiverid
     }

     try:
        self.collection.insert_one(message_obj)
     except Exception as e:
        logger.error(f"Failed to insert message to MongoDB: {e}")

     await self.channel_layer.group_send(
        self.room_group_name,
        {
            'type': 'chat_message',
            'message': message,
            'senderid': senderid,
            'receiverid': receiverid,
            'room_id': room_id
        }
    )
    async def handle_message_history(self, data):
     senderid = data.get('senderid')
     receiverid = data.get('receiverid')
     if not all([senderid, receiverid]):
        logger.error(f"Missing senderid or receiverid in message history request: {data}")
        return

    # Find the room_id based on the combination of senderid and receiverid
     existing_room = self.collection.find_one({
        '$or': [
            {'$and': [{'senderid': senderid}, {'receiverid': receiverid}]},
            {'$and': [{'senderid': receiverid}, {'receiverid': senderid}]}
        ]
    })
     if not existing_room:
        print("not found")
        logger.error(f"Room not found for senderid {senderid} and receiverid {receiverid}")
        return
     room_id = existing_room['room_id']
    # Retrieve all messages from the room where either ID can be the sender or receiver
    #  print("found")
     messages = list(self.collection.find({
        'room_id': room_id,
        '$or': [
            {'senderid': senderid, 'receiverid': receiverid},
            {'senderid': receiverid, 'receiverid': senderid}
        ]
     }))
    # Format the messages for sending
     formatted_messages = [{'message_id': str(msg['_id']), 'text': msg.get('text'), 'senderid': msg.get('senderid'), 'receiverid': msg.get('receiverid')} for msg in messages]
     await self.channel_layer.group_send(
        self.room_group_name,
        {
            'type': 'chat_message_history',
            'messages': formatted_messages
        }
     )    
    async def handle_edit_message(self, data):
        message_id = data.get('message_id')
        new_text = data.get('new_text')
        if not all([message_id, new_text]):
            logger.error(f"Missing fields in edit message request: {data}")
            return
        try:
            self.collection.update_one(
                {'_id': ObjectId(message_id)},
                {'$set': {'text': new_text}})
        except Exception as e:
            logger.error(f"Failed to update message in MongoDB: {e}")
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message_edit',
                'message_id': message_id,
                'new_text': new_text
            }
        )

    async def handle_delete_message(self, data):
        message_id = data.get('message_id')
        print("Delete Message ID",message_id)
        if not all([message_id]):
            logger.error(f"Missing fields in delete message request: {data}")
            return
        try:
            self.collection.delete_one({'_id': ObjectId(message_id)})
        except Exception as e:
            logger.error(f"Failed to delete message from MongoDB: {e}")

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message_delete',
                'message_id': message_id
            }
        )

    async def chat_message(self, event):
        message = event['message']
        senderid = event['senderid']
        receiverid = event['receiverid']

        await self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message,
            'senderid': senderid,
            'receiverid': receiverid
        }))

    async def chat_message_history(self, event):
        messages = event['messages']
        await self.send(text_data=json.dumps({
            'type': 'history',
            'messages': messages
        }))
    async def chat_message_edit(self, event):
        message_id = event['message_id']
        new_text = event['new_text']
        await self.send(text_data=json.dumps({
            'type': 'edit',
            'message_id': message_id,
            'new_text': new_text
        }))
    async def chat_message_delete(self, event):
        message_id = event['message_id']
        await self.send(text_data=json.dumps({
            'type': 'delete',
            'message_id': message_id
        }))