from faker import Faker
import pandas as pd
import datetime
import random

fake = Faker('pt_BR')

dados_list = []

while len(dados_list) < 30:  # Garante que serão gerados 10 dados brasileiros
    nome = fake.name()
    pais = fake.country()
    
    # Verifica se o país gerado é o Brasil
    if pais == 'Brasil':
        date = fake.date_between_dates(
            date_start=datetime.date(2020, 1, 1), 
            date_end=datetime.date(2024, 2, 20)
        )
        
        # Gerar um valor de dinheiro em real brasileiro e remover o código da moeda
        dinheiro = "{:.2f}".format(fake.random_number(digits=4, fix_len=True) + 100)
        
        cpf = fake.cpf()
        empresa = fake.company()
        city = fake.city()
        estado = fake.state()
        endereco = fake.address()
        email = fake.email()
        numero_telefone = fake.phone_number()
        
        dados_list.append({
            'nome': nome,
            'cpf': cpf,
            'email': email,
            'telefone': numero_telefone,
            'pagamento': dinheiro,
            'cidade': city,
            'estado': estado,
            'endereco': endereco,
            'empresa': empresa,
            'pais': pais,
            'data': date
        })

df = pd.DataFrame(dados_list)

file = f'dados_fake.txt'
path = '/workspaces/api-geral/PRJ/dados/'

df.to_csv(f'{path}{file}', sep=';', index=False)
print(f'Arquivo salvo: {file}')
print(f'Caminho: {path}')