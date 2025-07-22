from _user.models import User
from base.models import AbstractBaseModel
from django.db import models
from room.models import RoomModel


class MessageModel(AbstractBaseModel):
    room = models.ForeignKey(
        RoomModel,
        on_delete=models.CASCADE,
    )

    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    content = models.CharField(
        max_length=1000,
    )

    is_deleted = models.BooleanField(
        default=False,
    )
