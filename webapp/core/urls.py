from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import (
    JWTStatelessUserAuthentication as TokenAuth,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Yapp BE",
        default_version="v1",
    ),
    public=True,
    permission_classes=[AllowAny],
    authentication_classes=(
        BasicAuthentication,
        TokenAuth,
    ),
)


urlpatterns = [
    path(
        "admin/",
        admin.site.urls,
    ),
    path(
        "swagger/",
        schema_view.with_ui(cache_timeout=0),
        name="schema-swagger",
    ),
    path(
        "gatekeeper/",
        include("gatekeeper.urls"),
    ),
    path(
        "health/",
        include("health.urls"),
    ),
    path(
        "user/",
        include("_user.urls"),
    ),
    path(
        "chat/",
        include("chat.urls"),
    ),
]
