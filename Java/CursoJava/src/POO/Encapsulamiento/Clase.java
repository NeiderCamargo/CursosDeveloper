package POO.Encapsulamiento;

public class Clase {
    public static void main(String[] args){
        Encapsulamiento objeto = new Encapsulamiento();
        objeto.setName("John");//llamamos al metodo set y agregamos el nombre
        System.out.print(objeto.getName());//llamando al metodo get se imprime el valor asignado
    }
}
