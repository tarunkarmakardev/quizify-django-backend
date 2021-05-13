from django.contrib import admin
from .models import UserProfile
# Register your models here.


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'user_type']
    list_display_links = ['id', 'user']
