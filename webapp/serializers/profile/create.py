from _user.models import UserProfile
from rest_framework import serializers


class CreateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data, **kwargs):
        user = validated_data.pop("user")
        username = validated_data.pop("username")
        first_name = validated_data.pop("first_name")
        last_name = validated_data.pop("last_name")

        extra_fields = {
            "bio": validated_data.pop("bio", ""),
            "phone": validated_data.pop("phone", ""),
            "avatar": validated_data.pop("avatar", None),
        }

        user_profile_obj = UserProfile.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            username=username,
            **extra_fields,
        )

        return user_profile_obj
