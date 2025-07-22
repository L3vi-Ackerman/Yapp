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
    created_by = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    is_archived = models.BooleanField(
        default=False,
    )
