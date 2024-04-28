import requests
import pandas as pd
import time



url = 'viacep.com.br/ws/RS/Porto Alegre/Domingos/json/'

response = requests.get(url)
print('realizando response!')
dados = response.json()
print('transformando no formato json')

for resultado in dados:
    print(resultado)