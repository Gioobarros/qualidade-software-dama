from django.http import Http404
from rest_framework import status
from rest_framework import viewsets
from api.models.ong import Ong
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.serializer.ong import OngSerializer 


class OngView(viewsets.ModelViewSet):
    queryset = Ong.objects.all()
    serializer_class = OngSerializer

    def get_permissions(self):
        if self.action in ['partial_update', 'destroy']:
            return [IsAuthenticated()]
        
        return [AllowAny()]

    def create(self, request, *args, **kwargs):
        serializer = OngSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def retrieve(self, request, *args, **kwargs):
        try:
            item = self.get_object()

            serializer = self.get_serializer(item)

            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        except Http404:
            return Response({'erro': 'objeto não encontrado'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def list(self, request, *args, **kwargs):
        try:
            itens = self.get_queryset()

            if not itens.exists():
                return Response({'messagem': 'Nenhuma ONG foi achada'}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = self.get_serializer(itens, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

    def partial_update(self, request, *args, **kwargs):
        try:
            if 'username' in request.data:
                item = get_object_or_404(Ong, user__username=request.data.get("username"))

                serializer = self.get_serializer(item, data=request.data, partial=True)

                if serializer.is_valid():
                    serializer.save()

                    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({"erro": "campos obrigatórios ausentes na requisição"}, status=status.HTTP_406_NOT_ACCEPTABLE)
    
        except Exception:
            return Response({'erro': 'problema na api'}, status=status.HTTP_404_NOT_FOUND)
    

    def destroy(self, request, *args, **kwargs):
        try:
            if 'username' in request.data:
                item = get_object_or_404(Ong, user__username=request.data.get("username"))

                if item.user__perfil == 'ong':
                    item.delete()

                    return Response({'mensagem': 'Ong deletado com sucesso'}, status=status.HTTP_204_NO_CONTENT)
                
                else:
                    return Response({'erro': 'Usuário não tem permissão para ser excluído'}, status=status.HTTP_403_FORBIDDEN)
            else:
                return Response({"erro": "campos obrigatórios ausentes na requisição"}, status=status.HTTP_406_NOT_ACCEPTABLE)
            
        except Exception:
            return Response({'erro': 'problema na api'}, status=status.HTTP_404_NOT_FOUND)
    