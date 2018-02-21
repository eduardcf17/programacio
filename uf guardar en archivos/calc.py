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
	if operacion!="+" and operacion!="-"and operacion!="*"and operacion!="/"and operacion!="n":
		print "Error"
		print"introduzaca operacion"	
		operacion=(raw_input())

	try:
		print "pon el primer numero"
		num1=int(raw_input())
	except ValueError:
		print "Error es una letra introduce un numero"
		num1=int(raw_input())	
	
	try:
		print "pon el segundo numero"
		num2=int(raw_input())
	except ValueError:
		print "Error es una letra introduce un numero"
		num2=int(raw_input())	
	
	if (operacion=="+"):
		print suma(num1,num2)
	if (operacion=="-"):
		print resta(num1,num2)
	if (operacion=="*"):
		print multi(num1,num2)
	if (operacion=="/"):
		try:
			print div(num1,num2)
		except ZeroDivisionError:
			nprint "Error no se puede dividir entre 0"
			nnum2=int(raw_input())
			ndiv(num1,num2)

	
