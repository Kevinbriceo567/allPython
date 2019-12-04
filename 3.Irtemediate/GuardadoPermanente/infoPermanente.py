import pickle

class Persona:

    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad

        print("\nNueva persona " + nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:

    listPersonas = [type(object)]

    def __init__(self):

        FileListaP = open("listaP", "ab+")

        FileListaP.seek(0)

        try:

            self.listPersonas = pickle.load(FileListaP)

            print("Se cargaron {} personas del fichero externo".format(len(self.listPersonas)))

        except:
            print("Fichero vacío")

        finally:
            FileListaP.close()
            del(FileListaP)


    def agregarPersonas(self, p):
        self.listPersonas.append(p)
        self.guardarPersonasEnFile()

    def mostrarPersonas(self):
        for p in self.listPersonas:
            print(p)

    def guardarPersonasEnFile(self):
        FileListaP = open("ListaP", "wb")
        pickle.dump(self.listPersonas, FileListaP)
        FileListaP.close()
        del(FileListaP)

    def mostrarInfoFile(self):
        print("Información:")
        for p in self.listPersonas:
            print(p)


miLista = ListaPersonas()

p = Persona("Branko", "Masculino", 16)
miLista.agregarPersonas(p)
p = Persona("Kevin", "Masculino", 29)
miLista.agregarPersonas(p)
miLista.mostrarInfoFile()

'''

miLista.agregarPersonas(p)
p = Persona("Willians", "Masculino", 18)
miLista.agregarPersonas(p)

miLista.mostrarPersonas()'''