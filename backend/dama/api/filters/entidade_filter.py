import django_filters
from api.models.entidade import Entidade


class EntidadeFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(field_name='nome', lookup_expr='regex')

    municipio = django_filters.DateFilter(field_name='municipio', lookup_expr='regex')

    rua = django_filters.DateFilter(field_name='rua', lookup_expr='regex')

    tipo = django_filters.CharFilter(field_name='tipo', lookup_expr='exact')

    cep = django_filters.CharFilter(field_name='cep', lookup_expr='exact')

    class Meta:
        model = Entidade
        fields = ['nome', 'municipio', 'rua', 'tipo', 'cep']
