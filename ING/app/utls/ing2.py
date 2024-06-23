import os
import json
import pandas as pd
import sqlite3
from datetime import datetime
import shutil

# Definindo variáveis
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
data_igtao = datetime.now().strftime('%Y-%m-%d')

caminho_backup = '/workspaces/api-geral/ING/app/src/bckp/'
ctrl_ing = "/workspaces/api-geral/ING/app/src/data/landing/archiving_ctrl/controle_ingestao.txt"
landing = '/workspaces/api-geral/ING/app/src/data/landing/'
layouts = '/workspaces/api-geral/ING/app/src/layouts/'

# Listando diretórios
read_landing = os.listdir(landing)
print("Conteúdos do diretório 'landing':", read_landing)
read_layouts = os.listdir(layouts)
print("Conteúdos do diretório 'layouts':", read_layouts)
print('=====================')

# Processamento principal
for item in read_layouts:
    accept = os.path.join(layouts, item)
    if os.path.isdir(accept):
        print(f'{item} é uma pasta')
        subconteudos = os.listdir(accept)
        print(f'Conteúdos de {item}: {subconteudos}')

        caminho_estrutura_json = os.path.join(accept, 'estrutura.json')
        if os.path.exists(caminho_estrutura_json):
            print(f'Encontrado estrutura.json em {item}')

            # Carregar estrutura JSON
            with open(caminho_estrutura_json, 'r') as f:
                config_estrutura = json.load(f)
                print("Configuração estrutura:", config_estrutura)

            caminho_tabela_json = os.path.join(accept, f'tabela_{item}.json')
            with open(caminho_tabela_json, 'r') as f:
                config_colunas = json.load(f)
                print('Lendo estrutura de coluna json')

            for processo in config_estrutura['processos']:
                try:
                    banco = processo.get('banco')
                    nome_tabela = processo.get('tabela')
                    nomeArquivoChave = processo.get('nomeArquivoChave')
                    print(f'Nome banco de dados: {banco}')
                    print(f'Nome chave: {nomeArquivoChave}')
                    print(f'Nome tabela: {nome_tabela}')
                    print(f'==============================')

                    with open(ctrl_ing, 'r+') as controle_ingestao:
                        conteudo_load = controle_ingestao.readlines()
                        print(f'Conteúdo do arquivo de controle de ingestão: {conteudo_load}')

                        for root, dirs, lista in os.walk(landing):
                            print(f'Procurando em {root}...')
                            for nome_arquivo in lista:
                                print(f'Verificando arquivo: {nome_arquivo}')
                                if nomeArquivoChave in nome_arquivo:
                                    caminho_completo = os.path.join(root, nome_arquivo)
                                    print(f'Arquivo contendo a chave encontrado: {caminho_completo}')
                                    sav = os.path.basename(caminho_completo)
                                    print(f'Conteúdo a gravar: {sav}')

                                    if sav + '\n' not in conteudo_load:
                                        controle_ingestao.write(f"{sav}\n")
                                        print(f'Dado salvo: {sav}')
                                        controle_ingestao.flush()
                                        print('=================================')

                                        # Carregando dados
                                        if caminho_completo.endswith('.txt'):
                                            df = pd.read_csv(caminho_completo, delimiter=';', skiprows=[0], names=[col['nome'] for col in config_colunas['colunas']])
                                        elif caminho_completo.endswith('.csv'):
                                            df = pd.read_csv(caminho_completo, skiprows=[0], names=[col['nome'] for col in config_colunas['colunas']])
                                        elif caminho_completo.endswith('.bin'):
                                            pass
                                        else:
                                            raise ValueError("Formato de arquivo não suportado")
                                        print('Convertendo tipos de dados')

                                        # Converte tipos de dados conforme configuração
                                        for col in config_colunas['colunas']:
                                            if col['tipo'] == 'int':
                                                df[col['nome']] = df[col['nome']].astype(int)
                                            elif col['tipo'] == 'float':
                                                df[col['nome']] = df[col['nome']].astype(float)
                                            elif col['tipo'] == 'data':
                                                df[col['nome']] = pd.to_datetime(df[col['nome']], format=col.get('formato', None))

                                        print('Conectando no banco de dados')
                                        banco_caminho = f'/workspaces/api-geral/ING/database/{banco}'
                                        conn = sqlite3.connect(banco_caminho)
                                        print(f'Banco de dados: {banco_caminho}')
                                        print(f'Conectado!')
                                        cursor = conn.cursor()

                                        print('Criando tabela no banco de dados...')
                                        sql_create_table = f"CREATE TABLE IF NOT EXISTS {nome_tabela} ("
                                        for col in config_colunas['colunas']:
                                            sql_create_table += f"{col['nome']} {col['tipo']}, "
                                        sql_create_table = sql_create_table[:-2] + ")"
                                        cursor.execute(sql_create_table)

                                        print('Inserindo dados na tabela...')
                                        for index, row in df.iterrows():
                                            mapped_values = []
                                            for col in config_colunas['colunas']:
                                                mapped_values.append(row.get(col['nome'], None))
                                            print("Valores mapeados:", mapped_values)
                                            sql = f"INSERT INTO {nome_tabela} ({', '.join([col['nome'] for col in config_colunas['colunas']])}) VALUES ({', '.join(['?' for _ in mapped_values])})"
                                            print("SQL:", sql)
                                            cursor.execute(sql, mapped_values)

                                        print('Commit e fechamento da conexão...')
                                        conn.commit()
                                        conn.close()
                                        print("Ingestão de dados concluída com sucesso!")

                                        print("========================================")
                                        print("Movimentando arquivos")
                                        shutil.move(caminho_completo, caminho_backup)
                                        print(f'Arquivo enviado para bckp: {caminho_completo}')
                                        print(f'Destino: {caminho_backup}')

                                    else:
                                        print(f'Dados ignorados para o arquivo: {nome_arquivo}')

                except Exception as e:
                    print(f"Erro ao processar tabela: {processo}")
                    print(e)
