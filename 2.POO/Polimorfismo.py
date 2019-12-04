class Coche():

    def desplazamiento(self):
        print("4 Ruedas")

class Moto():

    def desplazamiento(self):
        print("2 ruedas")

class Camion():

    def desplazamiento(self):
        print("6 Ruedas")

vehiculo1=Moto()
vehiculo2=Coche()
vehiculo3=Camion()


def desplazamientoVehiculo(vehiculo): # MÉTODO POLIMORFICO
    vehiculo.desplazamiento()

desplazamientoVehiculo(vehiculo1) # LLAMA AL MÉTODO CORRESPONDIENTE DEL VEHICULO PASADO
desplazamientoVehiculo(vehiculo2)
desplazamientoVehiculo(vehiculo3)