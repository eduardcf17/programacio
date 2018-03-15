#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

def pedirRuta():
	print "On esta el fitxer"
	ruta=(raw_input())
	return ruta

def abrirArchivo(ruta):
	archivo=open(ruta)
	return archivo
	
	
while True:
	try:
		ruta=pedirRuta()
		archivo=abrirArchivo(ruta)	
		break
	except:
		print "Error en la ruta"


print archivo.read()
		
