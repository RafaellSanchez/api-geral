import requests
import pandas as pd
import time


file = '/workspaces/api-geral/CAR/repo_ford/ford/modelo_ford.txt'
df = pd.read_csv(file, delimiter=";")

# Filtro para encontrar linhas onde a coluna "nome_da_coluna" contenha a palavra "Ka"
df_filtrado = df[df['modelo'].str.contains('Ka')]

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
file = f'modelo_info_ka.txt'
path = '/workspaces/api-geral/CAR/repo_ford/ford/ka/'

time.sleep(3)
df.to_csv(f'{path}{file}', sep=';', index=False)
print(f'Arquivo salvo: {file}')
print(f'Caminho: {path}')










########################################################################################################
##                 versão anterior                                                                    ##
########################################################################################################

# # Corrigindo a definição da lista
# lista = [
#     4514,
#     8744,
#     8149,
#     6915,
#     6914,
#     8122,
#     4789,
#     813,
#     8745,
#     8401,
#     8402,
#     8440,
#     8441,
#     8442,
#     8443,
#     6916,
#     8444,
#     8445,
#     8446,
#     8447
# ]

# url_base = 'https://parallelum.com.br/fipe/api/v1/carros/marcas/22/modelos/'

# lista_ano_valor = []

# for modelo_codigo in lista:
#     url_ano = f'{url_base}{modelo_codigo}/anos'
#     response = requests.get(url_ano)
#     dados = response.json()
#     time.sleep(3)

#     for resultado in dados:
#         ano = resultado['codigo']
#         url_vlr = f'{url_base}{modelo_codigo}/anos/{ano}'
#         response = requests.get(url_vlr)
#         ano_valor = response.json()
#         print(f"Ano: {ano}, Valor: {ano_valor}")
        
#         if response.status_code == 200:
#             tipo = ano_valor['TipoVeiculo']
#             vlr = ano_valor['Valor']
#             marc = ano_valor['Marca']
#             mod = ano_valor['Modelo']
#             anMod = ano_valor['AnoModelo']
#             comb = ano_valor['Combustivel']
#             codf = ano_valor['CodigoFipe']
#             mRef = ano_valor['MesReferencia']
#             sglaComb = ano_valor['SiglaCombustivel']
            
#             lista_ano_valor.append({
#                 'tipo_veiculo': tipo,
#                 'valor':vlr,
#                 'marca':marc,
#                 'modelo':mod,
#                 'anoModelo':anMod,
#                 'combustivel':comb,
#                 'codigoFipe':codf,
#                 'mes_referencia':mRef,
#                 'sigla_combustivel':sglaComb,
#                 'Ano': ano
#             })
#         time.sleep(3)

# print('Criando um dataframe')
# df = pd.DataFrame(lista_ano_valor)
# print(df)

# print('Preparando para salvar df')
# file = f'modelo_info.txt'
# path = '/workspaces/api-geral/CAR/repo_ford/ford/ka/'

# time.sleep(3)
# df.to_csv(f'{path}{file}', sep=';', index=False)
# print(f'Arquivo salvo: {file}')
# print(f'Caminho: {path}')







# import requests
# import pandas as pd
# import time


# url_ano = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/22/modelos/{lista}/anos'
# response = requests.get(url_ano)
# dados = response.json()
# time.sleep(3)


# lista_ano = []

# for resultado in dados:
#     anos = resultado['codigo']
#     lista_ano.append({
#         'ano':anos
#     })

# #Acessando apenas os valores dos dicionários na lista
# valores = [item['ano'] for item in lista_ano]

# time.sleep(3)
# lista_ano_valor = []

# #Itera sobre cada ano, fazendo solicitações individuais para obter os valores
# for ano in valores:
#     url_vlr = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/22/modelos/{lista}/anos/{ano}'
#     response = requests.get(url_vlr)
#     ano_valor = response.json()
#     print(f"Ano: {ano}, Valor: {ano_valor}")
    
#     if response.status_code == 200:
#         tipo = ano_valor['TipoVeiculo']
#         vlr = ano_valor['Valor']
#         marc = ano_valor['Marca']
#         mod = ano_valor['Modelo']
#         anMod = ano_valor['AnoModelo']
#         comb = ano_valor['Combustivel']
#         codf = ano_valor['CodigoFipe']
#         mRef = ano_valor['MesReferencia']
#         sglaComb = ano_valor['SiglaCombustivel']
        

#         lista_ano_valor.append({
#             'tipo_veiculo': tipo,
#             'valor':vlr,
#             'marca':marc,
#             'modelo':mod,
#             'anoModelo':anMod,
#             'combustivel':comb,
#             'codigoFipe':codf,
#             'mes_referencia':mRef,
#             'sigla_combustivel':sglaComb,
#             'Ano': ano
#         })

# time.sleep(3)
# print('Criando um dataframe')
# df = pd.DataFrame(lista_ano_valor)
# print(df)

# print('Preparando para salvar df')
# file = f'modelo_info{mod}.txt'
# path = '/workspaces/api-geral/CAR/repo_ford/ford/ka/'

# time.sleep(3)
# df.to_csv(f'{path}{file}', sep=';', index=False)
# print(f'Arquivo salvo: {file}')
# print(f'Caminho: {path}')
