# CREAR Y ESCRIBIR
file = open("datos.txt", "w")  # w PARA MODO ESCRITURA

file.write('Hola')  # ESCRIBIENDO EN ARCHIVO

file.close()  # CERRANDO EL ARCHIVO

# LECTURA
file = open("datos.txt", "r")  # r PARA MODO LECTURA

print(file.read())  # FUNCIÓN QUE REGRESA UN STRING

file.readlines()  # DEVUELVE UNA LISTA CON CADA LÍNEA DEL ARCHIVO

file.seek(0)

print(file.read())