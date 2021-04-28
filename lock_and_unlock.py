import os

PATH = "/tmp/"
LOCK = PATH + "GloboPlay.lock"


def lock():
	if os.path.exists(PATH + LOCK):
		print("Lock failed. Exiting.")
		exit()		
	else:
		os.makedirs(PATH + LOCK)


def unlock():
	os.rmdir(PATH + LOCK)


# Getting started
lock()
unlock()