# FUNCIÓN QUE NO RECIBE ARGUMENTOS


def suma():
    num1 = 5
    num2 = 7
    print("\nSin argumentos =", num1+num2)


suma()

# FUNCIÓN QUE RECIBE ARGUMENTOS


def suma2(num1, num2):

    print("\nCon argumentos =", num1+num2)


suma2(2, 5)

# FUNCIÓN CON REGRESO DE VALOR


def suma3(num1, num2):

    resultado = num1+num2
    print()

    return resultado


print("Con regreso de valores =", suma3(3, 3))
