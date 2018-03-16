#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
def suma(num1,num2):
	summ=num1+num2
	return summ
	
def resta(num1,num2):
	rest=num1-num2
	return rest
	
def mult(num1,num2):
	multi=num1*num2
	return multi
	
def div(num1,num2):
	divi=num1/num2
	return divi

operacion=""	
while operacion!="n":
	print "Que operacion desea hacer: + - / * o N"
	operacion=(raw_input())
	while operacion!="+" and operacion!="-"and operacion!="*"and operacion!="/"and operacion!="n":
		print "Error"
		print"introduzaca operacion"	
		operacion=(raw_input())
	if operacion=="n":
		break
	while True:
		try:
			print "pon el primer numero"
			num1=int(raw_input())
			break
		except ValueError:
			print "Error es una letra introduce un numero"	
	while True:
		try:
			print "pon el segundo numero"
			num2=int(raw_input())
			break
		except ValueError:
			print "Error es una letra introduce un numero"	
	
	if (operacion=="+"):
		print suma(num1,num2)
	if (operacion=="-"):
		print resta(num1,num2)
	if (operacion=="*"):
		print multi(num1,num2)
	if (operacion=="/"):
		while True:
			try:
				print div(num1,num2)
				break
			except ZeroDivisionError:
				print "Error no se puede dividir entre 0 introduexi un altre numero"
				num2=int(raw_input())
				

	
