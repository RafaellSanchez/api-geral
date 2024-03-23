from pyspark.sql import SparkSession
import requests

# Inicializa uma sessão do Spark
spark = SparkSession.builder \
    .appName("Exemplo") \
    .getOrCreate()

url = 'https://parallelum.com.br/fipe/api/v1/carros/marcas/22/modelos'
response = requests.get(url)
dados = response.json()

data_list = []

if dados:
    modelos = dados['modelos']
    for modelo in modelos:
        codigo = modelo['codigo']
        nome = modelo['nome']
        
        data_list.append({
            'codigo': codigo,
            'modelo': nome
        })

# Cria o DataFrame do Spark
df = spark.createDataFrame(data_list)

file = 'modelos_ford.csv'
path = '/workspaces/api-geral/CAR/repo_ford/ford/'

# Salva o DataFrame como um arquivo CSV
df.write.csv(f'{path}{file}', header=True, mode='overwrite')
print(f'Arquivo salvo: {file}')
print(f'Caminho: {path}')
