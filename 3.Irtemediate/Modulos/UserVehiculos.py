# CLASE PADRE #
class Vehiculos():

    def __init__(self, marca, modelo): # CONSTRUCTOR
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    # COMPORTAMIENTOS
    def arrancar(self):

        self.enMarcha = True

    def acelerar(self):

        self.acelera = True

    def frenar(self):

        self.frena = True

    def estado(self):
        print("\nMarca:" + self.marca + "\nModelo " + self.modelo + "\nEn Marcha: " + str(self.enMarcha) + "\nAcelera: "+ str(self.acelera) + "\nFrena:" + str(self.frena))

######################
# CLASE HIJO MOTO #
class Moto(Vehiculos):
    hcaballito = ""

    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"

    def estado(self):
        print("\nMarca:" + self.marca + "\nModelo " + self.modelo + "\nEn Marcha: " + str(self.enMarcha) + "\nAcelera: "+ str(self.acelera) + "\nFrena:" + str(self.frena) + "\nCaballito:" + self.hcaballito)

######################
# CLASER HIJO FURGONETA #
class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado=cargar
        if(self.cargado):
            return "Furgoneta cargada"
        else:
            return "Furgoneta no cargada"

######################
# CLASE VEHICULOS ELECTRICOS #
class VElectricos(Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

        self.autonomia=100

    def cargarEnergia(self):
        self.cargando=True
######################
# CLASE HIJO BICICLETAS ELECTRICAS #
class BElectrica(VElectricos, Vehiculos):
    pass
