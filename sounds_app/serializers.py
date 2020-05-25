
from rest_framework import serializers
from .models import UserProfile


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('email', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }
        model = UserProfile

    def save(self):
        account = UserProfile(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        account.set_password(password)
        account.save()
        return account
