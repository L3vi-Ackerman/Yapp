from _user.models import User, UserProfile
from django.db import transaction
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from serializers.profile import CreateProfileSerializer


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
        write_only=True,
        validators=[
            UniqueValidator(
                queryset=UserProfile.objects.all(),
                message="A user with this username already exists.",
            )
        ],
    )
    firstName = serializers.CharField(
        required=True,
        max_length=25,
        write_only=True,
    )
    lastName = serializers.CharField(
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
        fields = [
            "id",
            "email",
            "password",
            "password2",
            "firstName",
            "lastName",
            "username",
        ]
        read_only_fields = ["id", "email"]

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
        email = validated_data["email"]
        password = validated_data.pop("password")
        username = validated_data.pop("username")
        firstName = validated_data.pop("firstName")
        lastName = validated_data.pop("lastName")

        validated_data.pop("password2")

        user = User(email=email)
        user.set_password(password)
        user.save()

        profile_data = {
            "user": user.id,
            "username": username,
            "first_name": firstName,
            "last_name": lastName,
        }

        profile_serializer = CreateProfileSerializer(data=profile_data)
        profile_serializer.is_valid(raise_exception=True)
        profile_serializer.save()

        if user.id is None:
            raise serializers.ValidationError(
                {
                    "user": "Failed to create user",
                }
            )
        return user
