# PERMITEN SIMPLIFICAR FUNCIONES

# LUEGO DE LOS DOS PUNTOS, SE ESPECIFICA QUE RETORNAR
area_Triangulo =lambda base,altura:(base*altura)/2

print(area_Triangulo(3, 4))

# AL CUBO
al_cubo = lambda numero:numero**3

print(al_cubo(3))

# VALOR
destaca_valor = lambda comision:"¡{}! $".format(comision)

comision_Ana = 15585

print(destaca_valor(comision_Ana))