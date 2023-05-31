package JavaTutorial;

public class ArreglosMultidimencionales {
    
    public static void main(String[] args){

        int [] [] numeros = {{1,2,3}, {4,5,6}};
        System.out.println(numeros [1] [2]);
        /*
         * Se recorre primero la matriz principal, colocamos [1] para seleccionar la segunda matriz,
         * luego se selecciona la posición del elemento de la segunda matriz [2]
         */

         //Cambiar poosiciones de la matriz 
         numeros [1][2] = 9;//se asigna recorriendo la matriz como en el paso anterior
         System.out.println(numeros [1][2]);

         //bucle atravez de la matriz
         for (int i=0; i<numeros.length; i++){
            for (int j=0; j<numeros[i].length; j++){
                System.out.println(numeros[i][j]);
            }
        }
    }  
}
