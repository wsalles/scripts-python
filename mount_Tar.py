# -*- coding: utf-8 -*-
import os, sys, fnmatch, collections, tarfile

path='.'
extension="*.mp4"
amount=3

#Listar todos os arquivos em files[]
files = []
for dirpath, dirs, x in os.walk(path):
	files += x
#Separar o DynamicRange
listDir = []
for x in files:
	if fnmatch.fnmatch(x, extension):
		if ("SDR" in x) and ("1PASS" not in x):
			filename = x.split('SDR')[0]			
			listDir.append(filename + 'SDR')
		elif ("HDR" in x) and ("1PASS" not in x):
			filename = x.split('HDR')[0]
			listDir.append(filename + 'HDR')
#Contar profiles
count = collections.Counter(listDir)
#print(listDir)
#print(count)

#Criando lista e dicionário de contagem dos arquivos
listCount = list(count)
dictCount = dict(count)

#print('################')
#print(listCount)
#print(listCount[0])
#print('################')
#print(dictCount)
#print('###################')
#print('# RESULTADO FINAL #')
#print('###################')
for x in listCount:
	if dictCount[x] == amount:
		#print('Aprovado para fazer o .TAR')
		#print('Pois o arquivo: ' + x + ' se repetiu: ' + str(dictCount[x]) + ' vezes.\n')
		if os.path.isfile(path + '/' + x + '_replace.tar'):
			print('O arquivo: '+ x + '_replace.tar  já existe')
		else:
			with tarfile.open(x + '_replace.tar', mode='w') as tar:
				for dirpath, dirs, file in os.walk(path):
					for addFiles in file:
						if fnmatch.fnmatch(addFiles, extension):
							#print('valor de x: ' + x)
							#print('add: ' + addFiles)
							if x in addFiles:							
								try:
									tar.addfile(tarfile.TarInfo(addFiles), open(dirpath + '/' + addFiles))
								except Exception as e:
									print('Erro ao gravar TAR' + str(e))
									pass
				tar.close()
	else:
		print('\nReprovado para fazer o .TAR')
		print('Pois o arquivo: '+ x + ' se repetiu apenas ' + str(dictCount[x]) + ' em vez de ' + str(amount) + ' vezes.')