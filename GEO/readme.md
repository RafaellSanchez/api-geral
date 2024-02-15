## Repositório Geo

Status: Desenvolvendo

### Estrutura:

diretório: GEO
 >      |-- bckp
 >      |     |___ dados_teste_2024-02-04 15:58:33.txt
 >      |     |___ dados_teste.json
 >      |
 >      |-- codigo
 >      |     |___ api-geo.bh.py
 >      |     |___ api-geo-mg.py
 >      |     |___ api-geo-pe.py
 >      |     |___ api-geo-sp.py
 >      |     |___ api-geo.py 
 >      |     |___ api-teste-geo.ipynb
 >      |     |___ cripto-teste.ipynb
 >      |     |___ igtao-silver.ipynb
 >      |     |___ igtao-sp.ipynb
 >      |     |___ ingestion-bronze.py
 >      |     |___ ingestion-silver.py
 >      |     |___ ingestion-sql.ipynb
 >      |     |___ teste.ipynb
 >      |
 >      |-- dados
 >      |     |___ dados_cript.bin
 >      |     |___ dados_criptografados.txt
 >      |     |___ dados_geo_BA.txt
 >      |     |___ dados_geo_MG.txt
 >      |     |___ dados_geo_PE.txt
 >      |     |___ dados_geo_SP.txt
 >      |     |___ dados_geo.txt
 >      |     |___ dados_id_uf.txt
 >      |
 >      |-- doc
 >      |
 >      |-- sql
 >           |
 >           |___ bd_geo.db
 >           |          |___ tables
 >           |                  |___ brnz_geo
 >           |                  |___ slvr_geo
 >           |
 >           |___ dados_geo.db
 >           |          |___ tables
 >           |                  |___ bronze_dados_geo
 >           |                  |___ silver_dados_geo
 >           |                  |___ sp_dados_geo
 >           |
 >           |___ teste_dados_criptografados.db
 >                      |___ tables
 >                              |___ dados_descriptografados


#### Descrição do Repositório:
 - Este repositório é dedicado a uma API de geolocalização fornecida pelo Instituto Brasileiro de Geografia e Estatística (IBGE), que disponibiliza uma variedade de recursos para consulta de informações geoespaciais do Brasil. A API permite acesso a dados detalhados sobre municípios, estados e regiões do país, oferecendo uma fonte confiável para integração em diversas aplicações.

#### Recursos Principais:

##### Consulta de Municípios: 
- A API oferece a capacidade de consultar informações detalhadas sobre municípios brasileiros, incluindo dados como nome, código IBGE, estado ao qual pertencem, coordenadas geográficas e outros atributos relevantes.

##### Consulta de Estados:
- Permite acessar informações sobre os estados brasileiros, incluindo nome, sigla, região a que pertencem, além de dados geográficos como latitude, longitude e limites territoriais.

##### Consulta de Regiões:
- Facilita a obtenção de dados sobre as regiões geográficas do Brasil, como nome, sigla, estados que compõem a região e coordenadas geográficas de referência.

##### Dados Atualizados:
- Os dados fornecidos pela API são mantidos atualizados pelo IBGE, garantindo precisão e confiabilidade para uso em aplicações de diversas áreas, como desenvolvimento de software, análise de dados e visualização geoespacial.

##### Documentação Abrangente:
- A API é acompanhada por uma documentação completa, que descreve detalhadamente os endpoints disponíveis, parâmetros de consulta e exemplos de uso, facilitando a integração por parte dos desenvolvedores.


##### Bibliotecas utilizadas:
    requests:
        Uma biblioteca Python simples e elegante para fazer solicitações HTTP. É amplamente utilizada para interagir com APIs da web e acessar recursos da internet.

    pandas:
        Uma poderosa biblioteca de análise de dados em Python. Ela oferece estruturas de dados flexíveis e ferramentas para manipulação e análise de dados, especialmente para conjuntos de dados tabulares.

    datetime:
        Um módulo Python que fornece classes para manipulação de datas e horários. Ele permite a criação, manipulação e formatação de objetos de data e hora em Python.

    json:
        Um módulo Python para trabalhar com dados JSON (JavaScript Object Notation). Ele fornece funções para serializar e desserializar objetos Python em JSON e vice-versa.

    cryptography.fernet:
        Uma biblioteca de criptografia Python que oferece implementações do algoritmo de criptografia simétrica Fernet. Ele é amplamente utilizado para criptografar e descriptografar dados de forma segura.

    time:
        Um módulo Python que fornece funções relacionadas ao tempo. Ele permite manipular o tempo em diferentes formatos, realizar operações de espera e medição de tempo.

    sqlite3:
        Um módulo Python que fornece uma interface para o SQLite, um sistema de gerenciamento de banco de dados SQL embutido. Ele permite interagir com bancos de dados SQLite usando operações SQL padrão.

    uuid:
        Um módulo Python que fornece funções para gerar, manipular e trabalhar com UUIDs (identificadores únicos universais). Ele é frequentemente usado para criar identificadores únicos para objetos em sistemas distribuídos.