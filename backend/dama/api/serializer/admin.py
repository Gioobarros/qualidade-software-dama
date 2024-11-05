from rest_framework import serializers
from api.models import Admin

class AdminSerializer(serializers.ModelSerializer):
    class meta:
        model = Admin
        fields = "__all__"
        