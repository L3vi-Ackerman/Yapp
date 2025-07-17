from django.urls import path

from _user.views import (
    CreateProfileView,
    DeleteProfileView,
    ListProfileView,
    RegisterUserView,
    RetrieveProfileView,
    UpdateProfileView,
)

urlpatterns = [
    path(
        "register/",
        RegisterUserView.as_view(),
        name="register-user",
    ),
    path(
        "create/",
        CreateProfileView.as_view(),
        name="create-user",
    ),
    path(
        "list/",
        ListProfileView.as_view(),
        name="list-user",
    ),
    path(
        "retrieve/<int:pk>/",
        RetrieveProfileView.as_view(),
        name="retrieve-user",
    ),
    path(
        "update/<int:pk>/",
        UpdateProfileView.as_view(),
        name="update-user",
    ),
    path(
        "delete/<int:pk>/",
        DeleteProfileView.as_view(),
        name="delete-user",
    ),
]
