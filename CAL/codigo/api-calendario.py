import requests
import pandas as pd

key = 'RGoTv8Dds6IPDbfRr5zteNvJDqWKYLTM'
url_api = f'https://calendarific.com/api/v2/holidays?&api_key={key}&country=BR&year=2024'

response = requests.get(url_api)
dados = response.json()

# print(dados)

dados_list = []

if 'response' in dados and 'holidays' in dados['response']:
    feriados = dados['response']['holidays']
    
    for feriado in feriados:
        nome = feriado['name']
        descricao = feriado['description'] if 'description' in feriado else ''
        data_iso = feriado['date']['iso']
        ano = feriado['date']['datetime']['year']
        mes = feriado['date']['datetime']['month']
        dia = feriado['date']['datetime']['day']
        
        dados_list.append({
            'Nome': nome,
            'Descrição': descricao,
            'Data_ISO': data_iso,
            'Ano': ano,
            'Mês': mes,
            'Dia': dia
        })

df = pd.DataFrame(dados_list)
# print(df)


file = f'calendario_br.txt'
path = '/workspaces/api-geral/CAL/dados/'

df.to_csv(f'{path}{file}', sep=';', index=False)
print(f'Arquivo salvo: {file}')
print(f'Caminho: {path}')
