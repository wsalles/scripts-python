#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, codecs, os, time, requests, paramiko
import smtplib as envio
from email import encoders

#Argumentos
ip = sys.argv[2]
site = sys.argv[3]
node = sys.argv[4]
#Configuracoes SSH
hostname = ip
port = 33001
username = 'SSH_USER'
password = 'SSH_PASSWORD'

#Contador de tentativas
cont = 1
#Tempo
tempo = time.strftime('%X')

def restartService():
        #Iniciando o cliente SSH
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.WarningPolicy())
        #Conexao SSH
        ssh.connect(hostname, port, username, password)
        ssh.exec_command('sudo /etc/init.d/asperanoded stop')
        print('Parando o servico: asperanoded...')
        time.sleep(4)
        print('Reiniciando o servico: asperanoded...')
        ssh.exec_command('sudo /etc/init.d/asperanoded restart')
        #Fechando SSH
        time.sleep(2)
        ssh.close()

#REINICIA O SERVICO
restartService()

#Variaveis
de = "suporte.plataformas@tvglobo.com.br"
para = (sys.argv[1].split(','))
assunto = ("[ASPERA][" + site + "][NODE " + node + "]: AVISO DE RESTART")

while True:
        r = os.system('curl -ki -u apiglobo:AP12o1E https://10.62.80.3:9092/ping | grep 200')
        if r == 0:
                print('Service normalizado')
                msg = ("""From: %s
To: %s
Subject: %s
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Disposition: inline
Content-Transfer-Encoding: 8bit

O problema ocorreu as %s e foi necessario %d tentativa(s) para reinicia-lo.
Service: asperanoded
Host: %s
NODE: %s
Site: %s""" % (de, ', '.join(para), assunto, tempo, cont, ip, node, site))
                s = envio.SMTP('10.7.118.200', 25)
                try:
                        s.sendmail(de, para, msg)
                        print('Email enviado com sucesso!')
                        s.quit()
                        break
                except Exception as e:
                        print('Erro ao enviar e-mail...')
                        print(e)
                        break
        else:
                print('Erro ao consultar a API\nUma nova tentativa sera realizada.')
                cont += 1
                restartService()
                continue