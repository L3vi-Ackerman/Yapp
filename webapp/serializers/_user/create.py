from django.db import transaction
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from serializers.profile import CreateProfileSerializer

from _user.models import User, UserProfile


class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="A user with this email already exists.",
            )
        ],
    )
    username = serializers.CharField(
        required=True,
        max_length=25,
        validators=[
            UniqueValidator(
                queryset=UserProfile.objects.all(),
                message="A user with this username already exists.",
            )
        ],
    )
    first_name = serializers.CharField(
        required=True,
        max_length=25,
    )
    last_name = serializers.CharField(
        required=True,
        max_length=25,
        write_only=True,
    )
    password = serializers.CharField(
        required=True,
        write_only=True,
        min_length=8,
    )
    password2 = serializers.CharField(
        required=True,
        write_only=True,
        min_length=8,
    )

    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {
                    "password2": "Password fields didn't match.",
                }
            )

        return attrs

    @transaction.atomic
    def create(self, validated_data: dict):
        validated_data.pop("password2")

        email = validated_data["email"]
        password = validated_data.pop("password")

        profile_data = {
            "username": validated_data.pop("username"),
            "first_name": validated_data.pop("first_name"),
            "last_name": validated_data.pop("last_name"),
        }

        user_obj = User.objects.create_user(
            email,
            password,
        )

        profile_serializer = CreateProfileSerializer(
            data={**profile_data, "user": user_obj.id}
        )

        profile_serializer.is_valid(raise_exception=True)
        profile_serializer.save()

        return user_obj
