package introducción.clases;

public class  CarMain {

  public static void main(String[] args) {
    // CREAR OBJETOS: LO QUE HACEMOS ES LLAMAR LOS PARAMETROS QUE HEMOS ASIGNADO AL
    // CONTRUCTOR
    // Clase /Objeto
    // Car cocheObjeto = new Car();
    // AL ASIGNAR LOS PARAMETROS ESTAMOS INSTANCIANDO UNA CLASE
    Car CocheObjeto2 = new Car("rojo", "hinda", "civic", 1430.54, 5.5);

    // LLAMAR OBJETO
    CocheObjeto2.acelerar(50);
    System.out.println(CocheObjeto2);

    // CREAR NUEVO OBJETO PARA LA CLASE COCHEELECTRICO
    CocheElectrico cocheEle = new CocheElectrico();

    cocheEle.motorEelectrico = "Ejemplo motor";
    cocheEle.color = "verde";
    cocheEle.fabricante = "Honda";
    cocheEle.modelo = "98";
    System.out.println(cocheEle);

    /*
     * METODOS SUPER: nos permite transladar el contructor del la clase principal
     * a un objeto creado de una clase que hereda parametros de la clase principal
     */
    CocheElectrico cocheEle2 = new CocheElectrico("azul", "alfa",
        "romeo", 1500d, 4.99, "TXTZ");

        System.out.println(cocheEle2);
        //EJECUTAR EL METODO SOBRESCRITO
        cocheEle2.acelerar(50);
        System.out.println(cocheEle2);

  }
}
