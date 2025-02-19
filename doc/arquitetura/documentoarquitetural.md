# DAMA – Defesa e Apoio às Mulheres Agredidas

# Documento de Arquitetura do Sistema

## Histórico de Revisões

| Data | Versão | Descrição | Autores |
| --- | --- | --- | --- |
| 30/10/2024 | 1.0 | Versão inicial | Felipe Costa, Giovana Barros e Leandro Sizilio |
| 18/02/2025 | 1.1 | Atualização de conteúdo | Felipe Costa, Giovana Barros e Leandro Sizilio |


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

### 5.3. Diagrama de Containers
![Texto alternativo](https://imgur.com/MdPAZJB.jpg)

      
### 6. Diagramas Conceituais
![Texto alternativo](https://imgur.com/VaKVXfs.jpg)

## 7.Detalhamento da Implementação e Ambiente Físico
### 7.1. Visão de Implementação
### 7.2. Diagramas de Componente – C4
### 7.3. Persistência
### 7.4. Interface de Usuário

