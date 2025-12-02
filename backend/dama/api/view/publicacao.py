from rest_framework.permissions import IsAuthenticated
from api.models.publicacao import Publicacao
from api.serializer.publicacao import PublicacaoSerializer
from api.filters.publicacao_filter import PublicacaoFilter
from .base import BaseModelViewSet


class PublicacaoView(BaseModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Publicacao.objects.all()
    serializer_class = PublicacaoSerializer
    filterset_class = PublicacaoFilter