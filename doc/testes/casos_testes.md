## Casos de testes do DAMA

### Histórico de alterações
| Data | Versão | Descrição | Autores |
| --- | --- | --- | --- |
| 13/05/25  | 0.0 | Versão inicial | Felipe da Costa, Giovana Beatriz e Leandro Sizilio |

## Testes funcionais
### Publicar relato
| Conteúdo     | Publicador     | Usuário     | Resultado Esperado     | Resultado Obtido     | Situação    | 
|--------------|---------------|---------------|---------------|---------------|---------------|
| Relato preenchido    | Usuário autenticado     | Preenche o campo corretamente e clica em “publicar”.      | Relato criado, status “sub”      |       |       | 
| Não preenchido     | Usuário autenticado      | Tenta publicar um relato sem preencher.    | Erro. Aviso de que o preenchimento do campo é obrigatório  |      |    |        
| Relato preenchido    | Usuário não autenticado      | Tenta publicar um relato sem estar autenticado    | Erro. Aviso de que apenas usuários autenticados podem publicar relatos. Redirecionado para login ou cadastro.       |       |    | 
| Alteração no relato     | Usuário autenticado diferente do publicador     | Tenta editar um relato publicado por outro usuário.    | Erro. Aviso de que aquele usuário não possui permissão para editar aquele determinado relato.       |      |     | 

### Fazer cadastro de profissional
| Username     | CPF    | Conselho     | Contato     | Perfil     | Usuário     | Resultado Esperado              | Resultado Obtido              | Situação   |
|--------------|---------------|---------------|---------------|---------------|---------------|----------------------------------|-------------------------------|------------|
| Maria     |16766253982      | 17/6257      | 84999999999 | pro  | Cadastrado corretamente  |Cadastro realizado|  |  |
| Maria     | Não preenchido      | 17/6257 | 84999999999 | pro   | CPF não preenchido |Erro. Aviso de que campo “CPF” é obrigatório|  |  |
| João     | 123      | 17/6239      | 84888888888      | pro      | CPF preenchido mas não válido      | Erro. Aviso de que o “CPF” é inválido  |  |   |
| Ana     | 16766253982      | 17/4208      | 84900000000      | pro      | CPF já cadastrado no sistema      | Erro. Aviso de que o “CPF” já está cadastrado  |  |  |
| Samir     | 09826863862     | Não preenchido | 84966286153     | pro      | O campo “Conselho” não foi preenchido      | Erro. Aviso de que o campo “Conselho” é obrigatório  |  |  |
| Bruna    | 51477258251      | 17/6258      | Não preenchido      | pro      | O campo “Contato” não foi preenchido      |  Erro. Aviso de que o campo “Contato” é obrigatório |  |   |
| Não preenchido     | 12534567891      | 17/5487 | 84977777777 | pro  | O campo “username” não foi preenchido | Erro. Aviso de que o campo “username” é obrigatório  |  |  |
| Laura    | 12534567891 | 17/5487      | 84977777777 | Não preenchido | O campo “perfil” não foi preenchido | Erro. Aviso de que o campo “perfil” é obrigatório|  |  |

### Fazer cadastro de ONGs
| Username     | Razão social    | CNPJ     | Contato     | Perfil     | Usuário     | Resultado Esperado              | Resultado Obtido              | Situação   |
|--------------|---------------|---------------|---------------|---------------|---------------|----------------------------------|-------------------------------|------------|
| ong-vida     |ONG Vida      | 73692874000184 | 84988888888 | ONG  | Cadastrado corretamente  |Cadastro realizado|  |  |
| ong-vida     |Não preenchido| 73692874000184 | 84988888888 | ONG   | O campo “razão social” não foi preenchido”|Erro. Aviso de que o campo “Razão Social” é obrigatório|  |  |
| ong-vida    |  ONG Vida | 123 | 84888888888      | ONG      | O campo “CNPJ” foi preenchido mas não válido| Erro. Aviso de que o campo “CNPJ” é inválido|  |   |
|ong-amor| ONG amor | 73692874000184| 84900000000      | ONG      |O CNPJ já está sendo utilizado| Erro. Aviso de que o CNPJ cadastrado já está cadastrado no sistema.|  |  |
|Não preenchido| ONG paz|11111111000111| 84966286153     | ONG      | O campo “Conselho” não foi preenchido      | Erro. Aviso de que o campo “Conselho” é obrigatório  |  |  |
|Não preenchido| ONG paz| 11111111000111| 84977777777 | ONG      | O campo “username” não foi preenchido | Erro. Aviso de que o campo “username” é obrigatório |  |   |
|ong-paz|ONG paz| 11111111000111| Não preenchido | ONG  | O campo “Contato” não foi preenchido | Erro. Aviso de que o campo “Contato” é obrigatório |  |  |
|ong-paz| ONG paz |11111111000111| 84977777777 | Não preenchido | O campo “perfil” não foi preenchido|Erro. Aviso de que o campo “perfil” é obrigatório|  |  |


## Testes não funcionais
### Publicaçao de relato

| **Categoria** | Usabilidade |
|-----------------|-------------|
| **Automatizado** | Não         |
| **Duração** | 2 minutos   |
| **Executado** | Não            |
| **Responsável** |             |
| **Data** |             |

#### Procedimentos:
Simular o preenchimento de um relato através dos usuários autenticados, perfil profissional e perfil ONG.

#### Critérios de Aceitação:
Os usuários devem conseguir identificar todos os campos obrigatórios.
#### Resultado:

### Tempo de resposta do cadastro de profissionais

| **Categoria** | Desempenho |
|-----------------|-------------|
| **Automatizado** | Não         |
| **Duração** | 1 minuto   |
| **Executado** | Não            |
| **Responsável** |             |
| **Data** |             |

#### Procedimentos:
Simular o preenchimento do cadastro de um profissional, utilizando dados válidos. Medir o tempo de resposta, entre o envio e o retorno da confirmação. 


#### Critérios de Aceitação:
Tempo de resposta menor ou igual a 3 segundos.

#### Resultado:


### Validação de segurança do CNPJ do cadastro de ONGs	

| **Categoria** | Segurança |
|-----------------|-------------|
| **Automatizado** | Não         |
| **Duração** | 3 minutos   |
| **Executado** | Não            |
| **Responsável** |             |
| **Data** |             |

#### Procedimentos:
Tentar fraudar a validação do campo “CNPJ” dos usuários profissionais, enviando dados falsos para API.


#### Critérios de Aceitação:
O sistema deve rejeitar qualquer conteúdo que não esteja no formato válido do CNPJ, não deve permitir a criação de um usuário com dados inválidos.

#### Resultado: