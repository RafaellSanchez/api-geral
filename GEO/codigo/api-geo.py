import requests
import pandas as pd
from datetime import datetime


timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

url = 'https://servicodados.ibge.gov.br/api/v1/localidades/distritos?orderBy=nome'

response = requests.get(url)

resul = response.json()

data_list = []

if resul:
    for resultado in resul:
        id = resultado['id']
        municipio = resultado['municipio']['nome']
        estado = resultado['municipio']['microrregiao']['mesorregiao']['UF']['nome']
        regiao = resultado['municipio']['microrregiao']['mesorregiao']['UF']['regiao']['nome']
        uf = resultado['municipio']['microrregiao']['mesorregiao']['UF']['sigla']
        
        
        data_list.append(
            {
                'id': id,
                'municipio' : municipio,
                'estado': estado,
                'regiao': regiao,
                'uf': uf,
                'data': timestamp
            }
        )
        
        # print(f"id: {id}")
        # print(f"municipio: {municipio}")
        # print(f"estado:  {estado}")
        # print(f"regiao: {regiao}")
        # print(f"uf: {uf}")
        
df = pd.DataFrame(data_list)