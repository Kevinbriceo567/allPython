def divide():

    try:

        op1 = float(input("\nIngrese a --> "))
        op2 = float(input("Ingrese b --> "))

        print("La división es: " + str(op1/op2))

    except ValueError:

        print("\nEl valor es erróneo")

    except ZeroDivisionError:

        print("\nLa división entre 0 no está definida")

    finally:

        print("Cálculo finalizado")


divide()
