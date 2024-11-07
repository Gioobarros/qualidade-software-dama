from rest_framework import viewsets
from api.models.administrador import Administrador
from api.serializer.administrador import AdministradorSerializer

class AdministradorViewSet(viewsets.ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer 
