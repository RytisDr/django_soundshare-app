from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, SoundFile, Sound, PasswordResetRequest


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff')


admin.site.register(UserProfile, UserAdmin)
admin.site.register(Sound)
admin.site.register(PasswordResetRequest)
admin.site.register(SoundFile)
