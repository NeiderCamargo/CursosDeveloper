package POO.Clases;

public class Llamar {
     //CREAR OBJETOS DE LA CLASE 
    public static void main(String[] args) {

        Main myObject = new Main();//Objeto de una clase
        Main myObject2 = new Main();
        System.out.println(myObject.x); //con x(.) podemos acceder a el atributo de la clase
        System.out.println(myObject2.x);
    }
}
