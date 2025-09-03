class Registro: 
    def __init__(self, tipo, cantidad, valorUnitario):
        self.tipo = tipo
        self.cantidad = cantidad
        self.valorUnitario = valorUnitario

class Facturas:
    def __init__(self, codigo):
        self.codigo = codigo
        self.registros = []
        self.total = 0

    def agregar_registro(self, tipo, cantidad, valorUnitario):
        nuevo_registro = Registro(tipo, cantidad, valorUnitario)
        self.registros.append(nuevo_registro)
        self.total = self.total + (cantidad * valorUnitario)
    
miFactura= Facturas(1234)
miFactura.agregar_registro("Gasimba", 2, 2000)
miFactura.agregar_registro("Papas", 2, 3000)

print(f'Total es {miFactura.total}')
