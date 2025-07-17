from _user.models import User
from rest_framework import serializers


class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
