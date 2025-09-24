import random
class Productos():
    def __init__(self, nombre):
        self.nombre = nombre 
        self.listaProductos = []

    def mostrar_productos(self):
        contador = 0
        for i in self.listaProductos:
            contador += 1
            print(f'Producto {contador}: {i.nombre}: {i.precio}$, Talla: {i.talla}, Color: {i.color}')


class Ropa(Productos):
    def __init__(self, nombre, precio, talla, color):
        super().__init__(nombre)
        self.precio = precio
        self.talla = talla
        self.color = color


class Tenis(Productos):
    def __init__(self, nombre, precio, talla, color):
        super().__init__(nombre)
        self.precio = precio
        self.talla = talla 
        self.color = color

class cliente:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.carrito = Carrito()

class Carrito: 
    def __init__(self):
        self.listaproductos = []
    
    def mostrar_carrito(self):
        contador = 0
        for i in self.listaproductos:
            contador += 1
            print(f'Producto {contador}: {i.nombre}: {i.precio}$, Talla: {i.talla}, Color: {i.color}')

    def calcular_total(self):
        acumulador = 0
        for i in self.listaproductos:
            acumulador = acumulador + i.precio
        return acumulador

class Pedido(Carrito):
    def __init__(self, cliente):
        super().__init__()
        self.idPedido = (random.randint(1000,9999))
        self.cliente = cliente

    def mostrar_factura(self):
        print(f'{self.cliente.nombre}, su pedido tiene id {self.idPedido}. Fue enviado al correo {self.cliente.correo}')

        

producto0 = Productos("Prueba")

camisa = Ropa("camisa", 3000, "M", "Rojo")
buzo = Ropa("buzo", 5000, "M", "Negro")
chaqueta = Ropa("chaqueta", 7000, "M", "Blanco")

botas = Tenis("botas", 6000, "38", "Azul")
tenis = Tenis("tenis", 6000, "38", "Naranja")
chanclas = Tenis("chanclas", 6000, "38", "Azul")


producto0.listaProductos.append(camisa)
producto0.listaProductos.append(buzo)
producto0.listaProductos.append(chaqueta)
producto0.listaProductos.append(botas)
producto0.listaProductos.append(tenis)
producto0.listaProductos.append(chanclas)

print("Ingrese su nombre y correo para crearle su carrito:")
nombreNuevo = input("Nombre: ")
correoNuevo = input("Correo: ")
clienteNuevo = cliente(nombreNuevo, correoNuevo)

while True:
    print("\nBienvenido a la Tienda")
    print("----------------------------------------------------")
    print("Estos son nuestros productos")
    producto0.mostrar_productos()
    print("----------------------------------------------------")
    print("¿Que desea hacer?")
    print("1. Agregar producto al carrito")
    print("2. Eliminar producto del carrito")
    print("3. Mostrar carrito")
    print("4. Calcular total del carrito")
    print("5. Realizar pedido")
    print("0. Salir")
    opcion = int(input("Ingrese su opcion: "))

    if opcion == 1:
        nombreAgregar = input("Ingrese el nombre del producto que desea agregar al carrito: ").lower()
        for j in producto0.listaProductos:
            if j.nombre == nombreAgregar:
                clienteNuevo.carrito.listaproductos.append(j)
    
    if opcion == 2:
        nombreEliminar = input("Ingrese el nombre del producto que desea eliminar del carrito: ").lower()
        for j in producto0.listaProductos:
            if j.nombre == nombreEliminar:
                clienteNuevo.carrito.listaproductos.remove(j)
    
    if opcion == 3:
        clienteNuevo.carrito.mostrar_carrito() 
    
    if opcion == 4:
        print(f'\nEl total es de {clienteNuevo.carrito.calcular_total()}')
    
    if opcion == 5:
        pedidoNuevo = Pedido(clienteNuevo)
        pedidoNuevo.mostrar_factura() 
        print(f'Y el total es de {clienteNuevo.carrito.calcular_total()}')

    if opcion == 0: 
        print("Muchas gracias por la visita")
        break
        
