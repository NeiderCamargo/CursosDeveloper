class Vehiculo:
    def __init__(self,marca, modelo,color):
        self.marca=marca
        self.modelo=modelo
        self.color=color
    
    def mostrar(self):
        print("Marca:",self.marca)
        print("Modelo:",self.modelo)
        print("Color:",self.color)
    
a1=Vehiculo("ford", "fiesta", "verde")
a1.mostrar()