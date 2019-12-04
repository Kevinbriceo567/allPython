palabra="Hola"
equipos=["Dolphins","Patriots","Jets","Bills"]
contador=0

# BUCLE CON STRING
for i in palabra:
    print("Palabra", end=" / ") # LO IMPRIME 4 VECES

print()

# BUCLE EN STRING USANDO ITERADOR
for i in palabra:
    print(i)

# BUCLE EN LISTA USANDO ITERADOR
for i in equipos:
    print(i)

# BUCLE CON LISTA INT
for i in [1,2,3]:
    print("Hola",end=" / ") # LO IMPRIME 3 VECES

print()

# COMPROBAR VALIDEZ DE E-MAIL
myEmail=input("Introduce E-mail --> ")

for i in myEmail:

    if(i=="@" or i=="."):

        contador+=1


if(contador!=0):
    print("Correcto")
else:
    print("Incorrecto")
