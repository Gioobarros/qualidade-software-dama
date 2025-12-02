from api.models.usuario import Usuario
from api.serializer.usuario import UsuarioSerializer
from api.filters.usuario_filter import UsuarioFilter
from .base import BaseModelViewSet


class UsuarioView(BaseModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filterset_class = UsuarioFilter