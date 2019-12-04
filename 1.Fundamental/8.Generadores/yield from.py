# ACCEDER A LOS SUB ELEMENTOS DE CADA ELEMENTO


def devuelveciudades(*ciudades):
    for elemento in ciudades:

            yield from elemento


ciudadesDevueltas = devuelveciudades("Madrid", "Santiago", "Miami", "Lisboa")


for i in ciudadesDevueltas:
    print(i)
