#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Programa que trasforma a html un csv
import datetime
def abrirLog(nombre_log):
    archivo_log = open(nombre_log, "a")
    guardar_log(archivo_log, "Iniciando registro de errores")
    return archivo_log
 
def guardar_log(archivo_log, mensaje):
    # Obtiene la hora actual en formato de texto
    hora_actual = str(datetime.datetime.now())
    # Guarda la hora actual y el mensaje de error en el archivo
    archivo_log.write(hora_actual+" "+mensaje+"\\n")


def pedirRuta():
	print "Escriu la ruta de la carpeta on esta l'arxiu"
	ruta=(raw_input())
	return ruta
	
def nomEntrada():
	print"Escriu el nom de l'arxiu sense extensio"
	nom=(raw_input())
	return nom
	
def nomResultado():
	print"Escriu en nom de sortida del arxiu"
	nomSortida=(raw_input())
	return nomSortida

	
def crearRutaCss(ruta):
	rutaCss=ruta+"/estils.css"
	return rutaCss
	
def crearRutaHtml(ruta,nomSortida):
	rutaHtml=ruta+"/"+nomSortida+".html"
	return rutaHtml
	
def crearRutaCsv(ruta,nom):
	ruta=ruta+"/"+nom+".csv"
	return ruta
	
while True:
	ruta=pedirRuta()
	nom=nomEntrada()
	nomSortida=nomResultado()
	rutaHtml=crearRutaHtml(ruta,nomSortida)
	rutaCss=crearRutaCss(ruta)
	abrir_log=abrirLog("log.txt")
	try:
		css=open(rutaCss,"w")
		ruta=crearRutaCsv(ruta,nom)
		csv=open(ruta,"r")
		html=open(rutaHtml,"w")
		break
	except:
		print "no se a podido abrir introduce de nuevo los datos"
		guardar_log(abrir_log,"Error al abrir los archivos,se cierra log"+"\n")
		abrir_log.close()
	
		
	
		
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
	css.write("h1{text-align:center;}"+"\n")
	css.write("*{background-color:LightCyan ;}"+"\n")
	css.write("table {"+"\n")
	css.write("border-collapse: collapse;"+"\n")
	css.write("}"+"\n")
	css.write("table, th, td {"+"\n")
	css.write("border: 1px solid black;"+"\n")
	css.write("}"+"\n")

html.write("<html>"+"\n")
html.write("<head>"+"\n")
html.write('<link rel="stylesheet" type="text/css" href="estils.css">'+"\n")
html.write('<meta charset="utf-8">')
html.write("</head>"+"\n")
html.write("<h1>TABLA</h1>")

html.write("<body>"+"\n")
html.write("<table>"+"\n")

for lineas in (csv):
	linea=lineas.split(",")
	try:
		lineasEscribir(linea) 
	except:
		print"Error al llamar a la función"
		guardar_log(abrir_log,"Error al llamar a la función: lineasEscribir linea 112 de codigo")

html.write("</table>")
html.write("\n")
html.write("</body>")
html.write("</html>")

crearCss()

html.close()
csv.close()
css.close
guardar_log(abrir_log,"Finaliza el programa")
abrir_log.close()

