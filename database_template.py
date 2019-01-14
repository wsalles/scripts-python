import mysql.connector

def cfg():
	config = {
		'user' : 'USER',
		'password' : 'PASSWORD',
		'host' : 'IP_ADDRESS',
		'port' : 3306,
		'database' : 'mam',
	}
	return config