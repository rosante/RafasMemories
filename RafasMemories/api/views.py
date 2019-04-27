from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import MemoriaSerializer

# Create your views here.
class MemoriaViewSet(viewsets.ModelViewSet):
    queryset = Memoria.objects.all()
    serializer_class = MemoriaSerializer