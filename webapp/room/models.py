from _user.models import User
from base.choices import RoomTypeChoices
from base.models._base import AbstractBaseModel
from django.db import models


class RoomModel(AbstractBaseModel):
    RoomType = RoomTypeChoices

    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    code = models.CharField(
        max_length=32,
        null=True,
    )
    group_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    room_type = models.CharField(
        max_length=50,
        choices=RoomType.choices,
        default=RoomType.DIRECT_MESSAGE,
        editable=False,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
    )
    is_archived = models.BooleanField(
        default=False,
    )
