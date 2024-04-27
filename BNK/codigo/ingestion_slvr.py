import sqlite3

print('iniciando conexao com o banco de dados!')
banco_de_dados = '/workspaces/api-geral/BNK/sql/bank.db'
# Conectar ao banco de dados SQLite
print('conectando ao banco de dados!')
conn = sqlite3.connect(banco_de_dados)

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

insert_silver = '''
INSERT INTO tb_bank_silver(
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
nome AS nome_empresa
,CAST(cnpj AS INTEGER) AS cnpj_empresa
,contrato_nome
,contrato_cnpj
,corporacao
,grupo
,isUnderestablishment
,CAST(cnpjnumber AS INTEGER) AS cnpj_number
,ender AS endereco
,enderIdentInfo AS enderecoInfo
,districtName AS distrito_nome
,townName AS cidade_nome
,ibgeCode AS codigo_ibge
,postCode AS codigo_postal
,country AS pais
,countryCode AS codigo_pais
,latitude
,longitude
,semana
,open AS aberto
,close AS fechado
,tipoTelefone
,codigoPais
,codigoArea
,numeroTelefone
,strftime('%Y%m%d_%H%M%S', 'now') AS thora_inclusao
,strftime('%Y-%m-%d', 'now') AS dtIgtao

from tb_bank_brnz;
'''

cursor.execute(insert_silver)

# Commit para salvar as alterações
conn.commit()
print('insert executado com sucesso!')
table_name = 'tb_bank_silver'

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