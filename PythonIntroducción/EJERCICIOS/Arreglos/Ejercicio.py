#Suma de elementos: Dado un arreglo de números enteros, debes encontrar la suma de todos sus elementos.
sumar_numeros=[1,2,3,4,5]#creamos el arreglo
def suma_elementos(sumar_numeros):#def definimos una función, en este caso el arreglo
    suma=0#creamos la variable que almacene el resultado
    for elemento in sumar_numeros:#recorremos el arreglo
        suma += elemento #sumamos el arreglo
    return suma #retornamos el valor de la suma

resultado=suma_elementos(sumar_numeros)#asignamos a una variable la función asignada
print(resultado) #se imprime el resultado

#2
arreglo_dupli=[1,1,2,3,4,5]# se crea el arreglo
def elementos_duplicados(arreglo_dupli):#definimos una función del arreglo

    duplicados=[]#aca se guarda los numeros repetidos

    for i in range(len(arreglo_dupli)):#se recorre el arreglo

        for j in range(i +1, len(arreglo_dupli)):#comparamos los datos

            #si el arreglo i == al arreglo j entonces e igual entonces va al arreglo de duplicados
            if arreglo_dupli[i]==arreglo_dupli[j] :

                duplicados.append(arreglo_dupli[i])#se guarda el numero duplicado
    return duplicados#se retornan los duplicados

resultado2=elementos_duplicados(arreglo_dupli)#se asigna los numeros a una variable
print(resultado2)#se muestran los resultados 

