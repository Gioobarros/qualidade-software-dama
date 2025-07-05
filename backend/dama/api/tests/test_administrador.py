import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404

@pytest.mark.django_db
class TestAdministradorView:

    def test_create_success(self, api_client):
        url = reverse('administrador-list')
        data = {
            "user": {
                "username": "admin2",
                "email": "admin2@test.com",
                "perfil": "admin",
                "password": "pass1234"
            }
        }
        response = api_client.post(url, data, format='json')
        assert response.status_code == 201
        assert response.data['user']['username'] == 'admin2'

    def test_create_invalid(self, api_client):
        url = reverse('administrador-list')
        data = {
            "user": {  # falta username
                "email": "admin2@test.com",
                "perfil": "admin",
                "password": "pass1234"
            }
        }
        response = api_client.post(url, data, format='json')
        assert response.status_code == 400
        assert 'username' in response.data['user']

    def test_list_requires_authentication(self, api_client, admin_user):
        url = reverse('administrador-list')
        # sem autenticação deve dar erro (por causa da validação)
        response = api_client.get(url)
        assert response.status_code in [401, 403]

        # autenticar
        user, _ = admin_user
        api_client.force_authenticate(user=user)
        response = api_client.get(url)
        assert response.status_code == 200
        assert isinstance(response.data, list)

    def test_retrieve(self, api_client, admin_user):
        user, admin = admin_user
        url = reverse('administrador-detail', kwargs={'pk': admin.pk})
        
        # sem autenticação
        response = api_client.get(url)
        assert response.status_code in [401, 403]
        
        # autenticado
        api_client.force_authenticate(user=user)
        response = api_client.get(url)
        assert response.status_code == 200
        assert response.data['user']['username'] == user.username

    def test_retrieve_not_found(self, api_client, admin_user):
        user, _ = admin_user
        api_client.force_authenticate(user=user)
        url = reverse('administrador-detail', kwargs={'pk': 99999})
        response = api_client.get(url)
        assert response.status_code == 404

    def test_partial_update_success(self, api_client, admin_user):
        user, admin = admin_user
        api_client.force_authenticate(user=user)
        url = reverse('administrador-list')
        data = {
            "username": user.username,
            "user": {
                "email": "novoemail@test.com"
            }
        }
        response = api_client.patch(url, data, format='json')
        assert response.status_code == 200
        assert response.data['user']['email'] == "novoemail@test.com"

    def test_partial_update_missing_username(self, api_client, admin_user):
        user, _ = admin_user
        api_client.force_authenticate(user=user)
        url = reverse('administrador-list')
        data = {
            "user": {
                "email": "novoemail@test.com"
            }
        }
        response = api_client.patch(url, data, format='json')
        assert response.status_code == 406
        assert 'Campos obrigatórios ausentes' in response.data['erro']

    def test_destroy_success(self, api_client, admin_user):
        user, admin = admin_user
        api_client.force_authenticate(user=user)
        url = reverse('administrador-list')
        data = {
            "username": user.username
        }
        response = api_client.delete(url, data, format='json')
        assert response.status_code == 204
        # verifica que o admin foi removido do DB
        from api.models.administrador import Administrador
        with pytest.raises(Administrador.DoesNotExist):
            Administrador.objects.get(pk=admin.pk)

    def test_destroy_missing_username(self, api_client, admin_user):
        user, _ = admin_user
        api_client.force_authenticate(user=user)
        url = reverse('administrador-list')
        data = {}
        response = api_client.delete(url, data, format='json')
        assert response.status_code == 406
        assert 'Campo de username ausente' in response.data['erro']
