import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    PERFIL=(
        ('ong', 'Ong'),
        ('pro', 'Profissional'),
        ('admin', 'Administrador'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    perfil = models.CharField(max_length=13, choices=PERFIL)