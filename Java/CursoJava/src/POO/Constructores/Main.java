package POO.Constructores;

public class Main {
    int x;

    /*
     * Tenga en cuenta que el nombre del constructor debe coincidir con el nombre de
     * la clase y no puede tener un tipo devuelto (como ). void
     */

    // crear clase constructora
    public Main() {
        x = 5;// se inicializa el atributo de la clase principal
    }

    /*Tenga en cuenta también que se llama al constructor cuando se crea el objeto. */
    public static void main(String[] args) {
        Main objeto = new Main();
        System.out.println(objeto.x);
    }
}
