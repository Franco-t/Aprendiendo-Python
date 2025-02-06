# calcular porcentaje


def es_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False


seleccion = input("Queres carlcular el porcentaje de un numero? y/n \n")

while seleccion != "n":
    if seleccion != "n" and seleccion != "y":
        print('Debes de responder solamente con "y" o con "n"')
        seleccion = input("Queres carlcular el porcentaje de un numero? y/n \n")

    else:
        numero = input("Introduce el numero que quieres saber su porcentaje\n")
        porcentaje = input("Introduce el porcentaje que deseas conocer\n")
        while not es_numero(numero) or not es_numero(porcentaje):
            print("ambos numeros debe de ser numeros")
            numero = input("Introduce el numero que quieres saber su porcentaje\n")
            porcentaje = input("Introduce el porcentaje que deseas conocer\n")
        numero = float(numero)
        porcentaje = float(porcentaje)
        resultado = (numero * porcentaje) / 100
        print(f"{resultado}")
        seleccion = input("Queres carlcular el porcentaje de un numero? y/n \n")

print("Programa terminado")
