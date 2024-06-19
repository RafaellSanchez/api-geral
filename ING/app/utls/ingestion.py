import os
import json

from datetime import datetime
import sqlite3
import pandas as pd


timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
ultimo_timestamp = None

backup_dir = "/workspaces/api-geral/ING/app/src/data/tmp/arquivoteste.txt"
landing = '/workspaces/api-geral/ING/app/src/data/landing/'
layouts = '/workspaces/api-geral/ING/app/src/layouts/'


read_landing = os.listdir(landing)
print("Conteúdos do diretório 'landing':", read_landing)
read_layouts = os.listdir(layouts)
print("Conteúdos do diretório 'layouts':", read_layouts)
print('=====================')

try:
    for item in read_layouts:
        accept = os.path.join(layouts, item)
        if os.path.isdir(accept):
            print(f'{item} é uma pasta')
            subconteudos = os.listdir(accept)
            print(f'Conteúdos de {item}: {subconteudos}')
            
            caminho_estrutura_json = os.path.join(accept, 'estrutura.json')
            if os.path.exists(caminho_estrutura_json):
                print(f'Encontrado estrutura.json em {item}')
                
                caminho_tabela_json = os.path.join(accept, f'tabela_{item}.json')
                print(f'Encontrando estrtura json em {caminho_tabela_json}')
                
                with open(f'{caminho_tabela_json}', 'r') as f:
                    config_colunas = json.load(f)
                    print('lendo estrutura de coluna json')
                
                with open(caminho_estrutura_json, 'r') as f:
                    config_estrutura = json.load(f)
                    print("Configuração estrutura:", config_estrutura)
                    key = config_estrutura.get('nomeArquivoChave')
                    database = config_estrutura.get('banco')
                    print(f'Palavra chave: {key}')
                    print('=====================')
                
                with open(backup_dir, 'r+') as dados:
                    conteudo_load = dados.readlines()
                    print(f'Conteúdo do arquivo de backup: {conteudo_load}')
                    
                    for root, dirs, lista in os.walk(landing):
                        print(f'Procurando em {root}...')
                        for nome_arquivo in lista:
                            print(f'Verificando arquivo: {nome_arquivo}')
                            if key in nome_arquivo:
                                caminho_completo = os.path.join(root, nome_arquivo)
                                print(f'Arquivo contendo a chave encontrado: {caminho_completo}')
                                sav = os.path.basename(caminho_completo)
                                print(f'Conteúdo a gravar: {sav}')
                                    
                                if sav + '\n' not in conteudo_load:
                                    dados.write(f"{sav}\n")
                                    print(f'Dado salvo: {sav}')
                                    dados.flush()
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
