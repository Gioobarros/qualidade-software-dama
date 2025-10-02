from django.db import models


class Entidade(models.Model):
    TIPO = (
        ('policial', 'Policial'),
        ('medica', 'Medica'),
        ('juridica', 'Juridica'),
    )

    nome = models.CharField(unique=True, max_length=100)
    municipio = models.CharField(unique=True, max_length=100)
    cep = models.CharField(max_length=8)
    rua = models.CharField(max_length=100, blank=True, null=True)
    contato = models.CharField(unique=True, max_length=20)
    tipo = models.CharField(max_length=20, choices=TIPO, default='policial')
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"Entidade: {self.nome}   Endereço: {self.rua} {self.municipio} {self.cep} Contato: {self.contato} {self.email}"


