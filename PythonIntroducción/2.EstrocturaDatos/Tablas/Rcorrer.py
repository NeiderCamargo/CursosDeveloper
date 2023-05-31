nombre_tabla=[["juan", "laura"],[21,32]]

#accedemos a las filas
for fila in nombre_tabla:
    #accedemos a las columnas
    for columna in fila: 
        #imprimimos la columna
        print(columna)
print()
#recorriendo indices y mostrar el objeto de cada indice
for i in range(len(nombre_tabla)):
    for j in range(len(nombre_tabla[i])):
        print(nombre_tabla[i][j])
        print("indice fila:",i)
        print("indice columna:",j)
print()
print()
#con while y los indices
fila =0
while fila < len(nombre_tabla):
    columna =0
    while columna <len(nombre_tabla):
        print(nombre_tabla[fila][columna])
        print("indice fila:",fila)
        print("indice columna:",columna)
        columna +=1 
        fila +=1