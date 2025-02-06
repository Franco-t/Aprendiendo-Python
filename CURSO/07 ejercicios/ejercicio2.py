# numeros pares entre dos intervalos


seleccion = input("Queres ver la cantidad de numeros pares entre dos numeros? y/n \n")

while seleccion != "n":
    if seleccion != "n" and seleccion != "y":
        print('Debes de responder solamente con "y" o con "n"')
        seleccion = input(
            "Queres ver la cantidad de numeros pares entre dos numeros? y/n \n"
        )

    else:
        inicio = input("Introduce el INICIO del intervalo en numero entero\n")
        fin = input("Introduce el FINAL del intervalo en numero entero\n")
        while not inicio.isdigit() or not fin.isdigit() or int(inicio) >= int(fin):
            print(
                "ambos numeros debe de ser enteros, y por favor, el primero debe de ser el menor y el segundo el mayor"
            )
            inicio = input("Introduce el INICIO del intervalo en numero entero\n")
            fin = input("Introduce el FINAL del intervalo en numero entero\n")
        inicio = int(inicio)
        fin = int(fin)
        for contador in range(inicio, fin + 1):
            if contador % 2 == 0:
                print(f"{contador}")
        seleccion = input(
            "Queres volver a ver la cantidad de numeros pares entre dos numeros? y/n"
        )

print("Programa terminado")
