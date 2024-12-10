import uuid
import base64
from des import DesKey
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models.profissional import Profissional
from api.serializer.profissional import ProfissionalSerializer

class ProfissionalViewSet(viewsets.ModelViewSet):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer 

    def create(self, request, *args, **kwargs):
        
        # se a senha foi passada...
        if 'senha' in request.data and request.data.get('senha') != '':

            dados_profissional = request.data

            senha = request.data.get('senha')

            # gero o id
            id = uuid.uuid4()

            # pego os 8 primeiros caracteres para usar como chave
            id_truncado = str(id)[:8]

            chave = DesKey(id_truncado.encode('ascii'))

            senha_criptografada = chave.encrypt(senha.encode('ascii'), padding=True)

            # trago a senha criptografada de bytes para string
            senha_criptografada = base64.b64encode(senha_criptografada).decode('utf-8')

            senha = str(senha_criptografada)

            # instancio o modelo
            profissional = Profissional.objects.create(
                id=id,
                nome_completo=request.data.get('nome_completo'),
                cpf=request.data.get('cpf'),
                login=request.data.get('login'),
                bio=request.data.get('bio'),
                contato=request.data.get('contato'),
                email=request.data.get('email'),
                senha=senha_criptografada,
                conselho=request.data.get('conselho')
            )

            # serializo ele
            serializador = self.get_serializer(profissional)

            return Response(serializador.data, status=status.HTTP_201_CREATED)
        
        # se a senha não foi passada
        else:
            return Response({'erro': 'o campo senha não foi informado'}, status=status.HTTP_406_NOT_ACCEPTABLE)






