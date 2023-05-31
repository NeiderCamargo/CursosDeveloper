package POO.Metodos;

public class AccesoObjeto {
    
     // Create a fullThrottle() method
     public void fullThrottle(){
        System.out.println("Metodo full throttle");
     }
      // Create a speed() method and add a parameter
      public void speed(int maxSpeed){
        System.out.println("Metodo speed is: " + maxSpeed);
      }

      public static void main(String[] args){
        //Ahora podemos acceder a varios metodos con un solo objeto creado 
        AccesoObjeto objeto = new AccesoObjeto();
        objeto.fullThrottle();
        objeto.speed(200);
      }
}
