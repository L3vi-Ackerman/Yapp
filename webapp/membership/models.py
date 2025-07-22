from _user.models import User
from base.models._uuid import UUIDModel
from django.db import models
from room.models import RoomModel


class MembershipModel(UUIDModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    room = models.ForeignKey(
        RoomModel,
        on_delete=models.CASCADE,
    )

    joined_at = models.DateTimeField(
        auto_now_add=True,
    )
