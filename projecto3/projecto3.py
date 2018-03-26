#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  projecto3.py
#  
#  Copyright 2018 edu <edu@edu-TOSHIBA-NB500>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
while True:
	try:
		print "Escriu el nom de la pelicula"
		nom=(raw_input())
		print"Escrou la mida"
		while True:
			try:
				mida=int(raw_input())
				break
			except:
				print"Error no es un numero"
		pelicula=open(nom,"b")
		break
	except:
		print "no se a podido abrir introduce el nombre correcto"
numeroPartes=mida/100;

for i in range(0,numeroPartes,1):
	nombre="parte"+i
	nombre=open(nom+".part"+i,w)
	contenido = pelicula.read(104857600)
	archivo.write(contenido)
for i in range(0,numeroPartes,1):
	nombre="parte"+i
	nombre.close()
