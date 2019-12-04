personas = [
    ('Kevin', 'Briceño', '26263200-8', 'Comp'),
    ('Willians', 'Briceño', '26263200-3', 'Meca'),
    ('Ingrid', 'Linarez', '26263200-5', 'Esti'),
    ('Ana', 'Vasquez', '26263200-1', 'Educ'),
]

for nombre, apellido, rut, profesion in personas:
    print(nombre, "RUT:", rut)

# INGRESANDO A SUBPOSICIONES
print(personas[2][0], personas[2][2])

carr = ""
hay = False
carr = int(input("Ingrese carrera a buscar --> "))

for nombre, apellido, rut, carrera in personas:
    if carr == carrera:
        print(nombre, "", apellido, "", carrera)
        hay = True

    if hay == False:
        print("No hay alumnos")
