import json
import pandas as pd
import sqlite3
import os
from datetime import datetime
import os.path
import time
import sys


arq_dir = "/workspaces/api-geral/ING/app/src/data/tmp/backup_arquivo.txt"
landing = '/workspaces/api-geral/ING/app/src/data/landing/'
file_tb_json = '/workspaces/api-geral/ING/app/src/layouts/cep/estrutura.json'
file_col_json = '/workspaces/api-geral/ING/app/src/layouts/cep/tabela_cep.json'
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

ultimo_timestamp = None
caminho_arquivo = None

with open(f'{file_col_json}', 'r') as f:
    config_colunas = json.load(f)
    print('lendo estrutura de coluna json')

with open(file_tb_json, 'r') as f:
    config_estrutura = json.load(f)
    print('lendo estrutura de coluna json')
    print(config_estrutura)
    key = config_estrutura['nomeArquivoChave']
    database = config_estrutura['banco']
    print(f"palavra chave: {key}")

try:  
    with open(arq_dir, 'r+') as dados:
        conteudo_load = dados.readlines()
        print(f'dados conteudo_load: {conteudo_load}')

        for root, dirs, lista in os.walk(landing):
            for nome_arquivo in lista:
                if key in nome_arquivo:
                    caminho_completo = os.path.join(root, nome_arquivo)
                    print(f'Arquivo encontrado: {caminho_completo}')
                    sav = os.path.basename(caminho_completo)
                    print(f'conteudo a gravar: {sav}')
                    
                    if sav + '\n' not in conteudo_load:
                        dados.write(f"{sav}\n")
                        print(f'dados salvo: {sav}')
                        print('dados gravado!')
                        dados.flush()
                        os.ftruncate(dados.fileno(), dados.tell())
                        print('=================================')
                        
                        if caminho_completo.endswith('.txt'):
                            dados = pd.read_csv(caminho_completo, delimiter=';', header=None, names=[col['nome'] for col in config_colunas['colunas']])
                        elif caminho_completo.endswith('.csv'):
                            dados = pd.read_csv(caminho_completo, header=None, names=[col['nome'] for col in config_colunas['colunas']])
                        elif caminho_completo.endswith('.bin'):
                            pass
                        else:
                            raise ValueError("Formato de arquivo não suportado")

                        print('convertendo tipos de dados')

                        for col in config_colunas['colunas']:
                            if col['tipo'] == 'int':
                                dados[col['nome']] = dados[col['nome']].astype(int)
                            elif col['tipo'] == 'float':
                                dados[col['nome']] = dados[col['nome']].astype(float)
                            elif col['tipo'] == 'data':
                                dados[col['nome']] = pd.to_datetime(dados[col['nome']], format=col.get('formato', None))

                        print('conctando no banco de dados')
                        banco = f'/workspaces/api-geral/ING/database/{database}'
                        conn = sqlite3.connect(f'{banco}')
                        print(f'banco de dados: {database}')
                        print(f'conectado!')
                        cursor = conn.cursor()

                        print('Criando tabela no banco de dados...')
                        sql_create_table = f"CREATE TABLE IF NOT EXISTS {config_estrutura['tabela']} ("
                        for col in config_colunas['colunas']:
                            sql_create_table += f"{col['nome']} {col['tipo']}, "
                        sql_create_table = sql_create_table[:-2] + ")"
                        cursor.execute(sql_create_table)

                        print('Inserindo dados na tabela...')
                        for index, row in dados.iterrows():
                            mapped_values = []
                            for col in config_colunas['colunas']:
                                mapped_values.append(row.get(col['nome'], None))
                            print("Valores mapeados:", mapped_values)
                            sql = f"INSERT INTO {config_estrutura['tabela']} ({', '.join([col['nome'] for col in config_colunas['colunas']])}) VALUES ({', '.join(['?' for _ in mapped_values])})"
                            print("SQL:", sql)
                            cursor.execute(sql, mapped_values)

                        print('Commit e fechamento da conexão...')
                        conn.commit()
                        conn.close()

                        print("Ingestão de dados concluída com sucesso!")
                    else:
                        print('dados ignorado!')
except FileExistsError as error:
    print(error)