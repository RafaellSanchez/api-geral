import requests
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq


from datetime import datetime


timestamp = datetime.now().strftime('%Y-%m-%d')

# url_api = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/29/municipios'
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
            'dtigtao': timestamp
            
        })



df = pd.DataFrame(dados_list)
print(df)


# df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
# table = pa.Table.from_pandas(df, preserve_index=True)
# pq.write_table(table, 'output.parquet')


# file = f'dados_geo_{sigla_uf}.txt'
# path = '/workspaces/api-geral/GEO/dados/'

# df.to_csv(f'{path}{file}', sep=';')
# print(f'Arquivo salvo: {file}')
# print(f'Caminho: {path}')























# import requests
# import pandas as pd
# from datetime import datetime


# timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# url = 'https://servicodados.ibge.gov.br/api/v1/localidades/distritos?orderBy=nome'

# response = requests.get(url)

# resul = response.json()

# data_list = []

# if resul:
#     for resultado in resul:
#         id = resultado['id']
#         municipio = resultado['municipio']['nome']
#         estado = resultado['municipio']['microrregiao']['mesorregiao']['UF']['nome']
#         regiao = resultado['municipio']['microrregiao']['mesorregiao']['UF']['regiao']['nome']
#         uf = resultado['municipio']['microrregiao']['mesorregiao']['UF']['sigla']
        
        
#         data_list.append(
#             {
#                 'id': id,
#                 'municipio' : municipio,
#                 'estado': estado,
#                 'regiao': regiao,
#                 'uf': uf,
#                 'data': timestamp
#             }
#         )
        
#         # print(f"id: {id}")
#         # print(f"municipio: {municipio}")
#         # print(f"estado:  {estado}")
#         # print(f"regiao: {regiao}")
#         # print(f"uf: {uf}")
        
# df = pd.DataFrame(data_list)