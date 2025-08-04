from django.urls import path

from .views import CreateRoomView, ListRoomView, RetrieveRoomView

urlpatterns = [
    path(
        "create/",
        CreateRoomView.as_view(),
        name="create-room",
    ),
    path(
        "list/",
        ListRoomView.as_view(),
        name="list-room",
    ),
    path(
        "retrieve/<str:code>/",
        RetrieveRoomView.as_view(),
        name="retrieve-room",
    ),
]
