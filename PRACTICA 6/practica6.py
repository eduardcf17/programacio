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


alumnos=[]
notas1=[]
notas2=[]
notas3=[]
