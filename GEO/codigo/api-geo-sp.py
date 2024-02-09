import requests
import pandas as pd
from datetime import datetime


timestamp = datetime.now().strftime('%Y-%m-%d')

url_api = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/35/municipios'

response = requests.get(url_api)

dados = response.json()

dados_list = []

# for result in dados:
#     print(result)



if dados:
    for resultado in dados:
        id = resultado['id']
        nome = resultado['nome']
        id_mun = resultado['microrregiao']['id']
        nm_mun = resultado['microrregiao']['nome']
        id_mcr = resultado['microrregiao']['mesorregiao']['id']
        nm_mcr = resultado['microrregiao']['mesorregiao']['nome']
        id_uf = resultado['microrregiao']['mesorregiao']['UF']['id']
        nm_uf = resultado['microrregiao']['mesorregiao']['UF']['nome']
        sigla_uf = resultado['microrregiao']['mesorregiao']['UF']['sigla']
        id_reg = resultado['microrregiao']['mesorregiao']['UF']['regiao']['id']
        nm_reg = resultado['microrregiao']['mesorregiao']['UF']['regiao']['nome']
        sigla_rg = resultado['microrregiao']['mesorregiao']['UF']['regiao']['sigla']
        rgimd_id = resultado['regiao-imediata']['id']
        rgimd_nm = resultado['regiao-imediata']['nome']
        rgint_id = resultado['regiao-imediata']['regiao-intermediaria']['id']
        rgint_nm = resultado['regiao-imediata']['regiao-intermediaria']['nome']
        rguf_id = resultado['regiao-imediata']['regiao-intermediaria']['UF']['id']
        rguf_sgl = resultado['regiao-imediata']['regiao-intermediaria']['UF']['sigla']
        rguf_nm = resultado['regiao-imediata']['regiao-intermediaria']['UF']['nome']
        rgrg_id = resultado['regiao-imediata']['regiao-intermediaria']['UF']['regiao']['id']
        rgrg_sgl = resultado['regiao-imediata']['regiao-intermediaria']['UF']['regiao']['sigla']
        rgrg_nm = resultado['regiao-imediata']['regiao-intermediaria']['UF']['regiao']['nome']
        
        
        dados_list.append({
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
            'rgimd_id': rgimd_id,
            'rgimd_nm': rgimd_nm,
            'rgint_id': rgint_id,
            'rgint_nm': rgint_nm,
            'rguf_id': rguf_id,
            'rguf_sgl': rguf_sgl,
            'rguf_nm': rguf_nm,
            'rgrg_id': rgrg_id,
            'rgrg_sgl': rgrg_sgl,
            'rgrg_nm': rgrg_nm,
            'dtigtao': timestamp
            
        })


df = pd.DataFrame(dados_list)
# print(df)


file = f'dados_geo_sp.txt'
path = '/workspaces/api-geral/GEO/dados/'

df.to_csv(f'{path}{file}', sep=';')
print(f'Arquivo salvo: {file}')
print(f'Caminho: {path}')