import pytest
from django.urls import reverse
from rest_framework.authtoken.models import Token
from api.models.relato import Relato
from api.models.usuario import Usuario

@pytest.mark.django_db
class TestRelatoViewSet:

    def test_create_relato(self, api_client, profissional):
        url = reverse('relato-list')
        data = {
            "conteudo": "Teste de relato",
            "publicador": profissional.user.username
        }
        response = api_client.post(url, data, format='json')
        assert response.status_code == 201
        assert response.data['conteudo'] == data['conteudo']
        assert response.data['publicador'] == profissional.user.username

    def test_list_relato(self, api_client, profissional):
        # Criar relato para listar
        Relato.objects.create(conteudo="Teste", publicador=profissional.user)
        url = reverse('relato-list')
        response = api_client.get(url)
        assert response.status_code == 200
        assert len(response.data) >= 1

    def test_retrieve_relato(self, api_client, profissional):
        relato = Relato.objects.create(conteudo="Conteudo detalhe", publicador=profissional.user)
        url = reverse('relato-detail', args=[relato.id])
        response = api_client.get(url)
        assert response.status_code == 200
        assert response.data['conteudo'] == "Conteudo detalhe"

    def test_partial_update_relato_forbidden(self, api_client, profissional):
        relato = Relato.objects.create(conteudo="Conteudo", publicador=profissional.user)
        url = reverse('relato-detail', args=[relato.id])
        data = {"conteudo": "Novo conteudo"}
        # Tentando atualizar sem autenticação
        response = api_client.patch(url, data, format='json')
        assert response.status_code in [401, 403]

    def test_partial_update_relato_as_admin(self, api_client, create_user):
        admin_user = create_user('admin1', perfil='admin')
        token, _ = Token.objects.get_or_create(user=admin_user)
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        
        other_user = create_user('user2', perfil='pro')
        relato = Relato.objects.create(conteudo="Conteudo", publicador=other_user)
        
        url = reverse('relato-detail', args=[relato.id])
        data = {"status": "aprovado"}
        response = api_client.patch(url, data, format='json')
        assert response.status_code == 200
        assert response.data['status'] == "aprovado"

    def test_delete_relato_forbidden(self, api_client):
        relato = Relato.objects.create(conteudo="Del relato", publicador=Usuario.objects.first())
        url = reverse('relato-detail', args=[relato.id])
        response = api_client.delete(url)
        assert response.status_code in [401, 403]
