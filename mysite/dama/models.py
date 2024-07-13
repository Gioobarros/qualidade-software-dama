import uuid
from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    usuario_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    nome_login = models.CharField(max_length=40, unique=True)

    senha = models.CharField(max_length=20)

    def __str__(self):
        return self.nome_login

class UsuarioProfissional(Usuario):
    nome_completo = models.CharField(max_length=100)

    cadastro_crp = models.CharField(max_length=11, unique=True)

    telefone = models.CharField(max_length=20)

    email = models.EmailField()

    def __str__(self):
        return f"Nome: {self.nome_completo} - CRP: {self.cadastro_crp} - 
        Telefone: {self.telefone} - Email: {self.email}"

class UsuarioOng(Usuario):
    cnpj = models.CharField(max_length=11, unique=True)

    razao_social = models.CharField(max_length=100, unique=True)

    telefone = models.CharField(max_length=20)  

    email = models.EmailField()

    def __str__(self):
        return f"Razão Social: {self.razao_social} - CNPJ: {self.cnpj} - 
        Telefone: {self.telefone} - Email: {self.email}"
    

class Denuncia(models.Model):
    denuncia_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    denunciante_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, unique=True)
    
    data_denuncia = models.DateTimeField(default=timezone.now)  

    descricao_denuncia = models.CharField(max_length=200)
    
    idade_vitima = models.PositiveIntegerField(null=True)

    tipo_local = models.CharField(max_length=30, null=True)

    relacao_autor = models.CharField(max_length=30, null=True)

    zona_cidade = models.CharField(max_length=30, null=True)


    def __str__(self):
        return (
            f"Data: {self.data_denuncia.day}/{self.data_denuncia.month}/{self.data_denuncia.year} - Denunciante_id: {self.denunciante_id} \n"
            f"Descricao: {self.descricao_denuncia}"
        )

class Relato(models.Model):
    relato_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    data_relato = models.DateTimeField(default=timezone.now) 

    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, unique=True)

    texto_relato = models.TextField()

    def __str__(self):
        return (
            f"Data: {self.data_relato.day}/{self.data_relato.month}/{self.data_relato.year} - Usuario_id: {self.usuario_id} \n"
            f"Descricao: {self.texto_relato}"
        )

class Comentario(models.Model):
    comentario_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    data_comentario = models.DateTimeField(default=timezone.now) 

    relato_id = models.ForeignKey(Relato, on_delete=models.CASCADE, unique=True)

    usuario_id = models.UUIDField(editable=False)

    texto_comentario = models.CharField(max_length=190)

    def __str__(self):
        return (
            f"Data: {self.data_comentario.day}/{self.data_comentario.month}/{self.data_comentario.year} - Usuario_id: {self.usuario_id} \n"
            f"Descricao: {self.texto_comentario}"
        )
    

class Material(models.Model):
    material_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    data_publicacao = models.DateTimeField(default=timezone.now) 

    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, unique=True)

    conteudo = models.TextField()

    arquivo_anexo = models.FileField(upload_to='anexos/', null=True, blank=True)

    def __str__(self):
        return (
            f"Data: {self.data_publicacao.day}/{self.data_publicacao.month}/{self.data_publicacao.year} - Publicante_id: {self.usuario_id} \n"
            f"Descricao: {self.conteudo}"
        )

