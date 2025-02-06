pelicula = ["iron man", "tranformers", "spider man"]
colores = list(("rojo", "verde", "azul"))
years = list(range(2000, 2025))
variada = ["victor", 30, 50.5, True, "Texto"]

print(pelicula)
print(colores)
print(years)
print(variada)

print(colores[0])
print(colores[-2])
print(colores[0:2])

colores.append("white")

print(colores)
contador = 0

print("\nEsto es con un contador\n")
for color in colores:
    print(f"El color {color} se encuentra en la posicion {contador}")
    contador += 1

print("\nEsto es con enumerate\n")

for lugar, color in enumerate(colores):
    print(f"El color {color} se encuentra en la posicion {lugar}")

productos = [
    ["Remera", "Roja"],
    ["Pantalon", "Azul"],
    ["Zapatilla", "Azul"],
]

print(productos)

for producto in productos:
    for color in producto:
        if producto.index(color) == 0:
            print(f"Producto: {color}")
        else:
            print(f"Color: {color}")

numeros = [1, 4, 7, 9, 5]

print(numeros)
# ordenar
numeros.sort()

print(numeros)
# agregar al final
numeros.append(3)

print(numeros)
# agregar al donde se indica
numeros.insert(3, 2)

print(numeros)
# remoevr con indice
numeros.pop(2)
print(numeros)

# remoevr indicando literalmente
colores.remove("rojo")
print(colores)

# dar la vuelta una lista
print(numeros)
numeros.reverse()
print(numeros)

# buscar dentor de una lista con in
print("azul" in colores)

# contar elementos
print(len(numeros))

# cuantas veces aparece un alemento en una lista

print(numeros.count(2))

# conseguir indice
print(numeros.index(2))

# unir listas
nuevalista = []

nuevalista.extend(numeros + colores)

print(nuevalista)
