import requests
import pandas as pd
import time



url = 'https://viacep.com.br/ws/RS/Porto Alegre/Domingos/json/'
response = requests.get(url)

if response.status_code == 200:
    print ('OK!')
else:
    print ('Boo!')
print('realizando response!')


dados = response.json()
print('transformando no formato json')

for resultado in dados:
    print(resultado)