import requests
import pandas as pd
from datetime import datetime
import json
from cryptography.fernet import Fernet
import time
import sqlite3
import uuid

timestamp = datetime.now().strftime('%Y-%m-%d')

url_api = 'https://servicodados.ibge.gov.br/api/v1/localidades/distritos?orderBy=nome'
response = requests.get(url_api)
dados = response.json()
dados_list = []

if dados:
    for resultado in dados:
        id = resultado['id']
        nome = resultado['nome']
        id_mun = resultado['municipio']['id']
        nm_mun = resultado['municipio']['nome']
        id_mcr = resultado['municipio']['microrregiao']['mesorregiao']['id']
        nm_mcr = resultado['municipio']['microrregiao']['mesorregiao']['nome']
        id_uf = resultado['municipio']['microrregiao']['mesorregiao']['UF']['id']
        nm_uf = resultado['municipio']['microrregiao']['mesorregiao']['UF']['nome']
        sigla_uf = resultado['municipio']['microrregiao']['mesorregiao']['UF']['sigla']
        id_reg = resultado['municipio']['microrregiao']['mesorregiao']['UF']['regiao']['id']
        nm_reg = resultado['municipio']['microrregiao']['mesorregiao']['UF']['regiao']['nome']
        sigla_rg = resultado['municipio']['microrregiao']['mesorregiao']['UF']['regiao']['sigla']
        uuid_value = uuid.uuid4().hex
        
        dados_list.append({
            'uuid': uuid_value,
            'id': id,
            'nome': nome,
            'id_mun': id_mun,
            'nm_mun': nm_mun,
            'id_mcr': id_mcr,
            'nm_mcr': nm_mcr,
            'id_uf': id_uf,
            'nm_uf': nm_uf,
            'sigla_uf': sigla_uf,
            'id_reg': id_reg,
            'nm_reg': nm_reg,
            'sigla_rg': sigla_rg,
            'dtigtao': timestamp
            
        })

df = pd.DataFrame(dados_list)

# Gerar uma chave de criptografia
key = Fernet.generate_key()
cipher_suite = Fernet(key)

json_string = df.to_json()

encrypted_data = cipher_suite.encrypt(json_string.encode())

arquivocript = '/workspaces/api-geral/GEO/dados/dados_cript.bin'
with open(arquivocript, "wb") as file:
    file.write(encrypted_data)
    print('Arquivo criptografado salvo!')
    print(f'Caminho: {arquivocript}')

time.sleep(4)
print('Carregando dados criptografados!')
print('................................')

with open(arquivocript, "rb") as file:
    encrypted_data = file.read()

decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
time.sleep(4)
print('Carregando...')
print('Arquivo descriptografado!')

df_descriptografado = pd.read_json(decrypted_data)
print('Preparando dados para ingestão no banco de dados!')
time.sleep(3)
print('Carregando...')
print('Criando bd')
conn = sqlite3.connect('/workspaces/api-geral/GEO/sql/bd_geo.db')
time.sleep(3)
print('Criando tabela')
df_descriptografado.to_sql('brnz_geo', conn, if_exists='replace', index=False)
conn.close()
print('Dados carregados na tabela')
