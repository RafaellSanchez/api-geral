import sqlite3

#função para mensagem
def mensagem(msg):
    print('-' *25)
    print(msg)
    print('-' *25)

#create table gold

print('iniciando conexao com o banco de dados!')
banco_de_dados = '/workspaces/api-geral/BNK/sql/bank.db'

# Conectar ao banco de dados SQLite
print('conectando ao banco de dados!')
conn = sqlite3.connect(banco_de_dados)

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

create_gold = '''
CREATE TABLE IF NOT EXISTS tb_bank_gld(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
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
    numeroTelefone TEXT,
    thora_inclusao,
    dtIgtao
);
'''
cursor.execute(create_gold)

mensagem('tabela criada')
# Commit para salvar as alterações
conn.commit()
# Execute uma consulta SQL para obter as colunas da tabela
cursor.execute("PRAGMA table_info(tb_bank_gld)")
colunas = cursor.fetchall()
print('carregando informações das colunas')
for coluna in colunas:
    print(coluna[1])

mensagem('fim da execucao')