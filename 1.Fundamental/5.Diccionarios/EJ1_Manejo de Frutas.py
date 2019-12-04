def menu():
    print("\n|MENÚ|")
    print("1. AGREGAR FRUTA")
    print("2. CANTIDAD DE ELEMENTOS")
    print("3. ELIMINAR ELEMENTO")
    print("4. CLAVES")
    print("5. VALORES")
    print("6. LISTADO COMPLETO")
    print("7. VACIAR DICCIONARIO")
    print("8. SALIR")

    op = 0

    op = int(input("\nIngrese operación --> "))

    return op


def agregarF(frutas):
    nombreF = input("\nIngrese nombre --> ")
    precioF = int(input("Ingrese precio --> "))
    cantidadF = int(input("Ingrese cantidad"))

    valor = (precioF, cantidadF)

    frutas[nombreF] = valor

    print("Fruta ingresada con exito")

def cantidad(frutas):
    print("\nCantidad de frutas:", len(frutas))


def eliminarF(frutas):
    nombreF = input("\nIngrese nombre de fruta a eliminar")

    frutas.pop(nombreF, "Fruta no encontrada")


def nombresF(frutas):
    claves = frutas.keys()
    print("\nNombres:")
    for c in claves:
        print(">", c)


def preciosF(frutas):
    valores = frutas.values()
    print("\nPrecios:", valores)


def listado(frutas):
    print("\nListado de frutas:")
    cantT=0

    for nombre, valor in frutas.items():
        precio, cantidad = valor
        print("Nombre:", nombre, "| Precio:", precio, "| Cantidad:", cantidad)
        cantT+=cantidad

    print(cantT)

def vaciar(frutas):
    print("\nListado vaciado")
    frutas.clear()

frutas = {'Manzana': (2, 25), 'Banana': (4, 35), 'Durazno': (3, 30)}

op = 0

while op != 8:
    op = menu()

    if op == 1:
        agregarF(frutas)

    elif op == 2:
        cantidad(frutas)

    elif op == 3:
        eliminarF(frutas)

    elif op == 4:
        nombresF(frutas)

    elif op == 5:
        preciosF(frutas)

    elif op == 6:
        listado(frutas)

    elif op == 7:
        vaciar(frutas)

    else:
        print("\nIngrese operación válida")

#@kevicii