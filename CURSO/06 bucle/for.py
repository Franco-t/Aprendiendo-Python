contador = 0
resultado = 0

for contador in range(0, 5):
    print(f"contador = {contador}")

seleccion = input("¿Quieres mostrar una tabla de multiplicar? (y/n): ")

while seleccion != "n":
    if seleccion != "n" and seleccion != "y":
        print("por favor responde con y/n solamente")
        seleccion = input("¿Quieres mostrar una tabla de multiplicar? (y/n): ")
    else:
        numero = int(input("Introduce la tabla a mostrar: "))

        for tabla in range(1, 11):
            print(f"{numero} x {tabla} = {numero * tabla}")

        seleccion = input("¿Quieres mostrar otra tabla de multiplicar? (y/n): ")

print("programa terminado")
