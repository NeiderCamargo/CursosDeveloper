package POO.Encapsulamiento;

/*El significado de Encapsulación, es asegurarse de que los datos "sensibles" están ocultos de los usuarios.
 Para lograr esto, debes: 
 Declare variables/atributos de clase como private
Proporcionar métodos públicos GET y Set para obtener acceso y actualizar el valor de una variableprivate
*/

public class Encapsulamiento {

    private String name;

    // Getter
    public String getName() {
        return name;// El método devuelve el valor de la variable .getname
    }

    // Setter
    public void setName(String newName) {
        this.name = newName;
        // El método toma un parámetro () y lo asigna a la variable. La palabra clave se
        // utiliza para referirse a la corriente objeto.setnewNamenamethis
    }
}
