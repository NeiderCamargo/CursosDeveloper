package introducción.clases;

public class PolimorfismoMain {
    
    public static void main(String[] args) {

        CocheElectrico coche1=new CocheElectrico();

        //Polimorfismo: nos permite trabajar de manera general con la clase
        //podemos saber la clase principal y la que hereda

        Car coche2= new CocheElectrico();
        
        //Si queremos saber el objeto a que clase pertenece 
        if(coche2 instanceof Car){
            System.out.println("coche");
        }
        if(coche2 instanceof CocheElectrico){
            System.out.println("CocheElectrico");
        }
        
        
    }
}
