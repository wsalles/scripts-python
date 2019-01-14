import os, sys, codecs, time, datetime, logging as log
os.system('cls')
print("""
###############################
### SCRIPT DE TESTE: PYTHON ###
###############################""")

class Logger:

	tempo = time.time()
	tempoArquivo = datetime.datetime.fromtimestamp(tempo).strftime('%Y-%m-%d')
	tempoData = datetime.datetime.fromtimestamp(tempo).strftime('[' + '%Y/%m/%d %H:%M:%S' + ']')
	log.basicConfig(filename=tempoArquivo + '_testeLogging.log', level=log.INFO,
					format=tempoData + '[%(levelname)s]:%(message)s')

	total = 0

	nome = input('>>> Digite seu nome: ')
	for x in range(3):
		num = int(input('>>> Digite um numero: '))
		total += num
		#print('Valor digitado foi: ' + str(num))
	log.info('Seu nome é: ' + nome)
	log.info('O total foi: ' + str(total))
	os.system('pause')

#Docs
#https://docs.python.org/3/howto/logging.html#logging-advanced-tutorial
#That’s the logger used by the functions:
#debug(), info(), warning(), error() and critical(),
#which just call the same-named method of the root logger. 