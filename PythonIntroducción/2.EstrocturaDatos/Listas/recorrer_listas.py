numeros=[1,2,3,4,5,6,7,8,9,10,11,12]

#recorrer los elementos
for lista in numeros:
    print(lista)

#recorrido de indices con numeros enteros
for i, numero in enumerate(numeros):
    print("El numero es el indice:",i, "es:", numero)

#recorrido de indices con strings
lista = ["Hola", "mundo"]
for i in range(len(lista)):
    print("El numero es el indice:",i, "es:", lista[i])

#con while y los indices
indice = 0
while indice < len(numeros):
    print(numeros[indice])
    indice = indice + 1
