# -*- coding: utf-8 -*-
import os, sys

path = 'Z:\\'
l = []

if os.path.exists(path):
	print('Unidade mapeada')
	print('A unidade será removida para teste')
	os.system('net use Z: /delete')
else:
	print('Unidade não está mapeada')
	os.system('net use Z: \\\\10.13.180.34\\sp-fileserver-01')
	l = os.listdir(path)
	print('Os arquivos da pasta são:')
	print(l)