import uuid
from django.db import models
from django.contrib.auth.models import User


class Profissional(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome_completo = models.CharField(max_length=100)
    cpf = models.CharField(unique=True, max_length=11)
    login = models.CharField(unique=True, max_length=100)
    senha = models.CharField(max_length=20)
    conselho = models.CharField(unique=True, max_length=20)
    contato = models.CharField(unique=True, max_length=20)
    email = models.EmailField(unique=True, max_length=40)
    bio = models.TextField()

    def __str__(self):
        return f"Nome completo: {self.nome_completo}   Conselho: {self.conselho}\nEmail: {self.email} Contato: {self.contato}"


