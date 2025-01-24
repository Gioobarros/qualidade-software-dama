from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializer.administrador import AdministradorSerializer, Administrador

class AdministradorView(APIView):
    def post(self, request):
        serializer = AdministradorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self, request):
        try:
            admin = Administrador.objects.all()
            if not admin.exists():
                return Response({'messagem': 'Nenhuma ONG foi achada'}, status=status.HTTP_404_NOT_FOUND)
            serializer = AdministradorSerializer(admin, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)