package Introducción.FUNCIONES;
public class Funciones {
    public static void main(String[] args) {
        /*Las funciones son agrupaciones de sentencias que pueden ser usadas en otro lugar */
        holaMundo();//IDENTIFICADOR DE LA FUNCIÓN
        //holaMundo("Alan");
        holaMundo(2);
        holaMundo("Neider");

        String hola=DevolverHola();
        System.out.print(hola);
       
    }
    /*Protected= solo clases hijas (que esten en el mismo paquete pueden invocar funciones)
     * Private= solo se puede invocar desde la clase que fue creada
     * public = se puede invocar fuera o dentro de la clase 
     */

     //La sobrecarga de metodos sucede cunado dos metodos tienen el mismo nombre
     //pero no funciona cuando dos o mas metodos tienen los mismos parametros
    public static void holaMundo() { //EL METODO QUE VAMOS A USAR PARA LLAMAR LA FUNCIÓN
        System.out.print("Hola Mundo");
        System.out.print("Hola Mundo");

    }

    private static void holaMundo(String name) {
        System.out.print("Hola "+name);
    }

    private static void holaMundo(Integer number) {
        System.out.print("El numero es "+number);
    }

    private static void holaMundo(String name, String surname) {
        System.out.print("Hola "+name+" "+surname);
    }

    //EN ESTE CASO PODEMOS DEVOLVER UN VALOR, ENTONCES DEBEMOS DECIR CUAL ES
    private static String DevolverHola() {
        return "Hola";
        //RETURN SE USA CUANDO DEBEMOS RETORNAR UN VALOR
    }
    private static int sum(int num1, int num2){
        return num1+num2;
    }
}
