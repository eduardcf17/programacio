/*
 * copia archivos
 * 
 *
 * 
 */
import java.io.*;

class palabrasEnLinea {
	
	
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
   
public static void main(String [] arg)throws IOException {
      String ruta;
      BufferedReader br = null;
      ruta=pedirRuta();
      br=abrirArchivo(ruta);
      leerArchivo(br);
      cerrarArchivo(br);
     
   }
}

