persona = {
    "nombre": "Tamara",
    "apellido": "Lezcano",
    "Edad": 23
}

print(persona)
print(type(persona))
print(persona["apellido"])

personas = [
    {
        "nombre": "Tamara",
        "apellido": "Lezcano",
        "edad": 23
    },
    {
        "nombre": "Franco",
        "apellido": "Gimenez",
        "edad": 24
    }
]

print(personas)

print(personas[1]["nombre"])

print("\nListado de personas\n")

for humano in personas:
    print("-------------------------------------")
    print(f"Nombre de la persona: {humano["nombre"]}")
    print(f"Apellido de la persona: {humano["apellido"]}")
    print(f"Edad de la persona: {humano["edad"]}")
    print("-------------------------------------\n")