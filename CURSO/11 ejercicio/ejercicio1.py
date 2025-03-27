"""
ejercicio 1: programa de lista con 8 numeros, y que realice lo siguiente
-recorrer la lista y mostrarla
-hacer una funcion que muestre la lista 
-ordenar y mostrar la lista
-mostrar su longitud
-buscar elemento por teclado
"""
def mostrarLista (listaMostrar):
    texto = ""
    for elemento in listaMostrar:
        texto = texto + str(elemento) + "\n"
    return texto

def ordenarLista(listaOrdenar):
    listaOrdenar.sort()
    
lista = [22,8,4,6,10,15,20,9]

for elemento in lista:
    print(elemento)

print("\nSe muestra lista mediante funcion")
print(mostrarLista(lista))

print("\nSe muestra lista ordenada")
ordenarLista(lista)
print(mostrarLista(lista))

print(f"La lista tiene: {len(lista)} elementos")

print("Quieres buscar un numero en la lista? yes/no")
opcion = input("Solo introduce y/n: ")

while opcion != "n":
    if opcion != "n" and opcion != "y":
        opcion = input ('Solamente podes ingresar un "n" o "y"')
    else:
        numeroBuscar = input("Introduce el numero a buscar en la lista: ")
        while not numeroBuscar.isdigit():
            numeroBuscar = input("Por favor introduci un numero: ")
        numeroBuscar = int (numeroBuscar)
        if numeroBuscar in lista:
            print(f"El elemento {numeroBuscar} se encuentra en la lista, en la poscicion {lista.index(numeroBuscar)}")
            opcion = input ('Quieres volver a buscar un numero en la lista? y/n: ')
        else:
            print(f"El elemento {numeroBuscar} NO se encuentra en la lista")
            opcion = input ('Quieres volver a buscar un numero en la lista? y/n: ')
print("Programa terminado")