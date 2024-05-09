import sqlite3

############################
#  EXECUTAR APENAS UMA VEZ #
############################


db = 'banco_cep.db'
banco_de_dados = f'/workspaces/api-geral/GEO/CEP/sql/db/{db}'
#conectar ao banco de dados SQLite
conn = sqlite3.connect(banco_de_dados)
cursor = conn.cursor()
print(f'db conectado: {db}')

tabela = 'tb_cep_brnz'
drop = f'''
drop table if exists {tabela};
'''
print(f'tabela excluida: {tabela}')
conn.commit()
print('executando uma nova query')
print(f'criando tabela: {tabela}')
query = f'''
CREATE TABLE IF NOT EXISTS {tabela}(
    ccep INTEGER,
    cep_loc INTEGER,
    ccep_compl INTEGER,
    logradouro TEXT,
    bairro TEXT,
    localidade TEXT,
    uf TEXTE,
    ibge TEXT,
    gia TEXT,
    ddd INTEGER,
    siafi INTEGER,
    nm_arquivo TEXT,
    data_arquivo TEXT
);
'''

cursor.execute(query)
print('query executada!')
conn.commit()
cursor.execute("PRAGMA table_info(tb_cep_brnz)")
colunas = cursor.fetchall()
print(f'describe da tabela: {tabela}')
print('resultado:')
for coluna in colunas:
    print(coluna[1])

conn.close()
print('codigo executado!')