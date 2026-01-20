from rest_framework import status
from rest_framework.response import Response
from api.models.ong import Ong
from api.serializer.ong import OngSerializer
from api.strategies.strategy_usuario import OngStrategy
from api.strategies.strategy_permissions import UsuarioPermission
from api.view.base import UsuarioValidatedViewSet
from api.constants import MESSAGES


class OngView(UsuarioValidatedViewSet):
    queryset = Ong.objects.all()
    serializer_class = OngSerializer
    usuario_strategy = OngStrategy()
    permission_strategy = UsuarioPermission()

    def get_permissions(self):
        return self.permission_strategy.get_permissions(self.action)

    def list(self, request, *args, **kwargs):
        return self._list_ongs(request)

    def partial_update(self, request, *args, **kwargs):
        """Atualiza parcialmente uma ONG."""
        def update_action():
            return super(OngView, self).partial_update(request, *args, **kwargs)
        return self._validated_action(request, update_action)

    def destroy(self, request, *args, **kwargs):
        """Remove uma ONG."""
        return self._validated_action(
            request,
            self._delete_ong,
            passes_validated_user=True
        )

    def _list_ongs(self, request):
        itens = self.filter_queryset(self.get_queryset())

        if not itens.exists():
            return Response(
                {MESSAGES['message']: MESSAGES['no_ong']},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(itens, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def _delete_ong(self, validated_user):
        if validated_user:
            validated_user.delete()
        return Response(
            {MESSAGES['message']: MESSAGES['ong_deleted']},
            status=status.HTTP_204_NO_CONTENT
        )
