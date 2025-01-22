from api.models.ong import Ong
from api.serializer.usuario import UsuarioSerializer
from rest_framework import serializers

class OngSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ong
        fields = ['username', 'password', 'email', 'razao_social', 'cnpj', 'contato']
        extra_kwargs = {'password' : {'write_only': True}}
        
    def create(self, validated_data):
        usuario_data = validated_data.pop('user')
        usuario_serializer = UsuarioSerializer(data=usuario_data)

        if usuario_serializer.is_valid():
            novo_usuario = usuario_serializer.save()
            ong = Ong.objects.create(user=novo_usuario, **validated_data)
            return ong

        return None