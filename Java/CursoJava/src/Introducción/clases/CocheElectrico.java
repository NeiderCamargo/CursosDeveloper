package introducción.clases;
/*
 * Extends nos permite heredar las caracteristicas de una clase
 */
public class CocheElectrico extends Car{
    //AGREGAMOS UN NUEVO OBJETO QUE SOLO PERTENECE A LA CLASE NUEVA
    String motorEelectrico;

    public CocheElectrico(){

    }
    public CocheElectrico(String motorEelectrico){
        this.motorEelectrico = motorEelectrico;
    }

    public CocheElectrico(String color, String fabricante, String modelo,
    double peso, double largo, String motorElectrico){
        //super: nos permite llamar un contructor de la clase principal
        super(color, fabricante, modelo, peso, largo);
        //luego asignamos el nuevo valor a la clase principal
        this.motorEelectrico=motorElectrico;
    }
    /*sobre escribir metodos: nos permite modificar un metodo heredado de la clase
     * principal
     */
    @Override
    public void acelerar(Integer cantidad){
        Integer cantidadAjustada=cantidad*2;
        super.acelerar(cantidadAjustada);
    }
    
    @Override//valora si el metodo existe en la clase principal
    public String toString() {
        return "CocheElectrico{" +
            " color='" + color + "'" +
            ", fabricante='" + fabricante + "'" +
            ", modelo='" + modelo + "'" +
            ", peso='" + peso + "'" +
            ", largo='" + largo + "'" +
            ", velocidad='" + velocidad + "'" +
            ", motorEelectrico='" + motorEelectrico + "'" +
            "}";
    }
}
