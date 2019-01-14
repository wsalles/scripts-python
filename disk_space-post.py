#-*- coding: utf-8 -*-
import sys, os, json, requests

def gerarToken(ip):
	url = 'http://' + ip + ':3333/auth'
	dados = {"username" : "wsalles","password" : "Globo123"}
	header = {"Content-Type": "application/json"}
	resposta = requests.post(url, data=json.dumps(dados), headers=header)
	meuToken = resposta.json()
	return meuToken['access_token']

def registry(process, ex1, ex2, ip):
	url = 'http://' + ip ':3333/processes/' + process
	token = gerarToken()
	dados = {'working' : "", 'extras1' : ex1, 'extras2' : ex2}
	header = {'Authorization' : 'JWT ' + token, "Content-Type": "application/json"}
	resposta = requests.put(url, data=json.dumps(dados), headers=header)

def percentDisk(path):
	stat = os.statvfs(path)
	total = (stat.f_bsize * stat.f_blocks) / 1024
	avail = (stat.f_bsize * stat.f_bavail) / 1024
	used = total-avail
	percent = float(used)/float(total)*100
	return percent

# Gerando token
ip = input('>> Digite o IP do REST API: ')
token = gerarToken(ip)
# Pegando a porcentagem
elemental = percentDisk("/mnt/elemental-new/Fluxo_4k")
ateme = percentDisk("/mnt/DISTRIBUICAO")
# Post
registry('Disk Space 4K', elemental, ateme, ip)