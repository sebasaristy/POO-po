class Tienda:
    def __init__(self, nombreTienda):
        self.nombreTienda = nombreTienda
        self.listaProductos = []

class Ropa:
    def __init__(self, nombre, precio, talla, color, tipo):
        self.nombre = nombre 
        self.precio = precio 
        self.talla = talla
        self.color = color
        self.tipo = tipo

class Carrito: 
    def __init__(self):
        self.productos = []

class cliente:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.carrito = Carrito
        
class Pedido(Carrito):
    def __init__(self, productos, clientes):
        super().__init__(productos)
        self.clientes = clientes 
        

