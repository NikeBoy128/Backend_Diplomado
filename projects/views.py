from django.shortcuts import render
# Create your views here.
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, permission_classes
from .models import Autos,Viajes,Gastos
from .serializers import AutosSerializer, GroupSerializer,ViajesSerializer,GastosSerializer
from rest_framework import permissions
from rest_framework import viewsets
from django.contrib.auth.models import Group

@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
class ExampleView(APIView):
    def get(self, request, format=None):
        content = {
            'user': str(request.user),  
            'auth': str(request.auth),  
        }
        return Response(content)


class WhoAmIView(APIView):
    def get(self, request):
        user = request.user
        groups = [group.name for group in user.groups.all()]
        return Response({
            "username": user.username,
            "email": user.email,
            "is_authenticated": user.is_authenticated,
            "roles": groups,
        })
class AutosViewSet(viewsets.ModelViewSet):
    queryset = Autos.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AutosSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = GroupSerializer


class ViajesViewSet(viewsets.ModelViewSet):
    queryset = Viajes.objects.all()
    serializer_class = ViajesSerializer

class GastosViewSet(viewsets.ModelViewSet):
    queryset = Gastos.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = GastosSerializer