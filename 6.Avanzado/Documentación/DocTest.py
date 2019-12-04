import doctest

# DEBEMOS COMPROBAR QUE LAS FUNCIONES HACEN SU TRABAJO
# USANDO EL MOSULO doctest NOS SERÁ POSIBLE

def areaTriangulo(base, altura):

    """
    CALCULA EL AREA DE UN TRIANGULO DADO

    >>> areaTriangulo(3, 6)
    8.0
    """

    return (base*altura)/2

# SI EL METODO NO DEVUELVE NADA = FUNCIONA
doctest.testmod()
# PUEDE QUE NO FUNCIONE, EN ESE CASO NOS NOTIFICARÁ DE TODO