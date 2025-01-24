from rest_framework import serializers
from api.models.administrador import Administrador
from api.serializer.usuario import UsuarioSerializer

class AdministradorSerializer(serializers.ModelSerializer):
    user = UsuarioSerializer()
    class Meta:
        model = Administrador
        fields = ['user']
        extra_kwargs = {'password' : {'write_only': True}}
        
    def create(self, validated_data):
        usuario_data = validated_data.pop('user')
        usuario_serializer = UsuarioSerializer(data=usuario_data)
        usuario_serializer.is_valid(raise_exception=True)
        novo_usuario = usuario_serializer.save()

        admin = Administrador.objects.create(user=novo_usuario, **validated_data)
        return admin

