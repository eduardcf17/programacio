


import java.io.*;
public class mayus {
    
		
	public static String capitalize(String nombre){
		char[] caracteres = nombre.toCharArray();
		caracteres[0] = Character.toUpperCase(caracteres[0]);
		for (int i = 0; i < nombre.length(); i++) 
			if (caracteres[i] == ' '){
				caracteres[i + 1] = Character.toUpperCase(caracteres[i + 1]);}
		String palabra2;
		palabra2=new String(caracteres);
		return palabra2;
		}
	
	
	
	
	
	
	
	
	
	
	public static void main (String[] args) throws IOException  {
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
	
	System.out.println("Escribe tu nombre");
	String texto;
	texto=reader.readLine();
	String palabraMayus;
	palabraMayus=capitalize(texto);
	System.out.println(palabraMayus);
	}
}

