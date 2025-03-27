from io import open
import pathlib
import shutil


#abrir fichero
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open(ruta, "a+")

#escribir

archivo.write("Te amo Tami \n")

#cerrar 

archivo.close()

#abrir fichero
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta, "r")

#leer contenido

#contenido = archivo_lectura.read()

#print(contenido)

#leer contenido y guardarlo en una lista

lista = archivo_lectura.readlines()

archivo_lectura.close()

print (lista)
linea = 0
for frase in lista:
    print(f"Esta es la linea {linea}: --" + frase)
    linea = linea + 1
    
#copiar
"""
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_texto_Copia.txt"
shutil.copyfile(ruta_original, ruta_nueva)
"""


#mover
'''
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto_Copia.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copia_nueva.txt"

shutil.move(ruta_original, ruta_nueva)
'''
#eliminar

import os
'''
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copia_nueva.txt"
os.remove(ruta_nueva)
'''
#comprobar si existe

import os.path

#print(os.path.abspath("./"))

if os.path.isfile(os.path.abspath("./") + "/fichero_texto22.txt"):
    print("Si existe")
else:
    print("El archivo no existe")