import pandas as pd 
import json as js 
import requests
from datetime import datetime
import time

#Obter o timestam no formato 'yyyyMMdd_HHmmss'
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
campo_data = datetime.now().strftime('%Y-%m-%d')
#api
url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,USD-BRLT'

requisicao = requests.get(url)
dados_json = js.loads(requisicao.content)
dados = dados_json
print('carregando api de cotação....')
time.sleep(5)
print('carregando...')

dfdados = pd.DataFrame(dados)
print('transformando em um df')
time.sleep(5)
print('carregando..')


#novo nome para coluna
new_column_name = {
    'bid': 'compra',
}

#alterando o nome
dfdados.rename(columns=new_column_name, inplace=True)

#novos rótulos para os indices
new_index_labels = ['moeda','moeda_real','comparando', 'meximo', 'minimo', 'variacao', 'porcentagem_variacao', 'compra', 'venda', 'timestamp', 'create_data']
dfdados.index = new_index_labels

dfdados = dfdados.assign(dt_igtao=campo_data)
dfdados = dfdados.rename_axis('NomeIndice').reset_index()

print('Alterando o index, atualizando os nomes...')
time.sleep(3)
print('Alterado!')

caminho_arquivo = '/workspaces/api-geral/BVL/dados/'
nome_arquivo = f'cotacao_atual_{timestamp}.csv'

print('salvando...')
time.sleep(3)
try:
    dfdados.to_csv(f'{caminho_arquivo}{nome_arquivo}', sep=';', index=True)
    print('Caminho encontrado...')
    time.sleep(3)
    print(f'Salvando o arquivo no caminho {caminho_arquivo}')

except FileExistsError as error:
    print('Caminho não encontrado', str(error))

print(f'Arquivo: {nome_arquivo} salvo com sucesso!')