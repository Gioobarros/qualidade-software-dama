from django.http import Http404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.serializer.profissional import ProfissionalSerializer, Profissional
from api.strategies.strategy_usuario import ProfissionalStrategy
from api.strategies.strategy_permissions import UsuarioPermission


class ProfissionalView(viewsets.ModelViewSet):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer
    permission_strategy = UsuarioPermission()
    usuario_strategy = ProfissionalStrategy()

    def get_permissions(self):
        return self.permission_strategy.get_permissions(self.action)

    def create(self, request, *args, **kwargs):
        try:
            # Valida o perfil do usuário

            # Serializa os dados para criação
            serializer = ProfissionalSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def retrieve(self, request, *args, **kwargs):
        try:
            # Valida o perfil do usuário
            self.usuario_strategy.validar_usuario(request)

            # Recupera o objeto
            item = self.get_object()
            serializer = self.get_serializer(item)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        except Http404:
            return Response({'erro': 'Objeto não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request, *args, **kwargs):
        try:
            # Valida o perfil do usuário
            self.usuario_strategy.validar_usuario(request)

            # Lista os objetos
            itens = self.get_queryset()
            if not itens.exists():
                return Response({'mensagem': 'Nenhum profissional encontrado'}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = self.get_serializer(itens, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def partial_update(self, request, *args, **kwargs):
        try:
            # Valida o perfil do usuário
            self.usuario_strategy.validar_usuario(request)

            if 'username' in request.data:
                item = get_object_or_404(Profissional, user__username=request.data.get("username"))

                # Atualiza parcialmente o objeto
                serializer = self.get_serializer(item, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response({"erro": "Campos obrigatórios ausentes na requisição"}, status=status.HTTP_406_NOT_ACCEPTABLE)

        except Exception as e:
            return Response({'erro': 'Problema na API'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        try:
            # Valida o perfil do usuário
            self.usuario_strategy.validar_usuario(request)

            if 'username' in request.data:
                item = get_object_or_404(Profissional, user__username=request.data.get("username"))

                # Verifica se o usuário tem permissão para deletar
                if item.user.perfil == 'pro':
                    item.delete()
                    return Response({'mensagem': 'Profissional deletado com sucesso'}, status=status.HTTP_204_NO_CONTENT)
                else:
                    return Response({'erro': 'Usuário não tem permissão para ser excluído'}, status=status.HTTP_403_FORBIDDEN)

            return Response({"erro": "Campos obrigatórios ausentes na requisição"}, status=status.HTTP_406_NOT_ACCEPTABLE)

        except Exception as e:
            return Response({'erro': 'Problema na API'}, status=status.HTTP_404_NOT_FOUND)
