from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from serializers.health import HealthCheckResponseSerializer


class HealthCheckView(RetrieveAPIView):
    permission_classes = (AllowAny,)

    serializer_class = HealthCheckResponseSerializer

    def get_object(self):
        data = {
            "status": ("Consider this message served - the server's up and running!"),
            "headers": self.request.headers,
        }
        return data
