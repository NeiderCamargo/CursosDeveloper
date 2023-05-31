package JavaTutorial;

public class Conversión {

    public static void main(String[] args) {
        /*
         * La conversión de tipos es cuando se asigna un valor de un tipo de datos
         * primitivo a otro tipo.
         * Ampliación de la fundición (automáticamente): conversión de un tipo más
         * pequeño a un tamaño de letra mayor
         * byte -> short -> char -> int -> long -> float -> double
         */
        int num1 = 9;
        double num2 = num1;
        System.out.println(num1);
        System.out.println(num2);

        /*
         * Estrechamiento de la fundición (manualmente): conversión de un tipo más
         * grande a un tipo de tamaño más pequeño
         * double -> float -> long -> int -> char -> short -> byte.
         * 
         * El estrechamiento de la fundición debe hacerse manualmente colocando el tipo
         * entre paréntesis delante del valor:
         */

         double num3=9.78d;
         int num4= (int) num3;
         System.out.println(num3);
         System.out.println(num4);
    }
}
