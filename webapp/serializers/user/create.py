from _user.models import User
from django.db import transaction
from rest_framework import serializers


class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        required=True,
        write_only=True,
    )
    password2 = serializers.CharField(
        required=True,
        write_only=True,
    )

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "password2",
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
        password = validated_data.pop("password")
        validated_data.pop("password2")

        user = User(**validated_data)
        user.set_password(password)
        user.save()

        if user.id is None:
            raise serializers.ValidationError(
                {
                    "user": "Failed to create user",
                }
            )
        return user
