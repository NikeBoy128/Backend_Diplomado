from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, AutosSerializer
from .models import Autos
class projectViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer