package JavaTutorial;

public class Arreglos {
    
    public static void main(String[] args){
        String[] cars = {"volvo", "BMW", "Ford", "mazda"};
        int[] num = {1,2,3,4,5,6,7,8,9};

        //ACCEDER A LOS ELEMENTOS DEL ARRAY Y EXTRAERLO
        System.out.println(cars[0]);

        //CAMBIAR LOS ELEMENTOS DE UN ARREGLO
        cars[0] = "Opel";
        System.out.println(cars[0]);

        //LONGITUD DE UN ARREGLO
        System.out.println(cars.length);
    }
}
