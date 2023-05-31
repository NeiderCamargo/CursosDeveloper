#crear diccionario
nombre_diccionario ={}
otro_diccionario = {
    "nombre": "alberto",
    "usuario": "alba_123",
}

#mostrar elementos
mi_diccionario = {
    "nombre": "juan",
    "edad": "23",
    "usuario": "j123",
}
print(mi_diccionario["nombre"])
print(mi_diccionario["usuario"])
print()
#recorrer diccionario
for llave in mi_diccionario:
    print(llave, ":", mi_diccionario[llave], sep="")    