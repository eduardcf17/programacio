#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  uneix.py
#  
#  Copyright 2018 cf17eduard.corral <cf17eduard.corral@E-xxx>
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




def cp(archivo,archivoCopia):
	lineas=archivo.read()
	numeroLineas=lineas.split("\n")
	archivo.seek(0,0)
	try:
		for i in range(0,len(numeroLineas),1):
			LineaCopiar=archivo.readline()
			archivoCopia.write(LineaCopiar)
	except:
		print "error"
	archivo.close()
	archivoCopia.close()
	

import sys
archivoCopia=open("/tmp/unio.txt","a")
for i in range (1,len(sys.argv),1):
	archivo=open(sys.argv,"r");
	cp(archivo,archivoCopia)
	
	
	
	
	
	
	
