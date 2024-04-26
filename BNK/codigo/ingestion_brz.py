import pandas as pd
import sqlite3
from datetime import datetime
import time

print('iniciando ingestao')
time.sleep(3)
print('carregando variaveis')
arquivo_trans = '/workspaces/api-geral/BNK/dados/dados_bank_20240426011326.txt'
df = pd.read_csv(arquivo_trans, delimiter=';', usecols=lambda column: column !='Unnamed: 0')

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


#################################################################
print('conectando novamente no banco de dados')
banco_de_dados = '/workspaces/api-geral/BNK/sql/bank.db'
# Conectar ao banco de dados SQLite
conn = sqlite3.connect(banco_de_dados)
time.sleep(3)
# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

print('carregando as variaveis para iniciar a ingestao')
print('abrindo arquivo csv')
time.sleep(3)
arquivo_trans = '/workspaces/api-geral/BNK/dados/dados_bank_20240426011326.txt'
file = pd.read_csv(arquivo_trans, delimiter=';', usecols=lambda column: column !='Unnamed: 0')
file.to_sql('tb_bank_brnz', conn, if_exists='replace', index=False)
print('arquivo ingerido!')
time.sleep(3)

print('commit')
# Commit para salvar as alterações
conn.commit()
print('fechando conexao')
# Fechar a conexão
conn.close()
time.sleep(3)

##################################################################

print('conectando no banco de dados!')
banco_de_dados = '/workspaces/api-geral/BNK/sql/bank.db'
# Conectar ao banco de dados SQLite
conn = sqlite3.connect(banco_de_dados)
# Criar um cursor para executar comandos SQL
cursor = conn.cursor()
print('iniciando conexao')
print('carregando variaveis')
table_name = 'tb_bank_brnz'
time.sleep(3)

print('carregando query sql para verificar os dados!')
query = f'''
select * from {table_name}
'''
cursor.execute(query)
resultados = cursor.fetchall()

for linha in resultados:
    print(linha)


print('dados carregados com sucesso!')