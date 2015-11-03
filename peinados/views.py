# coding=utf8
from rest_framework import status, renderers, generics
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.http import Http404
from .models import *
from .serializers import *
from rest_framework.generics import *
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from django.shortcuts import get_object_or_404

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class PeluqueriaViewSet(viewsets.ModelViewSet):

    queryset = Peluqueria.objects.all()
    serializer_class = PeluqueriaSerializer
    
class PeinadoViewSet(viewsets.ModelViewSet):

    queryset = Peinado.objects.all()
    serializer_class = PeinadoSerializer
    
class TamanoCabelloViewSet(viewsets.ModelViewSet):

    queryset = TamanoCabello.objects.all()
    serializer_class = TamanoCabelloSerializer
    
class RostroViewSet(viewsets.ModelViewSet):

    queryset = Rostro.objects.all()
    serializer_class = RostroSerializer
    
class OcasionViewSet(viewsets.ModelViewSet):

    queryset = Ocasion.objects.all()
    serializer_class = OcasionSerializer
    
class TipoCabelloViewSet(viewsets.ModelViewSet):

    queryset = TipoCabello.objects.all()
    serializer_class = TipoCabelloSerializer  
    
class SucursalViewSet(viewsets.ModelViewSet):

    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer