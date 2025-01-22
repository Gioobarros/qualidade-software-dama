from rest_framework import serializers
from api.serializer.usuario import UsuarioSerializer
from api.models.profissional import Profissional

class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = ['username', 'password', 'email', 'nome_completo', 'conselho', 'cpf', 'contato']
        extra_kwargs = {'password' : {'write_only': True}}
        
    def create(self, validated_data):
        usuario_data = validated_data.pop('user')
        usuario_serializer = UsuarioSerializer(data=usuario_data)

        if usuario_serializer.is_valid():
            novo_usuario = usuario_serializer.save()
            profissional = Profissional.objects.create(user=novo_usuario, **validated_data)
            return profissional

        return None
