from _user.models import UserProfile
from rest_framework import serializers


class CreateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            "user",
            "username",
            "first_name",
            "last_name",
            "address",
            "phone",
            "bio",
            "avatar",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]
