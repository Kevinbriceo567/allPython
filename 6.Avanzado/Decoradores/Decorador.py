# FUNCIONES QUE A SU VEZ AÑADEN FUNCIONALIDADES A OTRAS FUNCIONES

# FORMADO POR (A, B Y C)

# UN DECORADOR DEVUELVE OTRA FUNCIÓN
def decoradora(funcion_parametro):

    def funcion_interior():

        # Acciones adicionales que decoran

        print("Vamos a realizar un calculo")

        funcion_parametro()

        # Acciones adicionales

        print("Hemos terminado el cálculo")

    return funcion_interior()

@decoradora
def suma():

    print(15 + 5)
@decoradora
def resta():

    print(15 - 5)

suma()

resta()