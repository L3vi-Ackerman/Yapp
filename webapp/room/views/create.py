from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from serializers.room import CreateRoomSerializer

from room.models import RoomModel


class CreateRoomView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateRoomSerializer
    queryset = RoomModel.objects.all()
