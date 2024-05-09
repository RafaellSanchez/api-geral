import sqlite3
import time

print('iniciando processo transformação')
time.sleep(3)

print('carregando variaveis!')
try:
    banco = 'banco_cep.db'
    print('conectando com o banco de dados')
    banco_de_dados = f'/workspaces/api-geral/GEO/CEP/sql/db/{banco}'
    #conectar ao banco de dados SQLite
    conn = sqlite3.connect(banco_de_dados)
    cursor = conn.cursor()
    time.sleep(3)
    
    print('iniciando insert')
    insert_silver = '''
         INSERT INTO tb_cep_slver(
            ccep,
            cep_loc,
            ccep_compl,
            logradouro,
            bairro,
            localidade,
            uf,
            ibge,
            gia,
            ddd,
            siafi,
            nm_arquivo,
            data_arquivo,
            dthora_inclusao,
            dtIgtao
         )
         SELECT 
            ccep,
            cast(cep_loc as decimal) as cep_loc,
            cast(ccep_compl as decimal) as ccep_loc,
            logradouro,
            bairro,
            localidade,
            uf,
            ibge,
            gia,
            ddd,
            siafi,
            nome_arquivo as nm_arquivo,
            data_arquivo as data_arquivo,
            strftime('%Y%m%d_%H%M%S', 'now') as dthora_inclusao,
            strftime('%Y-%m-%d', 'now') as dtIgtao
        FROM tb_cep_brnz;
    '''
    
    cursor.execute(insert_silver)
    conn.commit()
    print('insert sucesso!')
except Exception as e:
    print(f'error: {e}')
    
print('Verificando tabela')
time.sleep(3)
tabela = 'tb_cep_slver'
query = f'''
select * from {tabela}
'''
cursor.execute(query)
resultados = cursor.fetchall()
print('Resultado:')
for linha in resultados:
    print(linha)
    
conn.close()