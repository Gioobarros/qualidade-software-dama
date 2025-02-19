from django.http import Http404
from rest_framework import status, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.strategies.strategy_permissions import UsuarioPermission
from api.strategies.strategy_usuario import AdminStrategy
from api.serializer.administrador import AdministradorSerializer
from api.models.administrador import Administrador

class AdministradorView(viewsets.ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer
    permission_strategy = UsuarioPermission()
    usuario_strategy = AdminStrategy()

    def get_permissions(self):
        return self.permission_strategy.get_permissions(self.action)

    def create(self, request, *args, **kwargs):
        try:
            self.usuario_strategy.validar_usuario(request)
            serializer = AdministradorSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, **kwargs):
        try:
            self.usuario_strategy.validar_usuario(request)
            item = self.get_object()
            serializer = self.get_serializer(item)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Http404:
            return Response({'erro': 'Objeto não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request, *args, **kwargs):
        try:
            self.usuario_strategy.validar_usuario(request)
            itens = self.get_queryset()
            
            if not itens.exists():
                return Response({'mensagem': 'Nenhum administrador encontrado'}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = self.get_serializer(itens, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def partial_update(self, request, *args, **kwargs):
        try:
            self.usuario_strategy.validar_usuario(request)

            if 'username' in request.data:
                item = get_object_or_404(Administrador, user__username=request.data.get("username"))

                serializer = self.get_serializer(item, data=request.data, partial=True)
                
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response({"erro": "Campos obrigatórios ausentes na requisição"}, status=status.HTTP_406_NOT_ACCEPTABLE)

        except Exception as e:
            return Response({'erro': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            self.usuario_strategy.validar_usuario(request)

            if 'username' in request.data:
                item = get_object_or_404(Administrador, user__username=request.data.get("username"))
                item.delete()
                return Response({'mensagem': 'Administrador deletado com sucesso'}, status=status.HTTP_204_NO_CONTENT)

            return Response({"erro": "Campos obrigatórios ausentes na requisição"}, status=status.HTTP_406_NOT_ACCEPTABLE)

        except Exception as e:
            return Response({'erro': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
