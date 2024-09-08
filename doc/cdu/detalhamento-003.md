# CDU003 - Manter Rede de Socorro

- **Ator principal**: Usuários logados
- **Resumo**: Adicionar ou remover pessoas de dentro da lista pessoal da rede de socorro
- **Pré-condição**: Estar logado 

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 1 - O usuário clica em Rede de Socorro  | |  
| | 2 - O sistema mostra uma página, com as pessoas que já estão cadastradas e os botões Adicionar Nova Pessoa, Atualizar Pessoa, Remover Pessoa | 
| 3 - O usuário clica em Adicionar Nova Pessoa |  |
|  |4 - O sistema mostra um formulário requisitando o nome, grau de parentesco e telefone da pessoa |
| 5 - O usuário preenche os dados |  |
|  | 6 - O sistema mostra os dados preenchidos e pede confirmação ao usuário |
| 7 - O usuário confirma os dados |  |
|  | 8 - O sistema exibe uma mensagem que a pessoa foi adicionada |
| | |

## Fluxo de Exceção I - Passo 5 - Adicionar Pessoa
| Ações do ator | Ações do sistema |
| :-----------------: |:-----------------: | 
| 1.1 - O usuário não preenche, ou apenas parcialmente, os dados requisitados | |  
| | 1.2 - O sistema exibe uma mensagem de erro |
| | O usuário é redirecionado ao passo 4 |
| | |

## Fluxo Principal - Atualizar Pessoa
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 1 - O usuário clica em Rede de Socorro | |  
| | 2 -  O sistema mostra uma página, com as pessoas que já estão cadastradas e os botões Adicionar Nova Pessoa, Atualizar Pessoa, Remover Pessoa |  
| 3 - O usuário clica em Atualizar Pessoa | |
| | 4 - O sistema mostra um formulário requisitando o nome, grau de parentesco e telefone da pessoa |
| 5 - O usuário preenche os dados | |
| | 6 - O sistema mostra os dados preenchidos e pede confirmação ao usuário |
| 7 - O usuário confirma os dados | |
| | 8 - O sistema exibe uma mensagem que a pessoa foi alterada |
| | |

## Fluxo de Exceção I - Passo 5 - Atualizar Pessoa
| Ações do ator | Ações do sistema |
| :-----------------: |:-----------------: | 
| 1.1 - O usuário não preenche, ou apenas parcialmente, os dados requisitados | |  
| | 1.2 - O sistema exibe uma mensagem de erro |
| | O usuário é redirecionado ao passo 4 |
| | |

## Fluxo Principal - Remover Pessoa
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 1 - O usuário clica em Rede de Socorro | |  
| | 2 - O sistema mostra uma página, com as pessoas que já estão cadastradas e os botões Adicionar Nova Pessoa, Adicionar Pessoa, Remover Pessoa |  
| 3- O usuário clica em Remover Pessoa |  |
|  | 4 - O sistema lista todas as pessoas cadastradas na rede  |
| 5 - O usuário seleciona a(s) pessoa(s) e clica em Remover |  |
|  | 6 - O sistema mostra a(s) pessoa(s) selecionadas e pede confirmação ao usuário |
| 7 - O usuário clica em remover |  |
|  | 8 - O sistema exibe uma mensagem que a(s) pessoa(s) foi/foram removidas |
|  |  | 

## Fluxo Principal - Listar Pessoas
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 1 - O usuário clica em Rede de Socorro | |  
| | 2 - O sistema mostra uma página, com as pessoas que já estão cadastradas e os botões Adicionar Nova Pessoa, Adicionar Pessoa, Remover Pessoa |  

> Obs. as seções a seguir apenas serão utilizadas na segunda unidade do PDSWeb (segundo orientações do gerente do projeto).

## Diagrama de Interação (Sequência ou Comunicação)

> Substituir pela imagem correspondente...

## Diagrama de Classes de Projeto

> Substituir pela imagem contendo as classes (modelo, visão e templates) que implementam o respectivo CDU...