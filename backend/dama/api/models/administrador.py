import uuid
from api.models.usuario import Usuario, models


class Administrador(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, blank=True, null=True, related_name='admin')

    def __str__(self):
        return f"Login: {self.username}"


