import os, shutil


if not os.path.isdir("./miCarpeta"):
    os.mkdir("./miCarpeta")
else :
    print("El directorio ya existe")

try:
    if os.path.isdir("./miCarpeta"):
        shutil.copytree("./miCarpeta", "./carpetaCopiada")
    else:
        print("El directorio a copiar no existe")
        
    print("Contenido de miCarpeta")
except:
    print("Ocurrio un error")
else:
    print("Todo funciono correctamente")
finally:
    print("fin de la iteracion")