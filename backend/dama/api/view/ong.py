from rest_framework import status
from rest_framework.response import Response
from api.models.ong import Ong
from api.serializer.ong import OngSerializer
from api.strategies.strategy_usuario import OngStrategy
from api.strategies.strategy_permissions import UsuarioPermission
from api.view.base import BaseModelViewSet
from api.constants import MESSAGES


class OngView(BaseModelViewSet):
    queryset = Ong.objects.all()
    serializer_class = OngSerializer
    usuario_strategy = OngStrategy()
    permission_strategy = UsuarioPermission()

    def get_permissions(self):
        return self.permission_strategy.get_permissions(self.action)

    def retrieve(self, request, *args, **kwargs):
        try:
            self.usuario_strategy.validar_usuario(request)
            return super().retrieve(request, *args, **kwargs)
        except Exception as error:
            return self._handle_server_error(error)

    def list(self, request, *args, **kwargs):
        try:
            self.usuario_strategy.validar_usuario(request)
            itens = self.filter_queryset(self.get_queryset())

            if not itens.exists():
                return Response(
                    {MESSAGES['message']: MESSAGES['no_ong']},
                    status=status.HTTP_404_NOT_FOUND
                )
            serializer = self.get_serializer(itens, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return self._handle_server_error(error)

    def partial_update(self, request, *args, **kwargs):
        try:
            self.usuario_strategy.validar_usuario(request)
            return super().partial_update(request, *args, **kwargs)
        except Exception as error:
            return self._handle_server_error(error)

    def destroy(self, request, *args, **kwargs):
        try:
            item = self.usuario_strategy.validar_usuario(request)
            item.delete()
            return Response(
                {MESSAGES['message']: MESSAGES['ong_deleted']},
                status=status.HTTP_204_NO_CONTENT
            )
        except Exception as error:
            return self._handle_server_error(error)
