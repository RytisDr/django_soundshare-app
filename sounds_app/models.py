from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
# Create your models here.


class Image(models.Model):
    image_path = models.CharField(max_length=200, unique=True)


class UserProfile(AbstractUser):
    email = models.EmailField(verbose_name='email',
                              unique=True, max_length=100)
    username = models.CharField(blank=True, max_length=25)
    description = models.TextField(blank=True, null=True)
    profile_image = models.OneToOneField(
        Image, on_delete=models.SET_NULL, null=True)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    indexes = [models.Index(fields=['username'])]

    def __str__(self):
        return self.email


class SoundFile(models.Model):
    file_path = models.CharField(max_length=200, unique=True)


class Sound(models.Model):
    title = models.CharField(max_length=200)
    uploaded_by = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='user_uploads')
    file = models.OneToOneField(
        SoundFile, on_delete=models.CASCADE)


class Favorites(models.Model):
    user = models.OneToOneField(
        UserProfile, on_delete=models.CASCADE, related_name='favorite_sounds')
    sound = models.OneToOneField(
        Sound, on_delete=models.CASCADE, related_name='favorites')


class Genre(models.Model):
    sound = models.ForeignKey(
        Sound, on_delete=models.SET_NULL, null=True, related_name='genres')
    genre_name = models.CharField(max_length=50)
