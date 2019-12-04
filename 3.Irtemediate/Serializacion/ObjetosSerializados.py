import pickle

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


coche1 = Vehiculos("Mazda", "R15")

coche2 = Vehiculos("Toyota", "R15")

cochesList=[coche1, coche2]

# ESCRIBIENDO ARCHIVO BINARIO
fileB = open("coches", "wb")

pickle.dump(cochesList, fileB)

fileB.close

del(fileB)

# LEYENDO ARCHIVO BINARIO
fileBRead = open("coches", "rb")

losCoches = pickle.load(fileBRead)

fileBRead.close

for c in losCoches:
    print("\n", c)  # MUESTRA INFORMACIÓN EL OBJETO VEHICULO GUARDADO

    print(c.estado())  # MOSTRANDO ESTADO DE CADA OBJETO VEHICULO