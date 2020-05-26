from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import PostSoundSerializer, SoundFileSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def post_sound_view(request):
    soundSerializer = PostSoundSerializer(data=request.data)
    soundFileSerializer = SoundFileSerializer(data=request.data)
    data = {}
    return Response(request.data)
    # if soundSerializer.is_valid() and PostSoundSerializer.is_valid():
