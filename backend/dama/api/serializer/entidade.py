from rest_framework import serializers
from api.models.entidade import Entidade

class EntidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entidade
        fields = '__all__'
        
    def create(self, validated_data):
        entidade = Entidade.objects.create(**validated_data)
        return entidade
