# Considerações
Escolhemos o DuckDB como banco não relacional para nosso projeto principalmente pelo contexto analítico de nosso dataset e pela performance do banco.
O fato do DuckDB armazenar os dados em colunas no lugar de linhas facilita a leitura de apenas das colunas necessárias para a consulta, permite uma maior compressão dos dados, processamento vetorizado e parelelismo.
A linguagem de consultas é o SQL padrão, o que facilitou bastante nossa adaptação. O processamento do Duck possui 4 passos principais: 
1. Análise e parsing (verifica validade da sintaxe e transforma a consulta em uma estrutura de dados) 
2. Otimização do plano(remove colunas e tabelas desnecessárias, aplica filtros)
3. Execução vetorizada(reliza a consulta em vetores de, por exemplo, 1024 valores em vez de linha por linha. Isso otmiza o uso do hardware, como a memória cache do processador)
4. Multithreading automático(divide o serviço por várias threads)

Apesar de ser um banco orientado a análise e não transações concorrentes de escrita, o DuckDB implementa um modelo de controle de transações ACID (Atomicidade, Consistência, Isolamento e Durabilidade) com base em MVCC (Multi-Version Concurrency Control) o que é o suficiente para garantir isolamento entre leituras e gravações e a integridade dessas operações. Como nosso cenário envolvia majoritariamente consultas de leitura e análises, o controle de transações não chegou a ser uma grande preocupação para nõs.

A recuperação no Duck também é simplificada, pois podemos simplesmente copiar o arquivo binário do banco, quando estamos no modo persistente. No quesito segurança, esse banco é projetado para uso local, em um ambiente seguro, assim toda camada de segurança deve ser implementada pelo usuário. Por exemplo: arquivo do banco não é criptografado por padrão, logo, esse binário poderia ser guardado em um volume seguro do HD ou algo assim. Caso seja necessário acesso multiusuário, por exemplo, devemos utilizar ferramentas externas para adicionar camadas de autenticação, pois o Duck não possui sistema de usuários, senhas ou permissões. A proteção contra SQL injection existe, mas não é automática, cabendo ao usuário utilizar técnicas como bind parâmeters para evitar scripts maliciosos. 

# Modelo lógico:
![Modelo lógico](./assets/mod_logico.png)
