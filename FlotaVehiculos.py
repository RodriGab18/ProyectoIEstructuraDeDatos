class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class FlotaVehiculos:
    def __init__(self):
        self.cabeza = None

    def ingresarVehiculo(self, vehiculo):
        nuevoNodo = Nodo(vehiculo)
        if not self.cabeza:
            self.cabeza = nuevoNodo
        else:
            actual = self.cabeza
            while actual.siguiente:  
                actual = actual.siguiente
            actual.siguiente = nuevoNodo  

    def mostrarVehiculos(self):
        actual = self.cabeza
        if not actual:
            print("No hay vehículos en la flota.")
            return
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("Esos son todos los vehículos ingresados.")

    def buscarUnVehiculo(self, placa):
        actual = self.cabeza
        while actual:
            if actual.dato.placa == placa:
                return actual.dato
            actual = actual.siguiente
        return None
        
    def eliminarVehiculo(self, placa):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.dato.placa == placa:
                if anterior: 
                    anterior.siguiente = actual.siguiente
                else:  
                    self.cabeza = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False