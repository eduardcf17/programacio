/*
 * funcionesLeer.java
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
	
	
	public static void escribirArchivo(String ruta,int cuantasLineas,BufferedReader reader)throws IOException{
		FileWriter fichero = null;
        PrintWriter pw = null;
		try{
		fichero = new FileWriter(ruta);
		pw = new PrintWriter(fichero);
		for (int i = 0; i < cuantasLineas; i++){
			System.out.println("Escribe texto de linea "+i);
			String texto;
			texto=reader.readLine();
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
		String ruta;
		BufferedReader br = null;
		ruta=pedirRuta();
		br=abrirArchivo(ruta);
		leerArchivo(br);
		cerrarArchivo(br);
		int cuantasLineas;
		cuantasLineas=0;
		try{
			System.out.println("Escribe el numero de lineas");
			String texto;
			texto=reader.readLine();
			cuantasLineas = Integer.parseInt(texto);
			}
		catch(Exception e4) {
            e4.printStackTrace();
        }
		escribirArchivo(ruta,cuantasLineas,reader);
		
	}
}

