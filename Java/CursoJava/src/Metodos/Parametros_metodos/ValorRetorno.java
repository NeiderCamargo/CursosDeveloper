package Metodos.Parametros_metodos;

public class ValorRetorno {
    
    // VALORES DE RETORNO
    /*
     * los void la palabra clave, utilizada en los ejemplos anteriores, indica que
     * el método no debe devolver un valor. Si tu desea que el método devuelva un
     * valor, puede usar un tipo de datos primitivo ( como int, char, etc. ) en
     * lugar de void, y usa el return palabra clave dentro del método:
     */
    
     static int MyMetodo( int x){
        return x + 5;
     }

     public static void main( String[] args ){
        System.out.println(MyMetodo(3));
     }
}
