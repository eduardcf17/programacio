#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

def head(numero,archivo):
	try:
		for i in range(0,numero,1):
			print archivo.readline()
	except:
		print "error"
		



archivo=open("/home/cf17eduard.corral/Documents/prueba.txt")
print"Introduce el numero"
numero=int(raw_input())
head(numero,archivo)
