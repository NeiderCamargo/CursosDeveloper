package POO.Metodos;

public class PubEstatic {

    /*
     * A menudo verá programas Java que tienen static o public atributos y métodos.
     * 
     * En el ejemplo anterior, creamos un static método, lo que significa que se
     * puede acceder sin crear un objeto de la clase, diferente public, al que solo
     * se puede acceder objetos:
     */

     //static metodo
     static void StaticM(){
        System.out.println("Metodo estatico:");
     }
     
     //public metodo
     public void PublicM(){
        System.out.println("Metodo publico:");
     }

     public static void main(String[] args){
        StaticM(); /*El metodo statico se puede acceder sin necesidad de crear un objeto de la clase */
        //PublicM();

        PubEstatic Obj1=new PubEstatic();
        Obj1.PublicM();
       
     }
}
