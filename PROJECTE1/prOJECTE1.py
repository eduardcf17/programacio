#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 
print "Escriu la ruta del arxiu"
ruta=(raw_input())
rutaHtml=ruta+"/resultat.html"
ruta=ruta+".tsv"

csv=open(ruta,"r")
html=open(rutaHtml,"w")

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
