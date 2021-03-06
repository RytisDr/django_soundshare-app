from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from .serializers import PostSoundSerializer, SoundFileSerializer, SoundsSerializer, GenreSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.parsers import FormParser, MultiPartParser, MultiPartParserError
from django.core.files.storage import FileSystemStorage
import os
from django.db import transaction
from ..models import Sound


class SoundList(generics.ListAPIView):
    serializer_class = SoundsSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Sound.objects.all().order_by('-created_at')
        query = self.request.query_params.get('query', None)
        userId = self.request.query_params.get('userId', None)
        if query is not None:
            queryset = queryset.filter(title__icontains=query)
        if userId is not None:
            queryset = queryset.filter(uploaded_by=userId)
        return queryset


class SoundDetail(generics.RetrieveAPIView):
    queryset = Sound.objects.all()
    serializer_class = SoundsSerializer
    permission_classes = [AllowAny]


class UsersSounds(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SoundsSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Sound.objects.filter(uploaded_by=2)
        return queryset


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def post_sound(request, format=None):
    fileSerializer = SoundFileSerializer(data=request.data)
    data = {}

    if fileSerializer.is_valid():
        with transaction.atomic():
            try:
                postFile = request.data['file']
            except:
                data = "No file posted"
            if postFile:
                fileExtension = os.path.splitext(postFile.name)[1]
                if fileExtension != '.mp3':
                    data = "Wrong file format, only .mp3 is allowed."
                else:
                    soundFile = fileSerializer.save()
            if soundFile:
                genreSerializer = GenreSerializer(
                    data=request.data)
                if genreSerializer.is_valid():
                    genre = genreSerializer.save()
                else:
                    data = genreSerializer.errors
            if genre:
                soundPostSerializer = PostSoundSerializer(
                    data=request.data, context={'user': request.user, 'file': soundFile, 'genre': genre})
                if soundPostSerializer.is_valid():
                    data = soundPostSerializer.save()
                else:
                    data = soundPostSerializer.errors
    else:
        data = fileSerializer.errors

    return Response({"response": data})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def favorite_sound(request):
    return Response("Favorite a sound here")


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfavorite_sound(request):
    return Response("Unfavorite a sound here")


class RemoveSound(generics.DestroyAPIView):
    queryset = Sound.objects.all()
    serializer_class = SoundsSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.uploaded_by == request.user:
            self.perform_destroy(instance)
            return Response({"response": "Sound has been removed."})
        else:
            return Response({"response": "Could not be removed."})
