class Empleado:
    def __init__(self,nombre,dni,salario,antiguedad):
        self.nombre=nombre
        self.dni=dni
        self.salario=salario
        self.antiguedad=antiguedad
    
    def mostrar(self):
        print("Nombre:",self.nombre)
        print("dni:",self.dni)
        print("Salario:",self.salario)
        print("Antiguedad:",self.antiguedad)
    
    def cal_salario(self):
        impuesto = 0.1 * self.salario - 0.01 * self.antiguedad * self.salario
        salarioNeto=self.salario-impuesto
        return salarioNeto  
    
e1=Empleado("Neider", "1010", 120, 20,)
e1.mostrar()

print("Salario Neto:",e1.cal_salario())
