from rest_framework import serializers
from api.models.administrador import Administrador

class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password' : {'write_only': True}}
        
    def create(self, validated_data):
        admin = Administrador.objects.create_user(**validated_data)
        return admin
        