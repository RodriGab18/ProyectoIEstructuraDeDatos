class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class Mantenimiento:
    def __init__(self, fecha="", descripcion="", costo=0):
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__costo = costo
        self.primero = None

    @property
    def fecha(self):
        return self.__fecha
        
    @fecha.setter
    def fecha(self, nuevaFecha):
        self.__fecha = nuevaFecha

    @property
    def descripcion(self):
        return self.__descripcion
        
    @descripcion.setter
    def descripcion(self, nuevaDescripcion):
        self.__descripcion = nuevaDescripcion

    @property
    def costo(self):
        return self.__costo
        
    @costo.setter
    def costo(self, nuevacosto):
        self.__costo = nuevacosto

    def __str__(self):
        return f"Fecha: {self.fecha}, Descripción: {self.descripcion}, Costo: Q{self.costo}"

    def __repr__(self):
        return self.__str__() 

    def añadirMantenimiento(self, mantenimiento):
        nuevo_nodo = Nodo(mantenimiento)
        if not self.primero:
            self.primero = nuevo_nodo
            nuevo_nodo.siguiente = nuevo_nodo  
        else:
            actual = self.primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.primero

    def eliminarMantenimiento(self, mantenimiento_a_eliminar):
        if not self.primero:
            return False

        actual = self.primero
        anterior = None
        while True:
            if actual.dato == mantenimiento_a_eliminar:  
                if anterior: 
                    anterior.siguiente = actual.siguiente
                else: 
                    if actual.siguiente == self.primero: 
                        self.primero = None
                    else:
                        self.primero = actual.siguiente
                        ultimo = self.primero
                        while ultimo.siguiente != actual:  
                            ultimo = ultimo.siguiente
                        ultimo.siguiente = self.primero
                return True
            anterior = actual
            actual = actual.siguiente
            if actual == self.primero:
                break
        return False

    def mostrarMantenimiento(self):
     if not self.primero:
         return []

     actual = self.primero
     mantenimientos = []
     while True:
         mantenimientos.append(actual.dato)  # Aquí almacenamos el objeto Mantenimiento
         actual = actual.siguiente
         if actual == self.primero:
             break
     return mantenimientos

    def calcularCostoTotal(self):
        if not self.primero:
            return 0
        
        total = 0
        actual = self.primero
        while True:
            total += actual.dato.costo
            actual = actual.siguiente
            if actual == self.primero:
                break
        return total