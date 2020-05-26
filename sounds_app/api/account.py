
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from . serializers import RegistrationSerializer, PasswordResetSerializer, PasswordResetConfirmSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .. models import UserProfile, PasswordResetRequest


@api_view(['POST'])
@permission_classes([AllowAny])
def registration(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save()
        data['response'] = 'registered'
        data['email'] = account.email
        data['username'] = account.username
    else:
        data = serializer.errors
    return Response(data)


@api_view(['POST'])
@permission_classes([AllowAny])
def password_reset(request):
    serializer = PasswordResetSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        post_email = request.data['email']
        try:
            user = UserProfile.objects.get(email=post_email)
        except:
            return Response("User with this email does not exist")
        if user:
            data = serializer.save()
    else:
        data = serializer.errors

    return Response(data)


@api_view(['POST'])
@permission_classes([AllowAny])
def password_reset_confirm(request):
    serializer = PasswordResetConfirmSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        post_email = request.data['email']
        post_token = request.data['token']
        try:
            user = UserProfile.objects.get(email=post_email)
            prr = PasswordResetRequest.objects.get(
                token=post_token, user=user.id)
            user = prr.user
        except:
            return Response("Check credentials and try again")
        if user:
            data = serializer.save()
    else:
        data = serializer.errors

    return Response(data)
