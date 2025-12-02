from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http import Http404


class BaseModelViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except ValueError as e:
            return Response({"erro": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        try:
            item = self.get_object()
            serializer = self.get_serializer(item)
            return Response(serializer.data)

        except Http404:
            return Response(
                {'erro': 'não encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )

        except Exception as e:
            return Response(
                {"erro": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def list(self, request, *args, **kwargs):
        try:
            itens = self.filter_queryset(self.get_queryset())

            if not itens.exists():
                return Response(
                    {'mensagem': 'Nenhum item encontrado'},
                    status=status.HTTP_204_NO_CONTENT
                )

            serializer = self.get_serializer(itens, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"erro": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
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

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"erro": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def destroy(self, request, *args, **kwargs):
        try:
            if 'id' in request.data:
                item_id = request.data['id']
                item = self.queryset.get(id=item_id)
            else:
                item = self.get_object()

            item.delete()
            return Response(
                {'mensagem': 'Item excluído com sucesso'},
                status=status.HTTP_204_NO_CONTENT
            )

        except Exception as e:
            return Response(
                {"erro": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )