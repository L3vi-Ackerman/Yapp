from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from serializers.profile import CreateProfileSerializer
from serializers.user import RegisterUserSerializer


class RegisterUserView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer


class CreateProfileView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateProfileSerializer
