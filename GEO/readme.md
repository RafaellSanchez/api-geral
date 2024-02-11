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
 >      |     |___ igtao-silver.ipynb
 >      |     |___ igtao-sp.ipynb
 >      |     |___ ingestion-sql.ipynb
 >      |     |___ teste.ipynb
 >      |
 >      |-- dados
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
 >            |___ dados_geo.db
 >                      |___ tables
 >                              |___ bronze_dados_geo
 >                              |___ silver_dados_geo
 >                              |___ sp_dados_geo


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