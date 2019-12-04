def decoradora(funcion_parametro):

    def funcion_interior(*args):

        # Acciones adicionales que decoran

        print("Vamos a realizar un calculo")

        funcion_parametro(*args)

        # Acciones adicionales

        print("Hemos terminado el cálculo")

    return funcion_interior()

@decoradora
def suma(num1, num2):

    print(num1 + num2)

@decoradora
def resta(num1, num2):

    print(num1 - num2)


suma(15, 5)

resta(15, 5)
