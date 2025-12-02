import pytest
from django.urls import reverse
from rest_framework.authtoken.models import Token


@pytest.mark.django_db
class TestAuthViews:

    def test_login_success(self, api_client, create_user):
        # Criar usuário para login
        username = "userlogin"
        password = "strongpassword123"
        create_user(username=username, password=password, perfil='pro')

        url = reverse('login')
        data = {
            "username": username,
            "password": password
        }

        response = api_client.post(url, data, format='json')

        assert response.status_code == 200
        assert "token" in response.data  # espera receber token

    def test_login_fail_wrong_password(self, api_client, create_user):
        username = "userlogin"
        password = "strongpassword123"
        create_user(username=username, password=password, perfil='pro')

        url = reverse('login')
        data = {
            "username": username,
            "password": "wrongpass"
        }

        response = api_client.post(url, data, format='json')

        assert response.status_code == 400 or response.status_code == 401
        assert "token" not in response.data

    def test_login_fail_no_user(self, api_client):
        url = reverse('login')
        data = {
            "username": "nonexistent",
            "password": "doesntmatter"
        }
        response = api_client.post(url, data, format='json')
        assert response.status_code == 400 or response.status_code == 401
        assert "token" not in response.data

    def test_logout_success(self, api_client, create_user):
        # Criar usuário e token
        user = create_user(username="logoutuser", password="mypassword", perfil='pro')
        token, _ = Token.objects.get_or_create(user=user)

        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse('logout')

        response = api_client.post(url, {}, format='json')

        assert response.status_code == 200
        with pytest.raises(Token.DoesNotExist):
            Token.objects.get(key=token.key)

    def test_logout_fail_no_auth(self, api_client):
        url = reverse('logout')
        response = api_client.post(url, {}, format='json')
        assert response.status_code == 401 or response.status_code == 403
