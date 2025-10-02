import uuid
from django.db import models
from api.models.usuario import Usuario


class Publicacao(models.Model):
    STATUS = (
        ('sub', 'Analise'),
        ('ok', 'Aprovada'),
        ('del', 'Deletada'),
    )

    TAGS = (
        ('relato', 'Relato'),
        ('noticia', 'Noticia'),
        ('estatistica', 'Estatistica'),
        ('projeto', 'Projeto'),
    )

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    conteudo = models.TextField()
    publicador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='publicacoes')
    data_criacao = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=11, choices=TAGS, default='vazio')
    imagem_publicacao = models.ImageField(upload_to='publicacoes', default='media/dama.png', blank=True, null=True)
    status = models.CharField(max_length=8, choices=STATUS, default='sub')

    def __str__(self):
        return f"publicador: {self.publicador.username} tag: {self.tag} conteudo: {self.conteudo} criacao: {self.data_criacao}"   


