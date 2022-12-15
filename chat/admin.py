from django.contrib import admin
from .models import UserProfile, chatMessages
from BLOG.models import *


admin.site.register(UserProfile)
admin.site.register(chatMessages)
admin.site.register(Avatar)

