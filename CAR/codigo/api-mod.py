import requests
import pandas as pd

url = 'https://parallelum.com.br/fipe/api/v1/carros/marcas'
response = requests.get(url)

dados = response.json()

data_list = []

if dados:
    if 'marcas' in dados:
        modelos = dados['marcas']
        for modelo in modelos:
            codigo = modelo['codigo']
            nome = modelo['nome']
            # print(f"codigo: {codigo}")
            # print(f"nome: {nome}")
            
            data_list.append({
                'codigo': codigo,
                'modelo': nome
            })
    else:  
        for modelo in dados:
            codigo = modelo['codigo']
            nome = modelo['nome']
            # print(f"codigo: {codigo}")
            # print(f"nome: {nome}")
            
            data_list.append({
                'codigo': codigo,
                'modelo': nome 
            })

df = pd.DataFrame(data_list)
print(df)

file = 'modelos.txt'
path = '/workspaces/api-geral/CAR/dados/'

df.to_csv(f'{path}{file}', sep=';', index=False)
print(f'Arquivo salvo: {file}')
print(f'Caminho: {path}')
