package POO.Constructores;

public class ConParametros {
    int x=5;

    public  ConParametros (int y ){//Se le agrega un parametro al constructor
        x=x+y;//vamos a sumar el parametro de la clase y el del constructor
    }

    public static void main(String[] args){
        ConParametros objeto = new ConParametros(5);//se le asigna un valor a y, atributo del constructor
        System.out.println(objeto.x);
    }
}
