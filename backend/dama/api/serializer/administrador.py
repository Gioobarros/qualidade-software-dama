from rest_framework import serializers
from api.models.administrador import Administrador

class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = "__all__"
        