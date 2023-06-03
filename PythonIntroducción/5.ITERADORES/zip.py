#Zip permite convinador dos o mas iterables en una misma estroctura
#si tenemos dos listas con zip podemos combinarlas en una lista de tuplas
lista1=[1,2,3]
lsita2=["a", "b", "c"]
convinador=zip(lista1,lsita2)#agregamos ambos arreglos a la variable convinador
print (type(convinador))#ver que tipo de dato es

#recorrer arreglo y mostrar
for elemento in convinador:
    print(elemento)