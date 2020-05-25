from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UserProfile
from .serializers import RegistrationSerializer
from .permissions import IsOwnerOrNoAccess
