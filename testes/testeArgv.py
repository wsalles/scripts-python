#-*- coding: utf-8 -*-
import os, sys

def argumentos(*argv):    
	for arg in argv:
		print(str(argv) + " - Argumento: " + arg)

#argumentos(sys.argv[1], sys.argv[2], sys.argv[3])
print(sys.argv[1])