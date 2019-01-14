import os, sys

os.system('cls')

letra='005TD'

#while True:
#letra = input('>>> Digite uma letra: ')
##Convertendo caracter em bytes
letra = bytes(letra, 'utf-8')

##Adiciondo a próxima letra
proxLetra = bytes([letra[4] + 15 + 1])
##Convertendo byte em String
proxLetra = str(proxLetra)
letra = str(letra[0:5])
print('CURRENT: ' + letra[2:-1])
print('A próxima TAPE é: ' + letra[2:-2] + proxLetra[2])