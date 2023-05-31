package Metodos;

public class SobreCargaMetodos {

    // Con sobrecarga del método, múltiples métodos pueden tener el mismo nombre con
    // diferentes parámetros:

    static int plusMetodo(int x, int y){
        return x + y;
    }
    static double plusMetodo(double x, double y){
        return x + y;
    }

    public static void main(String[] args){
        int myInt = plusMetodo(4, 5);
        double myDouble = plusMetodo(5.2,4.5);
        System.out.println("Int "+myInt);
        System.out.println("Double "+myDouble);
    }
}
