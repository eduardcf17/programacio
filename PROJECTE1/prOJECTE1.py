#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
while True:
	try:
		print "Escriu la ruta del arxiu"
		ruta=(raw_input())
		rutaHtml=ruta+"resultat.html"
		ruta=ruta+".tsv"
		csv=open(ruta,"r")
		rutaCss=ruta+"estilis.css"
		css=open(rutaCss,"w")
		break
	except:
		print "no se a podido abrir introduce la ruta correcta"
	
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
	
def crearCss():
	css.write("table {"+"\n")
	css.write("border-collapse: collapse;"+"\n")
	css.write("}"+"\n")
	css.write("table, th, td {"+"\n")
	css.write("border: 1px solid black;"+"\n")
	css.write("}"+"\n")
	

    

	
	
	

html.write("<html>"+"\n")
html.write("<head>"+"\n")
html.write("TABLA"+"\n")
html.write('<link rel="stylesheet" type='+ruta+' href=estils.css">'+"\n")
html.write("</head>"+"\n")


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
crearCss()
html.close()
csv.close()
css.close
