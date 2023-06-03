lista_num=[1,2,3,4,5,6]
#necesitamos que multiplique solo los numeros pares *2
pares_x_dos=[x*2 for x in lista_num if x%2==0]
print(pares_x_dos)

#Ahora vamos a ver cuantas "r" hay en una cadena string
lista_letras="Mi perro es muy divertido por consentido"
letras_r=[i for i in lista_letras if i=="r"]
print(letras_r)
print(len(letras_r))