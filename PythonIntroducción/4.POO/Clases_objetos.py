class Persona:
    #el constructor _init_para inicializar los atributos de la clase
    def __init__(self, nombre, edad, dirección, estatura, uso_lentes):
    #el constructor toma como refe a self, que se refiere al objeto que se esta creando
    #si no se coloca self el objeto no podra acceder a sus propios atributos o metodos
        self.nombre = nombre
        #se le asigna un valor al atributo de la clase .nombre=nombre
        #self se usa para referirse al objeto de la clase
        self.edad = edad
        self.dirección = dirección
        self.estatura = estatura
        self.uso_lentes = uso_lentes
#creamos un objeto de la clase persona y asignamos valores a los atributos
p1=Persona("Neider", 23, "avenida1", 186, False)
print(p1.nombre, p1.edad, p1.dirección, p1.estatura, p1.uso_lentes)