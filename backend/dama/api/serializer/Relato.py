from rest_framework import serializers
from api.models import Relato

class RelatoSerializer(serializers.ModelSerializer):
    class meta:
        model = Relato
        fields = "__all__"
        