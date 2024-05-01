import pandas as pd
import os
import time
from datetime import datetime

print('iniciando codigo')
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

print('carregando variaveis')
time.sleep(3)
caminho = '/workspaces/api-geral/GEO/CEP/dados/'
palavra_chave = 'mairipora'
lista_caminho = os.listdir(caminho)

#Lista df para os DataFrames de cada arquivo
dfs = []
print('iniciando iteração')
try:
    time.sleep(3)
    print('verificando a palavra chave')
    for nome_arquivo in lista_caminho:
        if palavra_chave in nome_arquivo: #verifica a palavra chave
            src_arquivo = os.path.join(caminho, nome_arquivo)
            print("Lendo arquivo:", src_arquivo)
            
            df = pd.read_csv(src_arquivo, delimiter=';')
            dfs.append(df) #adc df a lista
            
    print('verificação para cada df')
    #se existir algum df na lista, concatenar todos os df da lista em um único df
    if dfs:
        df_final = pd.concat(dfs)
        caminho_saida = '/workspaces/api-geral/GEO/CEP/dados/'
        arquivo_fnl = f'resultado_concat_{timestamp}.txt'
        df_final.to_csv(f'{caminho_saida}{arquivo_fnl}', sep=';', index=False)
        print("Arquivo salvo em:", caminho_saida)
    else:
        print("Nenhum arquivo encontrado.")
except Exception as e:
    print(e)