import pytest
from django.urls import reverse
from api.models.profissional import Profissional
from api.models.usuario import Usuario

@pytest.mark.django_db
class TestProfissionalViewSet:

    def test_create_profissional(self, api_client):
        url = reverse('profissional-list')  
        data = {
            "nome_completo": "Prof Test",
            "conselho": "12345",
            "cpf": "000.000.000-00",
            "contato": "contato@teste.com",
            "user": {
                "username": "prof_test",
                "email": "prof@test.com",
                "perfil": "pro",
                "password": "strongpass123"
            }
        }
        response = api_client.post(url, data, format='json')
        assert response.status_code == 201
        assert response.data['nome_completo'] == data['nome_completo']
        assert response.data['user']['username'] == data['user']['username']

    def test_list_profissional(self, api_client, profissional, token):
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse('profissional-list')
        response = api_client.get(url)
        assert response.status_code == 200
        assert len(response.data) >= 1

    def test_retrieve_profissional(self, api_client, profissional, token):
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse('profissional-detail', args=[profissional.id])
        response = api_client.get(url)
        assert response.status_code == 200
        assert response.data['nome_completo'] == profissional.nome_completo

    def test_partial_update_profissional(self, auth_client, profissional):
        url = reverse('profissional-detail', args=[profissional.id])
        data = {"contato": "novo_contato@teste.com", "username": profissional.user.username}
        response = auth_client.patch(url, data, format='json')
        # Espera sucesso na atualização
        assert response.status_code == 202 or response.status_code == 200
        assert response.data['contato'] == "novo_contato@teste.com"

    def test_delete_profissional(self, auth_client, profissional):
        url = reverse('profissional-detail', args=[profissional.id])
        data = {"username": profissional.user.username}
        response = auth_client.delete(url, data, format='json')
        # Espera 204 no sucesso
        assert response.status_code == 204
