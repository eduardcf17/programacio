#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
añadir(notas,nota):
	notas.append(nota)
	



notas=[]
	
for i in range(i=0,9,1):
	while True:
		try:
			print "Pon la nota"
			nota=int(raw_input())
			añadir(notas,nota)
			break
		except ValueError:
			print "Error es una letra introduce un numero"	

Inicial  : 1, 2, 3, 4, 5
Mitja: 3.0
Màxim: 5
Mínim: 1

Correcció: 1, 10, 3, 4, 5
Mitja: 4.6
Màxim: 10
Mínim: 1
