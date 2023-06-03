#Nos permite crear clases a partir de otras clases
#lo que da una gerarquia de padre he hijo
class Gato:
    def __init__(self,nombre,edad, raza, sexo):
        self.nombre=nombre
        self.edad=edad
        self.raza=raza
        self.sexo=sexo
    
    #Metodo
    def presentar (self):
        return print("Mi gato se llama ", self.nombre, " tiene ", self.edad," es de raza ",self.raza,
        " y es una ",self.sexo)
    
#Creamos una nueva instancia de la clase
gato2=Gato("Niña", 3, "mezcla", "hembra")
gato2.presentar()

#HERENCIA
#Es util cuando tengamos dos clases que se parezcan, pero tienen particularidades
class Animal:
    def __init__(self,especie,edad):
        self.especie=especie
        self.edad=edad
    def hablar(self):
        #metodo bacio
        pass

    def moverse(self):
        #metodo bacio
        pass
    def describeme(self):
        print("Soy un animal de tipo: ", type(self).__name__)
    
#clase perro, que hereda de la clase animal la especie y la edad
class Perro(Animal):
    pass
#instanciamos una clase heredada
mi_perro=Perro("Mamifero",4)
mi_perro.describeme()#R/: Soy un animal de tipo: Perro

#Sobrescribir metodos

class Perro(Animal):
    def hablar(self):
        print("Guau")
    def moverse(self):
        print("en cuatro patas")

class Vaca(Animal):
    def hablar(self):
        print("Muuuu")
    def moverse(self):
        print("4 patas")

class Abeja(Animal):
    def hablar(self):
        print("Bzzzz")
    def moverse(self):
        print("Volando")
    #Nuevo metodo
    #Abeja hereda los metodos de Animal y se le puede agregar mas metodos
    def picar(self):
        print("Picar")
    
    #Podemos tener tres tipos de objetos:
    #1: los heredados directamente
    #2: los que se heredan pero pueden alterarse los parametros
    #3: Los agregados

#A las clases nuevas les agregamos parametros
mi_perro=Perro("Mamifero", 10)
mi_vaca=Vaca("Mamifero", 20)
mi_abeja=Abeja("Insecto", 1)
#Llamamos a los objetos
mi_vaca.hablar()#Muuuuuu
mi_abeja.describeme()
mi_abeja.picar()

#Si queremos que perro tenga un parametro extra en el contructor, como: "el dueño"
#para hacerlo usamos "super" que invoca el contructor de la clase Animal, para agregarle
#el atributo "dueño"
class Perro(Animal):
    def __init__(self,especie,edad, dueño):
        super().__init__(especie,edad)
        self.dueño=dueño
nuevo_perro=Perro("Mamifero",7,"luis")
print(nuevo_perro.especie)
print(nuevo_perro.edad)
print(nuevo_perro.dueño)