import requests
import pandas as pd

url = 'https://parallelum.com.br/fipe/api/v1/carros/marcas/22/modelos'
response = requests.get(url)
dados = response.json()

data_list = []

if dados:
    modelos = dados['modelos']
    for modelo in modelos:
        codigo = modelo['codigo']
        nome = modelo['nome']
        print(f"codigo: {codigo}")
        print(f"nome: {nome}")
        
        data_list.append({
            'codigo':codigo,
            'modelo':modelo
        })
df = pd.DataFrame(data_list)
print(df)

file = 'modelo_ford.txt'
path = '/workspaces/api-geral/CAR/repo_ford/ford/'

df.to_csv(f'{path}{file}', sep=';', index=False)
print(f'Arquivo salvo: {file}')
print(f'Caminho: {path}')