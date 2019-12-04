# CON RETORNO
def factorialC(numf):
    fact = 1

    for i in range(1, numf + 1, 1):
        fact = fact * i

    return fact
##################################
numf = int(input("\nIngrese número a factorizar --> "))

resultado = (factorialC(numf))

print(f"\nEl factorial de {numf} es {resultado}")





# SIN RETORNO
def factorialS(numf):
    fact = 1
#
    for i in range(1, numf + 1, 1):
        fact = fact * i

    print(f"\n{numf}!={fact}")

numf = int(input("\nIngrese número a factorizar --> "))

factorialS(numf)