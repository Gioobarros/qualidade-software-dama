from rest_framework import serializers
from api.models.ong import Ong

class OngSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ong
        fields = "__all__"
        