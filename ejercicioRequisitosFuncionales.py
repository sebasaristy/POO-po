
class Motor:
    def __init__(self):
        self.estado = False

    def encender_motor(self):
        self.estado = True
        print("El motor ha sido encendido")
    
    def apagar_motor(self):
        self.estado = False
        print("El motor ha sido apagado")

class Vehiculo:
    def __init__(self, marca, tipo, placa, estado):
        self.marca = marca
        self.tipo = tipo
        self.placa = placa
        self.estado = estado
        self.motor = Motor()

class Flota:
    def __init__(self, nombre):
        self.nombre = nombre
        self.listaVehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.listaVehiculos.append(vehiculo)
        print("Ha sido agregado exitosamente")

    def eliminar_vehiculo(self, placa):
        for b in self.listaVehiculos:
            if placa == b.placa:
                self.listaVehiculos.remove(b)
        print("El vehiculo fue eliminado exitosamente")

    def mostrar_carros(self):
        contador = 0
        for carro in self.listaVehiculos:
            contador += 1
            print(f'\nInformacion del carro {contador}: \nMarca: {carro.marca} --Tipo: {carro.tipo} --Placa: {carro.placa} --Estado: {carro.estado}')
    
    def total_carros(self):
        print(f'El total de carros es: {len(self.listaVehiculos)}')

    def buscar_carro(self, placa):
        for buscar in self.listaVehiculos:
            if buscar.placa == placa:
                return 1
        return 0

flota1 = Flota("mico")
carro1 = Vehiculo("Mitsubishi", "todoterreno", 13, "En servicio")
carro2 = Vehiculo("BMW", "deportivo", 12, "Sin servicio")
carro3 = Vehiculo("Chevrolet", "deportivo", 14, "En servicio")

flota1.agregar_vehiculo(carro1)
flota1.agregar_vehiculo(carro2)
flota1.agregar_vehiculo(carro3) 

while True:
    print("\nBienvenido a la Flota")
    print("Seleccione una opcion:")
    print("1. Agregar un vehiculo a la Flota")
    print("2. Eliminar un vehiculo de la flota")
    print("3. Mostrar vehiculos")
    print("4. Mostrar total vehiculos")
    print("5. Buscar vehiculo por placa")
    print("6. Encender motor de un vehiculo")
    print("7. Apagar motor de un vehiculo")
    print("0. Salir")
    opcion = int(input(": "))

    if opcion == 1: 
        marcaNueva = input("Ingrese la marca del carro: ")
        nuevaPlaca = int(input("Ingrese la placa:  "))
        nuevoTipo = input("Ingrese el tipo de vehiculo: ")
        nuevoEstado = "En servicio"
        nuevoVehiculo = Vehiculo(marcaNueva, nuevaPlaca, nuevoTipo, nuevoEstado)
        flota1.agregar_vehiculo(nuevoVehiculo)
    
    elif opcion == 2:
        placaBuscar = int(input("Ingrese la placa del vehiculo que desea eliminar: "))
        flota1.eliminar_vehiculo(placaBuscar)

    elif opcion == 3:
        flota1.mostrar_carros()
    
    elif opcion == 4:
        flota1.total_carros()
    
    elif opcion == 5: 
        placaBuscar2 = int(input("Ingrese la placa del vehiculo que desea buscar: "))
        flota1.buscar_carro(placaBuscar2)
        if flota1.buscar_carro(placaBuscar2) == 1:
            print(f'Carro encontrado, {flota1.listaVehiculos[flota1.buscar_carro(placaBuscar2)].marca}, {flota1.listaVehiculos[flota1.buscar_carro(placaBuscar2)].tipo}, {flota1.listaVehiculos[flota1.buscar_carro(placaBuscar2)].estado}')
        elif flota1.buscar_carro(placaBuscar2) == 0:
            print(f'Carro no encontrado')

    elif opcion == 6:
        placaBuscar3 = int(input("Ingrese la placa del vehiculo que desea encender: "))
        flota1.buscar_carro(placaBuscar3)
        if flota1.buscar_carro(placaBuscar3) == 1:
            flota1.listaVehiculos[flota1.buscar_carro(placaBuscar3)].motor.encender_motor()
        elif flota1.buscar_carro(placaBuscar3) == 0:
            print(f'Carro no encontrado')

    elif opcion == 7:
        placaBuscar4 = int(input("Ingrese la placa del vehiculo que desea encender: "))
        flota1.buscar_carro(placaBuscar4)
        if flota1.buscar_carro(placaBuscar4) == 1:
            flota1.listaVehiculos[flota1.buscar_carro(placaBuscar4)].motor.apagar_motor()
        elif flota1.buscar_carro(placaBuscar4) == 0:
            print(f'Carro no encontrado')

    elif opcion == 0:
        print("Hasta luego")

    else:
        print("Ingrese un numero adecuado")
