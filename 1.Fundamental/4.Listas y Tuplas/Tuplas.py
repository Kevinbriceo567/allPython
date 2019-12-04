# LAS TUPLAS NO SE PUEDEN MODIFICAR DESPUÉS DE SU CREACIÓN

tupla = ("Kevin","José", 1, 2)
tupla1 = "Kevin","José", 1, 2

# IMPRIMIR EN POSICIÓN INDICADA
print(tupla[1])

# CONVERSIÓN DE TUPLA A LISTA
lista = list(tupla)
print(lista)

# CONVERSIÓN DE TUPLA A LISTA
tupla2 = tuple(lista)
print(tupla2)

# COMPROBAR EXISTENCIA DE ELEMENTO
print("Kevin" in tupla)

# CONTAR CANTIDAD DE VECES QUE SE REPITE EL ELEMENTO
print(tupla.count("José"))

# MOSTRAR CANTIDAD DE ELEMENTOS EN LA TUPLA
print(len(tupla))

# ASIGNAR MULTIPLES VALORES DE LA TUPLA A VARIAS VARIABLES
fechas = [("Kevin", (13, 1, 1995)), ("Willians", (29, 3, 1998))]

for nombre, (dia, mes, año) in fechas:
    print (f"{nombre} nació el día {dia}")


nombre, dia, mes, agno = fechas

print(nombre, mes, agno, dia)

# DESEMPAQUETADO
persona = ("Kevin", "Briceño")
nombre, apellido = persona
print(nombre)
