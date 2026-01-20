"""Módulo de visualizações para entidade Profissional."""
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from api.models.profissional import Profissional
from api.serializer.profissional import ProfissionalSerializer
from api.strategies.strategy_usuario import ProfissionalStrategy
from api.strategies.strategy_permissions import UsuarioPermission
from api.view.base import UsuarioValidatedViewSet
from api.constants import MESSAGES, FIELDS, PERFIS


class ProfissionalView(UsuarioValidatedViewSet):
    """ViewSet para gerenciar Profissional."""
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer
    permission_strategy = UsuarioPermission()
    usuario_strategy = ProfissionalStrategy()

    def get_permissions(self):
        return self.permission_strategy.get_permissions(self.action)

    def partial_update(self, request, *args, **kwargs):
        return self._validated_action(
            request,
            lambda: self._partial_update_profissional(request, *args, **kwargs)
        )

    def destroy(self, request, *args, **kwargs):
        return self._validated_action(
            request,
            lambda: self._delete_profissional(request)
        )

    def _partial_update_profissional(self, request):
        if FIELDS['username'] not in request.data:
            return Response(
                {MESSAGES['error']: MESSAGES['missing_required_fields']},
                status=status.HTTP_406_NOT_ACCEPTABLE
            )

        item = get_object_or_404(
            Profissional,
            user__username=request.data.get(FIELDS['username'])
        )

        serializer = self.get_serializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return self._handle_serializer_error(serializer.errors)

    def _delete_profissional(self, request):
        if FIELDS['username'] not in request.data:
            return Response(
                {MESSAGES['error']: MESSAGES['missing_required_fields']},
                status=status.HTTP_406_NOT_ACCEPTABLE
            )

        item = get_object_or_404(
            Profissional,
            user__username=request.data.get(FIELDS['username'])
        )

        if item.user.perfil == PERFIS['professional']:
            item.delete()
            return Response(
                {MESSAGES['message']: MESSAGES['professional_deleted']},
                status=status.HTTP_204_NO_CONTENT
            )

        return Response(
            {MESSAGES['error']: MESSAGES['no_permission']},
            status=status.HTTP_403_FORBIDDEN
        )
