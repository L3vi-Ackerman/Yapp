from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from serializers.profile import ListProfileSerializer

from _user.models import UserProfile


class ListProfileView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListProfileSerializer
    queryset = UserProfile.objects.all()
