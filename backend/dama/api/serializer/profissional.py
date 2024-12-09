from rest_framework import serializers
from api.models.profissional import Profissional

class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = ['nome_completo', 'cpf', 'login', 'senha', 'conselho', 'contato', 'email', 'bio']
        