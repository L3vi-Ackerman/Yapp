from django.contrib import admin
from room.models import RoomModel

from _user.models import User, UserProfile

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(RoomModel)
