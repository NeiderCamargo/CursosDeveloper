#esta ruta funciona cuando el moodulo esta en una subcarpeta, de la carpeta donde vamos a importar
#el modulo
#dirección de la carpeta donde esta el modulo:
#navegarDirectorio/explorar.explorar

#Directorio de la carpeta donde vamos a importar
#NavegaciónDirectorio
   # -explorar
   # -navegar.py

from  explorar.explorar import *
print(hola())

#importar desde otras hubicaciones
import sys
sys.path.append(r'ruta/del/modulo')

#renombrar modulo
import moduloconnombrelargo as m
print(m)
