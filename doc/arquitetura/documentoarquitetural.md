# DAMA – Defesa e Apoio às Mulheres Agredidas

# Documento de Arquitetura do Sistema

## Histórico de Revisões

| Data | Versão | Descrição | Autores |
| --- | --- | --- | --- |
| 30/10/2024 | 1.0 | Versão inicial | Felipe Costa, Giovana Barros e Leandro Sizilio |
| 18/02/2025 | 1.1 | Atualização de conteúdo | Felipe Costa, Giovana Barros e Leandro Sizilio |
| 26/02/2025 | 1.2 | Atualização dos diagramas | Felipe Costa, Giovana Barros e Leandro Sizilio |

## 1. Introdução

Este documento tem o descreve a arquitetura do sistema DAMA - Defesa e Apoio às Mulheres Agredidas, aborda os componentes e a infraestrutura do sistema, incluindo suas principais funcionalidades, interações e tecnologias envolvidas. O documento tem como principal objetivo a garantia da compreensão entre a equipe de desenvolvimento e as partes interessadas na estrutura do sistema.


## 2. Termos e Abreviações

Abaixo estão listados os termos específicos do sistema e suas respectivas descrições:

| Nome técnico | Descrição | 
| --- | --- |
| Relato | Registro público feito por uma ONG ou profissional sobre um determinado caso de violência contra a mulher, com o objetivo de informar e sensibilizar participantes da comunidade.|
| ONG | Organização que pode publicar relatos e materiais específicos, voltados para suporte às vítimas e conscientização da comunidade. | 
| Profissional| Especialista que pode contribuir com o cadastro de materiais de suporte, e orientações específicas para ajudar a combater a violência contra a mulher. | 
| Material |Recursos informativos e educacionais que podem ser cadastrados por ONGs ou profissionais, destinados a orientar a comunidade sobre temas relacionados à violência contra a mulher. | 
| Participante | Termo geral que identifica qualquer pessoa que interage com o sistema, incluindo aqueles que colaboram adicionando relatos, materiais.| 
|Informes | Conteúdo que pode ser cadastrado por usuários da ONG ou profissionais, com o objetivo de compartilhar notícias, dados, estatísticas e outras informações relevantes para apoiar e orientar as usuárias sobre o tema. | 

## 3. Requisitos Significantes

| Requisito | Descrição | 
| --- | --- | 
|Publicar relato | O sistema deve permitir que profissionais e ONGs publiquem relatos de violência. |
| Publicar informe | O sistema deve possibilitar a publicação de informes de ações em apoio e defesa da mulher. |
| Buscar e acessar relatos e informes|  O sistema deve permitir que participantes busquem e acessem relatos e informes.|     
|Moderar publicação|  O sistema deve permitir que administradores validem publicações feitas por usuários.|
|5.	Gerenciamento de usuários| O sistema deve permitir o cadastro, edição e exclusão de contas de usuários.|

## 4.	Restrições arquiteturais

### 4.1 Restrições técnicas

| Restrição | Contexto e/ou Motivação |
|---|---|
| Restrição de software e programação |  |
| RT1 | O sistema deve ser desenvolvido utilizando tecnologias web modernas e seguras. |
| Restrição de sistema operacional |  |
| RT2 |O sistema deve ser compatível com os principais sistemas operacionais (Windows, macOS, Linux).  |
| Restrições de Hardware |  |
| RT3 | O sistema deve ser acessível dispositivos com conexão à internet. |

## 5. Escopo do Sistema e Contexto

