import sqlite3

try:
    banco = 'banco_cep.db'
    print('conectando com o banco de dados')
    banco_de_dados = f'/workspaces/api-geral/GEO/CEP/sql/db/{banco}'
    #conectar ao banco de dados SQLite
    conn = sqlite3.connect(banco_de_dados)
    cursor = conn.cursor()
    
    insert_silver = '''
         INSERT INTO tb_cep_slver(
            cep,
            logradouro,
            bairro,
            localidade,
            uf,
            ibge,
            gia,
            ddd,
            siafi,
            dthora_inclusao,
            dtIgtao
         )
         SELECT 
            cep,
            logradouro,
            bairro,
            localidade,
            uf,
            ibge,
            gia,
            ddd,
            siafi,
           strftime('%Y%m%d_%H%M%S', 'now') AS dthora_inclusao,
           strftime('%Y-%m-%d', 'now') AS dtIgtao
        FROM tb_cep_brnz;
    '''
    
    cursor.execute(insert_silver)
    conn.commit()
    
except Exception as e:
    print(f'error: {e}')
    
print('Verificando tabela')
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