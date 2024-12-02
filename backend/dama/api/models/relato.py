import uuid
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Relato(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(default=datetime.now, editable=False)

    def __str__(self):
        return f"id: {self.id} conteudo: {self.conteudo}"   


