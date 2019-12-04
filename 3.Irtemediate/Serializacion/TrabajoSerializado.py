import pickle

# CREANDO ARCHIVO BINARIO
nameList = ["Pamela", "Emerson", "Jorge"]

fileBinario = open("nameList", "wb")  # ESCRITURA BINARIA

pickle.dump(nameList, fileBinario)

fileBinario.close

del(fileBinario)

# LEYENDO ARCHIVO BINARIO
fichero = open("nameList", "rb")

nameListLoaded=pickle.load(fichero)

print(nameListLoaded)