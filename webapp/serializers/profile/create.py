from _user.models import UserProfile
from rest_framework import serializers


class CreateProfileSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserProfile
        fields = [
            "user",
            "username",
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
