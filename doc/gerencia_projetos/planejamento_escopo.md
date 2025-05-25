# Planejamento do escopo do projeto DAMA

## 1. Objetivos SMART do projeto

O projeto DAMA (Defesa e Apoio às Mulheres Agredidas) tem como principal objetivo de ser uma plataforma que ofereça acesso facilitado, suporte e orientações para mulheres vítimas de violência, integrando informações educativas.

- **Específico (S)**: Plataforma informativa e educativa de apoio às mulheres vítimas de violência.

- **Mensurável (M)**: A efetividade do projeto será avaliada por meio de alguns critérios, tais como:
    - Aprovação em testes de funcionalidades e testes não funcionais, garantindo desempenho, segurança e estabilidade do sistema;
    - Resultados de testes de usabilidade com o público-alvo, com taxa mínima de 80% de aprovação levando em consideração os critérios: facilidade de uso e clareza das informações;
    - Avaliações empíricas realizadas por meio de formulários, com nota média maior ou igual a 4, utilizando um escala de 1 a 5, sobre a satisfação dos usuários com a plataforma.

- **Atingível (A)**: O objetivo é realista, a equipe possui conhecimentos das tecnologias utilizadas e apoio dos docentes que possuem maiores experiências.

- **Relevante (R)**: O projeto é socialmente relevante por oferecer apoio às mulheres em situação de algum tipo de vulnerabilidade.

- **Temporal (T)**: O prazo para a conclusão so projeto é até o primeiro semestre de 2025.

## 2. Declaração do escopo

- **Escopo**: O escopo inclui a criação de um sistema web que apresente:
    - Cadastro de usuários (ONGs e profissionais);
    - Publicação de relatos das vítimas por ONGs e Profissionais já cadastrados;
    - Cadastro e visualização de materiais educativos;
    - Interface acessível e responsiva;
    - Testes de usabilidade;
    - Documentação técnica;

- **Não Escopo**: O escopo atual não inclui as demais funcionalidades abaixo listadas:
    - Aplicativo móvel;
    - Atendimento psicológico direto pela plataforma;
    - Denúncias dentro da plataforma;
    - Cadastro de vítimas;

## 3. Estrutura Analítica do Projeto (EAP)

1. **Iniciação**
    - 1.1 Levantamento
        - 1.1.1 Pesquisa com o público-alvo
    - 1.2 Definição dos objetivos
    - 1.3 Documentação dos requisitos

2. **Planejamento**
    - 2.1 Planejamento do escopo
    - 2.2 Planejamento das tecnologias e ferramentas que serão utilizdas
    - 2.3 Definição do  cronograma

3. **Desenvolvimento**

    - 3.1 Backend (Django)
        - 3.1.1 Criação da API
        - 3.1.2 Modelagem do banco de dados

    - 3.2 Frontend (Angular)
        - 3.2.1 Interface
        - 3.2.2 Publicação de relatos e materiais educativos
        - 3.2.3 Visualização de materiais educativos

    - 3.3 Nuvem
        - 3.3.1 Configuração do ambiente
        - 3.3.2 Deploy da aplicação
        - 3.3.3 Integração com o banco de dados
        - 3.3.4 Configuração de variáveis de ambiente e segurança

    - 3.4 Testes
        - 3.4.1 Testes de funcionalidades
        - 3.4.2 Testes de usabilidade (Avaliação empírica)
        - 3.4.3 Testes unitários
        - 3.4.4 Testes da API
        - 3.4.5 Testes não funcionais
        - 3.4.6 Ajustes pós testes

## 4. Dicionário da EAP

