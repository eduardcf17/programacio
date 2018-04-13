/*
 * copia archivos
 * 
 *
 * 
 */
import java.io.*;

class projecto2S {
   public static void main(String [] arg) {
	  BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
      File archivo = null;
      FileWriter fichero = null;
      PrintWriter pw = null;
      BufferedReader br = null;
      File archivoCopia = null;
      System.out.println("entrando");
      String sql;
      sql="";
      String nombre;
      nombre="";
      try {
         // Apertura del fichero y creacion de BufferedReader para poder
         // hacer una lectura comoda (disponer del metodo readLine()).
         System.out.println("Escribe el nombre del archivo");
         nombre=reader.readLine();
         archivo = new File (nombre);
         sql=nombre+".sql";
         archivoCopia = new File (sql);
         br = new BufferedReader(new FileReader (archivo));
         String linea;
         pw = new PrintWriter(new FileWriter (archivoCopia));
         linea=br.readLine();
			System.out.println(linea);
		
		
		
		pw.println("SET AUTOCOMMIT=1;");
		pw.println("CREATE DATABASE IF NOT EXISTS projecto2 charset latin1;");
		pw.println("USE projecto2;");
		pw.println("CREATE TABLE IF NOT EXISTS project.TABLA (");
		
		
         // Lectura del fichero
         
         int contador;
         contador=0;
         
         
       
		
		String [] valor=linea.split("\t");
		int i;
		int maximo;
		maximo=valor.length;
		for (i=0;i<maximo;i++){
			pw.println(valor[i]+" VARCHAR(20),");
			}
         
         
         
         
         
         
            
      }
      catch(Exception e){
         e.printStackTrace();
      }finally{
         // En el finally cerramos el fichero, para asegurarnos
         // que se cierra tanto si todo va bien como si salta 
         // una excepcion.
         try{                    
            if( null != pw && null!=br  ){   
               br.close();     
               pw.close();     
               
            }                  
         }catch (Exception e2){ 
            e2.printStackTrace();
         }
      }
     
   }
}

