from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from _user.models import UserProfile


class DeleteProfileView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserProfile.objects.all()
