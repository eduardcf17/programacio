/*
 * Ex1.java
 * 
 * Copyright 2018 cf17eduard.corral <cf17eduard.corral@E-xxx>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */

import java.io.*;
public class gravainterval {
	public static void escribirArchivo(String ruta,int valorBajo,int valorMaximo)throws IOException{
		FileWriter fichero = null;
        PrintWriter pw = null;
		try{
		fichero = new FileWriter(ruta);
		pw = new PrintWriter(fichero);
		pw.println(valorBajo);
		pw.println(valorMaximo);
		}catch (Exception e) {
            e.printStackTrace();
        } finally {
           try {
           // Nuevamente aprovechamos el finally para 
           // asegurarnos que se cierra el fichero.
           if (null != fichero)
              fichero.close();
           } catch (Exception e2) {
              e2.printStackTrace();
           }
		}
	}
		public static void main (String args[])throws IOException {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		int valores[];
		valores = new int[50];
		int valorMasBajo;
		valorMasBajo=100;
		int valorMasAlto;
		valorMasAlto=0;
		String texto;
		int i;
		for (i=0; i<5; i++){
			while (true){
			try{
			System.out.println("Introdueix valor "+i+":");
			texto = reader.readLine();
			valores[i] = Integer.parseInt(texto);
			break;
			}
			catch(Exception e4) {
            e4.printStackTrace();
				}
			}
			if (valorMasBajo>valores[i]){
				valorMasBajo=valores[i];
				}
			if (valorMasAlto<valores[i]){
				valorMasAlto=valores[i];
				}
		}
		escribirArchivo("/tmp/interval.bin",valorMasBajo,valorMasAlto);
		
		
	}
}

