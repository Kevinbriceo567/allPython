import math

def raizCuadrada(listNum):

    """
    DEVUELVE UNA LISTA CON LA RAIZ CUADRADA DE CADA NUMERO EN LA LISTA PARAMETRO

    >>> lista=[]
    >>> for i in [4, 9]:
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    [2.0, 3.0]

    :param listNum:
    :return:
    """

    return [math.sqrt(n) for n in listNum]

print(raizCuadrada([9, 16, 25]))

import doctest
doctest.testmod()