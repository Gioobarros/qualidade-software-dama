from django.http import Http404
from rest_framework import status, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from api.filters.usuario_filter import UsuarioFilter  # Certifique-se de importar o filtro correto
from api.serializer.usuario import UsuarioSerializer, Usuario

class UsuarioView(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UsuarioFilter  # Aplicando o filtro correto

    def get_permissions(self):
        if self.action in ['partial_update', 'destroy']:
            return [IsAuthenticated()]
        return [AllowAny()]

    def create(self, request, *args, **kwargs):
        serializer = UsuarioSerializer(data=request.data)
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
            itens = self.filter_queryset(self.get_queryset())  # Aplicando os filtros corretamente
            if not itens.exists():
                return Response({'mensagem': 'Nenhum usuário foi achado'}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.get_serializer(itens, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def partial_update(self, request, *args, **kwargs):
        try:
            if 'username' in request.data:
                item = get_object_or_404(Usuario, username=request.data.get("username"))
                serializer = self.get_serializer(item, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"erro": "campos obrigatórios ausentes na requisição"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception:
            return Response({'erro': 'problema na api'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        try:
            if 'username' in request.data:
                item = get_object_or_404(Usuario, username=request.data.get("username"))
                item.delete()
                return Response({'mensagem': 'Usuario deletado com sucesso'}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"erro": "campos obrigatórios ausentes na requisição"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception:
            return Response({'erro': 'problema na api'}, status=status.HTTP_404_NOT_FOUND)
