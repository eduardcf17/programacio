#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 
print "Escriu la ruta del arxiu"
raw
csv=open("/home/cf17eduard.corral/Documents/PROGRAMACIO GIT/PROJECTE1/rd_e_gerdtot.tsv","r")
html=open("/home/cf17eduard.corral/Documents/PROGRAMACIO GIT/PROJECTE1/resultat.html","w")

def palabra(palabras):
	for palabra in palabras:
		html.write("<td>")
		html.write (palabra)
		html.write ("</td>")
def lineasEscribir(linea):
	html.write("<tr>")
	palabra(linea)
	html.write("</tr>")
	


html.write("<html>"+"\n")
html.write("<head>TABLA</head>"+"\n")
html.write("<body>"+"\n")
html.write("<table>"+"\n")
for lineas in (csv):
	linea=lineas.split("\t")
	lineasEscribir(linea) 
html.write("</table>")
html.write("\n")
html.write("</body>")
html.write("</html>")
#cada linea un tr y cada objeto de dentro un td

html.close()
csv.close()
