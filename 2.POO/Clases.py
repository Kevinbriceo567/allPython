# ESTABLECIENDO CLASE #
class Coche():

    # CONSTRUCTOR
    def __init__(self):

        # PROPIEDADES
        self.__anchoChasis = 120 # cm
        self.__largoChasis = 120
        self.__ruedas = 4 # ENCAPSULACIÓN CON '__'
        self.__enMarcha = False

    # COMPORTAMIENTOS
    def arrancar(self, arrancamos):
        self.__enMarcha=arrancamos

        if self.__enMarcha:
            chequeo=self.__chequeoInterno()

        if self.__enMarcha and chequeo:
            return "\nCoche en marcha"

        elif self.__enMarcha and chequeo==False:
            return "\nAlgo estuvo mal en el chequeo"

        else:
            return "\nCoche inmóvil"

    def estado(self):
        print("COCHE| RUEDAS: " + str(self.__ruedas) + " ANCHO: " + str(self.__anchoChasis) + " LARGO: " + str(self.__largoChasis))

    def __chequeoInterno(self):
        print("\nRealizando chequeo interno")

        self.gasolina='Ok'
        self.aceite='Ok'
        self.puertas='Cerradas'

        if self.gasolina=='Ok' and self.aceite=='Ok' and self.puertas=='Cerradas':
            return True
        else:
            return False

######################
# INSTANCIANDO OBJETOS DE CLASE 'Coche' #
coche1 = Coche()
coche2 = Coche()
######################
# USANDO COCHE 1 #
print(coche1.arrancar(True))

coche1.estado()
######################
# USANDO COCHE 2 #
print(coche2.arrancar(False))

# coche2.__ruedas = 5 # CAMBIANDO PROPIEDAD (NO SE PUEDE PORQUE ESTÁ ENCAPSULADA)
# coche2.__chequeoInterno() # NO PERIMTE LLAMAR MÉTODOS ENCAPSULADOS DESE AFUERA

coche2.estado()
######################


