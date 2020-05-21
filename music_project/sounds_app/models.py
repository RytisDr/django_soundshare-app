from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")
    description = models.TextField(blank=True, null=True)
    profile_image = models.ForeignKey(
        'Image', on_delete=models.SET_NULL, null=True)
    favorites = models.ForeignKey(
        'Sound', on_delete=models.SET_NULL, null=True)


class Sound(models.Model):
    title = models.CharField(max_length=200)

    indexes = [models.Index(fields=['title'])]


class Genres(models.Model):
    genre_name = models.CharField(max_lenght=50)
