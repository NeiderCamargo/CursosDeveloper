#la biblioteca estan organizadas en un directorio que contiene varios archivos de modulo
#y se usan juntos para proporcionar funciondalidades mas complejas
import math
x=16
raiz_cuadrada=math.sqrt(x)
print(raiz_cuadrada)#4.0

#Aca importaremos el modulo creado
#import mimodulos

#print(mimodulos.suma(4,3))
#print(mimodulos.resta(5, 4))

#Ahora podemos importar el modulo en un lugar especifico del codigo
#importar solo una biblioteca del modulo
from mimodulos import suma
print(suma(20,20))

#importar todo el modulo
from mimodulos import *
print(resta(20, 10))

