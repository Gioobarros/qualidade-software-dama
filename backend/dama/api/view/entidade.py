from rest_framework.permissions import IsAuthenticated
from api.models.entidade import Entidade
from api.serializer.entidade import EntidadeSerializer
from api.filters.entidade_filter import EntidadeFilter
from .base import BaseModelViewSet


class EntidadeView(BaseModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Entidade.objects.all()
    serializer_class = EntidadeSerializer
    filterset_class = EntidadeFilter