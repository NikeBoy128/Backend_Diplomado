
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Autos
from django.contrib.auth.models import Group
from .models import Viajes, Gastos
from django.contrib.auth.models import User

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')

class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=Group.objects.all()
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name','password','is_staff','is_active','groups')

    def create(self, validated_data):
        groups = validated_data.pop('groups')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  
        user.save()
        for group in groups:
            user.groups.add(group)
        return user

    def update(self, instance, validated_data):
        if 'groups' in validated_data:
            groups = validated_data.pop('groups')
            instance.groups.clear()
            for group in groups:
                instance.groups.add(group)
        return super().update(instance, validated_data)
class AutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autos
        fields = '__all__'



class GastosSerializer(serializers.ModelSerializer):
    viaje = serializers.PrimaryKeyRelatedField(queryset=Viajes.objects.all())
    class Meta:
        model = Gastos
        fields = '__all__'

class ViajesSerializer(serializers.ModelSerializer):
    auto = serializers.PrimaryKeyRelatedField(queryset=Autos.objects.all(), required=False)
    conductor = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    gastos = GastosSerializer(many=True, read_only=True)

    class Meta:
        model = Viajes
        fields = ['id','conductor', 'origen', 'destino', 'fecha', 'hora', 'auto', 'gastos']
