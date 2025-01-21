from rest_framework import serializers
from api.models.ong import Ong

class OngSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ong
        fields = ['username', 'password', 'email', 'razao_social', 'cnpj', 'contato']
        extra_kwargs = {'password' : {'write_only': True}}
        
    def create(self, validated_data):
        ong = Ong.objects.create_user(**validated_data)
        return ong