# CLASE PERSONA #
class Persona():
    def __init__(self,nombre, edad, residencia): # CONSTRUCTOR
        self.nombre=nombre
        self.edad=edad
        self.residencia=residencia

    def descripcion(self):
        print("Nombre:", self.nombre, "Edad:", self.edad, "Residencia:" , self.residencia)

# CLSE EMPLEADO #
class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado): # CONSTRUCTOR
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado) # EJECUTA EL MÉTODO __INI__ DE LA CLASE PADRE

        self.salario=salario
        self.antiguedad=antiguedad

    def descripcion(self):
        super().descripcion()
        print("Salario:", self.salario, "Antiguedad", self.antiguedad)

ManuelE = Empleado(300000, 15, "Antonio", 56, "Colombia")
ManuelE.descripcion()