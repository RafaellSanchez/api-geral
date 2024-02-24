import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Calcular a data de início como "um mês atrás"
um_mes_atras = datetime.now() - timedelta(days=30)
data_inicial = um_mes_atras.strftime('%Y-%m-%d')

# Obter os dados do índice Bovespa (^BVSP) a partir de uma data específica
dados_bvsp = yf.download('^BVSP', start=data_inicial)

# Ajustar a formatação dos valores para 0000.00
dados_bvsp = dados_bvsp.applymap('{:,.2f}'.format)

# Obter o timestamp no formato "yyyyMMdd_HHmmss"
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

df = pd.DataFrame(dados_bvsp)
df = df.assign(dtigtao=timestamp)

dados_bvsp = df


# Exibir as primeiras linhas do DataFrame para visualizar as informações
print(dados_bvsp.head())

# Salvar os dados do índice Bovespa em um arquivo de texto (txt)
nome_arquivo = f"Dados_BVSP_{timestamp}.txt"
caminho_arquivo = "/workspaces/api-geral/BVL/dados/"

try:
    dados_bvsp.to_csv(f"{caminho_arquivo}{nome_arquivo}", sep=';')
except FileNotFoundError as error:
    print(f'Erro ao salvar arquivo ', str(error))

print(f"Dados do índice Bovespa salvos com sucesso no arquivo '{nome_arquivo}'!")
print(f'Arquivo salvo com sucesso no diretório {caminho_arquivo}')