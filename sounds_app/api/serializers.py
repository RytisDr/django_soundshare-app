
from rest_framework import serializers
from .. models import UserProfile, Sound, SoundFile, PasswordResetRequest
from .. messaging import email_message
import django_rq


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


class PasswordResetConfirmSerializer(serializers.ModelSerializer):
    pass


class PostSoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sound
        fields = ['title', 'file']


class SoundFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoundFile
        fields = ['file_path']
