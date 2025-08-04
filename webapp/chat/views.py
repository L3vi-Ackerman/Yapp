from django.shortcuts import get_object_or_404, render
from room.models import RoomModel


def index(request):
    return render(
        request,
        "chat/index.html",
    )


def room(request, code):
    room = get_object_or_404(RoomModel, code=code)
    return render(request, "chat/room.html", {"room_name": room.name})
