# C (m/n) = m! (m - n)! * n!

# FUNCIONES #
def factorial(n):
    fact = 1

    for i in range(1, n + 1, 1):
        fact = fact * i

    return fact

def combinado(m, n):
    mf = 0
    nf = 0
    mnf = 0
    resultado = 0
    mf = factorial(m)
    nf = factorial(n)
    mnf = factorial(m - n)

    resultado = mf / (mnf * nf)

    return resultado


# VARIABLES #
m = 0
n = 0
comb = 0

# EJECUCIÓN #

m = int(input("\nIngrese m --> "))

n = int(input("Ingrese n --> "))

comb = combinado(m, n)

print(f"\nEl número combinado de {m}! / ({m} - {n}) * {m} es: {comb}")
