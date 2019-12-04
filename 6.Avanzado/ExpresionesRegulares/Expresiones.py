import re

cadena = "Hola vatos, Hola"

print("Buscando vatos", re.search("vatos", cadena))

print("Buscando dude", re.search("dude", cadena))

aBuscar = "Hola"

if re.search(aBuscar, cadena) is not None: # BUSCA SI STRING aBuscar ESTÁ EN STRING cadena

    print("He encontrado el texto")

else:

    print("No he encontrado el texto")

print(len(re.findall(aBuscar, cadena))) # REGRESA UNA LISTA CON LAS PALABRAS ENCONTRADAS