import pandas as pd
import numpy as np
from datetime import datetime
import time
import itertools
import re
import os
import shutil


'''
 Iniciar esse código para gerar os numeros para o jogo da mega.
'''

time.sleep(3)
def calcular_maior_numero_jogos(numeros_disponiveis, tamanho_jogo, quantidade_jogos):
    combinacoes = list(itertools.combinations(numeros_disponiveis, tamanho_jogo))
    
    jogos = []

    for combinacao in combinacoes:
        if len(jogos) >= quantidade_jogos:
            break
        if all(set(combinacao).isdisjoint(jogo) for jogo in jogos):
            jogos.append(combinacao)
    
    return jogos
print('Função carregada!')
time.sleep(3)



timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
diretorio = '/workspaces/api-geral/MGS/dados/'
palavra_chave = 'mFrequentes'  
ultimo_timestamp = None
caminho_arquivo = None

for root, dirs, files in os.walk(diretorio):
    for nome_arquivo in files:
        if palavra_chave in nome_arquivo:
            caminho_completo = os.path.join(root, nome_arquivo)
            timestamp = os.path.getmtime(caminho_completo)
            if ultimo_timestamp is None or timestamp > ultimo_timestamp:
                ultimo_timestamp = timestamp
                caminho_arquivo = caminho_completo

if caminho_arquivo:
    with open(caminho_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()

else:
    print(f'Nenhum arquivo correspondente à palavra-chave "{palavra_chave}" foi encontrado no diretório {diretorio}.')



print('Lendo o arquivo...') 
time.sleep(3)   
numeros_disponiveis = re.findall(r'\d+', conteudo)
numeros_disponiveis = [int(numero) for numero in numeros_disponiveis]
tamanho_jogo = 6
quantidade_jogos = 4
print('Passando os parametros...')
time.sleep(3)
jogos = calcular_maior_numero_jogos(numeros_disponiveis, tamanho_jogo, quantidade_jogos)

print('Passando as variavéis...')
time.sleep(3)
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
nome_arquivo = f'jogos_{timestamp}.txt'

diretorio_saida = '/workspaces/api-geral/MGS/dados/'
caminho_arquivo = diretorio_saida + nome_arquivo

print(f'Salvando o arquivo no caminho {diretorio_saida}')
time.sleep(3)
with open(caminho_arquivo, 'w') as arquivo_saida:
    for i, jogo in enumerate(jogos, start=1):
        arquivo_saida.write(f'Jogo {i}: {jogo}\n')

print(f'Arquivo "{nome_arquivo}" criado com osucesso!.')