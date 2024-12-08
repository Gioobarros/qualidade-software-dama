from rest_framework import status
from rest_framework import viewsets
from api.models.relato import Relato
from rest_framework.response import Response
from rest_framework.decorators import action
from api.serializer.relato import RelatoSerializer

class RelatoViewSet(viewsets.ModelViewSet):
    queryset = Relato.objects.all()
    serializer_class = RelatoSerializer


    @action(detail=False, methods=['get'])
    def listar_relatos(self, request):

        relatos = Relato.objects.all()

        if relatos:

            relatos_serializados = RelatoSerializer(relatos, many=True)

            return Response(relatos_serializados.data, status=status.HTTP_302_FOUND)
        
        else:
            return Response({'erro':'não existem relatos publicados'}, status=status.HTTP_404_NOT_FOUND)



