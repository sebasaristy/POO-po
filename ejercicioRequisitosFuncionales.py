
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
    def __init__(self, tipo, placa):
        self.tipo = tipo
        self.placa = placa  
        self.motor = Motor()
    
    def encender_motor(self):
        self.estado = True
    
    def apagar_motor(self):
        self.estado = False


class Flota:
    def __init__(self, nombre):
        self.nombre = nombre
        self.listaVehiculos = []

    def agregar_vehiculo(self, vehiculo):
        nuevoCarro = Vehiculo(vehiculo)
        self.listaVehiculos.append(nuevoCarro)
        print("Ha sido agregado exitosamente")

    def mostrar_carros(self):
        for carro in self.listaVehiculos:
            print(carro.placa)

flota1 = Flota("mico")
carro1 = Vehiculo("todoterreno")
print(carro1.placa)
flota1.agregar_vehiculo(carro1)
