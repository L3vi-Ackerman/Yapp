from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from serializers.room import RetrieveRoomSerializer

from room.models import RoomModel


class RetrieveRoomView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RetrieveRoomSerializer
    queryset = RoomModel.objects.all()
    lookup_field = "name"
