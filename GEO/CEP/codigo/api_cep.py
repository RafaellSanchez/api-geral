import requests
import pandas as pd
import time

#função para mensagem
def mensagem(msg):
    print('-' *25)
    print(msg)
    print('-' *25)

time.sleep(3)
mensagem('Iniciando aplicação!')
#Lista de logradouros
listas = ['Estrada','Estrada Armando','Mairipora','Rua','Estrada Rio Acima','Rio Abaixo','Avenida','Rodovia']

# url = 'https://viacep.com.br/ws/RS/Porto Alegre/Domingos+Jose/json/'
#realizar a iteração da listas de logradouros com a url da api
print('Realizando iteração!')
time.sleep(3)
for lista in listas:
    url = f'https://viacep.com.br/ws/SP/Mairipora/{lista}/json/'
    response = requests.get(url)
    
    print('Verificando status da requisição!')
    time.sleep(3)
    if response.status_code == 200:
        print ('requisição: OK!')
    else:
        print ('Erro!')
    
    dados = response.json()
    print('transformando no formato json')
    
    dados_lista = []
    print('iteração na api')
    #para cada nome na lista, será realizado uma iteração na api
    for resultado in dados:
        cep = resultado['cep']
        logradouro = resultado['logradouro']
        bairro = resultado['bairro']
        localidade = resultado['localidade']
        uf = resultado['uf']
        ibge = resultado['ibge']
        gia = resultado['gia']
        ddd = resultado['ddd']
        siafi = resultado['siafi']
        
        time.sleep(3)
        print('realizando append em uma lista')
        dados_lista.append({
            
            'cep': cep,
            'logradouro': logradouro,
            'bairro': bairro,
            'localidade': localidade,
            'uf': uf,
            'ibge': ibge,
            'gia': gia,
            'ddd': ddd,
            'siafi': siafi
            
            })
        
        time.sleep(3)
        print('transformando em um dataframe')
        #salvar cada iteração em uma dataframe e depois salva-lo em um arquivo txt delimitado 
        df = pd.DataFrame(dados_lista)
        
        mensagem(f'Preparando para salvar: {lista}')
        caminho = '/workspaces/api-geral/GEO/CEP/dados/'
        arquivo = f'dados_sp_mairipora_{lista}.txt'
        time.sleep(3)
        df.to_csv(f'{caminho}{arquivo}', sep=';', index=False)
        print(f'Arquivo salvo: {arquivo}')
        print(f'Caminho: {caminho}')

mensagem('Codigo finalziado!')