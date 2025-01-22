from rest_framework import serializers
from api.models.administrador import Administrador
from api.serializer.usuario import UsuarioSerializer

class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password' : {'write_only': True}}
        
    def create(self, validated_data):
        usuario_data = validated_data.pop('user')
        usuario_serializer = UsuarioSerializer(data=usuario_data)

        if usuario_serializer.is_valid():
            novo_usuario = usuario_serializer.save()
            admin = Administrador.objects.create(user=novo_usuario, **validated_data)
            return admin

        return None

