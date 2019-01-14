import urllib.request, json, time, os

url = "http://localhost/pessoas"

def imprimir():
	response = urllib.request.urlopen(url)
	contents = response.read()
	data = json.loads(contents.decode("utf8"))
	return (data["pessoas"][0]['cars']['car1'])	

def abrirPrograma():
	try:
		os.system('start mspaint')
	except:
		print ('Não é possível abrir o programa.\n')

while True:
	try:
		carro = imprimir()
	except:
		print('Não foi possível realizar o JSON')
	else:
		if (carro == 'Honda'):
			print('Achamos o HONDA! Será aberto o paint.')
			abrirPrograma()
		else:
			print(carro)
	time.sleep(5)