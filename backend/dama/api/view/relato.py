from django.http import Http404
from rest_framework import status
from rest_framework import viewsets
from api.filters.relato_filter import RelatoFilter
from api.serializer.relato import RelatoSerializer, Relato
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

class RelatoView(viewsets.ModelViewSet):
    queryset = Relato.objects.all()
    serializer_class = RelatoSerializer
    filterset_class = RelatoFilter
    search_fields = ['conteudo', 'data_criacao', 'status']
    ordering_fields = ['data_criacao']

    def get_permissions(self):
        if self.action in ['create', 'partial_update', 'destroy']:
            return [IsAuthenticated()]
        
        return [AllowAny()]

    def create(self, request, *args, **kwargs):
        serializer = RelatoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, *args, **kwargs):
        try:
            item = self.get_object()

            serializer = self.get_serializer(item)

            return Response(serializer.data)
        
        except Http404:
            return Response({'erro': 'objeto não encontrado'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def list(self, request, *args, **kwargs):
        try:
            itens = self.get_queryset()

            if not itens.exists():
                return Response({'messagem': 'Nenhum relato foi achado'}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = self.get_serializer(itens, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

    def partial_update(self, request, *args, **kwargs):
        try:
            item = self.get_object()

            serializer = self.get_serializer(
                item, 
                data=request.data, 
                partial=True, 
                context={
                    'usuario': request.user
                }
                )

            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def destroy(self, request, *args, **kwargs):
        try:
            if 'id' in request.data:
                item = get_object_or_404(Relato, id=request.data.get("id"))

                item.delete() 

                return Response({'mensagem': 'relato deletado com sucesso'}, status=status.HTTP_204_NO_CONTENT)

        except Exception:
            return Response({'erro': 'problema na api'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            