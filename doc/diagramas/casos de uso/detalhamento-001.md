# CDU001 - Publicar Relato


- **Ator principal**: Usuários do tipo ONG ou Profissionais
- **Resumo**: ONG ou Profissional publica um relato sobre um caso de violência contra mulheres.
- **Pré-condição**: Usuário estar cadastrado e logado e ser um Profissional ou uma ONG.




## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 1 - O usuário clica em "Mural de Força" na página inicial. | |  
| | 2 -  O sistema apresenta uma página com opções para acessar os relatos já publicados ou criar um novo relato. | 
| 3 - O usuário clica em "publicar relato". | |
| | 4 - O sistema apresenta um campo para ser adicionado o relato. |
| 5 - O usuário preenche o campo com o relato e clica em "publicar" | |
| | 6 - O sistema retorna um campo de confirmação de responsabilidade sobre as informações. |
|  8 - O relato é publicado.| |

## Fluxo Alternativo I - Usuário não cadastrado ou não logado.
| Ações do ator | Ações do sistema |
| :-----------------: |:-----------------: | 
| 1.1 - O usuário clica em "Publicar Relato" sem estar cadastrado ou logado. | |  
| | 1.2 - O sistema redireciona para uma página de cadastro.  |
| 1.3 - O usuário realiza o login ou se cadastra no sistema. | | 
| | 1.4 - O usuário valida os dados e redireciona para o "Mural de Força" com o campo para publicação disponível.  |


## Fluxo de Exceção 1 - Conexão interrompida.
| Ações do ator | Ações do sistema |
| :-----------------: |:-----------------: | 
| 1.1 - O usuário tenta enviar o relato, mas a conexão é interrompida antes da conclusão.  | |  
| | 1.2 - O sistema exibe uma mensagem de erro.  |
| | 1.3 - O sistema retorna a página de "Mural de força" após ter a conexão reestabelecida.  |



## Diagrama de Interação (Sequência ou Comunicação)

> Substituir pela imagem correspondente...


## Diagrama de Classes de Projeto

> Substituir pela imagem contendo as classes (modelo, visão e templates) que implementam o respectivo CDU...