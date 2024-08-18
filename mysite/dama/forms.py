import re
from django import forms
from .models import Usuario, UsuarioOng, UsuarioProfissional
from .models import Denuncia, Relato
from django.core.validators import RegexValidator


class UsuarioAnonimoForm(forms.Form):
    senha = forms.CharField(min_length=8, widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        fields = ['nome_login', 'senha']


class UsuarioOngForm(forms.Form):
    nome_login = forms.CharField(label='Nome de Usuario')
    
    senha = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Senha')
    
    razao_social = forms.CharField(min_length=1, label='Razão Social')
    
    cnpj = forms.CharField(min_length=14, max_length=14, label='CNPJ')
    
    email = forms.EmailField(label='Email')

    validador_telefone = RegexValidator(
        regex=r'^\d{2}\s*\d{5}-\d{4}$',
        message='Número de telefone inválido. Formato esperado: 84 91234-5678'
    )

    telefone = forms.CharField(
        label='Contato',
        validators=[validador_telefone],
        max_length=14
    )
    
    class Meta:
        model = UsuarioOng
        fields = ['nome_login', 'senha', 'razao_social', 'cnpj', 'email', 'telefone']


class UsuarioProfissionalForm(forms.Form):
    nome_login = forms.CharField(label='Nome de Usuario')
    
    senha = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Senha')
    
    nome_completo = forms.CharField(max_length=100, label='Nome Completo')

    validador_crp = RegexValidator(
        regex=r'^\d{2}\s*\d{5}$',
        message='CRP inserido é inválido'
        )

    cadastro_crp = forms.CharField(
        min_length=9,
        validators=[validador_crp], 
        label='CRP'
        )
    
    email = forms.EmailField(label='Email')

    validador_telefone = RegexValidator(
        regex=r'^\d{2}\s*\d{5}-\d{4}$',
        message='Número de telefone inválido. Formato esperado: 84 91234-5678'
    )

    telefone = forms.CharField(
        label='Contato',
        validators=[validador_telefone],
        max_length=14
    )
    
    class Meta:
        model = UsuarioOng
        fields = ['nome_login', 'senha', 'nome_completo', 'cadastro_crp', 'email', 'telefone']


class DenunciaForm(forms.Form):
    descricao_denuncia = forms.CharField(label='Descrição')
    
    idade_vitima = forms.IntegerField(label='Idade da Vitima')

    tipo_local = forms.CharField(label='Local da Violência')

    relacao_autor = forms.CharField(label='Relação com Agressor')

    zona_cidade = forms.CharField(label='Zona da Cidade Onde Ocorreu a Violência')

    vitima_tipo = forms.CharField(label='Vitima da Agressão')

    class Meta:
        model = Denuncia
        fields = ['idade_vitima', 'vitima_tipo', 'relacao_autor', 'tipo_local', 'zona_cidade', 'descricao_denuncia']

class RelatoForm(forms.ModelForm):
    texto_relato = forms.CharField(widget=forms.Textarea, label='texto_relato')

    class Meta:
        model = Relato
        fields = ['texto_relato']





# class Teste(forms.ModelForm):
#     senha = forms.CharField(min_length=1, widget=forms.PasswordInput)

#     confirmar_senha = forms.CharField(
#         min_length=1,
#         widget=forms.PasswordInput,
#         label='Confirmar Senha'
#     )

#     class Meta:
#         model = Usuario
#         fields = ['nome_login', 'senha']

#     def clean(self):
#         cleaned_data = super().clean()

#         senha = cleaned_data.get("senha")

#         confirmar_senha = cleaned_data.get("confirmar_senha")

#         if senha is not None and confirmar_senha is not None and senha != confirmar_senha:
#             self.add_error('confirmar_senha', 'As senhas não coincidem.')

#         return cleaned_data





