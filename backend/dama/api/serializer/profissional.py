from rest_framework import serializers
from api.serializer.usuario import UsuarioSerializer
from api.models.profissional import Profissional

class ProfissionalSerializer(serializers.ModelSerializer):
    user = UsuarioSerializer()
    class Meta:
        model = Profissional
        fields = ['nome_completo', 'conselho', 'cpf', 'contato', 'user']
        extra_kwargs = {'password' : {'write_only': True}}
        
    def create(self, validated_data):
        usuario_data = validated_data.pop('user')
        usuario_serializer = UsuarioSerializer(data=usuario_data)
        usuario_serializer.is_valid(raise_exception=True)
        novo_usuario = usuario_serializer.save()

        profissional = Profissional.objects.create(user=novo_usuario, **validated_data)
        return profissional
