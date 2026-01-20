from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http import Http404
from api.constants import MESSAGES, FIELDS


class BaseModelViewSet(viewsets.ModelViewSet):
    def _handle_serializer_error(self, serializer_errors):
        """Centraliza o tratamento de erros de serialização."""
        return Response(serializer_errors, status=status.HTTP_400_BAD_REQUEST)

    def _handle_server_error(self, error):
        """Centraliza o tratamento de erros do servidor."""
        return Response(
            {MESSAGES['error']: str(error)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    def _validated_action(self, request, action_callable, passes_validated_user=False):
        """Executa a ação após validar o usuário, centralizando o try/except."""
        try:
            validated_user = None
            if hasattr(self, 'usuario_strategy'):
                validated_user = self.usuario_strategy.validar_usuario(request)

            if passes_validated_user:
                return action_callable(validated_user)
            return action_callable()

        except Exception as error:  # fallback para garantir resposta consistente
            return self._handle_server_error(error)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return self._handle_serializer_error(serializer.errors)

        except ValueError as error:
            return Response(
                {MESSAGES['error']: str(error)},
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, *args, **kwargs):
        try:
            item = self.get_object()
            serializer = self.get_serializer(item)
            return Response(serializer.data)

        except Http404:
            return Response(
                {MESSAGES['error']: MESSAGES['not_found']},
                status=status.HTTP_404_NOT_FOUND
            )

    def list(self, request, *args, **kwargs):
        try:
            itens = self.filter_queryset(self.get_queryset())

            if not itens.exists():
                return Response(
                    {MESSAGES['message']: MESSAGES['no_items']},
                    status=status.HTTP_204_NO_CONTENT
                )

            serializer = self.get_serializer(itens, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Http404:
            return Response(
                {MESSAGES['error']: MESSAGES['not_found']},
                status=status.HTTP_404_NOT_FOUND
            )

    def partial_update(self, request, *args, **kwargs):
        try:
            item = self.get_object()

            serializer = self.get_serializer(
                item,
                data=request.data,
                partial=True
            )

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

            return self._handle_serializer_error(serializer.errors)

        except Http404:
            return Response(
                {MESSAGES['error']: MESSAGES['not_found']},
                status=status.HTTP_404_NOT_FOUND
            )

    def destroy(self, request, *args, **kwargs):
        try:
            if FIELDS['id'] in request.data:
                item_id = request.data[FIELDS['id']]
                item = self.queryset.get(id=item_id)
            else:
                item = self.get_object()

            item.delete()
            return Response(
                {MESSAGES['message']: MESSAGES['deleted_success']},
                status=status.HTTP_204_NO_CONTENT
            )

        except Http404:
            return Response(
                {MESSAGES['error']: MESSAGES['not_found']},
                status=status.HTTP_404_NOT_FOUND
            )
