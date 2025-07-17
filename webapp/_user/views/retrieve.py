from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from serializers.profile import RetrieveProfileSerializer

from _user.models import UserProfile


class RetrieveProfileView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RetrieveProfileSerializer
    queryset = UserProfile.objects.all()
