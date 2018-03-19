/*
 * llegeixinterval.java
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
public class llegeixinterval {
	public static BufferedReader abrirArchivo(String ruta){
	File archivo = null;
	BufferedReader br = null;
	try {
		// Apertura del fichero y creacion de BufferedReader para poder
		// hacer una lectura comoda (disponer del metodo readLine()).
		archivo = new File (ruta);
		br = new BufferedReader(new FileReader (archivo));
	}catch (IOException ex) {
			System.out.println(ex);
			}
		return br;
	}
	public static void leerArchivo(BufferedReader br)throws IOException{
		String linea;
		int contador;
		contador=0;
		while((linea=br.readLine())!=null){
			contador=contador+1;
			if(contador==1){
				System.out.print("El menor es: ");
				}
			if(contador==2){
				System.out.print("El mayor es: ");
				}
			System.out.println(linea);
			}
		}
	public static int diferencia(BufferedReader br)throws IOException{
		int diferencia;
		int diferencia1;
		diferencia1=0;
		int diferencia2;
		diferencia2=0;
		diferencia=0;
		String linea;
		linea="";
		String linea2;
		linea2="";
		
		linea=br.readLine();
		diferencia1 = Integer.parseInt(linea);
		
		
		
		linea2=br.readLine();
		diferencia2 = Integer.parseInt(linea2);
		
		
		diferencia=diferencia1-diferencia2;
		return diferencia;
		}
		
	public static void cerrarArchivo(BufferedReader br){
	   try{                    
            if(null!=br  ){   
               br.close();     
                }                  
         }catch (Exception e2){ 
            e2.printStackTrace();
         }
	   }
	
	public static void main (String args[])throws IOException {
	BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
	BufferedReader br = null;
	br=abrirArchivo("/tmp/interval.bin");
	leerArchivo(br);
	cerrarArchivo(br);
	br=abrirArchivo("/tmp/interval.bin");
	int diferencia;
	diferencia=diferencia(br);
	System.out.println("La difèrencia es: "+diferencia);
	
	}
}

