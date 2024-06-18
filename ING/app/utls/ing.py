import json
import pandas as pd
import sqlite3
import os
from datetime import datetime
import os.path
import time

list_dir = "/workspaces/api-geral/ING/app/src/data/landing/"
arq_dir = "/workspaces/api-geral/ING/app/src/data/tmp/arquivoteste.txt"
landing = '/workspaces/api-geral/ING/app/src/data/landing/'
file_tb_json = '/workspaces/api-geral/ING/app/src/layouts/teste/estrutura.json'
word_key = 'resultado'

listando_landing = os.listdir(list_dir)
print(listando_landing)

arquivo_list = []

for lista in listando_landing:
    sav = os.path.basename(lista)

    load = open(f"{arq_dir}", "a")
    save = list()
    save.append(sav)
    load.writelines(f"{save} \n")
    print('arquivo adicionado na lista')
    
for files in os.walk(landing):
    for nome_arquivo in files:
        if word_key in nome_arquivo:
            print(nome_arquivo)
            

with open(f'{file_tb_json}', 'r') as f:
    config_colunas = json.load(f)
    print('lendo estrutura de coluna json')
    print(config_colunas)
    key = config_colunas['nomeArquivoChave']
    print(f"palavra chave: {key}")

# word_key = 'teste'
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

ultimo_timestamp = None
caminho_arquivo = None

for root, dirs, files in os.walk(landing):
    for nome_arquivo in files:
        if key in nome_arquivo:
            caminho_completo = os.path.join(root, nome_arquivo)
            timestamp = os.path.getmtime(caminho_completo)
            if ultimo_timestamp is None or timestamp > ultimo_timestamp:
                ultimo_timestamp = timestamp
                caminho_arquivo = caminho_completo
                print(caminho_arquivo)