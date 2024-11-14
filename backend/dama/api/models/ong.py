import uuid
from django.db import models
from django.contrib.auth.models import User


class Ong(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    razao_social = models.CharField(unique=True, max_length=100)
    cnpj = models.CharField(unique=True, max_length=14)
    login = models.CharField(unique=True, max_length=100)
    senha = models.CharField(unique=True, max_length=20)
    contato = models.CharField(unique=True, max_length=20)
    email = models.EmailField(unique=True, max_length=40)
    bio = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"Razão Social: {self.razao_social}   CNPJ: {self.cnpj}\nEmail: {self.email} Contato: {self.contato}"


