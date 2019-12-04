for letra in "Python":

    if letra == "h":
        continue

    print("Viendo la letra: " + letra)

# CANTIDAD DE CARÁCTERES
nombre = "Pamela Segovia"

contador = 0

for i in nombre:

    if i == " ":
        break

    contador += 1

print(contador)
