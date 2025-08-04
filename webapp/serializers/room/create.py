import os

from hashids import Hashids
from rest_framework import serializers

from room.models import RoomModel


class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomModel
        fields = "__all__"
        read_only_fields = ["code", "created_by"]

    def create(self, validated_data):
        user = self.context["request"].user
        room_name = validated_data.get("name")

        hashids = Hashids(
            min_length=8,
            salt=os.environ.get("HASHID_SECRET_KEY", "default_salt"),
        )
        code = hashids.encode(abs(hash(room_name)))

        room = RoomModel.objects.create(
            **validated_data,
            created_by=user,
            code=code,
        )
        return room
