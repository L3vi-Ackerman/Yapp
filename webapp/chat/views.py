from django.http import Http404
from django.shortcuts import render
from room.models import RoomModel


def index(request):
    return render(
        request,
        "chat/index.html",
    )


def room(request, room_name):
    if not RoomModel.objects.filter(name=room_name).exists():
        raise Http404("Room does not exist")

    return render(request, "chat/room.html", {"room_name": room_name})
