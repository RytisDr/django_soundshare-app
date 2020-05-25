from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff')


admin.site.register(UserProfile, UserAdmin)
