#!/usr/bin/env python
# -*- coding: utf-8 -*-


def AfegirNota(alumnos,nota1,nota2,nota3):
	print"Escriu nom de l'alumne"
	alumno=(raw_input())
	alumnos.append(alumno)
	print"Escriu la nota de la primera avaluació"
	nota=int(raw_input())
	nota1.append(nota)
	print"Escriu la nota de la segona avaluació"
	nota=int(raw_input())
	nota2.append(nota)
	print"Escriu la nota de la tercera avaluació"
	nota=int(raw_input())
	nota3.append(nota)
	
def mostrarNota(alumnos,nota1,nota2,nota3):
	print "Alumnos  1ra     2na     3ra     final"
	for i in range (len(alumnos)):
		print alumnos[i]," ",nota1[i]," ",nota2[i]," ",nota3[i]," ",(nota1[i]+nota2[i]+nota3[i]




alumnos=[]
notas1=[]
notas2=[]
notas3=[]

opcio=(raw_input())
if opcio=="a"
	AfegirNota(alumnos,notas1,notas2,notas3)
if opcio=="m":
	mostrarNota(alumnos,notas1,notas2,notas3)
	
	
	
	
