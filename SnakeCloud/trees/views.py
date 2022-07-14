from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
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
    room_model = Room.objects.filter(name=room)
    if not room_model:
        try:
            new_room = Room(
                user=request.user,
                name=room,
                description=''
            )
            new_room.save()
            room_model = Room.objects.get(name=room)
            return render(request, 'trees/room_page.html', {'room': room_model})
        except Exception as e:
            return HttpResponse(e)
    else:
        room_model = Room.objects.get(name=room)
        return render(request, 'trees/room_page.html', {'room': room_model})
