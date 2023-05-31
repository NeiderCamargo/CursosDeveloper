package JavaTutorial;

public class ArreglosBucles {

    public static void main(String[] args) {
        /*
         * Puede recorrer los elementos de matriz con el bucle y utilizar la propiedad
         * para especificar cuántas veces debe ejecutarse el bucle.forlength
         */

        String[] cars = { "volvo", "BMW", "Ford", "mazda" };
        for (int i = 0; i < cars.length; i++) {
            System.out.println(cars[i]);
        }

        /*
         * También hay un bucle "for-each", que se utiliza exclusivamente para
         * recorrer elementos en matrices:
         */

         for(String i: cars){
            System.out.print(i);
         }
    }
}
