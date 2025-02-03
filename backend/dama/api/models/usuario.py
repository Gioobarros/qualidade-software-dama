import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    PERFIL=(
        ('ong', 'Ong'),
        ('pro', 'Profissional'),
        ('admin', 'Administrador'),
    )
    STATUS = (
        ('sub', 'Analise'),
        ('ok', 'Aprovada'),
        ('del', 'Deletada'),
    )
    perfil = models.CharField(max_length=13, choices=PERFIL)

    status = models.CharField(max_length=8, choices=STATUS, default='sub')

    def __str__(self):
        return self.username + ' ' + self.perfil + ' ' + self.status