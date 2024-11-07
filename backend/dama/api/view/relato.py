from rest_framework import viewsets
from api.models.relato import Relato
from api.serializer.relato import RelatoSerializer

class RelatoViewSet(viewsets.ModelViewSet):
    queryset = Relato.objects.all()
    serializer_class = RelatoSerializer
