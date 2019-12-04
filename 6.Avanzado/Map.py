# FILTRANDO EMPLEADOS POR SUELDO #
class Empleado:
    def __init__(self, nombre, cargo, salario):

        self.nombre= nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):

        return "{} que trabaja {} tiene un salario de {} $".format(self.nombre, self.cargo, self.salario)

listaEmpleados = [

    Empleado("Kevin", "Programador", 300),
    Empleado("Willians", "Programador", 400),
    Empleado("Branko", "Programador", 100)

]

def calculo_comision(empleado):

    if(empleado.salario<=300): # COMPROBAMOS RANGO DEL SALARIO

        empleado.salario = empleado.salario*1.03 # AGREGAMOS UN 3% AL SALARIO

    return empleado

# RECIBEN UNA FUNCIÓN Y UNA COLECCIÓN
listaE = map(calculo_comision, listaEmpleados)

for empleado in listaE:

    print(empleado)