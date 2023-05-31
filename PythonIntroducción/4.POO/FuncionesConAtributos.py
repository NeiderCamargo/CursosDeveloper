class Persona:
    def __init__(self, edad):
        self.edad=edad
    
    def mayor_edad(self):#Función que toma el atributo edad y devuelve un valor
        if self.edad >= 18:
            return True
        else:
            return False
p=Persona(20)
print(p.mayor_edad())