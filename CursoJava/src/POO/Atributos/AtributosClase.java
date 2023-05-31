package POO.Atributos;

public class AtributosClase {
    int x;
    // con el atributo (final) la variable no cambia de valor
    /*final*/ int y = 10;

    public static void main(String[] args) {
        AtributosClase atri = new AtributosClase();
        atri.x = 50; // se le agrega un valor al atributo llamado de la clase principal
        System.out.println(atri.x);// se lee ese atributo junto con el objeto

        // Tambien se puede cambiar el valor inicial
        AtributosClase atri2 = new AtributosClase();
        atri2.y = 100;// va a generar un error porque le asignamos un valor
        System.out.println(atri2.y);

        // Si crea múltiples objetos de una clase, puede cambiar los valores de atributo
        // en un objeto, sin afectar los valores de atributo en el otro:
    }
}
