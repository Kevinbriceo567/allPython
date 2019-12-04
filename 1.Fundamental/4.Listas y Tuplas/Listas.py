nombres = ['María', 'Pepe', 'Kevin', 'Willians']
a = [1, 2, 3, 4]

print("Lista Nombres: ", nombres)

print(nombres[1])

# RANGO DE ELEMENTOS A MOSTRAR
print(nombres[0:3])

# POSICIÓN 2 HASTA EL FINAL
print(nombres[2:])

# IMPRIMIENDO CON BUCLE FOR
for i in nombres:
    print(i)

# AGREGAR ELEMENTO AL FINAL
nombres.append('Branko')
print(nombres)

# AGREGAR ELEMENTO EN POSICIÓN DESEADA
nombres.insert(1, 'José')
print(nombres)

# AGREGAR OTRA LISTA
nombres.extend(['Andrés', 'Isabel'])
print(nombres)

# MOSTRAR ÍNDICE DEL ELEMENTO
print(nombres.index('Pepe'))

# COMPRUEBA SI EL ELEMENTO ESTÁ EN LA LISTA
print("Pepe" in nombres)

# REMOVER ELEMENTO
nombres.remove('Kevin')
print(nombres)

# REMOVER ÚLTIMO ELEMENTO
nombres.pop()
print(nombres)

# SUMAR LISTAS
nombres2 = ['Sandra', 'Lucia']

nombres3 = nombres + nombres2
print(nombres3)

# MULTIPLICAR LISTAS
nombresM = nombres * 2
print(nombresM)
