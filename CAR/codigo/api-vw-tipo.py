import requests
import pandas as pd

url = 'https://parallelum.com.br/fipe/api/v1/carros/marcas/59/modelos/5940/anos/2014-3'
response = requests.get(url)

dados_list = []
if response.status_code == 200:
    dados = response.json()
    tipo_veiculo = dados['TipoVeiculo']
    valor = dados['Valor']
    marca = dados['Marca']
    modelo = dados['Modelo']
    ano_modelo = dados['AnoModelo']
    combustivel = dados['Combustivel']
    codigo_fipe = dados['CodigoFipe']
    mes_referencia = dados['MesReferencia']
    sigla_combustivel = dados['SiglaCombustivel']
    
    dados_list.append({
        'tipo_veiculo': tipo_veiculo,
        'valor':valor,
        'marca':marca,
        'modelo':modelo,
        'anoModelo':ano_modelo,
        'combustivel':combustivel,
        'codigoFipe':codigo_fipe,
        'mes_referencia':mes_referencia,
        'sigla_combustivel':sigla_combustivel
        
    })
    
    
    print("Tipo de Veículo:", tipo_veiculo)
    print("Valor:", valor)
    print("Marca:", marca)
    print("Modelo:", modelo)
    print("Ano do Modelo:", ano_modelo)
    print("Combustível:", combustivel)
    print("Código FIPE:", codigo_fipe)
    print("Mês de Referência:", mes_referencia)
    print("Sigla do Combustível:", sigla_combustivel)
else:
    print("Falha ao recuperar os dados:", response.status_code)
    

df = pd.DataFrame(dados_list)
print(df)

file = 'modelo_vw_tipoVeiculo.txt'
path = '/workspaces/api-geral/CAR/dados/'

df.to_csv(f'{path}{file}', sep=';', index=False)
print(f'Arquivo salvo: {file}')
print(f'Caminho: {path}')