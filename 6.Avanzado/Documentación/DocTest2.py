import doctest

# DEBEMOS COMPROBAR QUE LAS FUNCIONES HACEN SU TRABAJO
# USANDO EL MOSULO doctest NOS SERÁ POSIBLE

def areaTriangulo(base, altura):

    """
    CALCULA EL AREA DE UN TRIANGULO DADO

    >>> areaTriangulo(3, 6)
    'Área: 9.0'

    >>> areaTriangulo(2, 2)
    'Área: 3.0'
    """

    return 'Área: ' + str((base*altura)/2)

# SI EL METODO NO DEVUELVE NADA = FUNCIONA
doctest.testmod()
# PUEDE QUE NO FUNCIONE, EN ESE CASO NOS NOTIFICARÁ DE TODO