import uuid
from django.db import models
from api.models.usuario import Usuario


class Notificacao(models.Model):
    STATUS = (
        ('sub', 'Analise'),
        ('ok', 'Resolvida'),
        ('not', 'Negada'),
    )
    
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    conteudo = models.TextField()
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='notificacoes', default=None)
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=8, choices=STATUS, default='sub')

    def __str__(self):
        return f"publicador: {self.usuario.username} conteudo: {self.conteudo} criacao: {self.data_criacao}"   




