# Documentação Técnica - Sistema DAMA

## 1. Visão Geral do Sistema

O DAMA é uma aplicação de back-end desenvolvida em Django REST para suportar a implementação de uma plataforma que oferece assistência e recursos para mulheres em situação de violência. Esta documentação descreve a arquitetura e a estrutura dos componentes de back-end, com foco nos modelos de dados, serialização, permissões, views, e gerenciamento de usuários e relatórios. O sistema utiliza uma abordagem modular e segue boas práticas de desenvolvimento RESTful.

## 2. Estrutura dos Apps e Componentes

O projeto DAMA é composto por dois apps principais: **Dama** e **API**, cada um dividido em pastas que organizam os diferentes componentes. Esta estrutura modular facilita a manutenção, escalabilidade e organização do código.

- [**Dama**](backend/dama/dama): App principal do Django.
- [**API**](backend/dama/api/): Responsável pela interface de comunicação, incluindo modelos, endpoints, serialização, autenticação e permissões.

### 2.1 Estrutura de Pastas e Arquivos
O app da API possui pastas para organizar os diferentes componentes da aplicação, descritas abaixo:

- **models/**: Define as classes de modelo que representam as entidades do sistema (Administrador, ONG, Profissional e Relato).
- **serializers/**: Responsável pela serialização e desserialização dos dados das entidades, permitindo transformar os objetos de modelo para JSON e vice-versa.
- **permissions/**: Contém as classes de permissão, definindo as regras de acesso para diferentes tipos de usuários (usuários comuns, profissionais e administradores).
- **urls/**: Define os endpoints de cada recurso, mapeando as URLs para as views correspondentes.
- **views/**: Implementa as operações CRUD e lógica de negócios de cada recurso. Usa viewsets para gerenciar requisições HTTP.

### 2.2 Arquivos Específicos
Cada pasta possui arquivos para os modelos principais do sistema:
  - **Administrador**
  - **ONG**
  - **Profissional**
  - **Relato**
  - **User** (modificado para personalizar e integrar a autenticação de usuários)

Esses arquivos estão em conformidade com o padrão do Django REST, permitindo fácil integração e expansão do sistema.

## 3. Modelos e Estrutura de Dados

O DAMA possui quatro modelos principais, com uma estrutura de herança que facilita a reutilização de código e o gerenciamento de diferentes tipos de usuários. Abaixo estão os detalhes dos modelos implementados:

### 3.1 Modelo Administrador
O modelo **Administrador** herda do `django.contrib.auth.models.User`, utilizando os campos de autenticação padrão e adicionando permissões específicas para a gestão e manutenção do sistema.

[Administrador](/backend/dama/api/models/administrador.py)

### 3.2 Modelo ONG
O modelo **ONG** também herda do `User`, representando organizações que oferecem suporte às usuárias. 

[ONGs](/backend/dama/api/models/ong.py)

### 3.3 Modelo Profissional
O modelo **Profissional** herda do `User` e representa especialistas que contribuem com conteúdos educativos e oferecem suporte psicológico ou jurídico. 

[Profissional](/backend/dama/api/models/profissional.py)

### 3.4 Modelo Relato
O modelo **Relato** não herda do `User` e é responsável por armazenar os relatos dos profissionais e ONGs. Cada relato está associado a um `User` para identificar a usuária que o criou, garantindo o armazenamento seguro e organizado dos registros de casos.

[Relato](/backend/dama/api/models/relato.py)

## 4. Serializers

Os serializers são responsáveis pela conversão dos modelos para JSON e vice-versa, tornando os dados compatíveis com a API. Os serializers implementados utilizam o `ModelSerializer` do Django REST para simplificar o mapeamento dos campos dos modelos.

[Serializadores](/backend/dama/api/serializer)

## 5. Permissões

O sistema tem controles de acesso e permissões para cada model 

[Permissões](/backend/dama/api/permissions)

## 6. Views e Endpoints

As views foram implementadas usando `viewsets` e classes `APIView` para facilitar o gerenciamento dos recursos. A estrutura de views é RESTful, com as operações CRUD organizadas para cada modelo.

[Views](/backend/dama/api/view)

## 7. URLs

As URLs são definidas de maneira modular para cada app, com endpoints RESTful para cada modelo. A estrutura de URLs segue a hierarquia dos apps e organiza os endpoints em grupos, facilitando o acesso e a documentação da API.

[URLs](/backend/dama/api/urls)

---