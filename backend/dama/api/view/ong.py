from django.http import Http404
from rest_framework import status, viewsets
from rest_framework.response import Response
from api.models.ong import Ong
from api.serializer.ong import OngSerializer
from api.strategies.strategy_usuario import OngStrategy
from api.strategies.strategy_permissions import UsuarioPermission


class OngView(viewsets.ModelViewSet):
    queryset = Ong.objects.all()
    serializer_class = OngSerializer
    usuario_strategy = OngStrategy()
    permission_strategy = UsuarioPermission()

    def get_permissions(self):
        # Estratégia de Permissão baseada na ação
        return self.permission_strategy.get_permissions(self.action)

    def create(self, request, *args, **kwargs):
        try:
            # Validar o usuário via Strategy
            
            # Processar a criação
            serializer = OngSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'erro': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, **kwargs):
        try:
            # Validar o usuário via Strategy
            self.usuario_strategy.validar_usuario(request)
            
            # Recuperar o objeto
            item = self.get_object()
            serializer = self.get_serializer(item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Http404:
            return Response({'erro': 'Objeto não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'erro': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request, *args, **kwargs):
        try:
            # Validar o usuário via Strategy
            self.usuario_strategy.validar_usuario(request)
            
            # Listar objetos
            itens = self.get_queryset()
            if not itens.exists():
                return Response({'mensagem': 'Nenhuma ONG encontrada'}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.get_serializer(itens, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'erro': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def partial_update(self, request, *args, **kwargs):
        try:
            # Validar o usuário via Strategy
            item = self.usuario_strategy.validar_usuario(request)
            
            # Atualizar objeto
            serializer = self.get_serializer(item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'erro': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            # Validar o usuário via Strategy
            item = self.usuario_strategy.validar_usuario(request)
            
            # Deletar o objeto
            item.delete()
            return Response({'mensagem': 'ONG deletada com sucesso'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'erro': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
