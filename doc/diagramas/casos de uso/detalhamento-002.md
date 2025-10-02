# CDU002 - Criar Conta para Profissional


- **Ator principal**: Usuários do tipo ONG ou Profissionais
- **Resumo**: Criação de conta para Administrador, Profissional 
- **Pré-condição**: Nenhuma



## Fluxo Principal
| Ações do ator | Ações do sistema | |
| :-----------------: | :-----------------: | :-----------------:|
|  O usuário clica em Cadastre-se na página inicial |  O sistema mostra uma página com um formulário pedindo os dados cadastrais ao profissional, além da possibilidade de inserir uma Bio sobre ele|  |
| O usuário preenche os dados e clica em Criar Cadastro | O sistema pede para o usuário confirmar os dados  | 
|  O usuário confirma e clica em Confirmar | O sistema valida as informações passadas |
| | O sistema mostra uma mensagem de boas vindas ao usuário e direciona ele para a página inicial |
| | |
| | |



## Fluxo Alternativo I - Passo 1
| Ações do ator | Ações do sistema |
| :-----------------: |:-----------------: | 
| 1.1 - O usuário clica em Cdastre-se na página do Mural de Força | O usuário é direcionado para o passo 2 do fluxo principal|  
| | |
| | |


## Fluxo Alternativo 2 - Passo 1
| Ações do ator | Ações do sistema |
| :-----------------: |:-----------------: | 
| 1.1 - O usuário clica em Cadastre-se na página de informes | O usuário é direcionado para o passo 2 do fluxo principal|  
| | |
| | |


## Fluxo Alternativo 2 - Passo 1
| Ações do ator | Ações do sistema |
| :-----------------: |:-----------------: | 
| 1.1 - O usuário clica em Cdastre-se após na página em que são listados os profissionais já cadastrados no sistema | O usuário é direcionado para o passo 2 do fluxo principal|  
| | |
| | |


## Fluxo de Exceção I - passo 3
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 2.1 - O usuário não preenche os dados, ou apenas parcialmente e clica em Criar cadastro | O sistema mostra uma mensagem pedindo que ele preencha todos os dados necessários |  
| | O sistema exibe uma mensagem pedindo que o usuário digite o conteudo do relato |  
| | 2.3 o usuário volta ao passo 3 |
| | |
| | |


## Fluxo de Exceção II - passo 3
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 2.1 - O usuário preenche o formulário com dados já existentes que são únicos, como CPF e email  | O sistema mostra uma mensagem informando que os dados á foram cadastrados |  
| | 2.3 o usuário volta ao passo 3 |
| | |
| | |



## Diagrama de Interação (Sequência ou Comunicação)

> Substituir pela imagem correspondente...


## Diagrama de Classes de Projeto

> Substituir pela imagem contendo as classes (modelo, visão e templates) que implementam o respectivo CDU...