#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  projecto3.py
while True:
	try:
		print "Escriu el nom de la pelicula"
		nom=(raw_input())
		print"Escrou la mida"
		while True:
			try:
				mida=int(raw_input())
				break
			except:
				print"Error no es un numero"
		pelicula=open(nom,"r")
		break
	except:
		print "no se a podido abrir introduce el nombre correcto"
numeroPartes=mida/100;

for i in range(0,numeroPartes,1):
	nombr=str(nom),"parte",str(i)
	nombr=str(nombr)
	nombre=open(nombr,"w")
	contenido = pelicula.read(104857600)
	nombre.write(contenido)
for i in range(0,numeroPartes,1):
	nombr=str(nom),"parte",str(i)
	nombre.close()
