#Poli == muchas, morfismo== formas
#Puedo crear metodos con el mismo nombre pero diferente comportamiento
class Animal:
    def __init__(self, especie,edad, color):
        self.especie=especie
        self.edad=edad
        self.color=color
    def mePresento(self):
        print("Es una especie:",self.especie, " con la edad:",self.edad,
        " y el color:",self.color)
    def cumpliAños(self):
        self.edad=self.edad+1

a1=Animal("Perro", 4, "negro")
a2=Animal("Gato", 5, "blanco")

a1.mePresento()#nos muestra los valores asignados anteriomente
a2.mePresento()#nos muestra los valores asignados anteriomente
print()
#Llamamos el metodo cumplir años, pero no se muestra nada
a1.cumpliAños()
a1.cumpliAños()
#al repetir los metodos se nos muestra ahora si la edad mas un año
#aca se presenta el polimorfismo, pues llamanos a el metodo pero ahora con un año mas del
#que tenia cuando asignamos los valores de 4 y 5 años de edad
a1.mePresento()#5
a2.mePresento()#6