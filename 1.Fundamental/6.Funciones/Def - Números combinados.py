# C (m/n) = m! (m - n)! * n!

# FUNCIONES #
def factorial(n):
    fact = 1

    for i in range(1, n + 1, 1):
        fact = fact * i

    return fact


# VARIABLES #
m = 0
n = 0
mf = 0
nf = 0
mnf = 0
resultado = 0

# EJECUCIÓN #

m = int(input("\nIngrese m --> "))
mf = factorial(m)

n = int(input("Ingrese n --> "))
nf = factorial(n)

mnf = factorial(m-n)
print(f"(m-n)! = {mnf}")

resultado = mf / (mnf * nf)

print(f"\nEl resultado de {mf} / ({m}-{n}) * {nf}: {resultado}")
