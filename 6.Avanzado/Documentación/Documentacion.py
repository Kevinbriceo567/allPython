# DEBEMOS DOCUMENTAR BIEN EL CODIGO PARA DEJAR
# MUY CLARO LO QUE SE HIZO

def areaTriangulo(base, altura):

    """CALCULA EL AREA DE UN TRIANGULO"""

    return "El área del cuadrado es: " + str((base * altura)/2)

class Areas:

    def areaCuadrado(lado):

        """CALCULA EL AREA DE UN CUADRADO MULTIPLICANDO AL LADO CONSIGO MISMO"""

        return "El área del cuadrado es: " +str(lado*lado)



# PEDIMOS IMPRIMIR LA DOCUMENTACIÓN DE LA FUNCIÓN
help(areaTriangulo)

# DOC DE LA FUNCION DE UNA CLASE
help(Areas.areaCuadrado)

# TODAS LAS FUNCIONES DE LA CLASE
help(Areas)