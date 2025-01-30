from api.models.ong import Ong
from api.serializer.usuario import UsuarioSerializer
from rest_framework import serializers

class OngSerializer(serializers.ModelSerializer):
    user = UsuarioSerializer()
    bio = serializers.CharField(read_only=True)
    class Meta:
        model = Ong
        fields = ['user', 'razao_social', 'cnpj', 'contato', 'bio']
        extra_kwargs = {'password' : {'write_only': True}}
        
    def create(self, validated_data):
        usuario_data = validated_data.pop('user')
        usuario_serializer = UsuarioSerializer(data=usuario_data)
        usuario_serializer.is_valid(raise_exception=True)
        novo_usuario = usuario_serializer.save()

        ong = Ong.objects.create(user=novo_usuario, **validated_data)
        return ong