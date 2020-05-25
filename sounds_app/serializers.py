
from rest_framework import serializers
from .models import UserProfile


class RegistrationSerializer(serializers.Serializer):

    class Meta:
        email = serializers.EmailField(required=True)
        password = serializers.CharField(required=True)
        extra_kwargs = {
            'password': {'write_only': True}
        }
        model = UserProfile

    def save(self):
        account = UserProfile(
            email=self.validated_data['email'],
        )
        password = self.validated_data['password']
        account.set_password(password)
        account.save()
        return account
