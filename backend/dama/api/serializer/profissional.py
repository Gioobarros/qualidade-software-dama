from rest_framework import serializers
from api.models.profissional import Profissional

class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = ['username', 'password', 'email', 'nome_completo', 'conselho', 'cpf', 'contato']
        extra_kwargs = {'password' : {'write_only': True}}
        
    def create(self, validated_data):
        profissional = Profissional.objects.create_user(**validated_data)
        return profissional
    
    # atualização ocorre com autenticação
    # def update(self, instance, validated_data):
    #     return None