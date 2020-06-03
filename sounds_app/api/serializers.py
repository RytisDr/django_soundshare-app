
from rest_framework import serializers
from .. models import UserProfile, Sound, SoundFile, PasswordResetRequest, Genre
from .. messaging import email_message
import django_rq
import os
import uuid
from django.db import transaction


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['email', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8}
        }

    def save(self):
        account = UserProfile(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        account.set_password(password)
        account.save()
        return account


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def save(self):
        user = UserProfile.objects.get(email=self.validated_data['email'])
        prr = PasswordResetRequest()
        prr.user = user
        prr.save()
        # will work on redis server (via Vangrant on Win)
        django_rq.enqueue(email_message, {
            'token': prr.token,
            'email': prr.user.email,
        })
        return "Check your email for password reset."


class PasswordResetConfirmSerializer(serializers.Serializer):
    email = serializers.EmailField()
    token = serializers.CharField(max_length=43)
    newPassword = serializers.CharField(write_only=True, min_length=8)

    def save(self):
        account = UserProfile.objects.get(email=self.validated_data['email'])
        newPassword = self.validated_data['newPassword']
        account.set_password(newPassword)
        account.save()

        return "Password has been reset."


class DeleteUserSerializer(serializers.Serializer):
    class Meta:
        model = UserProfile

    def delete(self):
        user = None
        user = self.context.get("user")
        account = UserProfile.objects.get(email=user.email)
        account.delete()
        return "Account deleted."


class PostSoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sound
        fields = ['title']

    def save(self):
        user = None
        user = self.context.get("user")
        title = self.validated_data['title']
        genre = self.context.get("genre")
        file_obj = self.context.get("file")
        model = Sound(title=title, uploaded_by=user,
                      sound_file=file_obj, genres=genre)
        model.save()
        return "Sound posted."


class SoundFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoundFile
        fields = ['file']

    def save(self):
        file_name_original = self.validated_data['file'].name
        file_format = os.path.splitext(file_name_original)[1]
        file_name_uuid = uuid.uuid4().hex + file_format
        self.validated_data['file'].name = file_name_uuid + file_format
        file_obj = self.validated_data['file']

        model = SoundFile(file=file_obj, file_name=file_name_uuid,
                          file_format=file_format)
        model.save()
        return model


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_name']

    def save(self):
        genreName = self.validated_data['genre_name']
        try:
            existingGenre = Genre.objects.get(genre_name=genreName)
            return existingGenre
        except:
            model = Genre(genre_name=genreName)
            model.save()
            return model


class SoundsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sound
        fields = ['']