### 5.1. Diagrama de Casos de Uso
Os principais casos de uso estão destacados em rosa nas imagens abaixo: 
![Texto alternativo](https://imgur.com/1Nhoaln.jpg)
![Texto alternativo](https://imgur.com/zSTv06Q.jpg)

##### CDU001 - Publicar Relato

- **Ator principal**: Usuários do tipo ONG ou Profissionais
- **Resumo**: ONG ou Profissional publica um relato sobre um caso de violência contra mulheres.
- **Pré-condição**: Usuário estar cadastrado e logado e ser um Profissional ou uma ONG.

##### CDU002 - Criar Conta para Profissional
- **Ator principal**: Usuários do tipo ONG ou Profissionais
- **Resumo**: Criação de conta para Administrador, Profissional 
- **Pré-condição**: Nenhuma

##### CDU003 - Listar Relatos
- **Ator principal**: Visitantes
- **Resumo**: Listagem de relatos verídicos feitos por Profissionais e/ou ONG's cadastradas 
- **Pré-condição**: Nenhuma

### 5.2. Diagrama de Contexto

![Texto alternativo](https://imgur.com/PTXbnIE.jpg)

![Diagrama de contexto atualizado](https://imgur.com/KhAiEkR.jpg)

##### Atores principais:
- **ONG**: Organizações que se cadastram no sistema para oferecer suporte às mulheres vítimas de violência. As ONGs podem validar seu CNPJ através de uma API externa.

- **Visitante**: Usuários que acessam o sistema, podem explorar todas as informações disponíveis.

- **Profissional**: Usuários especializados que se cadastram no sistema para fornecer suporte às mulheres vítimas de violência.

- **DAMA**: O sistema para apoio, orientação e defesa de mulheres vítimas de violência. Ele facilita a interação entre os diferentes atores e gerencia as funcionalidades principais.

##### Sistema externo:
- **API externa**: Integra-se com o sistema para validar o CNPJ das ONGs, garantindo a confiabilidade.

### 5.3. Diagrama de Containers
![Texto alternativo](https://imgur.com/MdPAZJB.jpg)

##### Principais containers:
A aplicação web foi desenvolvida com JavaScrpt e Angular que permite o acesso e interação dos três tipos de usuários com o sistema.A API service foi desenvolvida com Django REST, permite o gerenciamento da lógica da aplicação, processa as solicitações realizadas na aplicação web e interage com o banco de dados. O banco de dados armazena os dados do sistema, utiliza um modelo relacional para organizar as tabelas e os dados, é gerenciado e acessado através da API service.

##### Sistemas externos:
A API externa se integra com o sistema para realizar as chamadas da API, a comunicação é realizada através de JSON e HTTPS, que garante a troca de dados de forma segura. 

### 6. Diagramas Conceituais
![Texto alternativo](https://imgur.com/VaKVXfs.jpg)

| Conceito| Descrição |
|---|---|
| UsuarioProfissional| Representa um usuário profissional cadastrado no sistema, que possui conhecimentos especializados para oferecer ajuda aos demais usuários. |
| UsuarioOng | Representa uma organização não governamental (ONG) cadastrada no sistema, que pode oferecer ajuda aos demais usuários. |
| UsuarioAdministrador | Representa um administrador do sistema que possui permissões necessárias para gerenciar e administrar o sistema.    |
| Relato |  |
| DjangoUser | Modelo de usuário do Django. |

## 7.Detalhamento da Implementação e Ambiente Físico
### 7.1. Visão de Implementação
| Componente | Descrição |
|---|---|
| Backend| Servidor que lida com a lógica de aplicação e comunicação com o banco de dados. |
| Frontend | Componente responsável pela interface do usuário. |
| Banco de dados | Armazena todos os dados do sistema.    |
| API externa | Verifica a autenticidade do CNPJ fornecido pelas ONGs. |
### 7.2. Diagrama de componentes
#### Backend

| Componente | Descrição |
|---|---|
| API externa| Verifica a autenticidade do CNPJ fornecido pelas ONGs. |
| Aplicação web | Aplicação que permite o acesso dos usuários ao sistema. |
| DataBase | Banco de dados PostgresSQL, armazena os dados do sistema.    |
| Views | Recebe as requisições do frontedn e processa a lógica. |
| Serializer | Converte os objetos de django REST em JSON e de JSON para django REST. |
| Models | Define a estrutura dos dados no banco de dados e suas regras de negócios. |

![Backend](https://imgur.com/VtK5lFy.jpg)

O backend é responsável por processar as requisições recebidas pelo frontend, validar dados e interagir com o banco de dados. Utiliza o Django REST. A API Externa é usada para validar o CNPJ das ONGs, garantindo a autenticidade das informações.

#### Frontend

| Componente | Descrição |
|---|---|
| API | Componente que realiza a comunicação entre o frontend e o backend, enviando e recebenco os devidos dados. |
| Services | Componente que encapsula a lógica do frontend, manipulando os dados. |
| Solicitações| Componente em Angular que gerencia o envio das requisições para o backend. |
| Usuários | Componente em Angular que gerencia a exibição e interação com os dados dos usuários (ONG, visitante, profissional e administrador). |
| API externa| Verifica a autenticidade do CNPJ fornecido pelas ONGs. |
| DataBase | Banco de dados PostgresSQL, armazena os dados do sistema.    |

![Texto alternativo](https://imgur.com/eqoW3ED.jpg)

O frontend é composto por componentes desenvolvidos em Angular, que permitem a interação dos usuários com o sistema. 

### 7.2. Interface do usuário

A interface do sistema foi desenvolvida com foco na usabilidade e na experiência do usuário, garantindo que todos os atores interajam de forma intuitiva e eficiente.

Para o frontend a framework escolhido foi Angular, framework JavaScript, foi escolhido por ser um framework robusto, com componentes reutilizáveis, o que facilita a manutenção do sistema e integração eficiente com APIs REST. 

A seguir, estão imagens de como a interface do usuário está atualmente:

##### Index
![Index](https://imgur.com/IIBczer.jpg)
![Index](https://imgur.com/7BMLTDv.jpg)
![Index](https://imgur.com/jjr9LMW.jpg)

##### Conheça seus direitos
![Conheça direiros](https://imgur.com/Tqcf8dZ.jpg)
![Conheça direiros](https://imgur.com/U3T76Tv.jpg)

##### Mural de força
![Mural de força](https://imgur.com/4Wyq7jW.jpg)

##### Cadastro
###### Profissionais
![Cadastro](https://imgur.com/PIiR55S.jpg)
###### ONGs
![Cadastro](https://imgur.com/x27WOsg.jpg)

##### Login
![Login](https://imgur.com/og366j8.jpg)


## 8. Anexos

### Apresentação geral da API

Para a aplicação, foi utilizado o Swagger para descrever os recursos que a API do DAMA possui. A API segue os princípios REST, utilizando métodos HTTP padrão (GET, POST, PUT, PATCH, DELETE). Além disso, a API inclui endpoints para autenticação de usuários, garantindo acesso seguro às funcionalidades do sistema.

##### Principais funcionalidades
1. **Autenticação:** Endpoints para login e logout de usuários, garantindo acesso seguro ao sistema.
2. **Administradores:** Gerenciamento de administradores, com operações de CRUD para manter o controle de acesso e permissões.
3. **ONGs:** Cadastro e gerenciamento de ONGs, permitindo a inclusão de informações como razão social, CNPJ e contato.
4. **Profissionais:** Gerenciamento de profissionais especializados, que oferecem suporte e orientação aos usuários do sistema.
5. **Relatos:** Registro e gerenciamento de relatos ou denúncias feitas pelos usuários (ONGs e Profissionais), com informações como conteúdo, data de criação e status.
6. **Usuários:** Gerenciamento de usuários do sistema, incluindo operações de CRUD para manter os dados atualizados.

Abaixo, segue os detalhamentos de cada endpoint da aplicação:

![User](https://imgur.com/hltksoJ.jpg)
##### **Usuário**
- **GET /usuario/ (usuario_list):**
  - **Descrição:** Lista todos os usuários cadastrados no sistema.
- **POST /usuario/ (usuario_create):**
  - **Descrição:** Cria um novo usuário no sistema.
- **GET /usuario/(id)/ (usuario_read):**
  - **Descrição:** Retorna os detalhes de um usuário específico.
- **PUT /usuario/(id)/ (usuario_update):**
  - **Descrição:** Atualiza todos os campos de um usuário específico.
- **PATCH /usuario/(id)/ (usuario_partial_update):**
  - **Descrição:** Atualiza parcialmente os campos de um usuário específico.
- **DELETE /usuario/(id)/ (usuario_delete):**
  - **Descrição:** Remove um usuário do sistema.


![Profissional](https://imgur.com/v8xx5Bo.jpg)

##### **Profissional**
- **GET /profissional/ (professional_list):**
  - **Descrição:** Lista todos os profissionais cadastrados no sistema.
- **POST /profissional/ (professional_create):**
  - **Descrição:** Cria um novo profissional no sistema.
- **GET /profissional/(id)/ (professional_read):**
  - **Descrição:** Retorna os detalhes de um profissional específico.
- **PUT /profissional/(id)/ (professional_update):**
  - **Descrição:** Atualiza todos os campos de um profissional específico.
- **PATCH /profissional/(id)/ (professional_partial_update):**
  - **Descrição:** Atualiza parcialmente os campos de um profissional específico.
- **DELETE /profissional/(id)/ (professional_delete):**
  - **Descrição:** Remove um profissional do sistema.

![ONG](https://imgur.com/3dKejOF.jpg)

##### **ONG**
- **GET /ong/ (ong_list):**
  - **Descrição:** Lista todas as ONGs cadastradas no sistema.
- **POST /ong/ (ong_create):**
  - **Descrição:** Cria uma nova ONG no sistema.
- **GET /ong/(id)/ (ong_read):**
  - **Descrição:** Retorna os detalhes de uma ONG específica.
- **PUT /ong/(id)/ (ong_update):**
  - **Descrição:** Atualiza todos os campos de uma ONG específica.
- **PATCH /ong/(id)/ (ong_partial_update):**
  - **Descrição:** Atualiza parcialmente os campos de uma ONG específica.
- **DELETE /ong/(id)/ (ong_delete):**
  - **Descrição:** Remove uma ONG do sistema.

![Admin](https://imgur.com/FHNk7kL.jpg)

##### **Admin**
- **GET /admin/ (admin_list):**
  - **Descrição:** Lista todos os administradores cadastrados no sistema.
- **POST /admin/ (admin_create):**
  - **Descrição:** Cria um novo administrador no sistema.
- **GET /admin/(id)/ (admin_read):**
  - **Descrição:** Retorna os detalhes de um administrador específico.
- **PUT /admin/(id)/ (admin_update):**
  - **Descrição:** Atualiza todos os campos de um administrador específico.
- **PATCH /admin/(id)/ (admin_partial_update):**
  - **Descrição:** Atualiza parcialmente os campos de um administrador específico.
- **DELETE /admin/(id)/ (admin_delete):**
  - **Descrição:** Remove um administrador do sistema.
![Login](https://imgur.com/1G7v9hB.jpg)

##### **Login**
- **POST /login/ (login_create):**
  - **Descrição:** Realiza o login de um usuário no sistema.
  - **Uso:** Autentica o usuário e retorna um token de acesso.

![Logout](https://imgur.com/YlXtcJn.jpg)

##### **Logout**
- **POST /logout/ (logout_create):**
  - **Descrição:** Realiza o logout de um usuário no sistema.
  - **Uso:** Encerra a sessão do usuário e invalida o token de acesso.

![Relato](https://imgur.com/de1DAp1.jpg)

##### **Relato**
- **GET /relato/ (relato_list):**
  - **Descrição:** Lista todos os relatos cadastrados no sistema.
- **POST /relato/ (relato_create):**
  - **Descrição:** Cria um novo relato no sistema.
- **GET /relato/(id)/ (relato_read):**
  - **Descrição:** Retorna os detalhes de um relato específico.
- **PUT /relato/(id)/ (relato_update):**
  - **Descrição:** Atualiza todos os campos de um relato específico.
- **PATCH /relato/(id)/ (relato_partial_update):**
  - **Descrição:** Atualiza parcialmente os campos de um relato específico.
- **DELETE /relato/(id)/ (relato_delete):**
  - **Descrição:** Remove um relato do sistema.
