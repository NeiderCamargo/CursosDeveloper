#Declaración de la función
#def nombre_funcion(parametro, nombre_parametro):
    #parametros de la función
    #return valor, otro_valor

#ejemplo
def sumar(): #sin parametros
    a=50
    b=10
    return a+b 

resultado=sumar()
print(resultado)

#función con parametro
def caracter(n):
    if n==0:
        return "a"
resul=caracter(0)
print(resul)
print()
#con dos parametros
def mensaje(n, mensaje):
    if (n==0):
        print(mensaje)
        return 1 
    return 0
resulta= mensaje(0, 'bienvenido')
print(resulta) 