| Código   | Elemento                             | Descrição                                                                 |
|----------|--------------------------------------|---------------------------------------------------------------------------|
| 1        | Iniciação                            | Primeira etapa, pesquisas sobre o problema. |
| 1.1      | Levantamento                         | Coleta de informações junto ao público-alvo.                  |
| 1.1.1    | Pesquisa com o público-alvo          | Aplicação de questionários via Google Forms para entender as necessidades do público-alvo. |
| 1.2      | Definição dos objetivos              | Estabelecimento das metas do projeto. |
| 1.3      | Documentação dos requisitos          | Registro das funcionalidades esperadas. |
| 2        | Planejamento                         | Organização do escopo e tecnologias que serão utilizadas.               |
| 2.1      | Planejamento do escopo               | Definição dos objetivos do projeto, do que será e não será entregue. |
| 2.2      | Planejamento das tecnologias e ferramentas | Escolha das linguagens, frameworks, serviços e ferramentas a serem utilizadas. |
| 2.3      | Definição do cronograma              | Planejamento das datas e prazos para cada etapa do projeto. |
| 3        | Desenvolvimento                      | Construção do sistema, tanto backend quanto frontend. |
| 3.1      | Backend (Django)                     | Implementação do sistema. |
| 3.1.1    | Criação da API                       | Desenvolvimento dos endpoints. |
| 3.1.2    | Modelagem do banco de dados          | Estruturação do banco relacional. |
| 3.2      | Frontend (Angular)                   | Criação da interface do usuário e interações com o sistema. |
| 3.2.1    | Interface                            | Construção da estrutura visual da aplicação. |
| 3.2.2    | Publicação de relatos e materiais educativos | Funcionalidade para permitir que usuários cadastrados adicionem conteúdos. |
| 3.2.3    | Visualização de materiais educativos | Exibição de conteúdos educativos. |
| 3.3      | Nuvem                                | Hospedagem e deploy da aplicação. |
| 3.3.1    | Configuração do ambiente             | Preparação do ambiente na nuvem para rodar a aplicação. |
| 3.3.2    | Deploy da aplicação                  | Publicação da aplicação em ambiente online. |
| 3.3.3    | Integração com o banco de dados      | Conexão da aplicação com o banco de dados em nuvem. |
| 3.3.4    | Configuração de variáveis de ambiente e segurança | Ajustes de segurança e informações sensíveis. |
| 3.4      | Testes                               | Verificação da qualidade e funcionamento do sistema. |
| 3.4.1    | Testes de funcionalidades            | Verificação se as funcionalidades atendem aos requisitos. |
| 3.4.2    | Testes de usabilidade (Avaliação empírica) | Testes com usuários para avaliar o uso. |
| 3.4.3    | Testes unitários                     | Validação de pequenos trechos de código. |
| 3.4.4    | Testes da API                        | Testes dos endpoints da aplicação. |
| 3.4.5    | Testes não funcionais                | Testes de desempenho, segurança, entre outros aspectos não funcionais. |
| 3.4.6    | Ajustes pós testes                   | Correções e melhorias com base nos testes realizados. |

## 5. Escopo do produto e critérios de aceitação

O produto final será uma plataforma com funcionalidades voltadas à orientação de mulheres vítimas de violência. Estará disponível em ambiente de produção, conter documentação, apresentar interface, além de passar por testes.

#### Critérios de aceitação:
- O sistema deverá estar em um ambiente de nuvem e deve ser funcional;
- Os testes devem atingir resultados satisfatórios;
- Todos os requisitos definidos deverão estar implementados e funcionais;

## 6. Restrições
- O projeto deverá ser finalizado até o final do primeiro semestre de 2025;
- Recursos financeiros limitados;
- Trabalho realizado por poucos estudantes com disponibilidade limitada;

## 7. Premissas
- O público-alvo deverá participar dos testes de usabilidade;
- Os aplicativos gratuitos que são utilizados para desenvolvimento do projeto devem existir até a finalização do projeto;
- Não ocorrerá grandes mudanças nos requisitos até a finalização;

## Entrega dos artefatos
| Entrega                    | Descrição                                                                 |
|--------------------------|---------------------------------------------------------------------------|
| **Local de Entrega**     | Repositório do DAMA no GitHub, no diretório `doc/gerencia_projetos`.           |
| **Formato**              | Será entregue no formato `.md` e a apresentação será por meio de `slides`.                  |
| **Responsáveis**         | GitHub: qualquer integrante; GSA: todos os integrantes da equipe.         |
| **Prazo**                | Até 22 de maio de 2025.     |