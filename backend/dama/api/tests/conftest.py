import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from api.models.usuario import Usuario
from api.models.profissional import Profissional
from api.models.ong import Ong
from rest_framework.authtoken.models import Token

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user(db):
    def make_user(username, password='testpass123', perfil='pro'):
        user = Usuario.objects.create_user(username=username, password=password, perfil=perfil)
        return user
    return make_user

@pytest.fixture
def profissional(create_user):
    user = create_user('profissional1', perfil='pro')
    profissional = Profissional.objects.create(user=user, nome_completo="Pro User", conselho="123", cpf="000.000.000-00", contato="contato")
    return profissional

@pytest.fixture
def ong(create_user):
    user = create_user('ong1', perfil='ong')
    ong = Ong.objects.create(user=user, razao_social="Razao Social ONG", cnpj="00.000.000/0000-00", contato="contato")
    return ong

@pytest.fixture
def token(profissional):
    token, _ = Token.objects.get_or_create(user=profissional.user)
    return token

@pytest.fixture
def auth_client(api_client, token):
    api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    return api_client
