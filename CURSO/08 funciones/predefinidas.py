nombre = "   mi nombre es Franco   "

print(nombre)

print(type(nombre))

# detectar tipado

print(isinstance(nombre, str))

print(isinstance(nombre, int))

print(nombre.strip())

# comprobar variable vacia

if len(nombre) == 0:
    print("variable vacia")
else:
    print(f"La variable tiene contenido, tiene {len(nombre)} caracteres")

print(f"{nombre.find("Franco")}")

nombre = nombre.replace("Franco", "Tamara")

print(f"{nombre}")
