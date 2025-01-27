nada = None
cadena = "Hola soy una cadena de tipo string"
entero = 99
flotante = 4.2
booleano = True
lista = [10, 20, 30, 100, 200]
listaString = [44, "treinta", 30, "cuarenta"]
tuplaNoCambia = ("Franco", "Gimenez")
diccionario = {
    "nombre": "Franco",
    "apellido": "Gimenez",
}
rangos = range(9)
dato_BYTE = b"Probando"

print(nada)
print(cadena)
print(entero)
print(flotante)
print(booleano)
print(lista)
print(listaString)
print(tuplaNoCambia)
print(diccionario)
print(rangos)
print(dato_BYTE)

print(type(nada))
print(type(cadena))
print(type(entero))
print(type(flotante))
print(type(booleano))
print(type(lista))
print(type(listaString))
print(type(tuplaNoCambia))
print(type(diccionario))
print(type(rangos))
print(type(dato_BYTE))

# Convertir tipos

print(cadena + " " + str(entero))
print(int(flotante))
print(float(entero))