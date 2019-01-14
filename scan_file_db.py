#-*- coding: utf-8 -*-
import os, sys, csv, mysql.connector
import config.logFile as logFile
from datetime import datetime

# Configuracao BD
def cfg():
	conf = {'user' : 'USER', 'password' : 'PASSWORD', 'host' : 'IP_ADDRESS', 'port' : 3306, 'database' : 'mam'}
	return conf

def main():
	sistema = sys.platform[:3]
	if sistema == 'win':
		os.system('cls')
	elif sistema == 'lin':
		os.system('clear')
	try:
		os.remove('./files_exists.csv')
	except:
		pass
	#logFile.pastaExiste()
	logFile.inicializar_logger('./files_exists.csv')

def arquivoExiste(p, f):	
	if os.path.isfile(p + f):
		#ENCONTRADO, nao precisa imprimir
		logFile.logg.info(p + ';' + f + ';ENCONTRADO')
	else:
		logFile.logg.info(p + ';' + f + ';NAO_ENCONTRADO')

#FUNCAO PARA SELECIONAR O PATH A PARTIR DE UMA ESCOLHA
def selectPath():
	while True:
		opcao = input('>>> ')
		if opcao == '1':
			storage_id = '2a17c8cd-58c0-11e4-84ad-fa224f896c15'
			storage_path = '//10.4.168.16/StorageHR01/'
		elif opcao == '2':
			storage_id = '4453e749-58c0-11e4-84ad-fa224f896c15'
			storage_path = '//10.4.168.17/StorageHRMirror01/'
		elif opcao == '3':
			storage_id = '70461df9-58c0-11e4-84ad-fa224f896c15'
			storage_path = '//10.4.168.16/StorageHR02/'
		elif opcao == '4':
			storage_id = '9aa4b825-58c0-11e4-84ad-fa224f896c15'
			storage_path = '//10.4.168.17/StorageHRMirror02/'
		else:
			print('Opcao invalida! Selecione de 1 a 4')
			continue
		return storage_id, storage_path
		break

def selectTable(uuid):
	registry_list = []
	config = cfg()
	try:
		conn = mysql.connector.connect(**config)
		print('[DB] Conectado')
	except Exception as e:
		print('[DB] Erro ao conectar\n[CFG] Verifique as configuracoes de conexao.\n[CFG] Processo abortado!')
		raise e
		exit()
	query = ("SELECT path FROM mam.file f \
			INNER JOIN mam.file_storage fs ON \
			f.uuid = fs.file_uuid \
			WHERE fs.storage_uuid = '%s'" % uuid)	
	sql = conn.cursor()
	try:
		sql.execute(query)
		print('[SQL] OK')
	except Exception as e:
		print('[SQL] Falha ao executar SQL')
		conn.close()
		print('[DB] Fechado')		
		exit()
	results = sql.fetchall()
	registry_list = [x[0] for x in results]
	try:
		conn.close()
		print('[DB] Fechado')
	except Exception as e:
		print('[DB] Falha ao fechar o banco')
		raise e
	return registry_list



if __name__ == "__main__":
	main()

#SCRIPT EXECUTADO
start = datetime.now()
print("""
#################################
######## STORAGE GNEWS ##########
#################################

Escolha de 1-4:

1) StorageHR01
2) StorageHRMirror01
3) StorageHR02
4) StorageHRMirror02
	""")

#Seleciona o path
id_storage, path = selectPath()
#Carrega resultado do banco
query_list = selectTable(id_storage)

#Verifica se o arquivo existe
print('[SCAN] Verificando se arquivos existem...')
for x in query_list:
	arquivoExiste(path, x)

#FIM DO SCRIPT
end = datetime.now()
diff = end - start
print('[START] :' + str(start))
print('[END]: ' + str(end))
print('Processo demorou: ' + str(diff) + ' segundos.')
print('Processo demorou: ' + str(diff) + ' segundos.')