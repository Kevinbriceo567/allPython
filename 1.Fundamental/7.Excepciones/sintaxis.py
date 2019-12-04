def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multiplica(num1, num2):
    return num1 * num2


def divide(num1, num2):

    try:
        return num1 / num2

    except ZeroDivisionError:
        print("\nLa división entre 0 no está definida")
        return ""

# EJECUCIÓN #

# COMPROBAMOS QUE SE INGRESEN DATOS TIPO INT
while True:
    try:
        op1 = (int(input("\nIntroduce el primer numero --> ")))

        op2 = (int(input("Introduce el segundo numero --> ")))

        break

    except ValueError:
        print("\nIngrese Valores numéricos")

operacion = input("Introduce la operacion a realizar (suma,resta,multiplica,divide): ")

if operacion == "suma":
    print(suma(op1, op2))

elif operacion == "resta":
    print(resta(op1, op2))

elif operacion == "multiplica":
    print(multiplica(op1, op2))

elif operacion == "divide":
    print(divide(op1, op2))

else:
    print("Operacion no contemplada")

print("\nOperacion ejecutada. Continuacion de ejecucion del programa ")
