"""#Una tienda quiere llevar el control de los productos que vende. Por cada producto, necesita guardar el nombre, el precio y la cantidad disponible.
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

while True:
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
        break   


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
        break"""

#Vas a crear un pequeño sistema de calificaciones con las clases Estudiante y Curso. 
#Cada una deberá definirse con su propio constructor y métodos que operen sobre los atributos de instancia.

"""class Estudiantes:
    def __init__(self, nombre: str, edad: int, calificaciones: list[float]):
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = calificaciones
        self.promedio = 0

    def calcular_promedio(self):
        j = 0
        for i in range (0,len(self.calificaciones)):
            j = j + (self.calificaciones[i])
        promedio = j/len(self.calificaciones)
        self.promedio = promedio
    
    def mostrar_info(self):
        print(f'Estudiante: {self.nombre}(Edad: {self.edad}) -- Promedio: {self.promedio: .2f}')
    

class curso:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def promedio_general(self):
        suma = 0
        for k in range(0, len(self.estudiantes)):
            suma = suma + curso1.estudiantes[k].promedio
            promGen = suma/len(self.estudiantes)
        print(f'Promedio general: {promGen: .2f}')
    
    def mostrar_estudiantes(self):
        for j in range (0, len(self.estudiantes)):
            Estudiantes.mostrar_info(self.estudiantes[j])

s1 = Estudiantes("Ana", 20, [4.5, 3.7, 5.0])
s2 = Estudiantes("Luis", 22, [4.0, 4.2, 3,8])
s3 = Estudiantes("Maria", 19, [5.0, 5.0, 4.9])
curso1 = curso("Algebra Lineal")
curso1.agregar_estudiante(s1)
curso1.agregar_estudiante(s2)
curso1.agregar_estudiante(s3)

s1.calcular_promedio()
s2.calcular_promedio()
s3.calcular_promedio()

curso1.promedio_general()
curso1.mostrar_estudiantes()
"""

class libro:
    def __init__(self, titulo, autor, año, genero):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.genero = genero

def buscar_libro(titulo, lista):
    existe = False
    for libros in lista:
        if libros.titulo in lista:
            existe = True
    return existe

listaLibros = []

while True:
    print("Seleccione: ")
    print("1. Registrar libro")
    print("2. ")

    opcion = int(input(": "))
    if opcion == 1:
        titulo = input("Ingresar titulo: ")
        autor = input("Titulo: ")
        fecha = int(input("Fecha: "))
        genero = input("Genero: ")
        libroNuevo = libro(titulo, autor, fecha, genero)
        listaLibros.append(libroNuevo)
    
    elif opcion == 2:
        for libros in listaLibros:
            print(libros.autor)
            print(libros.titulo)
    
    elif opcion == 3: 
        tituloBuscar = ("Titulo: ")
        encontrarLibro = buscar_libro(tituloBuscar, listaLibros)
        if encontrarLibro == True:
            print("Existe")
        else: 
            print("No existe")

    elif opcion == 4:
        print(f'La cantidad de libros es {len(listaLibros)}')

    elif opcion == 0:
        print("Chao")
        break