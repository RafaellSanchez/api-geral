import sqlite3

#create table gold

print('iniciando conexao com o banco de dados!')
banco_de_dados = '/workspaces/api-geral/BNK/sql/bank.db'
# Conectar ao banco de dados SQLite
print('conectando ao banco de dados!')
conn = sqlite3.connect(banco_de_dados)

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()