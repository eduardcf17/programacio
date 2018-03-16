/*
 * funcionesLeer.java
 * 
 * Copyright 2018 edu <edu@edu-HP-Pavilion-15-Notebook-PC>
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

public class funcionesLeer{
	public static String pedirRuta()throws IOException{
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		System.out.println( "On esta el fitxer");
		String ruta;
		ruta=reader.readLine();
		return ruta;
	}
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
         while((linea=br.readLine())!=null){
			System.out.println(linea);
			}
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
		String ruta;
		BufferedReader br = null;
		ruta=pedirRuta();
		br=abrirArchivo(ruta);
		leerArchivo(br);
		cerrarArchivo(br);
		
	}
}

