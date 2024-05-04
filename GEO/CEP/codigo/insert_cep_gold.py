import sqlite3

#############################
#  EXECUTAR APENAS UMA VEZ  #
#############################

try:
    print('carregando variaveis')
    banco = 'banco_cep.db'
    print('conectando com o banco de dados')
    banco_de_dados = f'/workspaces/api-geral/GEO/CEP/sql/db/{banco}'
    #conectar ao banco de dados SQLite
    conn = sqlite3.connect(banco_de_dados)
    cursor = conn.cursor()
    
    insert_gold = '''
         INSERT INTO tb_cep_gld(
            cep,
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
            cep,
            logradouro,
            bairro,
            localidade,
            uf,
            ibge,
            gia,
            ddd,
            siafi,
            nm_arquivo
            data_arquivo,
            dthora_inclusao,
           strftime('%Y%m%d_%H%M%S', 'now') AS dthora_inclusao,
           strftime('%Y-%m-%d', 'now') AS dtIgtao
        FROM tb_cep_slver;
    '''
    
    cursor.execute(insert_gold)
    conn.commit()

except Exception as e:
    print(f'Error: {e}')
    
    
print('Verificando tabela')
tabela = 'tb_cep_gld'
query = f'''
select * from {tabela}
'''
cursor.execute(query)
resultados = cursor.fetchall()
print('Resultado:')
for linha in resultados:
    print(linha)
 
conn.close()
print('execução concluida')