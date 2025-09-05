class Motor:
    def __init__(self):
        self.estado = False

    def encender_motor(self):
        self.estado = True
    
    def apagar_motor(self):
        self.estado = False

class Vehiculo:
    def __init__(self, tipo, placa, existe):
        self.tipo = tipo
        self.placa = placa
        self.existe = existe
        self.motor = Motor()
    
    def encender_motor(self):
        self.estado = True
    
    def apagar_motor(self):
        self.estado = False



class Flota:
    def __init__(self, nombre):
        self.nombre = nombre
        self.listaVehiculos = []

    def agregar_vehiculo(self, tipo: str, placa: int, existe: False):
        nuevoCarro = Vehiculo(tipo, placa, existe)
        self.listaVehiculos.append(nuevoCarro)

    
