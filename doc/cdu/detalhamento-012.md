# CDU012 - Moderar Relato

- **Ator principal**: Administradores
- **Atores secundários**: Usuários	 
- **Resumo**: O administrador modera os relatos que são denunciados.
- **Pré-condição**: O adiminstrador deve estar logado e ter as devidas permissões para a moderação.
- **Pós-Condição**: O relato é removido ou mantido de acordo com a decisão do administrador.

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 1 - O usuário clica em "Moderar Relatos" na página de admin.  | |  
| | 2 - O sistema mostra a lista dos relatos denunciados na plataforma. | 
| 3 - O usuário escolhe uma denúncia. | |  
| | 4 - O sistema exibe o relato e comentário da denúncia feita, também mostra os botões "Excluir" ou "Manter". | 
| 5 - O usuário escolhe a opção "Excluir" e clica em "Confirmar". | |  
| | 6 - O sistema exibe uma mensagem que o relato foi removido. | 

## Fluxo Alternativo I - Passo 4.
| Ações do ator | Ações do sistema |
| :-----------------: |:-----------------: | 
| 1.1 - O usuário clica em "Manter" e "Confirmar". | |  
| | 1.2 - O sistema exibe uma mensagem que o relato foi mantido. | 
| | 1.3 - O usuário é direcionado para o passo 2. | 

## Fluxo Alternativo II - Passo 5. 
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 2.1 - O usuário clica apenas em "Confirmar". | |  
| | 2.2 - O sistema exibe uma mensagem que é preciso escolher uma opção para a denúncia. |  
| | 2.3 - O usuário é direcionado para o passo 4. | 

> Obs. as seções a seguir apenas serão utilizadas na segunda unidade do PDSWeb (segundo orientações do gerente do projeto).

## Diagrama de Interação (Sequência ou Comunicação)

> Substituir pela imagem correspondente...

## Diagrama de Classes de Projeto

> Substituir pela imagem contendo as classes (modelo, visão e templates) que implementam o respectivo CDU...