#!/usr/bin/env python
# -*- coding: utf-8 -*-

def MostrarNota(notas):
	if len(notas)>0:
		for i in range (len(notas)):
			print notas[i],","
	else:
		print"cap nota"
		
def AfegirNota(notas):
	print"Escriu la nota"
	nota=int(raw_input())
	notas.append(nota)

def camviarNota(notas,posicion,notaNueva):
	notas[posicion]=notaNueva
	
def eliminar(notas):
	notas=[]
	
def aprobar(notas):
	for i in range (len(notas)):
		if notas[i]>5:
			notas[i]=5

notas=[]


def interrogante():
	print"Escull una  de les seguents opcions opció"
	print"	m	Mostra les notes separades per coma segons l'exercici de llistes.  En cas que es cridi aquest comandament al començament, o després d'haver buidat l'array, mostrarà el missatge: 'cap nota'"
	print"	c   Canvia la nota de la posició p per n."
	print"	a	Afegeix una nova nota al final de a llista."
	print"	b	Buida les notes de la llista."
	print"	t	Aprova a tothom segons l'exercici de llistes."
	print"	d   «n»	Cerca la nota n i retorna la informació trobada segons l'exercici de llistes."
	print"	?	Mostra una ajuda amb un resum de les comandes disponibles."
	print"	x	Finalitza l'execució"
	
interrogante()
opcio=""
while opcio!="x":
	opcio=(raw_input())
	if opcio=="m":
		MostrarNota(notas)
		print"Que vol fer ?"
		opcio=(raw_input())
	
	if opcio=="a":
		AfegirNota(notas)
		print"Que vol fer ?"
		opcio=(raw_input())
		
	if opcio=="c":
		print"Posicion nota"
		p=int(raw_input())
		print "Nota nueva"
		n=int(raw_input())
		camviarNota(notas,p,n)
		print"Que vol fer ?"
		opcio=(raw_input())
	if opcio =="b":
		eliminar(notas)
		print"Que vol fer ?"
		opcio=(raw_input())
		
