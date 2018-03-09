/*
 * copia archivos
 * 
 *
 * 
 */
import java.io.*;

class cp {
   public static void main(String [] arg) {
      File archivo = null;
      FileWriter fichero = null;
      PrintWriter pw = null;
      BufferedReader br = null;
      File archivoCopia = null;
      System.out.println("entrando");
      try {
         // Apertura del fichero y creacion de BufferedReader para poder
         // hacer una lectura comoda (disponer del metodo readLine()).
         archivo = new File ("/home/cf17eduard.corral/Documents/prueba.txt");
         archivoCopia = new File ("/home/cf17eduard.corral/Documents/prueba1.txt");
         br = new BufferedReader(new FileReader (archivo));
         pw = new PrintWriter(new FileWriter (archivoCopia));
         

         // Lectura del fichero
         String linea;
         while((linea=br.readLine())!=null){
            pw.println(linea);
			System.out.println(linea);
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

