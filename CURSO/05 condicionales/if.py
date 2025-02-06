"""entrada = int(input("Ingrese un numero: "))

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
    print("La edad no puede ser negativa")"""

#if de multiple comprobacion
print("if de multiple comprobacion")

edadminima = 18
edadmaxima = 65

edad = int(input("Ingresa tu edad: "))

if edad >= edadminima and edad <= edadmaxima :
    print ("Edad optima")
else:
    print ("La edad no es optima")
