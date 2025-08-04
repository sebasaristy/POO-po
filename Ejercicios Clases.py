#Una tienda quiere llevar el control de los productos que vende. Por cada producto, necesita guardar el nombre, el precio y la cantidad disponible.
#El sistema debe permitir vender cierta cantidad de productos y mostrar cuántas unidades quedan. Si no hay suficientes unidades, debe mostrar un mensaje de advertencia.

class tiendaProductos:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_Productos(self):
        for producto in listaProductos:
            print(f'\nProducto : {producto.nombre}')
            print(f'Precio : {producto.precio}')
            print(f'Cantidad : {producto.cantidad}')

listaProductos = []
Leche = tiendaProductos("Leche", 2500, 0)
Arroz = tiendaProductos("Arroz", 3000, 5)
Cereal = tiendaProductos("Cereal", 2000, 5)
listaProductos.append(Leche)
listaProductos.append(Arroz)
listaProductos.append(Cereal)

print("Gestión de productos")

"""while True:
    print("\nSeleccione una opcion")
    print("1. Añadir productos")
    print("2. Vender productos")
    print("3. Mostrar productos")
    print("4. Salir")
    opcion = int(input("Ingrese el numero: "))

    if opcion == 1:
        nombreProducto = input("Nombre del producto: ")
        precioProducto = float(input("Precio del producto: "))
        cantidadProducto = int(input("Cantidad del producto: "))
        nuevoProducto = tiendaProductos(nombreProducto, precioProducto, cantidadProducto)
        listaProductos.append(nuevoProducto)
        nuevoProducto.mostrar_Productos()

    
    if opcion == 2:
        nombreProductoComprar = input("Nombre del producto que desea: ")
        for productos in listaProductos:
            if nombreProductoComprar == productos.nombre:
                if productos.cantidad == 0:
                    print("No hay mas unidades de este producto")
                else:
                    productos.cantidad = productos.cantidad - 1
                    
                
    if opcion == 3:
        print("\nLos productos son")
        for productos in listaProductos:
            print(productos.nombre, productos.precio, productos.cantidad)
    
    if opcion == 4:
        print("Hasta luego")
        break   """


#Quieres simular un sistema bancario sencillo. Cada cliente debe poder tener un número de cuenta, un titular y un saldo.
# El sistema debe permitir depositar dinero, retirar dinero (si hay suficiente), y consultar el saldo   

class sistemaBancario:
    def __init__(self,numeroCuenta, titular, saldo ):
        self.numeroCuenta = numeroCuenta
        self.titular = titular
        self.saldo = saldo

listaClientes = []

cliente1 = sistemaBancario(10, "Juan", 200000)
cliente2 = sistemaBancario(12, "Jose", 0)
listaClientes.append(cliente1)
listaClientes.append(cliente2)

while True:
    print("\nQue desea hacer")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Añadir nuevo cliente")
    print("5. Salir")
    opcion = int(input("Ingrese un numero: "))

    if opcion == 1:
        cliente = int(input("Ingrese su numero de cuenta: "))
        for cuenta in listaClientes:
            if cliente == cuenta.numeroCuenta:
                print("Hola", cuenta.titular, "\nSu saldo es de", cuenta.saldo)

    if opcion == 2:
        cliente = int(input("Ingrese su numero de cuenta: "))
        for cuenta in listaClientes:
            if cliente == cuenta.numeroCuenta:
                ingresoDinero = float(input("Ingrese la cantidad que quiere depositar: "))
                cuenta.saldo = cuenta.saldo + ingresoDinero
                print("El deposito fue exitoso.")
                print("Su saldo es de", cuenta.saldo)
    
    if opcion == 3:
        cliente = int(input("Ingrese su numero de cuenta: "))
        for cuenta in listaClientes:
            if cliente == cuenta.numeroCuenta:
                dineroRetirar = float(input("Ingrese la cantidad que desea retirar: "))
                if dineroRetirar > cuenta.saldo:
                    print("No hay saldo suficiente para retirar")
                else:
                    cuenta.saldo = cuenta.saldo - dineroRetirar
                    print("El retiro fue exitoso")
                    print("Su saldo es ahora de", cuenta.saldo)
    
    if opcion == 4:
        nuevoTitular = input("Ingrese su nombre: ")
        nuevoNumeroCuenta = int(input("Ingrese un nuevo numero de cuenta: "))
        while True: 
            for cuenta in listaClientes:
                if nuevoNumeroCuenta == cuenta.numeroCuenta:
                    print("Numero ya en uso")
                    nuevoNumeroCuenta = input("Ingrese un nuevo numero de cuenta: ")
                    break
                else:
                    break
            nuevoCliente = sistemaBancario(nuevoNumeroCuenta, nuevoTitular, 0)
            listaClientes.append(nuevoCliente)
            break
        
    if opcion == 5:
        print("Hasta luego")
        break

