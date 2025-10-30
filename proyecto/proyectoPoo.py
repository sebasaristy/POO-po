import random


class Productos:
    def __init__(self, tipo, nombre, precio, talla, color):
        self.tipo = tipo
        self.nombre = nombre 
        self.precio = precio
        self.talla = talla
        self.color = color
    
    def mostrar_info(self):
       return f'{self.nombre.capitalize()}, Precio: {self.precio}, Talla: {self.talla}, Color: {self.color}'

class Ropa(Productos):
    def __init__(self, tipo, nombre, precio, talla, color):
        super().__init__(tipo, nombre, precio, talla, color)

class Tenis(Productos):
    def __init__(self, tipo, nombre, precio, talla, color):
        super().__init__(tipo, nombre, precio, talla, color)
        
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.listaProductos = []

    def agregar_productos(self, producto):
        if not isinstance(producto, Productos):
            raise TypeError("Solo se agregan objetos de tipo Producto")
        self.listaProductos.append(producto)
        print(f'El producto "{producto.nombre}" ha sido agregado exitosamente')
        with open(self.nombre, "a") as f:
            f.write(f'{producto.tipo}, {producto.nombre}, {producto.precio}, {producto.talla}, {producto.color}\n')

    def mostrar_productos(self):
        if not self.listaProductos:
            print("No hay productos en la tienda")
        else:
            for i in self.listaProductos:
                print(i.mostrar_info())
    
    def crear_producto(self):
        try: 
            categoria = input("Ingrese la categoria que desea añadir (Ropa/Tenis): ").lower() 
            nNombre = input("Ingrese el nombre: ")
            nPrecio = int(input("Ingrese el precio: "))  
            nColor = input("Ingrese el color: ")

            if categoria == "ropa":
                nTalla = input("Ingrese la talla (S/M/L): ").capitalize()
                nProducto = Ropa(categoria, nNombre, nPrecio, nTalla, nColor)
                print(f'El producto ha sido creado exitosamente. ({nProducto.nombre.capitalize()})')   
            elif categoria == "tenis":
                nTalla = float(input("Ingrese la talla (numeros): "))
                nProducto = Tenis(categoria, nNombre, nPrecio, nTalla, nColor)
                print(f'El producto ha sido creado exitosamente. ({nProducto.nombre.capitalize()})')
            else:
                print(categoria)
                print("Categoria invalida")
                return
            self.listaProductos.append(nProducto)
        except ValueError:
            print("Error en los numeros ingresados")
        
    def cargar_productos(self):
        self.listaProductos = []
        with open(self.nombre, "r") as f:
            for linea in f:
                linea = linea.strip().split(",")
                if linea[0] == "ropa":
                    self.listaProductos.append(Ropa(str(linea[0]), str(linea[1]), int(linea[2]), str(linea[3]), str(linea[4])))
                elif linea[0] == "tenis":
                    self.listaProductos.append(Tenis(str(linea[0]), str(linea[1]), int(linea[2]), int(linea[3]), str(linea[4])))

    def guardar_en_archivo(self):
        try:
            with open(self.nombre, "w") as f:
                for v in self.listaProductos:
                    f.write(f'{v.categoria}, {v.nombre}, {v.precio}, {v.talla}, {v.color}\n')
            print(f'Productos agregados con exito')
        except:
            print(f'Error al guardar')

class Carrito: 
    def __init__(self):
        self.listaproductos = []
    
    def agregar_producto(self, producto):
        if not isinstance(producto, Productos):
            raise TypeError("Solo se agregan objetos de tipo Producto")
        self.listaproductos.append(producto)
        print(f'Producto {producto.nombre} agregado al carrito')
    
    def eliminar_producto(self, nombre):
        for producto in self.listaproductos:
            if producto.nombre.lower() == nombre.lower():
                self.listaproductos.remove(producto)
                print(f'Producto {nombre} eliminado del carrito')
                return
        print(f'No se encontró el producto ({nombre})')

    def mostrar_carrito(self):
        if not self.listaproductos:
            print("El carrito está vacio")
        else:
            print("Productos del carrito:")
            for p in self.listaproductos:
                print(f'{p.mostrar_info()}')

    def calcular_total(self):
        total = sum(p.precio for p in self.listaproductos)
        print(f'Total del carrito: {total}')
        return total

class Cliente:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.carrito = Carrito()
    
    def mostrar_cliente(self):
        print(f'Cliente: {self.nombre}. Correo: {self.correo}')

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente 
        self.idPedido = random.randint(1000, 9999)
        self.total = cliente.carrito.calcular_total()
    
    def mostrar_factura(self):
        print(f'FACTURA:')
        print(f'ID del pedido: {self.idPedido}')
        print(f'Cliente: {self.cliente.nombre}')
        self.cliente.carrito.mostrar_carrito()
        print(f'Total a pagar: {self.total}')
        print(f'Factura enviada al correo: {self.cliente.correo}')

if __name__ == "__main__": #pragma: no cover
    tienda1 = Tienda("Exito.txt")

    producto1 = Ropa("ropa","camisa", 3000, "M", "Rojo")
    producto2 = Ropa("ropa", "buzo", 5000, "M", "Negro")
    producto3 = Ropa("ropa", "chaqueta", 7000, "M", "Blanco")

    producto4 = Tenis("tenis","botas", 6000, 38, "Azul")
    producto5 = Tenis("tenis", "tenis", 6000, 38, "Naranja")
    producto6 = Tenis("tenis","chanclas", 6000, 38, "Azul")

    tienda1.agregar_productos(producto1)
    tienda1.agregar_productos(producto2)
    tienda1.agregar_productos(producto5)
    tienda1.agregar_productos(producto4)
    tienda1.cargar_productos()
    tienda1.guardar_en_archivo


    cliente1 = Cliente("mico", "correo")
    cliente1.mostrar_cliente()

    cliente1.carrito.agregar_producto(producto1)
    cliente1.carrito.agregar_producto(producto5)

    pedido1 = Pedido(cliente1)
    pedido1.mostrar_factura()

        
