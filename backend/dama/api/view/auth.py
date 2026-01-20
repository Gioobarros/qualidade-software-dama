"""Módulo de autenticação da aplicação."""
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from api.serializer.ong import OngSerializer
from api.serializer.profissional import ProfissionalSerializer


class LoginView(ObtainAuthToken):
    """View para login de usuários."""

    def post(self, request, *args, **kwargs):
        """Processar autenticação do usuário."""
        username = request.data.get('username')
        password = request.data.get('password')

        usuario = authenticate(username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            token, created = Token.objects.get_or_create(user=usuario)

            if not created:
                token.delete()
                token = Token.objects.create(user=usuario)

            response_data = {
                'token': token.key,
                'username': usuario.username,
                'perfil': usuario.perfil,
            }

            if usuario.perfil == 'ong':
                usuario_data = usuario.ong

                if usuario_data is not None:
                    usuario_response = OngSerializer(usuario_data).data
                    del usuario_response['user']

                    if usuario_response['bio'] is None:
                        usuario_response['bio'] = "vazio"

                    response_data['dados_usuario'] = usuario_response

            if usuario.perfil == 'pro':
                usuario_data = usuario.profissional

                if usuario_data is not None:
                    usuario_response = ProfissionalSerializer(usuario_data).data
                    del usuario_response['user']

                    if usuario_response['bio'] is None:
                        usuario_response['bio'] = "vazio"
                    response_data['dados_usuario'] = usuario_response

            return Response(response_data)

        return Response(
            {'mensagem': 'Login ou Senha invalido'},
            status=status.HTTP_401_UNAUTHORIZED
        )


class LogoutView(APIView):
    """View para logout de usuários."""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """Processar logout do usuário."""
        token_key = request.auth.key
        token = Token.objects.get(key=token_key)
        token.delete()
        return Response(
            {'detail': 'usuário deslogado'},
            status=status.HTTP_204_NO_CONTENT
        )
