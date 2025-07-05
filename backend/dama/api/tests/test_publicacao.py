import pytest
from django.urls import reverse
from rest_framework.authtoken.models import Token
from backend.dama.api.models.publicacao import Publicacao
from api.models.usuario import Usuario

@pytest.mark.django_db
class TestPublicacaoViewSet:

    def test_create_publicacao(self, api_client, profissional):
        url = reverse('publicacao-list')
        data = {
            "conteudo": "Teste de publicacao",
            "publicador": profissional.user.username
        }
        response = api_client.post(url, data, format='json')
        assert response.status_code == 201
        assert response.data['conteudo'] == data['conteudo']
        assert response.data['publicador'] == profissional.user.username

    def test_list_publicacao(self, api_client, profissional):
        # Criar publicacao para listar
        Publicacao.objects.create(conteudo="Teste", publicador=profissional.user)
        url = reverse('publicacao-list')
        response = api_client.get(url)
        assert response.status_code == 200
        assert len(response.data) >= 1

    def test_retrieve_publicacao(self, api_client, profissional):
        publicacao = Publicacao.objects.create(conteudo="Conteudo detalhe", publicador=profissional.user)
        url = reverse('publicacao-detail', args=[publicacao.id])
        response = api_client.get(url)
        assert response.status_code == 200
        assert response.data['conteudo'] == "Conteudo detalhe"

    def test_partial_update_publicacao_forbidden(self, api_client, profissional):
        publicacao = Publicacao.objects.create(conteudo="Conteudo", publicador=profissional.user)
        url = reverse('publicacao-detail', args=[publicacao.id])
        data = {"conteudo": "Novo conteudo"}
        # Tentando atualizar sem autenticação
        response = api_client.patch(url, data, format='json')
        assert response.status_code in [401, 403]

    def test_partial_update_publicacao_as_admin(self, api_client, create_user):
        admin_user = create_user('admin1', perfil='admin')
        token, _ = Token.objects.get_or_create(user=admin_user)
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        
        other_user = create_user('user2', perfil='pro')
        publicacao = Publicacao.objects.create(conteudo="Conteudo", publicador=other_user)
        
        url = reverse('publicacao-detail', args=[publicacao.id])
        data = {"status": "aprovado"}
        response = api_client.patch(url, data, format='json')
        assert response.status_code == 200
        assert response.data['status'] == "aprovado"

    def test_delete_publicacao_forbidden(self, api_client):
        publicacao = Publicacao.objects.create(conteudo="Del publicacao", publicador=Usuario.objects.first())
        url = reverse('publicacao-detail', args=[publicacao.id])
        response = api_client.delete(url)
        assert response.status_code in [401, 403]
