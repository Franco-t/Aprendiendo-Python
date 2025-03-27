import mimodulo

print(mimodulo.hola("Tamara"))

#modulo de fecha

import datetime

print(datetime.date.today())

print(datetime.datetime.now())

fecha = datetime.datetime.now()

print(fecha.year)

fechaPersonaliza = fecha.strftime("%d %m %Y %H:%M:%S")

print(fechaPersonaliza)

print(datetime.datetime.now().timestamp())