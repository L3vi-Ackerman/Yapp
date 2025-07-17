from django.db import models


class UserStatusChoices(models.TextChoices):
    ONLINE = "Online"
    OFFLINE = "Offline"
