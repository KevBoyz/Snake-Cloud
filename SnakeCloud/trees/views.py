from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
import json
from .models import *


@login_required(login_url='/auth/login/')
def dashboard(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        description = request.POST.get('description')
        try:
            room = Room(
                user=user,
                name=name,
                description=description
            )
        except Exception as e:
            return HttpResponse(e)
        room.save()
    elif request.method == 'GET':
        rooms = Room.objects.all()
        return render(request, 'trees/dashboard.html', {'rooms': rooms})


@login_required(login_url='/auth/login/')
def room_view(request, room):
    room_model = Room.objects.get(name=room)
    if not room_model:
        return HttpResponse(f'Room {room} not found')
    else:
        if request.user.id not in room_model.users:
            room_model.users[str(request.user.id)] = str(request.user)
            room_model.len = str(len(room_model.users))
            room_model.save()
        if request.method == 'POST':
            try:
                message = request.POST.get('message')
                msg = Chat_message(
                    user=request.user,
                    room=room_model,
                    message=message
                )
                msg.save()
                chat_messages = Chat_message.objects.filter(room=room_model)
                return render(request, 'trees/room_page.html', {'room': room_model, 'chat_messages': chat_messages})
            except Exception as e:
                return HttpResponse(e)
        elif request.method == 'GET':
            chat_messages = Chat_message.objects.filter(room=room_model)
            return render(request, 'trees/room_page.html', {'room': room_model, 'chat_messages': chat_messages})


@login_required(login_url='/auth/login/')
def new_room(request):
    if request.method == 'POST':
        room = request.POST.get('name')
        description = request.POST.get('description')
        try:
            new_room = Room(
                admin=request.user,
                name=room,
                description=description
            )
            new_room.save()
            room_model = Room.objects.get(name=room)
            return redirect(f'/utf8trees/{room}')
        except Exception as e:
            return HttpResponse(e)
    elif request.method == 'GET':
        return render(request, 'trees/new_room.html')
