import pandas as pd
import numpy as np
from datetime import datetime
import time
import itertools
import re
import os
import shutil



#função para mensagem
def mensagem(msg):
    print('-' *25)
    print(msg)
    print('-' *25)
    

print('Carregando as variaveis...')
path = '/workspaces/api-geral/MGS/dados/'
cp_path = '/workspaces/api-geral/MGS/bckp/'
name = 'MEGA SENA.txt'

time.sleep(3)
print('Listando o diretório')
print('Iterar sobre a variavel')
list_path = os.listdir(path)

for file_name in list_path:
    if name in file_name:
        src_file = os.path.join(path, file_name)
        dest_file = os.path.join(cp_path, file_name)
        shutil.copyfile(src_file, dest_file)
        print(f'Arquivo {file_name}, copiado para: {cp_path}')
print('Código concluido.')


mensagem(f'Arquivo copiado {name}')

'''
ETL para tratamento da base 'Mega'
'''
print('Iniciando o ETL')


time.sleep(3)
print('Carregando os dados')
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
timestamp_original = timestamp

''''
Dessa forma, o timestamp_original mantém o valor original do timestamp 
gerado no início do código, enquanto timestamp_arquivo armazena a data 
de modificação do arquivo, evitando assim a substituição acidental do 
valor original do timestamp que você deseja usar no nome do arquivo.
'''

print('Procurando arquivo no diretório pela palavra chave')
time.sleep(3)

diretorio = '/workspaces/api-geral/MGS/bckp/'
palavra_chave = 'MEGA'  

ultimo_timestamp = None
caminho_arquivo = None

print('Iniciando a iteração dos dados!')
time.sleep(3)
for root, dirs, files in os.walk(diretorio):
    for nome_arquivo in files:
        if palavra_chave in nome_arquivo:
            caminho_completo = os.path.join(root, nome_arquivo)
            timestamp = os.path.getmtime(caminho_completo)
            if ultimo_timestamp is None or timestamp > ultimo_timestamp:
                ultimo_timestamp = timestamp
                caminho_arquivo = caminho_completo

if caminho_arquivo:
    df = pd.read_csv(caminho_arquivo, sep=';')
    df_limp = df[df['Rateio 6 acertos'] != 'R$0,00']
    paths = "/workspaces/api-geral/MGS/dados/"
    ffilter = 'jogos_mega_filter_' + str(timestamp_original) + '.txt'
    
    df_save = df_limp.to_csv(f'{paths}{ffilter}', sep=';')
    print(f'Arquivo salvo {ffilter}')
    

else:
    print(f'Nenhum arquivo correspondente à palavra-chave "{palavra_chave}" foi encontrado no diretório {diretorio}.')

time.sleep(3)

print('Primeira parte do filtro carregado com sucesso!')
print('Iniciando o próxio passo.')
'''
Primeira parte - pegando o arquivo ajustado
'''

time.sleep(3)
print('Carregando variaveis')
'''
Filtrar numeros que foram extraidos no excel
'''

mensagem('Arquivo filtrado')

timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
timestamp_original = timestamp
''''
Dessa forma, o timestamp_original mantém o valor original do timestamp 
gerado no início do código, enquanto timestamp_arquivo armazena a data 
de modificação do arquivo, evitando assim a substituição acidental do 
valor original do timestamp que você deseja usar no nome do arquivo.
'''

diretorio = "/workspaces/api-geral/MGS/dados/"
palavra_chave = 'filter'  

ultimo_timestamp = None
caminho_arquivo = None

print('Iniciando a iteração dos dados!')
time.sleep(3)
for root, dirs, files in os.walk(diretorio):
    for nome_arquivo in files:
        if palavra_chave in nome_arquivo:
            caminho_completo = os.path.join(root, nome_arquivo)
            timestamp = os.path.getmtime(caminho_completo)
            if ultimo_timestamp is None or timestamp > ultimo_timestamp:
                ultimo_timestamp = timestamp
                caminho_arquivo = caminho_completo

if caminho_arquivo:
    df = pd.read_csv(caminho_arquivo, sep=';')


