# INICIANDO DICCIONARIO
dicc={"Alemania": "Berlín", "Francia": "París", "Venezuela": "Caracas"}

# IMPRIMIENDO TODOS LOS VALORES
print(dicc)

# AÑADIR ELEMENTO AL DICCIONARIO
dicc["Chile"] = "Miami"

# ACTUALIZANDO CON ATRIBURO UPDATE
dicc.update({"Chile": "Caracas"})
print(dicc)

# MODIFICAR DICCIONARIO
dicc["Chile"] = "Santiago"

# MOSTRAR VALOR DE CLAVE ESPECÍFICA
print(dicc["Francia"])

# ELIMINAR VALOR DE DICCIONARIO
if "Zimba" in dicc:
    del dicc["Zimba"]
    print("Eliminado")

else:
    print("No existe")

# OBTIENE Y ELIMINA LA CLAVE DESEADA
valorE = (dicc.pop("Venezuela", "No existe"))

print(valorE)

# PUEDEN ALMACENAR VALORES NUMÉRICOS
jugadores={7: "CR7", 10: "Messi"}

print(jugadores[7])

# CREAR DICCIONARIO DESDE TUPLA
paises = ["Venezuela", "Brasil", "Chile"]
paisesDicc = {paises[0]: "Caracas", paises[1]: "Sao Paulo", paises[2]: "Santiago"}

print(paisesDicc)

# EJEMPLO CON UN JUGADOR
basket = {23: "Jordan", "Nombre": "Michael", "Equipo": "Chicago", "anillos": [1991, 1992, 1993, 1996, 1997, 1998]}
print(basket)
print(basket["Equipo"])

# CLAVES DEL DICCIONARIO
print("\n", dicc.keys())

# LLAVES DEL DICCIONARIO
print(dicc.values())

# CANTIDAD DE ELEMENTOS
print(len(dicc))
