from datetime import datetime
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.serializer.relato import RelatoSerializer, Relato
from api.serializer.usuario import Usuario
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import authentication_classes, permission_classes


class NotificacaoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        self.check_permissions(request)  

        try:
            if 'user' in request.data:

                if request.data.get('user') and 'username' in request.data.get('user'):

                    user = request.data.get('user')

                    username = user['username']

                    usuario = get_object_or_404(Usuario, username=username)

                    if usuario.perfil != 'admin':

                        del user['user']

                        relato = user

                        serializer = RelatoSerializer(data=request.data, publicador=usuario)

                        if serializer.is_valid():
                            serializer.save()
                            return Response(serializer.data, status=status.HTTP_201_CREATED)
                    else:
                        return Response({"error": "Usuário com perfil 'admin' não pode criar relato."}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({"error": "'username' não encontrado no campo 'user'."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": "'user' não encontrado nos dados da requisição."}, status=status.HTTP_400_BAD_REQUEST)

        except Usuario.DoesNotExist:
            return Response({'erro': f'usuário {username} não encontrado no sistema'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"error": f"Ocorreu um erro: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def get(self, request, id=None):
        self.permission_classes = [AllowAny]  
        
        try:
            if 'data_inicio'in request.GET and 'data_fim' in request.GET and 'palavra_chave' in request.data:

                relatos_filtrados = None

                if request.GET.get('data_inicio') and request.GET.get('data_fim'):

                    relatos_filtrados = self.relato_por_data(request)

                if request.GET.get('palavra_chave'):

                    trecho = request.GET.get('palavra_chave')

                    relatos_filtrados = self.relato_por_trecho(trecho, relatos_filtrados)  
                    
                serializer = RelatoSerializer(relatos_filtrados, many=True)

                return Response(serializer.data, status=status.HTTP_200_OK)

            relato = Relato.objects.all()

            if not relato.exists():
                return Response({'messagem': 'Nenhum relato publicado'}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = RelatoSerializer(relato, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except ValueError:
            return Response({"erro": "formato de data inválido"}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def delete(self, request, id):
        self.check_permissions(request)  

        try:
            relato = get_object_or_404(Relato, id=id)

            relato.delete()

            return Response({'sucesso': f'relato removido do sistema'}, status=status.HTTP_204_NO_CONTENT)

        except Relato.DoesNotExist:
            return Response({'erro': f'relato não encontrado no sistema'}, status=status.HTTP_404_NOT_FOUND)

        except Exception:
            return Response({'erro': 'problema na api'}, status=status.HTTP_404_NOT_FOUND)
    