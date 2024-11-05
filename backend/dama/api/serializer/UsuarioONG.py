from rest_framework import serializers
from api.models import ONG

class ONGSerializer(serializers.ModelSerializer):
    class meta:
        model = ONG
        fields = "__all__"
        