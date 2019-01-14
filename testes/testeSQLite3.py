import sqlite3

conexao = sqlite3.connect('database.db')
query = conexao.cursor()

def criarTabela():
	query.execute('CREATE TABLE IF NOT EXISTS ingressos (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL, \
					status TEXT NOT NULL, cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP);')

try:
	criarTabela()
except:
	print('Não foi possível criar o banco de dados\nVerifique se o mesmo já existe.')