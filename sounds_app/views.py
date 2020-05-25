
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import RegistrationSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


@api_view(['POST'])
@permission_classes([AllowAny])
def registration_view(request):
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
