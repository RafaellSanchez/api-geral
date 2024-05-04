import sqlite3
import time

############################
#  EXECUTAR APENAS UMA VEZ #
############################

print('iniciando prep create')
time.sleep(3)

print('carregando as variaveis.')
time.sleep(3)
db = 'banco_cep.db'
banco_de_dados = f'/workspaces/api-geral/GEO/CEP/sql/db/{db}'
#conectar ao banco de dados SQLite
conn = sqlite3.connect(banco_de_dados)
cursor = conn.cursor()
print(f'db conectado: {db}')

tabela = 'tb_cep_gld'
drop = f'''
drop table if exists {tabela};
'''
print(f'tabela excluida: {tabela}')
conn.commit()
time.sleep(3)
print('executando uma nova query')
print(f'criando tabela: {tabela}')

query = f'''
CREATE TABLE IF NOT EXISTS {tabela}(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cep TEXT,
    logradouro TEXT,
    bairro TEXT,
    localidade TEXT,
    uf TEXT,
    ibge TEXT,
    gia TEXT,
    ddd INTEGER,
    siafi INTEGER,
    nm_arquivo TEXT,
    data_arquivo TEXT,
    dthora_inclusao,
    dtIgtao
);
'''

cursor.execute(query)
print('executando query')
time.sleep(3)
conn.commit()
print('realizando commit')
time.sleep(3)
cursor.execute("PRAGMA table_info(tb_cep_gld)")
colunas = cursor.fetchall()
print(f'describe da tabela: {tabela}')
print('resultado:')
for coluna in colunas:
    print(coluna[1])

print('-----------------')
conn.close()
print('codigo encerrado!')
print(f'tabela criada: {tabela}')
