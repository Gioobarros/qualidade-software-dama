from rest_framework import serializers
from api.models.usuario import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'perfil', 'password', 'status']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        usuario = Usuario.objects.create_user(**validated_data)
        return usuario