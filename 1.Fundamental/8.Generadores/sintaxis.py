def generapares(limite):

    num = 1

    while num <= limite:

        yield num*2

        num = num + 1


devuelvePares = generapares(10)

# ENTRE LAS LLAMADAS, EL GENERADOR ENTRA EN MODO DE SUSPENSIÓN

for i in devuelvePares:

    print(i)

