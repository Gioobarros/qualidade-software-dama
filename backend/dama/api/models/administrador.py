import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class Administrador(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"Login: {self.username}"


