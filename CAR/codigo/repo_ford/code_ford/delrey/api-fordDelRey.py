import requests
import pandas as pd
import time


file = '/workspaces/api-geral/CAR/repo_ford/ford/modelo_ford.txt'
df = pd.read_csv(file, delimiter=";")

df_filtrado = df[df['modelo'].str.contains('Del')]

# Pegando os valores únicos da coluna que está sendo filtrada
valores_filtrados = df_filtrado['codigo'].unique()

url_base = 'https://parallelum.com.br/fipe/api/v1/carros/marcas/22/modelos/'

lista_ano_valor = []

for valor_filtrado in valores_filtrados:
    url_ano = f'{url_base}{valor_filtrado}/anos'
    response = requests.get(url_ano)
    dados = response.json()
    time.sleep(3)

    for resultado in dados:
        ano = resultado['codigo']
        url_vlr = f'{url_base}{valor_filtrado}/anos/{ano}'
        response = requests.get(url_vlr)
        ano_valor = response.json()
        print(f"Ano: {ano}, Valor: {ano_valor}")
        
        if response.status_code == 200:
            tipo = ano_valor['TipoVeiculo']
            vlr = ano_valor['Valor']
            marc = ano_valor['Marca']
            mod = ano_valor['Modelo']
            anMod = ano_valor['AnoModelo']
            comb = ano_valor['Combustivel']
            codf = ano_valor['CodigoFipe']
            mRef = ano_valor['MesReferencia']
            sglaComb = ano_valor['SiglaCombustivel']
            
            lista_ano_valor.append({
                'tipo_veiculo': tipo,
                'valor':vlr,
                'marca':marc,
                'modelo':mod,
                'anoModelo':anMod,
                'combustivel':comb,
                'codigoFipe':codf,
                'mes_referencia':mRef,
                'sigla_combustivel':sglaComb,
                'Ano': ano
            })
        time.sleep(3)

print('Criando um dataframe')
df = pd.DataFrame(lista_ano_valor)
print(df)

print('Preparando para salvar df')
file = f'modelo_info_delrey.txt'
path = '/workspaces/api-geral/CAR/repo_ford/ford/ka/'

time.sleep(3)
df.to_csv(f'{path}{file}', sep=';', index=False)
print(f'Arquivo salvo: {file}')
print(f'Caminho: {path}')

