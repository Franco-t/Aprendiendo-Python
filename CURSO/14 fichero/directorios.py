import os, shutil

#crear carpeta

if not os.path.isdir("./miCarpeta"):
    os.mkdir("./miCarpeta")
else :
    print("El directorio ya existe")

#eliminar carpeta
"""
if os.path.isdir("./miCarpeta"):
    os.rmdir("./miCarpeta")
else:
    print("El directorio no existe")
"""

if os.path.isdir("./miCarpeta"):
    if not os.path.isdir("./carpetaCopiada"):
        shutil.copytree("./miCarpeta", "./carpetaCopiada")
    else:
        print("El directorio ya existe")
else:
    print("El directorio a copiar no existe")
    
print("Contenido de miCarpeta")

contenido = os.listdir("./miCarpeta")

for ficheros in contenido:
    print(ficheros)