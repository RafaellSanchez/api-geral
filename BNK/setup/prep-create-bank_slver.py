import sqlite3

#create table silver

print('iniciando conexao com o banco de dados!')
banco_de_dados = '/workspaces/api-geral/BNK/sql/bank.db'
# Conectar ao banco de dados SQLite
print('conectando ao banco de dados!')
conn = sqlite3.connect(banco_de_dados)

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

create_silver = '''
CREATE TABLE IF NOT EXISTS test_bank_silver(
    nome_empresa TEXT, 
    cnpj_empresa INTEGER,
    contrato_nome TEXT, 
    contrato_cnpj TEXT, 
    corporacao TEXT, 
    grupo TEXT, 
    isUnderestablishment TEXT, 
    cnpjnumber INTEGER, 
    endereco TEXT, 
    enderecoInfo TEXT, 
    distrito_nome TEXT, 
    cidade_nome TEXT, 
    codigo_ibge TEXT, 
    codigo_postal TEXT, 
    pais TEXT, 
    codigo_pais TEXT, 
    latitude FLOAT, 
    longitude FLOAT, 
    semana TEXT, 
    aberto TEXT, 
    fechado TEXT, 
    tipoTelefone TEXT, 
    codigoPais TEXT, 
    codigoArea TEXT, 
    numeroTelefone TEXT    
);
'''
cursor.execute(create_silver)
print('realizando commit')
# Commit para salvar as alterações
conn.commit()
print('fechando conexao!')
# Fechar a conexão
conn.close()