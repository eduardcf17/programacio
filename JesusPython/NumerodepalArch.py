#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Pedir Archivo 3

while True:
	try:
		Question = raw_input("What file do you want to open? ")
		OpenFile = open(Question)
		break
	except IOError:
		print "This file doesn't exist"

print "This is the content of the file"
print ""

for line in OpenFile:
	word = line.split()
	print "Number of words: ",len(word)
