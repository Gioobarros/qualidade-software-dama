import django_filters
from models.usuario import Usuario


class UsuarioFilter(django_filters.FilterSet):
    login = django_filters.CharFilter(field_name='username', lookup_expr='exact')
    situacao = django_filters.CharFilter(field_name='status', lookup_expr='exact')
    tipo_perfil = django_filters.CharFilter(field_name='perfil', lookup_expr='exact')


    class Meta:
        model = Usuario
        fields = ['username', 'status', 'perfil']