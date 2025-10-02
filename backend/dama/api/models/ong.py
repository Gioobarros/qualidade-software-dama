import uuid
from api.models.usuario import Usuario
from django.db import models



class Ong(models.Model):
    razao_social = models.CharField(unique=True, max_length=100)
    cnpj = models.CharField(unique=True, max_length=14)
    contato = models.CharField(unique=True, max_length=20)
    bio = models.TextField(blank=True, null=True, default=None)
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, blank=True, null=True, related_name='ong')

    def __str__(self):
        return f"Razão Social: {self.razao_social}   CNPJ: {self.cnpj}"


