#Crea una clase Persona que tenga dos atributos privados: nombre y edad, y un método público
#  presentarse, que imprima el nombre y la edad de la persona. Además, crea dos métodos públicos:
#  cambiar_nombre y cambiar_edad, que permitan modificar los atributos privados de la persona.

class Persona:
    def __init__(self,nuevo_nombre, nueva_edad):
        self._nombre=nuevo_nombre
        self._edad=nueva_edad
    
    def presentarse(self):
        print("Ni mombre es:",self._nombre, " y mi edad es:",self._edad)

    def cambio_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    
    def cambio_edad(self,nueva_edad):
        selfueva_edad._edad = n

a1=Persona("Neider", 10)
print(a1.presentarse())

a1.cambio_nombre("fabian")
a1.cambio_edad(20)

print(a1.presentarse())

