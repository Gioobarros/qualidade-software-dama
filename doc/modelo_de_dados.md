# Modelo de Dados

## Diagrama ER

<img src="https://imgur.com/kIwFDTP.png" width="1000" height="100%" />

## Modelo Relacional

<img src="https://imgur.com/bqG8zKp.png" width="600" height="100%" />

## Dicionário de Dados

--- 
*Tabela* : Usuário Administrador

Descrição : Armazena as informações dos usuários anônimos						

| Nome | Descrição | Tipo de Dado | Tamanho | Null | PK | FK | Unique | Identity | Default | Check | 
| ------- | --------- | ------------ | ------- | ---- | -- | -- | ------ | -------- | ------- | ----- |
| id | identificador único | UUIDField |   | &#9744;  | &#9745; | &#9744; | &#9745; | &#9744; | uuid.uuid4  |   | 
| login | nome de login do usuário | TEXT | 100  | &#9744;  | &#9744; | &#9744; | &#9745; | &#9744; |   |   | 
| senha | senha de acesso do usuário | VARCHAR | 20 | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 

*Tabela* : Usuário Profissional								

Descrição : Armazena as informações dos usuários profissionais									

<!-- | usuario | Instância de django.User | django.contrib.auth.models.User |  | &#9744;  | &#9745; | &#9744; | &#9745; | &#9744; |   |   |  -->

| Nome | Descrição | Tipo de Dado | Tamanho | Null | PK | FK | Unique | Identity | Default | Check | 
| ------- | --------- | ------------ | ------- | ---- | -- | -- | ------ | -------- | ------- | ----- |
| id | identificador único | UUIDField |   | &#9744;  | &#9745; | &#9744; | &#9745; | &#9744; | uuid.uuid4  |   |
| login | nome de login do usuário | TEXT | 100  | &#9744;  | &#9744; | &#9744; | &#9745; | &#9744; |   |   | 
| senha | senha de acesso do usuário | VARCHAR | 20 | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   |  
| nome_completo | nome completo para identificação dos profissionais | TEXT | 100  | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| cpf | cadastro de pessoa física do profissional | VARCHAR | 11  | &#9744;  | &#9744; | &#9744; | &#9745; | &#9744; |   |   | 
| conselho | numero de certificado no conselho regional do profissional | VARCHAR | 20  | &#9744;  | &#9744; | &#9744; | &#9745; | &#9744; |   |   | 
| contato | telefone para contato do usuário | VARCHAR | 11 | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| email | email para contato | TEXT |  40 | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| bio | informações acerca do currículo do profissional | TEXT |   | &#9745;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 

*Tabela* : Usuário Ong									

Descrição : Armazena as informações dos usuários ONGs									


| Nome | Descrição | Tipo de Dado | Tamanho | Null | PK | FK | Unique | Identity | Default | Check | 
| ------- | --------- | ------------ | ------- | ---- | -- | -- | ------ | -------- | ------- | ----- |
| id | identificador único | UUIDField |   | &#9744;  | &#9745; | &#9744; | &#9745; | &#9744; | uuid.uuid4  |   |
| login | nome de login do usuário | TEXT | 100  | &#9744;  | &#9744; | &#9744; | &#9745; | &#9744; |   |   | 
| senha | senha de acesso do usuário | VARCHAR | 20 | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| razao_social | nome vinculada ao cnpj da organização | TEXT | 100 | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| cnpj | cadastro de pessoa jurídica da organização  | VARCHAR | 14  | &#9744;  | &#9744; | &#9744; | &#9745; | &#9744; |   |   | 
| contato | telefone para contato do usuário | VARCHAR | 11 | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| email | email para contato | TEXT |  40 | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| bio | informações acerca da organização | TEXT |   | &#9745;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 

--- 
*Tabela* : Relato

Descrição : Armazena as informações dos relatos

Observações : Esta tabela utilizara uma chave estrangeira da tabela Usuário

| Nome | Descrição | Tipo de Dado | Tamanho | Null | PK | FK | Unique | Identity | Default | Check | 
| ------- | --------- | ------------ | ------- | ---- | -- | -- | ------ | -------- | ------- | ----- |
| id | identificador único | UUIDField |   | &#9744;  | &#9745; | &#9744; | &#9745; | &#9744; | uuid.uuid4  |   |
| conteudo | texto descrito no relato | TEXT |   | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
