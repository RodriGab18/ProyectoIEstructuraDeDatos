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
            while actual.siguiente:  # Ir al final de la lista
                actual = actual.siguiente
            actual.siguiente = nuevoNodo  # Añadir el nuevo nodo al final

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
                if anterior:  # Si no es el primer nodo
                    anterior.siguiente = actual.siguiente
                else:  # Si es el primer nodo
                    self.cabeza = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False