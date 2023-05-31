package Metodos.Parametros_metodos;

public class Ejercicio {
    
    static void Permisos( int edad ){

        if(edad >=18){
            System.out.println("Ingrese por favor");
        }else{
            System.out.println("No puede ingresar");
        }
    }

    public static void main (String[] args) {
        Permisos(17);
    }
}