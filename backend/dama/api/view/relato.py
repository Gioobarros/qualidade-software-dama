from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializer.relato import RelatoSerializer, Relato

class RelatoView(APIView):
    def post(self, request):
        serializer = RelatoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self, request):
        try:
            relato = Relato.objects.all()
            if not relato.exists():
                return Response({'messagem': 'Nenhuma ONG foi achada'}, status=status.HTTP_404_NOT_FOUND)
            serializer = RelatoSerializer(relato, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    # @action(detail=False, methods=['get'])
    # def listar_relatos(self, request):

    #     relatos = Relato.objects.all()

    #     if relatos:

    #         relatos_serializados = RelatoSerializer(relatos, many=True)

    #         return Response(relatos_serializados.data, status=status.HTTP_302_FOUND)
        
    #     else:
    #         return Response({'erro':'não existem relatos publicados'}, status=status.HTTP_404_NOT_FOUND)



