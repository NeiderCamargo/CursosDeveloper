#SE USA ESPECIALMENTE PARA LISTAS
lista=["Pagina1", "pagina2", "pagina2"]
marcapaginas=iter(lista)#con esto asignamos el recorrido de la lista a una variable

#cada pagina se muestra de manera secuencial tal y como esta ordenada en la lista
print(next(marcapaginas))
print(next(marcapaginas))
print(next(marcapaginas))