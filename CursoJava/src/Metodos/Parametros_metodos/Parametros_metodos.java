package Metodos.Parametros_metodos;

public class Parametros_metodos {

    // MULTIPLES PARAMETROS

    // FORMAS DE UNIR DOS TEXTOS, UNO QUE NOS DA EL PROGRAMA Y OTRO QUE
    // SELLECIONAMOS NOSOTROS

    public static void MyMetodo(String frame, int edad) {
        // El siguiente ejemplo tiene un método que toma un String llamado fname como
        // parámetro. Cuando se llama al método, pasamos un nombre, que se utiliza
        // dentro del método para imprimir el nombre completo:
        System.out.println(frame + "tiene " + edad + " años");
    }

    public static void main(String[] args) {
        MyMetodo("Neider ", 5);
        MyMetodo("Paola ", 8);

    }
    // Cuando un parámetro se pasa al método, se llama un argumento. Entonces, del
    // ejemplo anterior: fname es un parámetro, mientras Liam, Jenny y Anja son
    // argumentos.
}
    
    



