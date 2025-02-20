from Mantenimiento import Mantenimiento
from Vehiculo import Vehiculo
from FlotaVehiculos import FlotaVehiculos
import os

detenerse = 1
flotilla = FlotaVehiculos()

os.system("cls")
print("---SISTEMA DE FLOTA DE VEHÍCULOS---")
print("Presione cualquier tecla para ingresar")
input()
while detenerse == 1:
    os.system("cls")
    print("Bienvenido al sistema de mantenimiento.")
    print("Por favor, ingrese la opción que necesite realizar.")
    print("1. Añadir vehículo.")
    print("2. Gestión de vehículo.")
    print("3. Eliminar un vehículo.")
    print("4. Buscador de vehículos.")
    print("5. Salir.")
    opcion = input("Opción: ")

    if opcion == "1":
        os.system("cls")
        print("Añadir vehículos.")
        print("Por favor, ingrese los datos que se solicitan a continuación.")
        placa = input("Placa (Ejemplo: P123ABC): ")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        
        año = int(input("Año (superior a 1980): "))
        while año < 1980 or año > 2025:
            print("El año del vehículo debe ser superior a 1980 y menor a 2026.")
            año = int(input("Año: ")) 
        
        kilometraje = int(input("Kilometraje: "))
        while kilometraje < 0:
            print("Ingrese un kilometraje válido.")
            kilometraje = int(input("Kilometraje: "))
        
        nuevoVehiculo = Vehiculo(placa, marca, modelo, año, kilometraje)
        flotilla.ingresarVehiculo(nuevoVehiculo)
        input("Vehículo añadido con éxito, presione cualquier tecla para continuar.")

    elif opcion == "2":
        os.system("cls")
        print("Gestión de vehículo.")
        print("A continuación, ingrese la opción que desea realizar.")
        print("1. Añadir mantenimiento a un vehículo.")
        print("2. Consultar mantenimientos del vehículo.")
        print("3. Eliminar un mantenimiento.")
        opcion2 = input("Opción: ")

        if opcion2 == "1":
           if opcion2 == "1":
            print("Añadir un nuevo mantenimiento, ingrese la placa del vehículo.")
            placaBuscador = input("Placa: ")
            vehiculo = flotilla.buscarUnVehiculo(placaBuscador)
            if vehiculo:
                fecha = input("Fecha de mantenimiento: ")
                descripcion = input("Descripción del mantenimiento: ")
                costo = 100 
                mantenimiento = Mantenimiento(fecha, descripcion, costo)
                vehiculo.mantenimientos.añadirMantenimiento(mantenimiento)
                print("Mantenimiento agregado con éxito.")
                input()
            else:
                print("Vehículo no encontrado.")
                input()

        elif opcion2 == "2":
            print("Consultar mantenimientos del vehículo por placa.")
            placaBuscador = input("Placa: ")
            vehiculo = flotilla.buscarUnVehiculo(placaBuscador)
            if vehiculo:
                mantenimientos = vehiculo.mantenimientos.mostrarMantenimiento()
                if mantenimientos:
                    for mant in mantenimientos:
                        print(mant)
                        input()
                else:
                    print("No hay mantenimientos registrados para este vehículo.")
                    input()
            else:
                print("Vehículo no encontrado.")
                input()

        elif opcion2 == "3":
            print("¿Está seguro de eliminar el último mantenimiento?")
            print("1. Sí.    2. No.")
            eliminadorOpcion = input("Opción: ")
            if eliminadorOpcion == "1":
                print("Ingrese la placa del vehículo.")
                placaBuscador = input("Placa: ")
                vehiculo = flotilla.buscarUnVehiculo(placaBuscador)
                if vehiculo:
                    mantenimientos = vehiculo.mantenimientos.mostrarMantenimiento()
                    if mantenimientos:
                        ultimo_mantenimiento = mantenimientos[-1]  
                        vehiculo.mantenimientos.eliminarMantenimiento(ultimo_mantenimiento) 
                        print("Último mantenimiento eliminado con éxito.")
                        input()
                    else:
                        print("No hay mantenimientos para eliminar.")
                        input()
                else:
                    print("Vehículo no encontrado.")
                    input()
            else:
                print("Operación cancelada.")
                input()

    elif opcion == "3":
        os.system("cls")
        print("Eliminar vehículo.")
        print("Ingrese la placa del vehículo que desea eliminar de la flota.")
        placaBuscador = input("Placa: ")
        vehiculo = flotilla.buscarUnVehiculo(placaBuscador)
        if vehiculo:
            print(vehiculo)
            print("¿Desea eliminarlo?")
            print("1. Sí.   2. No.")
            opcion3 = input("Opción: ")
            if opcion3 == "1":
                flotilla.eliminarVehiculo(placaBuscador)
                print("Vehículo eliminado.")
                input()
            else:
                print("Operación cancelada.")
                input()
        else:
            print("Vehículo no encontrado.")
            input()

    elif opcion == "4":
        os.system("cls")
        print("Buscador de vehículos.")
        print("Seleccione la opción que necesite.")
        print("1. Buscar vehículo por placa.")
        print("2. Listar todos los vehículos ingresados.")
        opcion4 = input("Opción: ")
        
        if opcion4 == "1":
            print("Ingrese la placa del vehículo a mostrar.")
            placaBuscador = input("Placa: ")
            vehiculo = flotilla.buscarUnVehiculo(placaBuscador)
            if vehiculo:
                print(vehiculo)
                input()
            else:
                print("Vehículo no encontrado.")
                input()

        elif opcion4 == "2":
            print("Se mostrarán todos los vehículos ingresados.")
            flotilla.mostrarVehiculos()
            input("Presione cualquier tecla para continuar.")

    elif opcion == "5":
        os.system("cls")
        print("Saliendo...")
        print("Rodrigo Gabriel Pérez Vásquez, 1576224")
        detenerse = 0