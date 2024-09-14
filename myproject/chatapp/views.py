import os
from django.shortcuts import render, redirect, get_object_or_404
from .models import Message
from .forms import MessageForm
from pymongo import MongoClient
from bson import ObjectId
from django.http import JsonResponse
from dotenv import load_dotenv
load_dotenv()
# MongoDB connection settings (adjust according to your setup)
MONGO_DB_HOST = os.getenv('MONGO_DB_HOST')
MONGO_DB_PORT = int(os.getenv('MONGO_DB_PORT'))  # Ensure port is an integer
MONGO_DB_NAME = os.getenv('MONGO_DB_NAME')
MONGO_COLLECTION_NAME = 'CHAT_MSGS'
# notifications/views.py
def connect_to_mongodb():
    client = MongoClient(MONGO_DB_HOST, MONGO_DB_PORT)
    db = client[MONGO_DB_NAME]
    collection = db[MONGO_COLLECTION_NAME]
    return collection
def message_list(request):
    collection = connect_to_mongodb()
    messages = list(collection.find())
    return render(request, 'chatapp/message_list.html', {'messages': messages})

def message_detail(request, message_id):
    collection = connect_to_mongodb()
    message = collection.find_one({'_id': ObjectId(message_id)})
    return render(request, 'chatapp/message_detail.html', {'message': message})

def message_create(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            collection = connect_to_mongodb()
            message_obj = {
                'room_id': form.cleaned_data['room_id'],
                'text': form.cleaned_data['text'],
            }
            collection.insert_one(message_obj)
            return redirect('message_list')
    else:
        form = MessageForm()

    return render(request, 'chatapp/message_form.html', {'form': form})

def message_update(request, message_id):
    collection = connect_to_mongodb()
    message = collection.find_one({'_id': ObjectId(message_id)})

    if request.method == 'POST':
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            updated_message = {
                'room_id': form.cleaned_data['room_id'],
                'text': form.cleaned_data['text'],
            }
            collection.update_one({'_id': ObjectId(message_id)}, {'$set': updated_message})
            return redirect('message_list')
    else:
        form = MessageForm(initial=message)

    return render(request, 'chatapp/message_form.html', {'form': form})

def message_delete(request, message_id):
    collection = connect_to_mongodb()
    if request.method == 'POST':
        collection.delete_one({'_id': ObjectId(message_id)})
        return redirect('message_list')
    else:
        message = collection.find_one({'_id': ObjectId(message_id)})
        return render(request, 'chatapp/message_confirm_delete.html', {'message': message})
