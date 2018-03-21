/*
 * projecto2.java
 * 
 */


public class sense títol {
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
	
	
	public static void escribirArchivo(String ruta,BufferedReader reader)throws IOException{
		FileWriter fichero = null;
        PrintWriter pw = null;
		try{
		fichero = new FileWriter(ruta);
		pw = new PrintWriter(fichero);
		
		pw.println( texto +" Numero de linea: "+i);
			
		}
		} catch (Exception e) {
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
	System.out.println("Escribe el nombre del archivo");
	String nombre;
	nombre=reader.readLine();
		
	}
}








SET AUTOCOMMIT=1;

CREATE DATABASE IF NOT EXISTS sanitat charset latin1;

USE sanitat;

CREATE TABLE IF NOT EXISTS sanitat.HOSPITAL (
