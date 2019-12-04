def menu():
    op = 0
    print("\n|MENÚ|")
    print("1.MOSTRAR AGENDA")
    print("2.INGRESAR CONTACTO")
    print("3.ELIMINAR CONTACTO")
    print("4.COMPROBAR EXISTENCIA")
    print("5.SALIR")

    op = int(input("\nIngrese opción a realizar --> "))

    return op


def mostrarA(dicc):
    print("\n|Agenda de contactos|")
    for rut, nombre in dicc.items():
        print("Nombre:", nombre, "RUT:", rut)


def ingresarC(dicc):
    rut = input("\nIngrese rut de cliente --> ")
    nombre = input("Ingrese nombre de cliente ")

    dicc[rut] = nombre
    print("Cliente ingresado exitosamente")


def eliminarC(dicc):
    rut = input("Ingrese rut de cliente a eliminar --> ")

    elim = dicc.pop(rut, 'Rut de cliente no encontrado')


def existe(dicc):
    rut = input("Ingrese rut de cliente a buscar --> ")

    if rut in dicc:  # COMPRUEBA EXISTENCIA
        print("Cliente existe en la agenda")

    else:
        print("Cliente no existe en la agenda")


def salir():
    print("Fin de ejecución")
    exit(0)


dicc = {'262632008': 'Kevin', '262632873': 'Ingrid'}

op = 0

while op != 5:
    op = menu()

    if op == 1:
        mostrarA(dicc)

    elif op == 2:
        ingresarC(dicc)

    elif op == 3:
        eliminarC(dicc)

    elif op == 4:
        existe(dicc)

    elif op == 5:
        salir()

    else:
        print("\nOpción inválida")

#@kevicii