#ITERAR LISTAS
lista=[1,2,3,4,5]
#for elemento in clase iterable
for elemento in lista:#la variable elemento toma los valores de la clase
    print(elemento)#se muestran todos los elementos de la lista
print()

#ITERAR CADENAS DE TEXTO
cadena="NEIDER"
for elemento in cadena:
    print(elemento)
print()
#enumerar la posición 
for c in enumerate(cadena):#enumerate agrega el indice de cada caracter
    print(c)

#SABER SI UNA CLASE ES ITERABLE
from collections.abc import Iterable
cadena="NEIDER"
numero=9
print (isinstance(cadena, Iterable))#true

#Convertir texto en lista
print(list("NEIDER"))
#sumar numeros
print(sum([1,2,3,4,5]))

#SEPARAR LOS DATOS
print("-".join ("NEIDER"))
