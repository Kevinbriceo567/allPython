import doctest
import re

def compruebaMail(mailUsuario):

    """

    EVALUA UN MAIL RECIBIDO EN BUSCA DEL @:
    2@ = MAL
    1@ = TAL VEZ
    TEXTO@ = MAL

    >>> compruebaMail('kevin@gmail.com')
    True

    """

    arroba = mailUsuario.count('@')

    arroba = str(arroba)

    if (arroba!=1 or arroba.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0):

        return False

    else:

        return True