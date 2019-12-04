edad = int(input("Digite su edad: "))

if 0 <= edad < 100:
    print("Edad valida")

    if edad>18:
        print("Mayor de edad")
    else:
        print("Menor de edad")

else:
    print("Edad no valida")
