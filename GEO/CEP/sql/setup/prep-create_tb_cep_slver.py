import sqlite3
import time
banco_de_dados = '/workspaces/api-geral/GEO/CEP/sql/db/banco_cep.db'
#conectar ao banco de dados SQLite
conn = sqlite3.connect(banco_de_dados)
cursor = conn.cursor()
time.sleep(3)
query = '''
CREATE TABLE IF NOT EXISTS tb_cep_slver(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cep TEXT,
    logradouro TEXT,
    bairro TEXT,
    localidade TEXT,
    uf TEXTE,
    ibge TEXT,
    gia TEXT,
    ddd INTEGER,
    siafi INTEGER,
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
conn.close()
print('codigo encerrado!')
print('tabela criada')
