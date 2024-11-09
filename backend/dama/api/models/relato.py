import uuid
from django.db import models
from django.contrib.auth.models import User


class Relato(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # publicador_id = models.ForeignKey(uuid, on_delete=models.CASCADE)

    conteudo = models.TextField()

    def __str__(self):
        return f"Publicador: {self.publicador_id}"   


