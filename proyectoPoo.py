import random
from typing import List, ClassVar, Set
from abc import ABC, abstractmethod

class Productos:
    def __init__(self, nombre, precio, talla, color):
        self.nombre = nombre 
        self.precio = precio
        self.talla = talla
        self.color = color

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.listaProductos = []

    def agregar_productos(self, producto):
        self.listaProductos.append(producto)
        print(f'El producto ha sido agregado exitosamente')

    def mostrar_productos(self):
        for i in range (0, len(self.listaProductos)):
            print(f'{self.listaProductos[i].nombre.capitalize()}, Precio: {self.listaProductos[i].precio}, Talla: {self.listaProductos[i].talla}, Color: {self.listaProductos[i].color}')
    
    def crear_producto(self):
        categoria = input("Ingrese la categoria que desea añadir (Ropa/Tenis): ").lower()
        if categoria == "ropa":
            nNombre = input("Ingrese el nombre: ")
            nPrecio = int(input("Ingrese el precio: "))
            nTalla = input("Ingrese la talla (S/M/L): ").capitalize()
            nColor = input("Ingrese el color: ")
            nProducto = Ropa(nNombre, nPrecio, nTalla, nColor)
            print(f'El producto ha sido creado exitosamente. ({nProducto.nombre.capitalize()})')
            self.listaProductos.append(nProducto)
            
        if categoria == "tenis":
            nNombre = input("Ingrese el nombre: ")
            nPrecio = int(input("Ingrese el precio: "))
            nTalla = int(input("Ingrese la talla (numeros): "))
            nColor = input("Ingrese el color: ")
            nProducto = Tenis(nNombre, nPrecio, nTalla, nColor)
            print(f'El producto ha sido creado exitosamente. ({nProducto.nombre.capitalize()})')
            self.listaProductos.append(nProducto)


class Ropa(Productos):
    def __init__(self, nombre, precio, talla, color):
        super().__init__(nombre, precio, talla, color)

class Tenis(Productos):
    def __init__(self, nombre, precio, talla, color):
        super().__init__(nombre, precio, talla, color)

class cliente:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.carrito = Carrito()

class Carrito: 
    def __init__(self):
        self.listaproductos = []
    
    def mostrar_carrito(self):
        for i in range (0, len(self.listaProductos)):
            print(f'{self.listaProductos[i].nombre.capitalize()}, Precio: {self.listaProductos[i].precio}, Talla: {self.listaProductos[i].talla}, Color: {self.listaProductos[i].color}')

    def calcular_total(self):
        acumulador = 0
        for i in self.listaproductos:
            acumulador = acumulador + i.precio
        return acumulador

class Pedido():
    def __init__(self, cliente):
        self.idPedido = (random.randint(1000,9999))
        self.cliente = cliente

    def mostrar_factura(self):
        print(f'{self.cliente.nombre}, su pedido tiene id {self.idPedido}. Fue enviado al correo {self.cliente.correo}')

        
tienda1 = Tienda("Exito")

camisa = Ropa("camisa", 3000, "M", "Rojo")
buzo = Ropa("buzo", 5000, "M", "Negro")
chaqueta = Ropa("chaqueta", 7000, "M", "Blanco")

botas = Tenis("botas", 6000, "38", "Azul")
tennis = Tenis("tenis", 6000, "38", "Naranja")
chanclas = Tenis("chanclas", 6000, "38", "Azul")

tienda1.agregar_productos(camisa)
tienda1.agregar_productos(buzo)
tienda1.agregar_productos(botas)
tienda1.agregar_productos(tennis)
tienda1.crear_producto()

tienda1.mostrar_productos()

cliente1 = cliente("mico", "correo")


        