else:
    print(f'Nenhum arquivo correspondente à palavra-chave "{palavra_chave}" foi encontrado no diretório {diretorio}.')

time.sleep(3)
print('Carregando dados da mega')
print('DataFrame carregado!')


time.sleep(3)
print('Limpando DataFrame')
print('Removendo colunas...')
print('Filtrando apenas o numeros sorteados!')
df_clean = df.drop(['Concurso', 'Data do Sorteio', 'Ganhadores 6 acertos', 'Cidade / UF', 'Rateio 6 acertos','Ganhadores 5 acertos','Rateio 5 acertos','Ganhadores 4 acertos','Rateio 4 acertos','Acumulado 6 acertos','Arrecadação Total','Estimativa prêmio','Acumulado Sorteio Especial Mega da Virada','Observação'], axis= 1)
print('Filtro concluido.')

time.sleep(3)
print('Carregando variaveis para salvar o arquivo...')
data_save = "/workspaces/api-geral/MGS/bckp/"
file_save = 'numeros_completos_' + str(timestamp_original) + '.txt'

time.sleep(3)
print('Salvando o DataFrame...')
df_save = df_clean.to_csv(f'{data_save}{file_save}', header=False, index=False, sep=';')
print(f'Arquivo salvo: {file_save}')

time.sleep(3)
print('Finalizado o tratamento, iniciando o próxio passo.')



mensagem('Inic 5 prt código')


time.sleep(3)
print('Carregando as variáveis...')
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
timestamp_original = timestamp

diretorio = "/workspaces/api-geral/MGS/bckp/"
palavra_chave = 'completos'


ultimo_timestamp = None
caminho_arquivo = None

print('Iniciando a iteração dos dados!')
time.sleep(3)
for root, dirs, files in os.walk(diretorio):
    for nome_arquivo in files:
        if palavra_chave in nome_arquivo:
            caminho_completo = os.path.join(root, nome_arquivo)
            timestamp = os.path.getmtime(caminho_completo)
            if ultimo_timestamp is None or timestamp > ultimo_timestamp:
                ultimo_timestamp = timestamp
                caminho_arquivo = caminho_completo

if caminho_arquivo:
    df = pd.read_csv(caminho_arquivo, delimiter=';', header=None)


else:
    print(f'Nenhum arquivo correspondente à palavra-chave "{palavra_chave}" foi encontrado no diretório {diretorio}.')


df = df.apply(pd.to_numeric, errors='coerce') # Converte todos os valores do DataFrame para números, tratando possíveis erros como NaN (Not a Number)

time.sleep(3)
print('df carregado.')
print('Utilizando lib numpy')
# Cria uma lista 'valores_filtrados' que contém os valores entre 1 e 60 presentes no DataFrame
# Converte a lista 'valores_filtrados' em um array NumPy
# Encontra os valores mais frequentes no array e suas contagens
valores_filtrados = [valor for valor in df.values.flatten() if 1 <= valor <= 60]
valores_array = np.array(valores_filtrados)
valores_mais_frequentes, contagens = np.unique(valores_array, return_counts=True)

time.sleep(3)
print('Valores filtrados...')
print('Numeros mais frequentes encontrados')
# Obtém os índices dos valores mais frequentes em ordem decrescente
# Seleciona os valores mais frequentes com base nos índices encontrados
indices_mais_frequentes = np.argsort(-contagens)[:24]
valores_mais_frequentes = valores_mais_frequentes[indices_mais_frequentes]

time.sleep(3)
print('Ordenando numeros em ordem descrecente')
nome = f'valores_mFrequentes_{timestamp_original}.txt'

local = "/workspaces/api-geral/MGS/dados/"
valores_mais_frequentes_str = np.array2string(valores_mais_frequentes)
print(f'Caminho do arquivo: {local}{nome}')

time.sleep(3)
print('Salvando arquivo...')

if not os.path.exists(local):
    os.makedirs(local)

with open(f"{local}{nome}", "w") as novo_arq:
    novo_arq.write(valores_mais_frequentes_str)
    print(f'Arquivo salvo: {local}, com o nome: {nome}')
print('Codigo carregado com sucesso!')
print('Próxixo código a executar:')
print(f'Arquivo : {nome}')