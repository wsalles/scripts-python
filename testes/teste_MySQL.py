#!/usr/bin/python
import mysql.connector

db = mysql.connector.connect(host="IP_ADDRESS",		# your host, usually localhost
                     user="USER",					# your username
                     passwd="PASSWORD",				# your password
                     db="minhainfra")				# name of the data base
query = db.cursor()

# Use all the SQL you like
#query.execute("SELECT * FROM pessoas")
novoNome = input('>>> Digite um novo nome: ')
query.execute("UPDATE pessoas SET nome = '%s' where id_pessoa = 1 " % (novoNome))
#result = query.execute("SELECT * FROM pessoas")
#printa = query.fetchall()
# print all the first cell of all the rows
#for row in printa():
#    print(" ", row[0], " ", row[1], " ", row[2], " ", row[3])
db.commit()
db.close()