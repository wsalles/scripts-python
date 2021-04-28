import sqlite3

conn = sqlite3.connect('database.db')
query = conn.cursor()


def create_table():
	query.execute('CREATE TABLE IF NOT EXISTS ingressos \
					(id INTEGER PRIMARY KEY AUTOINCREMENT, \
					titulo TEXT NOT NULL, \
					status TEXT NOT NULL, \
					cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP);')


try:
	create_table()
	print("Created table!")
except Exception as e:
	print('The database cannot be created.\nMake sure it already exists.')
	print(f"More details about the error:\n{e}")
