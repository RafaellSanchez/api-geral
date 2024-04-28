import sqlite3

print('iniciando conexao com o banco de dados!')
banco_de_dados = '/workspaces/api-geral/BNK/sql/bank.db'
# Conectar ao banco de dados SQLite
print('conectando ao banco de dados!')
conn = sqlite3.connect(banco_de_dados)

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()



insert_gold = '''
INSERT INTO tb_bank_gld(
nome_empresa
,cnpj_empresa
,contrato_nome
,contrato_cnpj
,corporacao
,grupo
,isUnderestablishment
,cnpjnumber
,endereco
,enderecoInfo
,distrito_nome
,cidade_nome
,codigo_ibge
,codigo_postal
,pais
,codigo_pais
,latitude
,longitude
,semana
,aberto
,fechado
,tipoTelefone
,codigoPais
,codigoArea
,numeroTelefone
,thora_inclusao
,dtIgtao
)
SELECT 
 id
,nome_empresa
,cnpj_empresa
,contrato_nome
,contrato_cnpj
,corporacao
,grupo
,isUnderestablishment
,cnpjnumber
,endereco
,enderecoInfo
,distrito_nome
,cidade_nome
,codigo_ibge
,codigo_postal
,pais
,codigo_pais
,latitude
,longitude
,semana
,aberto
,fechado
,tipoTelefone
,codigoPais
,codigoArea
,strftime('%Y%m%d_%H%M%S', 'now') AS thora_inclusao
,strftime('%Y-%m-%d', 'now') AS dtIgtao

FROM tb_bank_silver;
'''

cursor.execute(insert_gold)

# Commit para salvar as alterações
conn.commit()

print('insert executado com sucesso!')
table_name = 'tb_bank_gld'

query = f'''
select * from {table_name}
'''
cursor.execute(query)
resultados = cursor.fetchall()

for linha in resultados:
    print(linha)
    


# Fechar a conexão
conn.close()
print('execucao finalizada!')