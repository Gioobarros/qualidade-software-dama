# Modelo de Dados

## Diagrama ER

<img src="https://imgur.com/77v4XHv.png" width="600" height="100%" />

## Modelo Relacional

<img src="https://imgur.com/D5SYc7t.png" width="600" height="100%" />

## Dicionário de Dados

--- 
**Tabela** : Usuário									

*Descrição* : Armazena as informações dos usuários									

*Observações* : O tipo de Tipo de usuario deveria ser CHOICE para a pessoa escolher entre os tipos ONG, PROFISSIONAL E NORMAL.

| Nome | Descrição | Tipo de Dado | Tamanho | Null | PK | FK | Unique | Identity | Default | Check | 
| ------- | --------- | ------------ | ------- | ---- | -- | -- | ------ | -------- | ------- | ----- |
| usuario_id | identificação do usuário | INTEGER |  | &#9744;  | &#9745; | &#9744; | &#9744; | &#9744; |   |   | 
| nome_login | nome de login do usuário | TEXT |   | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| senha | senha de acesso do usuário | VARCHAR | 255 | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| telefone | telefone para contato do usuário | INTEGER | 11 | &#9745;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| tipo | tipo de usuario, podendo ser ONG, PROFISSIONAL ou NORMAL | BIT |   | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| razão_social | forma de confirmação do tipo ONG | TEXT |  | &#9745;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| email | email para contato | TEXT |   | &#9745;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| nome_completo | nome completo para verificações profissionais | TEXT |   | &#9745;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| carteira | forma para confirmar o profissional | TEXT |   | &#9745;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 

--- 
**Tabela** : Denúncia

*Descrição* : Armazena as informações das denuncias

*Observações* :

| Nome | Descrição | Tipo de Dado | Tamanho | Null | PK | FK | Unique | Identity | Default | Check | 
| ------- | --------- | ------------ | ------- | ---- | -- | -- | ------ | -------- | ------- | ----- |
| descricao_denuncia | Texto da denuncia | TEXT |   | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| tipo_local | local onde ocorreu | CHAR |   | &#9745;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| relacao_autor | relacao da vitima com o autor | TEXT |   | &#9745;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| zona_cidade | zona da cidade onde ocorreu | CHAR |   | &#9745;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| idade_vitima | idade da vitima | INTEGER |   | &#9745;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| data_denuncia | data de quando ocorrreu | DATE |   | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| denuncia_id | identificação da denuncia | INTEGER |   | &#9744;  | &#9745; | &#9744; | &#9744; | &#9744; |   |   | 


--- 
**Tabela** : Relato

*Descrição* : Armazera as informações dos relatos

*Observações* : Esta tabela utilizara duas chaves estrangeiras, sendo uma da tabela Usuário e outra da tabela comentario.

| Nome | Descrição | Tipo de Dado | Tamanho | Null | PK | FK | Unique | Identity | Default | Check | 
| ------- | --------- | ------------ | ------- | ---- | -- | -- | ------ | -------- | ------- | ----- |
| texto_relato | Texto descrito no relato | TEXT |   | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| relato_id | identificação do relato | INTEGER |   | &#9744;  | &#9745; | &#9744; | &#9744; | &#9744; |   |   | 
| usuario_id | identificação do usuario | INTEGER |   | &#9744;  | &#9744; | &#9745; | &#9744; | &#9744; |   |   | 
| data_relato | data de publicação do relato | DATE |   | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 

--- 
**Tabela** : Material

*Descrição* : Armazena os materiais didaticos do site

*Observações* : Esta tabela utiliza a a chave estrangeira da tabela usuario.

| Nome | Descrição | Tipo de Dado | Tamanho | Null | PK | FK | Unique | Identity | Default | Check | 
| ------- | --------- | ------------ | ------- | ---- | -- | -- | ------ | -------- | ------- | ----- |
| counteúdo | Conteudo do material publicado | TEXT |   | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| referencias | referencias utilizadas no material postado | TEXT |   | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| arquivo_anexado | arquivos que fazem referencia ao material postado | VARCHAR | 255  | &#9745;  | &#9744; | &#9745; | &#9744; | &#9744; |   |   | 
| usuario_id | identificação do usuario que fez a publicação | INTEGER |   | &#9744;  | &#9744; | &#9745; | &#9744; | &#9744; |   |   | 
| material_id | identificação do material | INTEGER |   | &#9744;  | &#9745; | &#9744; | &#9744; | &#9744; |   |   | 
| data_material | Data do momento que foi publicado o material | DATE |   | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
