# -*- coding: utf-8 -*-
import os, sys, fnmatch, collections, tarfile, time, datetime
import settings.util_GloboPlayAtemeTar as utilidades

path = "/mnt/ateme/ateme_EG/"
dest = "/home/ateme/GloboPlayAtemeTar/"
extension = "*.mp4"
amount = 6

#LOCK NA PASTA
utilidades.lock()

#Listar todos os arquivos em files[]
files = []
for dirpath, dirs, x in os.walk(path):	
	if ("2398" in dirpath) or ("2997" in dirpath) or ("5994" in dirpath):
		files += x
#Separar o DynamicRange
listDir = []
for x in files:
	if fnmatch.fnmatch(x, extension):
		if ("SDR" in x) and ("1PASS" not in x):
			filename = x.split("SDR")[0]			
			listDir.append(filename + "SDR")
		elif ("HDR" in x) and ("1PASS" not in x):
			filename = x.split("HDR")[0]
			listDir.append(filename + "HDR")
#Contar profiles
count = collections.Counter(listDir)

#Criando lista e dicionário de contagem dos arquivos
listCount = list(count)
dictCount = dict(count)

for x in listCount:
	if dictCount[x] == amount:
		if os.path.isfile(dest + x + "_replace.tar"):
			print("O arquivo: "+ x + "_replace.tar  já existe")
		else:
			with tarfile.open(dest + x + "_replace.tar", mode="w") as tar:
				for dirpath, dirs, file in os.walk(path):
					if ("2398" in dirpath) or ("2997" in dirpath) or ("5994" in dirpath):
						for addFiles in file:
							if fnmatch.fnmatch(addFiles, extension):
								if x in addFiles:							
									try:
										tar.addfile(tarfile.TarInfo(addFiles), open(dirpath + "/" + addFiles))										
									except Exception as e:
										gerarLog("[ERROR]: Não foi possível gerar o arquivo >> "+ x + "_replace.tar")
										print("Erro ao gravar TAR" + str(e))
										pass
				utilidades.gerarLog("[SUCESSO]: Gerado o arquivo >> " + x + "_replace.tar")
				utilidades.enviarEmail(x + "_replace.tar")
				tar.close()
	else:
		print("\nReprovado para fazer o .TAR")
		print("Pois o arquivo: "+ x + " se repetiu apenas " + str(dictCount[x]) + " em vez de " + str(amount) + " vezes.")

utilidades.unlock()