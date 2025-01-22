from api.models.relato import Relato
from rest_framework import serializers

class RelatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relato
        fields = ['conteudo', 'publicador', 'data_criacao']

    def create(self, validated_data):
        relato = Relato.objects.create(**validated_data)
        return relato
        