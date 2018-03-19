#!/usr/bin/env python
# -*- coding: utf-8 -*-
#cp

Archivo = open("/home/cf17jesus.atset/Escriptori/Trabajos/Archivosprogramacion/Archivito","r")
Lines = Archivo.readlines()
Copia = open("/home/cf17jesus.atset/Escriptori/Trabajos/Archivosprogramacion/Copia","w")
Copia.writelines(Lines)


