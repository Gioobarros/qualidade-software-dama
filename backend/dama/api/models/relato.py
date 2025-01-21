import uuid
from django.db import models
from profissional import Profissional


class Relato(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    conteudo = models.TextField()
    publicador = models.ForeignKey(Profissional, on_delete=models.CASCADE, related_name='relatos', default=None)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"publicador: {self.publicador.username} conteudo: {self.conteudo} criacao: {self.data_criacao}"   


