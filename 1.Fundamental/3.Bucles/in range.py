for i in range(5):
    print(f"Hola a 5 / {i}")

for i in range(10, 20):
    print(f"Hola de 10 a 20 / {i}")

for i in range(1, 20, 3):
    print(f"Hola de 3 en 3 / {i}")

valido = False

email = input("Intoduce E-mail --> ")

for i in range(len(email)):

    if email[i] == "@":

        valido = True

if valido:

    print("E-mail correcto")

else:

    print("E-mail incorrecto")
