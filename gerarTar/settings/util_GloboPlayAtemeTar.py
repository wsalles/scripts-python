# -*- coding: utf-8 -*-
import os, time, datetime
import logging as log
import smtplib as envio

LOCKNAME='GloboPlayAtemeTar.lock'
PATH='/var/lock/' + LOCKNAME

class tempoReal:
	tempo = time.time()
	tempoArquivo = datetime.datetime.fromtimestamp(tempo).strftime('%Y-%m-%d')
	tempoData = datetime.datetime.fromtimestamp(tempo).strftime('[' + '%Y/%m/%d %H:%M:%S' + ']')

def gerarLog(i):
	try:
		if os.path.exists('/var/log/scripts/'):
			log.basicConfig(filename='/var/log/scripts/' + tempoReal.tempoArquivo + '_GloboPlayAtemeTar.log', level=log.INFO,
					format=tempoReal.tempoData + '[%(levelname)s]%(message)s')
			return log.info(i)
	except:
		print('Não foi possível localizar o diretório.')
		os.mkdir('/var/log/scripts/')
		print('Diretório criado')
		log.basicConfig(filename='/var/log/scripts/' + tempoReal.tempoArquivo + '_GloboPlayAtemeTar.log', level=log.INFO,
					format=tempoReal.tempoData + '[%(levelname)s]%(message)s')
		return log.info(i)


def enviarEmail(file):
	de = 'Suporte Plataformas <suporte.plataformas@tvglobo.com.br>'
	para = ['Fabio Faria <fabio.faria@tvglobo.com.br>','Fabio Ferreira <Fabio.Ferreira@tvglobo.com.br>',
			'Fabio Pereira <fabio.pereira@tvglobo.com.br>','#tecnologia-desis-plataformas <tecnologiadesisplataformas@tvglobo.com.br>',
			'#TECNOLOGIA-EXIBICAORJ-COMUNICACAO <#TECNOLOGIA-EXIBICAORJ-COMUNICACAO@tvglobo.com.br>',
			'#DTED-EXIBICAORJ-SISTEMAS <#DTED-EXIBICAORJ-SISTEMAS@tvglobo.com.br>',
			'Raphael Salomao <raphael.salomao@tvglobo.com.br>',
			'Wallace Salles <wallace.salles@tvglobo.com.br>']
	paraTeste = ['Raphael Salomao <raphael.salomao@tvglobo.com.br>',
				'Wallace Salles <wallace.salles@tvglobo.com.br>',
				'Jorge Costa <jorge.costa@tvglobo.com.br>']
	assunto = '[Publicação 4k] Replace: Sucesso'
	mensagem = ("""From: %s
To: %s
Subject: %s
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Disposition: inline
Content-Transfer-Encoding: 8bit

Arquivo %s foi entregue com sucesso!

Atenciosamente;
Suporte Plataformas | Ramal: *21 3000
tecnologiadesisplataformas@tvglobo.com.br
""" % (de, paraTeste, assunto, file))

	try:
		mail = envio.SMTP('10.62.0.121', 25)		
		#mail = envio.SMTP('10.7.118.200', 25)		
		mail.ehlo()
		mail.sendmail(de, paraTeste, mensagem.encode("utf8"))
		mail.close()
		print("Successfully sent email")
	except:
	   print("Error: unable to send email")


def lock():
	if os.path.exists(PATH):
		print("Lock failed. Exiting.")
		exit()		
	else:
		os.makedirs(PATH)
		time.sleep(1)

def unlock():
	os.rmdir(PATH)