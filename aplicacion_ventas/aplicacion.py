from modelos import Producto, Cliente
from pedido import Factura
from descuentos import DescuentoVIP, DescuentoVolumen, SinDescuento
from impuestos import IVA, Excentos

cliente = Cliente(123, "peo", False)

producto1 = Producto(45, "Arepas", "alimentos", 2000)
producto2 = Producto(56, "Suscripcion netflix", "servicios", 25000)
producto3 = Producto(67, "Computador", "tecnologia", 2000000)

miFactura = Factura(cliente)

miFactura.agregar_linea(producto2, 10)

descuentoAplicar = DescuentoVolumen()
impuestoAplicar = IVA()

print(miFactura.calcular_total(descuentoAplicar, impuestoAplicar))
