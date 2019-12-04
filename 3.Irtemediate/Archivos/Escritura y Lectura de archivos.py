import csv, sys, os

def menu():  # MENÚ GENÉRICO
    print("\n|MENU|")
    print("1. Crear/Sobreescribir archivo")
    print("2. Agregar línea de texto")
    print("3. Leer archivo")
    print("4. Vaciar archivo")
    print("5. Salir")

    op = 0

    op = int(input("Ingrese operación --> "))

    return op

def csArchivo(): # ARCHIVO CREADO EN LA CARPETA DEL PROYECTO
    print("\nArchivo 'Datos.txt' creado")

    file = open("Datos.txt", "w")

    file.close()


def agregarL():
    file = open("Datos.txt", "a")

    nuevaL = input("\nIngrese línea a insertar --> ")

    file.write(nuevaL)
    file.write("\n")

    file.close()


def leer(): # PUEDE USARSE PARÁMETRO r+ PARA LECTURA Y ESCRITURA
    file = open("Datos.txt", "r+")

    if file.read() == "":
        print("\nArchivo sin texto")

    else:
        print("\nArchivo:")
        file.seek(0)  # POSICIONAMOS EL CURSOR AL COMIENZO DEL ARCHIVO
        print(file.read())

    file.close()


def vaciarA():
    file = open("Datos.txt", "w")

    print("\nArchivo 'Datos.txt' vaciado")

    file.close()

def salir():
    print("\nFin de ejecución")
    exit(0)


# INICIO DE EJECUCIÓN #

op = 0

while op != 5:

    op = menu()

    if op == 1:
        csArchivo()

    elif op == 2:
        agregarL()

    elif op == 3:
        leer()

    elif op == 4:
        vaciarA()

    elif op == 5:
        salir()

    else:
        print("\nOperación inválida")

#@kevicii