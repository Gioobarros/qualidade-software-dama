import django_filters
from api.models.publicacao import Publicacao


class PublicacaoFilter(django_filters.FilterSet):
    palavra_chave = django_filters.CharFilter(field_name='conteudo', lookup_expr='regex')

    data_inicio = django_filters.DateFilter(field_name='data_criacao', lookup_expr='gte')

    data_fim = django_filters.DateFilter(field_name='data_criacao', lookup_expr='lte')

    status = django_filters.CharFilter(field_name='status', lookup_expr='exact')

    tag = django_filters.CharFilter(field_name='tag', lookup_expr='exact')

    class Meta:
        model = Publicacao
        fields = ['palavra_chave', 'data_criacao', 'tag']
