from abc import ABC, abstractmethod

class Transporte:
    def __init__(self, tipo, placa, marca, color, valor):
        self.tipo = tipo   #str
        self.placa = placa #int
        self.marca = marca #str
        self.color = color #str
        self.valor = valor #int
        
    @abstractmethod
    def calcular_impuesto(self):
        ...

class Auto(Transporte):
    def __init__(self, placa, marca, color, valor, tipo):
        super().__init__(placa, marca, color, valor, tipo)
    
    def calcular_impuesto(self):
        return self.valor*0.10 + self.valor

class Camion(Transporte):
    def __init__(self, placa, marca, color, valor, tipo):
        super().__init__(placa, marca, color, valor, tipo) 
    
    def calcular_impuesto(self):
        return self.valor*0.15 + self.valor

class Moto(Transporte): 
    def __init__(self, placa, marca, color, valor, tipo):
        super().__init__(placa, marca, color, valor, tipo)
    
    def calcular_impuesto(self):
        return self.valor*0.05 + self.valor

class Empresa:
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo
        self.listaVehiculo = []

    def agregar_vehiculo(self, v):
        self.listaVehiculo.append(v)
        print(f'El vehiculo {v.placa} ha sido agregado exitosamente')
        with open(self.nombreArchivo, "a") as f:
            f.write(f' {v.tipo}, {v.placa}, {v.marca}, {v.color}, {v.valor}\n')

    def guardar_en_archivo(self):
        try:
            with open(self.nombreArchivo, "w") as f:
                for v in self.listaVehiculo:
                    f.write(f' {v.tipo}, {v.placa}, {v.marca}, {v.color}, {v.valor}\n')
            print(f'Vehiculos agregado correctamente')
        except:
            print(f'Hubo un error al guardar.')
        
    def cargar_vehiculos(self):
        self.listaVehiculo = []
        
        with open(self.nombreArchivo, "r") as f:
            for linea in f:
                linea = linea.strip().split(",")
                if linea[0] == "Auto":
                    self.listaVehiculo.append(Auto(str(linea[0]), int(linea[1]), str(linea[2]), str(linea[3]), int(linea[4])))
                elif linea[0] == "Camion":
                    self.listaVehiculo.append(Camion(str(linea[0]), int(linea[1]), str(linea[2]), str(linea[3]), int(linea[4])))
                elif linea[0] == "Moto":
                    self.listaVehiculo.append(Moto(str(linea[0]), int(linea[1]), str(linea[2]), str(linea[3]), int(linea[4])))
        


mico = Empresa("popo.txt")

auto1 = Auto("Auto", 123, "Chevrole", "Rojo", 5000)
camion1 = Camion("Camion", 143, "renau", "azul", 6000)
moto1 = Moto("Moto", 654, "Kawa", "niche", 2000)

"""mico.agregar_vehiculo(auto1)
mico.agregar_vehiculo(camion1)
mico.agregar_vehiculo(moto1)"""

mico.cargar_vehiculos()