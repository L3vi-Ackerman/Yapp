from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from serializers.room import ListRoomSerializer

from room.models import RoomModel


class ListRoomView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListRoomSerializer
    queryset = RoomModel.objects.all()
