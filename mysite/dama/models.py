from django.db import models
import uuid

class UsuarioAnonimo(models.Model):
    usuario_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nome_login = models.CharField(max_length=40, unique=True)
    senha = models.CharField(max_length=20)

class UsuarioProfissional(models.Model):
    nome_login = ""
    senha = ""


class UsuarioOng(models.Model):
    nome_login = ""

# Create your models here.
