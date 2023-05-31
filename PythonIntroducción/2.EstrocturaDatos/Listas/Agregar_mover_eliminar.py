#Asignar valores a una lista vacia
numeros = []
numeros.append(1)
numeros.append(2)
print(numeros)
#se pueden unir dos listas una bacia y otra llena para agregar elementos
numero = []
numero = numero + [10,20,30]
print(numero)

print()
print()
#remover un indice 
palabras = ["maduro", "hermano", "casa"]
palabras.pop(1)#remueve "hermano"
print(palabras)
#remover asignando un objeto de la lista
palabras.remove("casa")
print(palabras)