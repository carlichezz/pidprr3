from rest_framework import serializers
from .models import Estudiante,Facultad,Grupo

class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        fields = ('__all__')

class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = ('__all__')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ('__all__')