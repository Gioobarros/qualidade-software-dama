from rest_framework import serializers
from api.models import Profissional

class ProfissionalSerializer(serializers.ModelSerializer):
    class meta:
        model = Profissional
        fields = "__all__"
        