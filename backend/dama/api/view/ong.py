from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializer.ong import OngSerializer, Ong


class OngView(APIView):
    
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
        


    
