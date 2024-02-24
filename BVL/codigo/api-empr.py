import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Lista das principais empresas (exemplo)
empresas = ['ABEV3.SA', 'PETR4.SA', 'ITUB4.SA', 'BBDC4.SA', 'VALE3.SA']

# Calcular a data de início como "15 dias atrás"
quinze_dias_atras = datetime.now() - timedelta(days=15)
data_inicial = quinze_dias_atras.strftime('%Y-%m-%d')

# Loop para obter os dados de cada empresa e salvar em arquivos de texto separados
for empresa in empresas:
    dados_empresa = yf.download(empresa, start=data_inicial)

    # Ajustar a formatação dos valores para 0000.00
    dados_empresa = dados_empresa.applymap('{:,.2f}'.format)

    # Obter o timestamp no formato "yyyyMMdd_HHmmss"
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    df = pd.DataFrame(dados_empresa)
    df = df.assign(dt_igtao=timestamp)
    
    dados_empresa = df

    # Salvar os dados da empresa em um arquivo de texto (txt)
    nome_arquivo = f"Dados_{empresa}_{timestamp}.txt"
    caminho_arquivo = '/workspaces/api-geral/BVL/dados/'
    
    try:
        dados_empresa.to_csv(f'{caminho_arquivo}{nome_arquivo}', sep='\t')
        print(f'Arquivo salvo com sucesso no caminho: {caminho_arquivo}')
    
    except FileExistsError as error:
        print('Arquivo não encontrado.', str(error))

    print(f"Dados da empresa {empresa} salvos com sucesso no arquivo '{nome_arquivo}'!")