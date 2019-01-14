# -*- coding: utf-8 -*-
import os, time

LOCK=r"\lock\GloboPlayAtemeTar.lock"
PATH=r"C:\Temp"

def lock():
	if os.path.exists(PATH + LOCK):
		print("Lock failed. Exiting.")
		exit()		
	else:
		os.makedirs(PATH + LOCK)
		time.sleep(1)

def unlock():
	os.rmdir(PATH + LOCK)

lock()
unlock()