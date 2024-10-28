from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
import uuid


class UsuarioAnonimo(models.Model):
    # AO SER INSTANCIADA, CRIA APENAS A TABELA usuario_anonimo
    nome_login = models.CharField(max_length=100, blank=False)

    senha = models.CharField(max_length=20, blank=False, null=False)

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_login


class UsuarioProfissional(models.Model):
    # AO SER INSTANCIADA, CRIA APENAS A TABELA usuario_profissional
    nome_login = models.CharField(max_length=100, blank=False)

    senha = models.CharField(max_length=20, blank=False, null=False)

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    nome_completo = models.CharField(max_length=100, blank=False, null=False)

    cadastro_crp = models.CharField(max_length=11, blank=False, null=False, unique=True)
    
    telefone = models.CharField(max_length=20,blank=False, null=False)  

    email = models.EmailField(blank=False, null=False)

    def __str__(self):
        return f"Razão Social: {self.nome_completo} - CNPJ: {self.cadastro_crp} - Telefone: {self.telefone} - Email: {self.email}"


class UsuarioOng(models.Model):
    # AO SER INSTANCIADA, CRIA APENAS A TABELA usuario_ong
    nome_login = models.CharField(max_length=100, blank=False)

    senha = models.CharField(max_length=20, blank=False, null=False)

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    
    cnpj = models.CharField(max_length=11, unique=True, blank=False, null=False)

    razao_social = models.CharField(max_length=100, unique=True,blank=False, null=False)

    telefone = models.CharField(max_length=20,blank=False, null=False)  

    email = models.EmailField(blank=False, null=False)

    def __str__(self):
        return f"Razão Social: {self.razao_social} - CNPJ: {self.cnpj} - Telefone: {self.telefone} - Email: {self.email}"


class Denuncia(models.Model):
    id = models.BigAutoField(editable=False, unique=True, primary_key=True)
    
    data_denuncia = models.DateTimeField(default=timezone.now)  

    descricao_denuncia = models.TextField()
    
    idade_vitima = models.PositiveIntegerField(blank=True, null=True)

    tipo_local = models.CharField(max_length=30,blank=True,  null=True)

    relacao_autor = models.CharField(max_length=30,blank=True,  null=True)

    zona_cidade = models.CharField(max_length=30, blank=True, null=True)

    vitima_tipo = models.CharField(max_length=30,blank=True,  null=True)


    def __str__(self):
        return (
            f"Data: {self.data_denuncia.day}/{self.data_denuncia.month}/{self.data_denuncia.year} - Denunciante_id: {self.denunciante_id} \n"
            f"Descricao: {self.descricao_denuncia}"
        )


class Relato(models.Model):
    relato_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    Relato = models.TextField()
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    def dataformatada(self):
        return self.created_at.strftime('%d-%m')
    def __str__(self):
        return self.text[:500]

class Comentario(models.Model):
    id = models.BigAutoField(editable=False, unique=True, primary_key=True)

    data_comentario = models.DateTimeField(default=timezone.now) 

    relato = models.OneToOneField(Relato, on_delete=models.CASCADE, unique=True)

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)

    texto_comentario = models.TextField(blank=False, null=False)

    def __str__(self):
        return (
            f"Data: {self.data_comentario.day}/{self.data_comentario.month}/{self.data_comentario.year} - Usuario: {self.usuario.username} \n"
            f"Descricao: {self.texto_comentario}"
        )
  
    
class Material(models.Model):
    id = models.BigAutoField(editable=False, unique=True, primary_key=True)

    data_publicacao = models.DateTimeField(default=timezone.now) 

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    conteudo = models.TextField()

    arquivo_anexo = models.FileField(upload_to='anexos/', null=True, blank=True)

    def __str__(self):
        return (
            f"Data: {self.data_publicacao.day}/{self.data_publicacao.month}/{self.data_publicacao.year} - Publicante_id: {self.usuario.username} \n"
            f"Descricao: {self.conteudo}"
        )

