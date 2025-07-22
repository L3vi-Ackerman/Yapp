from django.db.models import TextChoices


class RoomTypeChoices(TextChoices):
    DIRECT_MESSAGE = "DM", "Direct Message"
    GROUP_CHAT = "GC", "Group Chat"
