from rest_framework import serializers

from room.models import RoomModel


class ListRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomModel
        fields = [
            "id",
            "name",
            "code",
            "group_name",
            "is_archived",
            "created_by",
            "created_at",
        ]
