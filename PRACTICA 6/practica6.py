#!/usr/bin/env python
# -*- coding: utf-8 -*-


def AfegirNota(alumnos,nota1,nota2,nota3):
	print"Escriu nom de l'alumne"
	alumno=(raw_input())
	alumnos.append(alumno)
	print"Escriu la nota de la primera avaluació"
	nota=int(raw_input())
<<<<<<< HEAD
=======
<<<<<<< HEAD
	while nota>10 or nota <0:
		print "Nota erronia torna a posarla"
		nota=int(raw_input())
=======
>>>>>>> 47cb9c5098abc546c319647772a5e3f862ef8aeb
>>>>>>> d62f61c37c9d79085efeee92351d81ab34f18add
	nota1.append(nota)
	print"Escriu la nota de la segona avaluació"
	nota=int(raw_input())
	nota2.append(nota)
	print"Escriu la nota de la tercera avaluació"
	nota=int(raw_input())
	nota3.append(nota)
<<<<<<< HEAD
	
def mostrarNota(alumnos,nota1,nota2,nota3):
	print "Alumnos  1ra     2na     3ra     final"
	for i in range (len(alumnos)):
		print alumnos[i]," ",nota1[i]," ",nota2[i]," ",nota3[i]," ",(nota1[i]+nota2[i]+nota3[i]
=======
<<<<<<< HEAD
	
def mostrarNota(alumnos,nota1,nota2,nota3):
	print "Alumnos\t\t1ra\t2na\t3ra\tfinal"
	for i in range (len(alumnos)):
		print alumnos[i],"\t",nota1[i],"\t",nota2[i],"\t",nota3[i],"\t",float((nota1[i]+nota2[i]+nota3[i])/3)
		print "-----------------------------------------------"
		
def aprobar(notas1,notas2,notas3):
	for i in range (len(notas1)):
		if notas[i]>5:
			notas[i]=5
	for i in range (len(notas2)):
		if notas[i]>5:
			notas[i]=5
	for i in range (len(notas3)):
		if notas[i]>5:
			notas[i]=5
>>>>>>> d62f61c37c9d79085efeee92351d81ab34f18add




<<<<<<< HEAD
=======
def ajuda():
	print"a «nom» «n1» «n2» «n3»	Insereix les tres notes d'un nou alumne."
	print"m	Mostra els alumnes i les seves notes"
	print"t	Aprova a tothom."
	print"n «nomant» «nomnou»	Canvia el nom del primer alumne que es digui nomant. Si no hi ha cap, mostra error."
	print"c «nom» «eval» «n» Canvia la nota de l'avaluació aval de l'alumne amb nom nom per n."
	print"?	Mostra una ajuda amb un resum de les comandes disponibles."
	print"x	Finalitza l'execució"
=======
>>>>>>> 47cb9c5098abc546c319647772a5e3f862ef8aeb


>>>>>>> d62f61c37c9d79085efeee92351d81ab34f18add
alumnos=[]
notas1=[]
notas2=[]
notas3=[]
<<<<<<< HEAD

opcio=(raw_input())
if opcio=="a"
	AfegirNota(alumnos,notas1,notas2,notas3)
if opcio=="m":
	mostrarNota(alumnos,notas1,notas2,notas3)
	
	
	
	
=======
<<<<<<< HEAD

ajuda()
opcio=""
while opcio!="x":
	opcio=(raw_input())
	if opcio=="a":
		AfegirNota(alumnos,notas1,notas2,notas3)
		print"Que vol fer ?"
	if opcio=="m":
		mostrarNota(alumnos,notas1,notas2,notas3)
		print"Que vol fer ?"
		
		
	if opcio=="t":
		aprobar(notas1,notas2,notas3)
		print"Que vol fer ?"
		
		




	
	
=======
>>>>>>> 47cb9c5098abc546c319647772a5e3f862ef8aeb
>>>>>>> d62f61c37c9d79085efeee92351d81ab34f18add
