package JavaTutorial;

public class Cadenas {

    public static void main(String[] args) {
        String holaMundo = "'hola' Mundo";
        /*
         * Una cadena en Java es en realidad un objeto, que contiene métodos que pueden
         * realizar ciertas operaciones en cadenas. Por ejemplo, la longitud de una
         * cadena se puede encontrar con el método:length()
         */
        System.out.println(holaMundo.length());//Cantidad de caracteres 
        System.out.println(holaMundo.toUpperCase());//TEXTO EN MAYUSCULA
        System.out.println(holaMundo.toLowerCase());//texti en minuscula

        //ENCONTRAR LA POSICIÓN DE UNA (FRASE) EN UN TEXTO, QUE ESTE ENTRE COMILLAS SIMPLES
        System.out.println(holaMundo.indexOf("hola"));
    }
}
