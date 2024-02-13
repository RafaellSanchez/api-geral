import sqlite3

# Especificar o caminho para o banco de dados SQLite
caminho_banco_dados = '/workspaces/api-geral/GEO/sql/bd_geo.db'

# Conectar ao banco de dados SQLite (ou criar um novo se não existir)
conn = sqlite3.connect(caminho_banco_dados)

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Script para criar a nova tabela slvr_geo
create_silver = '''
-- Criar a nova tabela slvr_geo para armazenar dados normalizados
CREATE TABLE IF NOT EXISTS slvr_geo (
    uuid TEXT,  -- Identificador único para cada registro
    id INTEGER,  -- ID único para cada registro
    nome TEXT,  -- Nome do distrito
    idMunicipio INTEGER,  -- ID do município associado ao distrito
    nomeMunicipio TEXT,  -- Nome do município associado ao distrito
    idMacro INTEGER,  -- ID da macroregião associada ao município
    nomeMacroMunicipio TEXT,  -- Nome da macroregião associada ao município
    idUf INTEGER,  -- ID do estado associado ao município
    estado TEXT,  -- Nome do estado associado ao município
    siglaUf TEXT,  -- Sigla do estado associado ao município
    idRegiao INTEGER,  -- ID da região associada ao estado
    regiao TEXT,  -- Nome da região associada ao estado
    siglaRegiao TEXT,  -- Sigla da região associada ao estado
    dtIgtao DATE  -- Data de ingestão dos dados
);
'''

# Executar o script para criar a nova tabela
cursor.execute(create_silver)

# Consulta para selecionar os dados da tabela bronze e inseri-los na tabela silver
consulta_insert = '''
-- Selecionar e normalizar os dados da tabela bronze para inserção na tabela silver
INSERT INTO slvr_geo (
    uuid,
    id,
    nome,
    idMunicipio,
    nomeMunicipio,
    idMacro,
    nomeMacroMunicipio,
    idUf,
    estado,
    siglaUf,
    idRegiao,
    regiao,
    siglaRegiao,
    dtIgtao
)
SELECT
    uuid,  -- Identificador único
    CAST(id AS INTEGER),  -- ID convertido para inteiro
    nome,  -- Nome do distrito
    CAST(id_mun AS INTEGER) AS idMunicipio,  -- ID do município
    nm_mun AS nomeMunicipio,  -- Nome do município
    CAST(id_mcr AS INTEGER) AS idMacro,  -- ID da macroregião
    nm_mcr AS nomeMacroMunicipio,  -- Nome da macroregião
    CAST(id_uf AS INTEGER) AS idUf,  -- ID do estado
    nm_uf AS estado,  -- Nome do estado
    sigla_uf AS siglaUf,  -- Sigla do estado
    CAST(id_reg AS INTEGER) AS idRegiao,  -- ID da região
    nm_reg AS regiao,  -- Nome da região
    sigla_rg AS siglaRegiao,  -- Sigla da região
    strftime('%Y-%m-%d', 'now') AS dtIgtao  -- Data de ingestão (atual)
FROM
    brnz_geo;  -- Tabela bronze
'''

# Executar a consulta para selecionar e inserir os dados
cursor.execute(consulta_insert)

# Commit para salvar as alterações
conn.commit()

# Consulta SQL para listar todas as tabelas no banco de dados
show_tables_query = "SELECT name FROM sqlite_master WHERE type='table';"
cursor.execute(show_tables_query)

# Recuperar o resultado da consulta e imprimir as tabelas
tables = cursor.fetchall()
print("Tabelas no banco de dados:")
for table in tables:
    print(table[0])

# Fechar a conexão
conn.close()
