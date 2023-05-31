package introducción.clases;
//La clase abstracta nos permite impedir que la clase sea instanciada
//Solo puede ser instanciada desde las clases hijas 
public abstract class Car {
    
    //ATRIBUTOS
    String color;
    String fabricante;
    String modelo;
    double peso;
    double largo;
    Integer velocidad=0;
    //CONSTRUCTORES
    /*
     * El metodo constructor recibe unos parametros estos parametros son enviados desde 
     * fuera de la clase y se asignan a los objetos que se creen a partir de la clase
     * con la palabra "this"
     */
    public Car(){

    }
    public Car(String color, String fabricante, String modelo, double peso, double largo) {
        this.color = color;
        this.fabricante = fabricante;
        this.modelo = modelo;
    }
    //COMPORTAMIENTO == METODOS


    public void acelerar(Integer cantidad){
        if(cantidad>0 && cantidad <= 120){
            this.velocidad += cantidad;
        }
    }

    //DEVUELVE EL VALOR DE LAS PROPIEDADES Y PERMITE CREAR E IMPRIMIR OBJETOS
    @Override
    public String toString() {
        return "Car{" +
            " color='" + color + "'" +
            ", fabricante='" + fabricante + "'" +
            ", modelo='" + modelo + "'" +
            ", peso='" + peso + "'" +
            ", largo='" + largo + "'" +
            ", velocidad='" + velocidad + "'" +
            "}";
    }

   
    
}
