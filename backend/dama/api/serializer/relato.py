from api.models.relato import Relato
from rest_framework import serializers
from api.serializer.usuario import Usuario
from django.shortcuts import get_object_or_404


class RelatoSerializer(serializers.ModelSerializer):
    publicador = serializers.CharField()
    class Meta:
        model = Relato
        fields = ['id','conteudo', 'data_criacao', 'status', 'publicador']

    def create(self, validated_data):
        username = validated_data.pop('publicador')
        usuario = get_object_or_404(Usuario, username=username)
        relato = Relato.objects.create(publicador=usuario, **validated_data)

        return relato


    def update(self, instance, validated_data):
        usuario = self.context.get('usuario')
        
        if usuario == instance.publicador or usuario.perfil == 'admin':
            for attr, value in validated_data.items():
                if attr == 'status' and usuario.perfil == 'admin':
                    setattr(instance, attr, value)
        
        instance.save()
        return instance
        