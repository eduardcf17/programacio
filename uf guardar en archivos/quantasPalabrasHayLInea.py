#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


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




palabras = archivo.read()
lineas=palabras.split('\n')
contador=0
for i in lineas:
	contador=contador+1
	NumeroPalabras=len(i.split(" "))
	print "linea ",contador,"numero de palabras: ",NumeroPalabras #si pones i salen las palabras de cada linea



		
