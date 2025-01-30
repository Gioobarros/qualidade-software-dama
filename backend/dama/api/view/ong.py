from django.http import Http404
from rest_framework import status
from api.models.ong import Usuario
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.serializer.ong import OngSerializer, Ong
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import authentication_classes, permission_classes


class OngView(APIView):

    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = OngSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self, request):
        try:
            ongs = Ong.objects.all()
            if not ongs.exists():
                return Response({'messagem': 'Nenhuma ONG foi achada'}, status=status.HTTP_404_NOT_FOUND)
            serializer = OngSerializer(ongs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
    def patch(self, request):
        self.permission_classes = [IsAuthenticated]  
        self.check_permissions(request)  

        try:
            username = request.data.get('username')

            usuario = get_object_or_404(Usuario, username=username)

            ong = get_object_or_404(Ong, user=usuario)

            serializer = OngSerializer(ong, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        
        except Usuario.DoesNotExist:
            return Response({'erro': f'usuário {username} não encontrado no sistema'}, status=status.HTTP_404_NOT_FOUND)

        except Ong.DoesNotExist:
            return Response({'erro': f'dados da ONG não encontrados no sistema'}, status=status.HTTP_404_NOT_FOUND)
    
        except Exception:
            return Response({'erro': 'problema na api'}, status=status.HTTP_404_NOT_FOUND)


    def delete(self, request):
        self.permission_classes = [IsAuthenticated]  
        self.check_permissions(request)  

        try:
            username = request.data.get('username')

            usuario = get_object_or_404(Usuario, username=username)

            ong = get_object_or_404(Ong, user=usuario)

            ong.delete()

            return Response({'sucesso': 'o usuário foi deletado'}, status=status.HTTP_204_NO_CONTENT)

        except Usuario.DoesNotExist:
            return Response({'erro': f'usuário {username} não encontrado no sistema'}, status=status.HTTP_404_NOT_FOUND)

        except Ong.DoesNotExist:
            return Response({'erro': f'dados da ONG não encontrados no sistema'}, status=status.HTTP_404_NOT_FOUND)
    
        except Exception:
            return Response({'erro': 'problema na api'}, status=status.HTTP_404_NOT_FOUND)








    
