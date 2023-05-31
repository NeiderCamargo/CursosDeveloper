package introducción.Break_Continue;

public class Clase1 {
    public static void main(String[] args) {
        int count=0;
        while(count<10){
            count++;//CADA ITERACIÓN QUEDA REGISTRADA EN ESTA VARIABLE
            if(count==6){
                //continue;//SALTA DEL NUMERO 5 AL 7
                break;//ROMPE EL FLUJO DE EJECUCIÍON
            }

            System.out.println("Hola Mundo"+count);
        }
    }
}
