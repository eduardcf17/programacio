#!/usr/bin/env python
# -*- coding: utf-8 -*-
#CPB

Archivo = open("/home/cf17jesus.atset/Escriptori/Trabajos/Archivosprogramacion/Archivito","r")
Bits = int(input("How many bytes do you want to copy? "))
Lines = Archivo.read(Bits)
Copia = open("/home/cf17jesus.atset/Escriptori/Trabajos/Archivosprogramacion/Copia2","w")
Copia.writelines(Lines)


