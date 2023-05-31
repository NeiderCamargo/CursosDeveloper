package POO.Atributos;

public class MulAtributos {

    String nombre = "Neider";
    String apellido = "Camargo";
    int edad =18;

    public static void main(String[] args){
        MulAtributos persona = new MulAtributos();
        System.out.println("Su nombre es: "+persona.nombre+persona.apellido+ " y su edad es de: "+
        persona.edad+" años");
    }
}
