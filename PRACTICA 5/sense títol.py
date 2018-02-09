#!/usr/bin/env python
# -*- coding: utf-8 -*-

def MostrarNota(notas):
	for i in range(notas.length):
		print notas[i],","
		
def AfegirNota(notas):
	print"Escriu la nota"
	nota=int(raw_input())
	notas.append(nota)






notas[]

print "Escull una  de les seguents opcions opció"
print"m	Mostra les notes separades per coma segons l'exercici de llistes.  En cas que es cridi aquest comandament al començament, o després d'haver buidat l'array, mostrarà el missatge: 'cap nota'"
print"c «p» «n»	Canvia la nota de la posició p per n."
print"a	Afegeix una nova nota al final de a llista."
print"b	Buida les notes de la llista."
print"t	Aprova a tothom segons l'exercici de llistes."
print"d «n»	Cerca la nota n i retorna la informació trobada segons l'exercici de llistes."
print"?	Mostra una ajuda amb un resum de les comandes disponibles."
print"x	Finalitza l'execució"

opcio=(raw_input())
if opcio=="m":
	MostrarNota(notas[])

if opcio=="a":
	AfegirNota(notas[])
