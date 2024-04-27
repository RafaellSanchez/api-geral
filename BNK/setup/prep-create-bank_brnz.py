import sqlite3

#create table bronze

print('iniciando conexao com o banco de dados!')
banco_de_dados = '/workspaces/api-geral/BNK/sql/bank.db'
# Conectar ao banco de dados SQLite
print('conectando ao banco de dados!')
conn = sqlite3.connect(banco_de_dados)

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

print('criando tabela bronze')
query = '''
CREATE TABLE IF NOT EXISTS tb_bank_brnz(
    nome TEXT, 
    cnpj TEXT,
    contrato_nome TEXT, 
    contrato_cnpj TEXT, 
    corporacao TEXT, 
    grupo TEXT, 
    isUnderestablishment TEXT, 
    cnpjnumber TEXT, 
    ender TEXT, 
    enderIdentInfo TEXT, 
    districtName TEXT, 
    townName TEXT, 
    ibgeCode TEXT, 
    postCode TEXT, 
    country TEXT, 
    countryCode TEXT, 
    latitude FLOAT, 
    longitude FLOAT, 
    semana TEXT, 
    open TEXT, 
    close TEXT, 
    tipoTelefone TEXT, 
    codigoPais TEXT, 
    codigoArea TEXT, 
    numeroTelefone TEXT
    
);
'''
print('executando query')
cursor.execute(query)

print('realizando o commit')
# Commit para salvar as alterações
conn.commit()
print('fechando a conexao')
# Fechar a conexão
conn.close()