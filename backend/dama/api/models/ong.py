import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class Ong(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    razao_social = models.CharField(unique=True, max_length=100)
    cnpj = models.CharField(unique=True, max_length=14)
    contato = models.CharField(unique=True, max_length=20)
    bio = models.TextField(default=None)

    def __str__(self):
        return f"Razão Social: {self.razao_social}   CNPJ: {self.cnpj}"


