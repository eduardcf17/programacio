#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 

def cp(archivo,archivoCopia):
	lineas=archivo.read()
	numeroLineas=lineas.split("\n")
	archivo.seek(0,0)
	try:
		for i in range(0,len(numeroLineas),1):
			LineaCopiar=archivo.readline()
			archivoCopia.write(LineaCopiar)
	except:
		print "error"
	archivo.close()
	archivoCopia.close()
	


archivo=open("/home/edu/Documentos/programacio/uf guardar en archivos/prueba","r")
archivoCopia=open("/home/edu/Documentos/programacio/uf guardar en archivos/pruebaCopia","a");

cp(archivo,archivoCopia)
