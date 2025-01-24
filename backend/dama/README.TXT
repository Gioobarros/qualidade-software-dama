Seguinte:
Consertei as notas, porém existe um problema no serializer do profissional ( que vai se estender para os outros)
Quando eu passo o campo "user" na requisição abaixo:
{
    "nome_completo": "profissional",
    "cpf": "11111111111",
    "user": {
        "password": "1234",
        "username": "teste_senha",
        "email": "outro_pro@teste.com",
        "perfil": "pro"
        },
    "conselho": "RN 0200-9",
    "contato": "84 909990119"
}

ele valida o JSON acima mas, na hora de salvar, o "user" não vai para o ProfissionalASerializer, já fiz a adição dele nos fields = [], porém ainda assim deu erro
se resolvermos isso, provavelmente teremos de replicar em ong e administrador, aí vamos testar o resultado de verdade e terminar a issue