from secrets import token_urlsafe
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
# Create your models here.


class Image(models.Model):
    image_path = models.CharField(max_length=200, unique=True)


class UserProfile(AbstractUser):
    email = models.EmailField(verbose_name='email',
                              unique=True, max_length=100)
    username = models.CharField(max_length=25)
    description = models.TextField(blank=True, null=True)
    profile_image = models.OneToOneField(
        Image, on_delete=models.SET_NULL, null=True)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    indexes = [models.Index(fields=['username'])]

    def __str__(self):
        return f"{self.email} - {self.username}"

    #file_name = models.CharField(max_length=200, unique=True)


class SoundFile(models.Model):
    file_format = models.CharField(max_length=5, null=False)
    file_name = models.CharField(max_length=50, unique=True, null=False)
    file = models.FileField(upload_to='sounds', default=None, null=False)

    def __str__(self):
        return f"{self.id} --- {self.file_name}"


class Genre(models.Model):
    genre_name = models.CharField(max_length=20)

    def __str__(self):
        return self.genre_name


class Sound(models.Model):
    title = models.CharField(max_length=200, null=False)
    uploaded_by = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='user_uploads', null=False)
    sound_file = models.OneToOneField(
        SoundFile, on_delete=models.CASCADE, null=False)
    genres = models.ForeignKey(
        Genre, null=True, on_delete=models.SET_NULL, related_name='sounds')

    def __str__(self):
        return f"{self.title} - {self.uploaded_by}"


class Favorites(models.Model):
    user = models.OneToOneField(
        UserProfile, on_delete=models.CASCADE, related_name='favorite_sounds')
    sound = models.OneToOneField(
        Sound, on_delete=models.CASCADE, related_name='favorites')

    def __str__(self):
        return f"{self.user.id} - {self.sound}"


class PasswordResetRequest(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    token = models.CharField(max_length=43, default=token_urlsafe)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.created_timestamp} - {self.updated_timestamp} - {self.token}'
