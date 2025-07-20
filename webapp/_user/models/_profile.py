from base import AbstractBaseModel
from base.choices import UserStatusChoices
from django.core.validators import FileExtensionValidator
from django.db import models

from _user.models._user import User


class UserProfile(AbstractBaseModel):
    UserStatus = UserStatusChoices

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    first_name = models.CharField(
        max_length=25,
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        max_length=25,
        null=False,
        blank=False,
    )
    username = models.CharField(
        max_length=25,
        unique=True,
    )

    bio = models.CharField(
        max_length=300,
        blank=True,
    )

    address = models.CharField(
        max_length=40,
        blank=True,
    )

    phone = models.CharField(
        max_length=10,
        blank=True,
    )

    avatar = models.ImageField(
        upload_to="users/avatars/",
        null=True,
        validators=[
            FileExtensionValidator(
                [
                    "png",
                    "jpeg",
                    "jpg",
                ]
            )
        ],
    )
