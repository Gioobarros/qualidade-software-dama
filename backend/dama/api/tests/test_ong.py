import pytest
from django.urls import reverse
from api.models.ong import Ong

@pytest.mark.django_db
class TestOngViewSet:

    def test_create_ong(self, api_client):
        url = reverse('ong-list')
        data = {
            "user": {
                "username": "ong_test",
                "email": "ong@test.com",
                "perfil": "ong",
                "password": "strongpass123"
            },
            "razao_social": "Razão Social Teste",
            "cnpj": "11.111.111/1111-11",
            "contato": "contato@teste.com"
        }
        response = api_client.post(url, data, format='json')
        assert response.status_code == 201
        assert response.data['razao_social'] == data['razao_social']
        assert response.data['user']['username'] == data['user']['username']

    def test_list_ong(self, api_client, ong, token):
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse('ong-list')
        response = api_client.get(url)
        assert response.status_code == 200
        assert any(o['razao_social'] == ong.razao_social for o in response.data)

    def test_retrieve_ong(self, api_client, ong, token):
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse('ong-detail', args=[ong.id])
        response = api_client.get(url)
        assert response.status_code == 200
        assert response.data['razao_social'] == ong.razao_social

    def test_partial_update_ong(self, auth_client, ong):
        url = reverse('ong-detail', args=[ong.id])
        data = {
            "contato": "novo_contato@teste.com",
            "user": {
                "username": ong.user.username
            }
        }
        response = auth_client.patch(url, data, format='json')

        assert response.status_code in [200, 202]
        assert response.data['contato'] == "novo_contato@teste.com"

    def test_delete_ong(self, auth_client, ong):
        url = reverse('ong-detail', args=[ong.id])
        data = {"username": ong.user.username}
        response = auth_client.delete(url, data, format='json')
        assert response.status_code == 204
        # Verifica que a ONG foi removida do banco
        with pytest.raises(Ong.DoesNotExist):
            Ong.objects.get(pk=ong.id)
