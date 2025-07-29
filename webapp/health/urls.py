from django.urls import path

from .views import AuthHealthCheckView, HealthCheckView

urlpatterns = [
    path(
        "",
        HealthCheckView.as_view(),
        name="health-check",
    ),
    path(
        "auth",
        AuthHealthCheckView.as_view(),
        name="auth-health-check",
    ),
]
