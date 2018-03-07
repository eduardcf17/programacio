/*
 * sense títol.java
 * 
 *
 * 
 */

import java.io.*; 
public class cp {
	public static void copiar(String ruta,String ruta2)throws IOException {
		File archivo = new File(ruta);
		
		for (int i=0;true;i++){
			
			
			
			
			
			}
		
		
		
		}
		
public static void EscribirFichero (String ruta)throws IOException {
	File archivo = new File(ruta);
	BufferedWriter bw;
	if(archivo.exists()) {
		bw = new BufferedWriter(new FileWriter(archivo));
		bw.write("El fichero de texto ya estaba creado.");
	} else {
		bw = new BufferedWriter(new FileWriter(archivo));
		bw.write("Acabo de crear el fichero de texto.");
	}
	bw.close();
}





	public static void main(String[] args) throws IOException {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		String ruta = "/home/cf17eduard.corral/Documents/prueba1.txt";
		String ruta1 = "/home/cf17eduard.corral/Documents/prueba.txt";
		EscribirFichero(ruta,ruta1);

		
		
		
	}
}

