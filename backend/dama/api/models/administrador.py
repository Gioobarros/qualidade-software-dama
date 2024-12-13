import uuid
from django.db import models
from django.contrib.auth.models import User


class Administrador(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    login = models.CharField(unique=True, max_length=100)
    senha = models.CharField(unique=True, max_length=20)

    def __str__(self):
        return f"Login: {self.login}"


