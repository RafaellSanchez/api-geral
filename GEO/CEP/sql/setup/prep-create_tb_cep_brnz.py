import sqlite3

banco_de_dados = '/workspaces/api-geral/GEO/CEP/sql/db/banco_cep.db'
#conectar ao banco de dados SQLite
conn = sqlite3.connect(banco_de_dados)
cursor = conn.cursor()


query = '''
CREATE TABLE IF NOT EXISTS tb_cep_brnz(
    cep TEXT,
    logradouro TEXT,
    bairro TEXT,
    localidade TEXT,
    uf TEXTE,
    ibge TEXT,
    gia TEXT,
    ddd INTEGER,
    siafi INTEGER
);
'''

cursor.execute(query)
conn.commit()
conn.close()