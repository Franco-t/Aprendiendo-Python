"""
ejercicio5.
crear una lista con el contenido de esta tabla
accion      aventura        deporte
gta         assins          fifa
cod         crash           pro
pubg        prince          moto 
"""

bibliotecaJuegos = [
    {
        "categoria":"accion",
        "juegos":["gta", "cod", "pubg"]    
    },
    {
        "categoria":"aventura",
        "juegos":["assins", "crash", "prince"] 
    },
    {
        "categoria":"deporte",
        "juegos":["fifa", "pro", "moto"] 
    }
]

for categoria in bibliotecaJuegos:
    print (f"======{categoria['categoria']}======")
    for juego in categoria['juegos']:
        print(juego)