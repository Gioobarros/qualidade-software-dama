# CDU004 - Denunciar Relato

- **Ator principal**: Membros inscritos
- **Atores secundários**: Moderadores	 
- **Resumo**: O membro denuncia um relato. 
- **Pré-condição**: Existir um relato a ser denunciado.
- **Pós-Condição**: A denúncia é submetida a um moderador da plataforma.

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 1 - O membro clica em um relato. | |  
| | 2 - O sistema mostra um botão "Denunciar". | 
| 3 - O usuário clica no botão. | |  
| | 4 - O sistema exibe uma caixa de pequena de texto para explicar o motivo da denúncia. | 
| 5 - O usuário insere seu comentário e clica em "Submeter Denúncia". | |  
| | 6 - O sistema exibe uma mensagem informando que a denúncia foi submetida a um moderador da plataforma e o sistema redireciona o usuário para o "Mural de Força". | 

## Fluxo Alternativo I - Passo 5. 
| Ações do ator | Ações do sistema |
| :-----------------: |:-----------------: | 
| 1.1 - O usuário não insere um comentário e clica em "Submeter Denúncia" | |  
| | 1.2 - O sistema mostra uma mensagem pedindo para que algum comentário seja digitado. |
| | 1.3 - O usuário é direcionado para o passo 4. |
 

## Imagem Representativa do Caso de Uso
![Nome do Caso de Uso](.png)

> Obs. as seções a seguir apenas serão utilizadas na segunda unidade do PDSWeb (segundo orientações do gerente do projeto).

## Diagrama de Interação (Sequência ou Comunicação)

> Substituir pela imagem correspondente...

## Diagrama de Classes de Projeto

> Substituir pela imagem contendo as classes (modelo, visão e templates) que implementam o respectivo CDU...