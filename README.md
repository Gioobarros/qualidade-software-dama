# DAMA - Denúncia Anônima de Mulheres Agredidas

<img src="https://imgur.com/fktwWmk.png" width="600" height="100%" />


#
O projeto DAMA (Denúncias Anônimas de Mulheres Agredidas) é uma ferramenta digital dedicada ao apoio, orientação e defesa das mulheres vítimas de qualquer tipo de violência. O site oferece recursos educacionais e um espaço para relatos e denúncias, visando fornecer suporte seguro para as usuárias.


# Equipe e Formas de Contato
[Fábio Ricardo Eduardo Cavalcante (fabioricardoeduardocavalcante)](https://github.com/fabioricardoeduardocavalcante).
#
 [Felipe da Costa Ferreira (Felipe-CF)](https://github.com/Felipe-CF)
 #
 [Giovana Beatriz Barros Firmino da Silva (Gioobarros)](https://github.com/Gioobarros)
 #
 [Igor Gabriel dos Santos (Igor1208gabriel)](https://github.com/Igor1208gabriel)
 #
 [Leandro Ramos Sizilio (LeandroSizilio)](https://github.com/LeandroSizilio)
 

# Horário de Reuniões

* Quintas-feiras das 10h30 às 12h00

# Documentação

[Link para os documentos do projeto](doc/documentacao.md)

# Manual da Desenvolvedor

[Orientações para os desenvolvedores do projeto](doc/guia-ds/guia.md)

# Execução do projeto
Para rodar o projeto, siga os passos abaixo: 

### Passos para executar o projeto
1. Clone o repositório do projeto:
<br>
` git clone https://github.com/tads-cnat/dama.git `
<br>

2. Acesse o diretório:
<br>
`cd dama `
`cd mysite`
<br>

3. Ative o ambiente virtual (venv):
<br>
`python -m venv venv`
`.\venv\Scripts\activate`
<br>

4. Instale o Django:
<br>
` pip install django`
<br>

5. Execute as migrações:
<br>
`python manage.py makemigrations`
`python manage.py migrate`
<br>

6. Inicie o servidor do Django:
<br>
`python manage.py runserver`
<br>

7. Acesse o projeto em seu navegador.