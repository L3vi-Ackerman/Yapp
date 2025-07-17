from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from serializers.profile import UpdateProfileSerializer

from _user.models import UserProfile


class UpdateProfileView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateProfileSerializer
    queryset = UserProfile.objects.all()
