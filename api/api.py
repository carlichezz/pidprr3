from .models import Estudiante, Facultad, Grupo
from rest_framework import viewsets, permissions
from .serializers import StudentSerializer,FacultadSerializer,GrupoSerializer
# from rest_framework.decorators import action
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

class FacultadViewSet (viewsets.ModelViewSet):
    queryset = Facultad.objects.all()
    permission_classes = [permissions.AllowAny] #PROVICIONAL
    serializer_class = FacultadSerializer

class GrupoViewSet (viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    permission_classes = [permissions.AllowAny] #PROVICIONAL
    serializer_class = GrupoSerializer

class StudentViewSet (viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    permission_classes = [permissions.AllowAny] #PROVICIONAL
    serializer_class = StudentSerializer

    # @action(detail=False)
    # def by_category(self,request):
    #      grupo = self.request.query_params.get('grupo',None)
    #      Estudiante.objects.filter(grupo=grupo)

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet