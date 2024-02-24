import sqlite3
import datetime
import pandas as pd


caminho_banco_dados = '/workspaces/api-geral/PRJ/bd_prj.db'

try:
    # Conectar ao banco de dados SQLite (ou criar um novo se não existir)
    conn = sqlite3.connect(caminho_banco_dados)

    file = '/workspaces/api-geral/PRJ/dados/dados_fake.txt'
    df = pd.read_csv(file, sep=';')

    df.to_sql('brnz_fake', conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()
    print('Dados Carregados na tabela')
except FileExistsError as e:
    print(f'erro : {e}')
except:
    print('Erro na criação da tabela')