# LAS FUNCIONES LAMBA Y FILTER PUEDEN COMPLEMENTARSE DE BUENA MANERA

#FILTRANDO NUMEROS PAR #
def numero_par(num):

    if num % 2 == 0:

        return True

    return False

numeros = [24, 13, 5, 8, 9]

print(list(filter(numero_par, numeros)))

print(list(filter(lambda numero_p: numero_p%2==0, numeros)))

# FILTRANDO EMPLEADOS POR SUELDO #
class Empleado:
    def __init__(self, nombre, cargo, salario):

        self.nombre= nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):

        return "{} que trabaja {} tiene un salario de {} $".format(self.nombre, self.cargo, self.salario)

listaEmpleados = [

    Empleado("Kevin", "Programador", 300000),
    Empleado("Willians", "Programador", 400000),
    Empleado("Branko", "Programador", 100000)

]

salarios_altos = filter(lambda empleado:empleado.salario>200000, listaEmpleados)

for empleado_salario in salarios_altos:

    print(empleado_salario)