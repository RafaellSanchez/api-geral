import pandas as pd
import sqlite3
import os

print('carregando variaveis')
caminho = '/workspaces/api-geral/GEO/CEP/dados/'
palavra_chave = 'resultado_concat'
# arquivo = 'resultado_concat_20240501_162447.txt'

lista_caminho = os.listdir(caminho)
try:
    
    for nome_arquivo in lista_caminho:
        if palavra_chave in nome_arquivo:
            src_arquivo = os.path.join(caminho, nome_arquivo)
            # print(src_arquivo)
            # print(nome_arquivo)

            df = pd.read_csv(f'{src_arquivo}', delimiter=';', usecols=lambda column: column !='Unnamed: 0')
            df['nome_arquivo'] = nome_arquivo
            data = nome_arquivo[17:32]
            df['data_igtao'] = data
            # print(df)
            
            print('carregando informações no df')
            banco = 'banco_cep.db'
            print('conectando com o banco de dados')
            banco_de_dados = f'/workspaces/api-geral/GEO/CEP/sql/db/{banco}'
            #conectar ao banco de dados SQLite
            conn = sqlite3.connect(banco_de_dados)
            cursor = conn.cursor()

            df.to_sql('tb_cep_brnz', conn, if_exists='replace', index=False)
            print('arquivo ingerido')
            conn.commit()
            
            #backp
            backup = '/workspaces/api-geral/GEO/CEP/backp/'
            save = df.to_csv(f'{backup}{nome_arquivo}')
            print(f'arquivo salvo no caminho:{backup}')
            print(f'nome do arquivo: {nome_arquivo}')
            
except Exception as e:
    print(f'Error: {e}')
 
        
print('Verificando tabela')
tabela = 'tb_cep_brnz'
query = f'''
select * from {tabela}
'''
cursor.execute(query)
resultados = cursor.fetchall()
print('Resultado:')
for linha in resultados:
    print(linha)     



















# print('carregando variaveis')
# caminho = '/workspaces/api-geral/GEO/CEP/dados/'
# palavra_chave = 'resultado_concat'
# # arquivo = 'resultado_concat_20240501_162447.txt'

# lista_caminho = os.listdir(caminho)
# try:
#     for nome_arquivo in lista_caminho:
#         if palavra_chave in nome_arquivo:
#             src_arquivo = os.path.join(caminho, nome_arquivo)
#             print(src_arquivo)

#             df = pd.read_csv(f'{src_arquivo}', delimiter=';', usecols=lambda column: column !='Unnamed: 0')
#             # print(df)
#             print('carregando informações no df')
#             banco = 'banco_cep.db'
#             print('conectando com o banco de dados')
#             banco_de_dados = f'/workspaces/api-geral/GEO/CEP/sql/db/{banco}'
#             #conectar ao banco de dados SQLite
#             conn = sqlite3.connect(banco_de_dados)
#             cursor = conn.cursor()

#             df.to_sql('tb_cep_brnz', conn, if_exists='replace', index=False)
#             print('arquivo ingerido')
#             conn.commit()

# except Exception as e:
#     print(f'Erro: {e}')

# print('Verificando tabela')
# tabela = 'tb_cep_brnz'
# query = f'''
# select * from {tabela}
# '''
# cursor.execute(query)
# resultados = cursor.fetchall()
# print('Resultado:')
# for linha in resultados:
#     print(linha)