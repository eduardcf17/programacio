#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Pedir Archivo

while True:
	try:
		Question = raw_input("What file do you want to open? ")
		OpenFile = open(Question,"r")
		break
	except IOError:
		print "This file doesn't exist"

print "This is the content of the file"
print ""
print OpenFile.read()

