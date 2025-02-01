from datetime import datetime
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.timezone import make_aware
from django.shortcuts import get_object_or_404
from api.serializer.relato import RelatoSerializer, Relato
from api.serializer.usuario import Usuario
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import authentication_classes, permission_classes


class RelatoView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)  

        try:
            if 'publicador' in request.data and request.data.get('publicador') != '':

                publicador = request.data.get('publicador')

                usuario = get_object_or_404(Usuario, username=publicador)

                if usuario.perfil != 'admin':

                    serializer = RelatoSerializer(data=request.data)

                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)

                    return Response({"error": "serializer invalido"}, status=status.HTTP_400_BAD_REQUEST)

                else:
                    return Response({"error": "Usuário com perfil 'admin' não pode criar relato."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": "'username' não encontrado no campo 'user'."}, status=status.HTTP_400_BAD_REQUEST)

        except Usuario.DoesNotExist:
            return Response({'erro': f'usuário não encontrado no sistema'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"error": f"Ocorreu um erro: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
    def relato_por_data(self, data_inicio, data_fim):

        inicio = make_aware(datetime.strptime(data_inicio, "%Y-%m-%d"))

        fim = make_aware(datetime.strptime(data_fim, "%Y-%m-%d"))

        relatos_filtrados = Relato.objects.filter(
            data_criacao__gte=inicio, 
            data_criacao__lte=fim
            ).order_by('data_criacao')

        return relatos_filtrados
    

    def relato_por_trecho(self, trecho, relatos_filtrados):

        if relatos_filtrados is not None:

            relatos_filtrados = relatos_filtrados.filter(conteudo__icontains=trecho).order_by('data_criacao')

        return relatos_filtrados


    def get(self, request, id=None):
        try:
            if 'data_inicio'in request.GET and 'data_fim' in request.GET and 'palavra_chave' in request.GET:

                relatos_filtrados = None

                if request.GET.get('data_inicio') and request.GET.get('data_fim'):

                    relatos_filtrados = self.relato_por_data(
                        request.GET.get('data_inicio'),
                        request.GET.get('data_fim'),

                        )

                if request.GET.get('palavra_chave'):

                    trecho = request.GET.get('palavra_chave')

                    relatos_filtrados = self.relato_por_trecho(trecho, relatos_filtrados)  
                    
                serializer = RelatoSerializer(relatos_filtrados, many=True)

                return Response(serializer.data, status=status.HTTP_200_OK)
            
            else:
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
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)  

        try:
            relato = get_object_or_404(Relato, id=id)

            relato.delete()

            return Response({'sucesso': f'relato removido do sistema'}, status=status.HTTP_204_NO_CONTENT)

        except Relato.DoesNotExist:
            return Response({'erro': f'relato não encontrado no sistema'}, status=status.HTTP_404_NOT_FOUND)

        except Exception:
            return Response({'erro': 'problema na api'}, status=status.HTTP_404_NOT_FOUND)
    

    def patch(self, request):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)

        try:
            if 'id' in request.GET and request.GET.get('id') is not None:

                id = request.GET.get('id')

                if 'conteudo' not in request.data or request.data.get('novo_conteudo') == '':
                    return Response({"erro": "conteudo passado vazio"}, status=status.HTTP_400_BAD_REQUEST)

                relato = Relato.objects.get(id=id)

                serializer = RelatoSerializer(relato, data=request.data, partial=True)

                if serializer.is_valid():
                    serializer.save()

                    return Response({"message": "Relato atualizado com sucesso!"}, status=status.HTTP_200_OK)
            else:
                return Response({"erro": "id vazio ou não passado"}, status=status.HTTP_400_BAD_REQUEST)
                
        except Relato.DoesNotExist:
            return Response({"erro": "relato não existe."}, status=status.HTTP_404_NOT_FOUND)
            