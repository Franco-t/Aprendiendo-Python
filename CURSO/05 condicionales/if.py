entrada = int(input("Ingrese un numero: "))

if entrada % 2 == 0:
    print(f"El numero {entrada} es par")
else:
    print(f"El numero {entrada} es impar")

edad = int(input("Ingresa tu edad: "))


print("La edad no puede ser negativa")
edad = int(input("Ingresa tu edad: "))
if edad >= 0:
    print(f"Tu edad es: {edad}")

    if edad >= 18:
        print("Eres mayor de edad")
else:
    print("La edad no puede ser negativa")
