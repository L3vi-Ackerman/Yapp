from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from serializers.health import HealthCheckResponseSerializer


class AuthHealthCheckView(RetrieveAPIView):
    permission_classes = IsAuthenticated

    serializer_class = HealthCheckResponseSerializer

    def get_object(self):
        data = {
            "status": ("Consider this message served - the server's up and running!",),
            "headers": self.request.headers,
            "email": self.request.user.email,
        }

        return data
