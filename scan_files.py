#-*- coding: utf-8 -*-
import glob, os, mysql.connector
import database_losysweb_rj as db
from datetime import datetime

#FUNCAO PARA SELECIONAR O PATH A PARTIR DE UMA ESCOLHA
def selectPath():	
	while True:
		opcao = input('>>> ')
		if opcao == '1':
			storage_id = '2a17c8cd-58c0-11e4-84ad-fa224f896c15'
			storage_path = '\\\\10.4.168.16\\StorageHR01'
		elif opcao == '2':
			storage_id = '4453e749-58c0-11e4-84ad-fa224f896c15'
			storage_path = '\\\\10.4.168.17\\StorageHRMirror01'
		elif opcao == '3':
			storage_id = '70461df9-58c0-11e4-84ad-fa224f896c15'
			storage_path = '\\\\10.4.168.16\\StorageHR02'
		elif opcao == '4':
			storage_id = '9aa4b825-58c0-11e4-84ad-fa224f896c15'
			storage_path = '\\\\10.4.168.17\\StorageHRMirror02'
		else:
			print('Opcao invalida! Selecione de 1 a 4')
			continue
		return storage_id, storage_path
		break

# FUNCAO PARA LISTAR OS ARQUIVOS
def fileList(p):
	file_list = []
	# ZERANDO O ARQUIVO
	open('./file_list.txt', 'w').close()
	# ABRINDO O ARQUIVO PARA LER E ESCREVER
	f = open('./file_list.txt', 'a')
	print('[LOADING] Carregando os arquivos e diretorios de pastas')
	for root, dirs, files in os.walk(p):
		for file in files:
			fp = os.path.join(root, file)
			if len(fp) >= 45:
				file_list.append(fp)
				f.write(fp + '\n')
	f.close()
	return file_list

# FUNCAO PARA LISTAR AS PASTAS
def folderList(p):
	folder_list = []
	# ZERANDO O ARQUIVO
	open('./folder_list.txt', 'w').close()
	# ABRINDO O ARQUIVO PARA LER E ESCREVER
	f = open('./folder_list.txt', 'a')
	print('[LOADING] Carregando os diretorios de pastas')
	for root, dirs, files in os.walk(p):
		for d in dirs:
			fp = os.path.join(root, d)
			if len(fp) >= 45:				
				fp = fp.replace(p, '')
				fp = fp.replace('\\', '/')
				fp = fp[1:]
				f.write(fp + '\n')
				folder_list.append(fp)
	f.close()
	return folder_list

def selectTable(uuid):
	registry_list = []	
	conf = db.cfg()
	try:
		conn = mysql.connector.connect(**conf)
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

######## INICIO DO SCRIPT ########
print("""
#######################################
####### STORAGE CLEANER - GNEWS #######
#######################################

Selecione uma das opcoes abaixo para scannear:

1) StorageHR01 (10.4.168.16)
2) StorageHRMirror01 (10.4.168.16)
3) StorageHR02 (10.4.168.17)
4) StorageHRMirror02 (10.4.168.17)
""")
#SCRIPT EXECUTADO
start = datetime.now()
# SELECIONA O VALOR DO STORAGE_UUID E O STORAGE_NAME
storage_id, storage_path = selectPath()
# CRIA A LISTA DE ACORDO O RETORNO DO SELECT
query_list = selectTable(storage_id)
# DIFF
folders_list = folderList(storage_path)
# ZERANDO O ARQUIVO
open('./delete_list.txt', 'w').close()
# ABRINDO O ARQUIVO PARA LER E ESCREVER
f = open('./delete_list.txt', 'a')
# VARIAVEL TEMPORARIA PARA CAPTURAR OS ITENS EXISTES NO BANCO
tmp = []
# VERIFICACAO (DIFF)
for x in folders_list:
	for y in query_list:
		if x in str(y):
			tmp.append(x)

# REMOVENDO ARQUIVOS REGISTRADO DA LISTA
[folders_list.remove(x) for x in tmp if x in folders_list]

# IMPRIMINDO ARQUIVOS NAO REGISTRADOS
for x in folders_list:
	f.write(x + '\n')

print('[FILE] Arquivo delete_list.txt gerado com sucesso.')


#FIM DO SCRIPT
end = datetime.now()
diff = end - start
print('[START]:' + str(start))
print('[END]: ' + str(end))
print('[END] Processo demorou: ' + str(diff) + ' segundos.')