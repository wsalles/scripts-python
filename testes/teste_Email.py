import os, sys, codecs, time, datetime, smtplib as envio
os.system('cls')
print("""
###############################
### SCRIPT DE TESTE: PYTHON ###
###############################""")

#Envio de e-mail
def enviarEmail():
	de = 'Suporte Plataformas <suporte.plataformas@tvglobo.com.br>'
	para = ['Wallace Salles <wallace.salles@tvglobo.com.br>', 'Marcos Morais <marcos.morais@tvglobo.com.br>']
	assunto = 'Robot CEDOC - Solicitação de fitas LTO-5 para Backup'
	mensagem = ("""From: %s
To: %s
Subject: %s
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Disposition: inline
Content-Transfer-Encoding: 8bit

SAEM / ACERVO,
Novamente precisamos repor as fitas no Robô LTO-5.
Poderiam iniciar o processo de inclusão assim que possível?

Atenciosamente;
Suporte Plataformas | Ramal: *21 3000
tecnologiadesisplataformas@tvglobo.com.br
""" % (de, para, assunto))

	try:
		mail = envio.SMTP('10.7.118.200', 25)
		mail.ehlo()
		#mail.starttls()
		#mail.login('', '')
		mail.sendmail(de, para, mensagem.encode("utf8"))
		mail.close()
		print("Successfully sent email")
	except:
	   print("Error: unable to send email")

	os.system('pause')