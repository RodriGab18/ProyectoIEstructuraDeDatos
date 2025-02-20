from Mantenimiento import Mantenimiento

class Vehiculo:
    def __init__(self, placa, marca, modelo, año, kilometraje):
        self.__placa = placa
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__kilometraje = kilometraje
        self.mantenimientos = Mantenimiento()

    @property
    def placa(self):
        return self.__placa
    
    @placa.setter
    def placa(self, nuevaPlaca):
        self.__placa = nuevaPlaca

    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, nuevaMarca):
        self.__marca = nuevaMarca

    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, nuevoModelo):
        self.__modelo = nuevoModelo

    @property
    def año(self):
        return self.__año
    
    @año.setter
    def año(self, nuevoAño):
        self.__año = nuevoAño

    @property
    def kilometraje(self):
        return self.__kilometraje
    
    @kilometraje.setter
    def kilometraje(self, nuevoKilometraje):
        self.__kilometraje = nuevoKilometraje    

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año}) - Placa: {self.placa}, Kilometraje: {self.kilometraje} km"

    def añadirMantenimiento(self, fecha, descripcion, costo):
        nuevoMantenimiento = Mantenimiento(fecha, descripcion, costo)
        self.mantenimientos.añadirMantenimiento(nuevoMantenimiento)
    
    def consultarMantenimiento(self):
        return self.mantenimientos.mostrarMantenimiento()
    
    def calcularMantenimientos(self):
        return self.mantenimientos.calcularCostoTotal()