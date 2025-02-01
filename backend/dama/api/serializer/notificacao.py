from rest_framework import serializers
from api.models.usuario import Usuario
from api.serializer.usuario import Usuario, UsuarioSerializer
from api.models.notificacao import Notificacao
  

class NotificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacao
        fields = ['id', 'conteudo', 'user', 'data_criacao', 'status']

    def create(self, validated_data):
        usuario_data = validated_data.pop('user')
        usuario_serializer = UsuarioSerializer(data=usuario_data)
        usuario_serializer.is_valid(raise_exception=True)
        novo_usuario = usuario_serializer.save()

        notificaccao = Notificacao.objects.create(user=novo_usuario, **validated_data)

        return notificaccao

        


