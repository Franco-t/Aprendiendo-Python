"""
ejercicio4.
crear un codigo que tenga 4 variables, una lista, un string,
un entero y un booleano y que imprima un mensaje
segun el tipo de dato de cada variable. Usar funciones
"""

def comprobadorTipo(dato, tipo):
    tipoDato = isinstance (dato, tipo)
    texto =""
    if tipoDato:
        texto = f"El {dato} es un tipo {tipo}"
    else:
        texto = f"El {dato} NO es un tipo {tipo}"
    return texto
    
miLista = ["Tamara", "Franco"]
numero = 22 

print(comprobadorTipo(miLista, list))