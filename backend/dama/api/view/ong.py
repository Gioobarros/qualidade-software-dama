from api.models.ong import Ong
from django.shortcuts import render
from rest_framework import viewsets
from api.serializer.ong import OngSerializer

class OngViewSet(viewsets.ModelViewSet):
    queryset = Ong.objects.all()
    serializer_class = OngSerializer 
