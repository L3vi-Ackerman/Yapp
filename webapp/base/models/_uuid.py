from uuid import uuid4

from django.db import models


class UUIDModel(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
        db_index=True,
    )
