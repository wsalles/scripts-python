# -*- coding: utf-8 -*-
import os, glob

path="C:\\Temp\\TesteTar"
extension="*.txt"

files = glob.glob(os.path.join(os.getcwd(), path, extension))
corpus = []

for x in files:
	with open(x) as f_input:
		corpus.append(f_input.read())
		#corpus.append(f_input.readlines())

print(corpus)