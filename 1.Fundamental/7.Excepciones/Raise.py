import math


def raiz(num1):

    if num1 < 0:
        raise ValueError("Número no puede ser negativo")

    else:
        return math.sqrt(num1)


op1 = int(input("Introduce un número --> "))

try:
    print(raiz(op1))

except ValueError as ErrorNúmeroNegativo:

    print(ErrorNúmeroNegativo)

print("Programa finalizado")
