#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Head

Archivo = open("/home/cf17jesus.atset/Escriptori/Trabajos/Archivosprogramacion/Archivito")
Lines = Archivo.readline()
Numberlines=int(input("How many lines do you want to see "))
for i in range(Numberlines):
	print Archivo.readline()

