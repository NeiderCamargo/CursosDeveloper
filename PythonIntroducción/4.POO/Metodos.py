class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    #Creamos el metodo saludar
    def saludar(self):
        print("Hola " + self.nombre)
p=Persona("Juan") #Asignamos un nombre al parametro  
p.saludar()#ejecutamos 