from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

class PedidoInvalidoError(Exception): ...

@dataclass
class LineaPedido:
    descripcion: str
    cantidad: int
    peso_unitario: float 

class Pedido:
    def __init__(self):
        self.lineas: List[LineaPedido] = []

    def agregar_linea(self, desc, cantidad, peso):
        linea = LineaPedido(desc, cantidad, peso)
        self.lineas.append(linea)

    def calcular_total(self):
        return sum(l.cantidad for l in self.lineas)

    def calcular_peso(self):
        return sum(l.cantidad * l.peso_unitario for l in self.lineas)
        

class Transporte(ABC):
    def __init__(self, capacidad, velocidad, costo_base):
        self.capacidad = capacidad
        self.velocidad = velocidad
        self.costo_base = costo_base

    @abstractmethod
    def soporta(self, peso):
        ...

    @abstractmethod
    def calcular_tiempo(self, distancia):
        ...

    @abstractmethod
    def calcular_costo(self, distancia, peso):
        ...

class Bicicleta(Transporte):
    def soporta(self, peso):
        if peso <= 15:
            return True
        else:
            return False

    def calcular_tiempo(self, distancia):
        return distancia/self.velocidad

    def calcular_costo(self, distancia, peso):
        return self.costo_base + (distancia*0.20)

class Moto(Transporte):

    def soporta(self, peso):
        if peso <= 50:
            return True
        else:
            return False

    def calcular_tiempo(self, distancia):
        return distancia/self.velocidad

    def calcular_costo(self, distancia, peso):
        return self.costo_base + (distancia*0.60) + (peso*0.05)

class Furgoneta(Transporte):
    def soporta(self, peso):
        return True

    def calcular_tiempo(self, distancia):
        return distancia/self.velocidad

    def calcular_costo(self, distancia, peso):
        return self.costo_base + (distancia*1.20) + (peso*0.10)

class GestorEnvios:
    def __init__(self):
        self.transportes: List[Transporte] = []

    def registrar_transporte(self, transporte):
        self.transportes.append(transporte)
        with open("transportes.txt", "a") as f:
            f.write(f"{type(transporte).__name__}, {transporte.capacidad}, {transporte.velocidad}, {transporte.costo_base}\n")

    def cargar_medios_de_transporte(self):
        with open("transportes.txt", "r") as f:
            for linea in f:
                linea = linea.strip().split(",")
                if linea[0] == "Bicicleta":
                    self.transportes.append(Bicicleta(int(linea[1]), int(linea[2]), float(linea[3])))
                elif linea[0] == "Moto":
                    self.transportes.append(Moto(int(linea[1]), int(linea[2]), float(linea[3])))
                elif linea[0] == "Furgoneta":
                    self.transportes.append(Furgoneta(int(linea[1]), int(linea[2]), float(linea[3])))

    def asignar(self, pedido, distancia, estrategia="cualquiera"):
        peso = pedido.calcular_peso()

        if peso <= 0 or distancia <= 0:
            raise PedidoInvalidoError("Distancia y peso deben ser mayores a 0")

        candidatos = [t for t in self.transportes if t.soporta(peso) == True]

        if estrategia == "cualquiera":
            elegido = candidatos[0]
        else:
            elegido = min(candidatos,key=lambda t: t.calcular_costo(distancia, peso))

        return elegido

gestor = GestorEnvios()
gestor.cargar_medios_de_transporte()

pedido = Pedido()
pedido.agregar_linea("Arepas", 5, 0.5)
pedido.agregar_linea("Gaseosa", 7, 2)

gestor.cargar_medios_de_transporte()
