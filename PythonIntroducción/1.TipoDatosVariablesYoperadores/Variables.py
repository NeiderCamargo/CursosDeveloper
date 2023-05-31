#Asignación de variables
mi_texto = "hola"
mi_numero = 134
#imprimir valores
print(mi_texto)
print(mi_numero)

#Reasignación de valores a variables
mi_text = "Hola de nuevo"
variable_mixta = "texto"
mi_num = 506

#ahora Reasignacións valores
mi_text = "nuevo texto"
mi_num = 9999
variable_mixta = 12.5
nueva_variable = mi_num

print(mi_text)
print(mi_num)
print(variable_mixta)
print(nueva_variable)
print()
print()
#lecturas de numeros 

#leemos el primer numero
numero1=input("Ingrese un numero")
#leemos el segundo numero
numero2=input("Ingrese un numero")
#en este punto ambos numeros son string(debemos convertirlos)
numero1=int(numero1)#vuelve la variable numero1 en un entero con "int"
numero2=floar(numero2)
print(numero1, "+", numero2, "=", numero1+numero2)