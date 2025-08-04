from rest_framework import serializers

from room.models import RoomModel


class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomModel
        fields = "__all__"
        read_only_fields = ["created_by"]

    def perform_create(self, request):
        serializers.save(created_by=self.request.user)
