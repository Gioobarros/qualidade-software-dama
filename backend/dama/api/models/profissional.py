import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class Profissional(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome_completo = models.CharField(max_length=100)
    cpf = models.CharField(unique=True, max_length=11)
    conselho = models.CharField(unique=True, max_length=20)
    contato = models.CharField(unique=True, max_length=20)
    bio = models.TextField(default=None)

    def __str__(self):
        return f"Nome completo: {self.nome_completo}   Conselho: {self.conselho}\nEmail: {self.email} Contato: {self.contato}"


