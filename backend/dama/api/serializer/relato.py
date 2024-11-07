from api.models.relato import Relato
from rest_framework import serializers

class RelatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relato
        fields = "__all__"
        