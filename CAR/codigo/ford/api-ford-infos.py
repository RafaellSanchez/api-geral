import requests
import pandas as pd
import time

url_ano = 'https://parallelum.com.br/fipe/api/v1/carros/marcas/22/modelos/4514/anos'
response = requests.get(url_ano)
dados = response.json()
time.sleep(3)


lista_ano = []

for resultado in dados:
    anos = resultado['codigo']
    lista_ano.append({
        'ano':anos
    })

#Acessando apenas os valores dos dicionários na lista
valores = [item['ano'] for item in lista_ano]

time.sleep(3)
lista_ano_valor = []

#Itera sobre cada ano, fazendo solicitações individuais para obter os valores
for ano in valores:
    url_vlr = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/22/modelos/4514/anos/{ano}'
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
        
        #Adiciona os dados à lista fora do if
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
file = f'modelo_info.txt'
path = '/workspaces/api-geral/CAR/dados/ford/'

time.sleep(3)
df.to_csv(f'{path}{file}', sep=';', index=False)
print(f'Arquivo salvo: {file}')
print(f'Caminho: {path}')

























# import requests
# import pandas as pd


# url = 'https://parallelum.com.br/fipe/api/v1/carros/marcas/22/modelos/4514/anos/2013-1'
# response = requests.get(url)

# dados_list = []
# if response.status_code == 200:
#     dados = response.json()
#     tipo_veiculo = dados['TipoVeiculo']
#     valor = dados['Valor']
#     marca = dados['Marca']
#     modelo = dados['Modelo']
#     ano_modelo = dados['AnoModelo']
#     combustivel = dados['Combustivel']
#     codigo_fipe = dados['CodigoFipe']
#     mes_referencia = dados['MesReferencia']
#     sigla_combustivel = dados['SiglaCombustivel']
    
#     dados_list.append({
#         'tipo_veiculo': tipo_veiculo,
#         'valor':valor,
#         'marca':marca,
#         'modelo':modelo,
#         'anoModelo':ano_modelo,
#         'combustivel':combustivel,
#         'codigoFipe':codigo_fipe,
#         'mes_referencia':mes_referencia,
#         'sigla_combustivel':sigla_combustivel
        
#     })
    
    
#     print("Tipo de Veículo:", tipo_veiculo)
#     print("Valor:", valor)
#     print("Marca:", marca)
#     print("Modelo:", modelo)
#     print("Ano do Modelo:", ano_modelo)
#     print("Combustível:", combustivel)
#     print("Código FIPE:", codigo_fipe)
#     print("Mês de Referência:", mes_referencia)
#     print("Sigla do Combustível:", sigla_combustivel)
# # else:
# #     print("Falha ao recuperar os dados:", response.status_code)
    

# df = pd.DataFrame(dados_list)
# print(df)
