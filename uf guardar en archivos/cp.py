#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 

def cp(archivo):
	try:
		while True:
			nuevo=archivo.readline()
	except:
		print "error"
		



archivo=open("/home/cf17eduard.corral/Documents/prueba.txt")
print"Introduce el numero"
numero=int(raw_input())
head(numero,archivo)
