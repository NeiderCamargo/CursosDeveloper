#POTENCIACIÓN
print (5**2) #25

b= 2
a= 3
print (b ** a) #8

#DIVISIÓN
print(10/3) # 3.3333333333333335
print (10//3) #3 

#MODULO
7%2 #7/2=3 y el resto es igual a 1 

#numeros pares cuyo resto es cero
print(6%2), print(12%2), print(44%2) # =0

#OPERACIONES DE ASIGNACIÓN
x=10
x+=5 #es como escribir x = x + 5
print(x) #15 
#x-=5 # resta
#x*=5 # multipliación
#x/=5 # división
#x//=5 # división
xx=10
xx%=3
print(xx) #1

y=10
y**=2
print(y) #100

#String
print("Neider "*3) #repite tres veces el string
print()
#OPERADORES LOGICOS
#A y AND, ambos valores deben ser true, para que sea true. Y ambos tienen que ser 
#false para que sea false. 
print(True and True)#true
print(True and False)#false
print()
#A OR B. El valor de la derecha define si es true o false, el de la izquierda no.
#true or false= true. False or false = false
print(True or False) #tue
print(True or True)#true
print(False or False) #false
print(False or True) #true

#not= invierte el true y el false
print(not True)#false
print(not False)#true
print()
#or extendido
#Si los dos valores son true, el resultado es false
#si los dos valores son false, el resultado es false
a=bool(1)#true
b=bool(0)#false
print(a ^ b)